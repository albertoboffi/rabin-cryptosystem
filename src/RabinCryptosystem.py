#!/usr/bin/env python

from .KeyGenerator import KeyGenerator
from .algorithms import *

from decimal import *
getcontext().prec = 1000000 # adjust precision to deal with large numbers

__author__ = 'Alberto Boffi'
__deprecated__ = False

class RabinCryptosystem:

    # Input: -
    # Output: -
    # Behavior: Initialize the key generator and generates the keys
    
    def __init__(self):

        self.key_generator = KeyGenerator()
        self.generateKeys()

    # Input: Original Plaintext
    # Output: New Plaintext 
    # Behavior: Adds to the original plaintext a prefix equal to the plaintext itself
        
    def __addPrefix(self, plaintext:int) -> int:

        s_pt = str(plaintext)
        pref_pt = int(s_pt + s_pt)

        return pref_pt
    
    # Input: Candidate extended plaintexts
    # Output: Correct plaintext
    # Behavior: Finds the number that is repeat twice in one of a candidate extended plaintexts

    def __getPlaintext(self, plaintexts: list) -> None:

        for i in range(0, 4):

            s_pt = str(plaintexts[i])            
            len_pt = len(s_pt)

            fh = s_pt[: len_pt // 2]
            sh = s_pt[len_pt // 2 :]

            if (fh == sh): return int(fh)

    # Input: -
    # Output: -
    # Behavior: Generates a key pair

    def generateKeys(self) -> None:

        keys = self.key_generator.generateKeys()
        self.k_pri = keys["private"]
        self.k_pub = keys["public"]

    # Input: Plaintext
    # Output: Ciphertext
    # Behavior: Encrypts the plaintext using the public key

    def encrypt(self, plaintext: int) -> int:

        extended_plaintext = self.__addPrefix(plaintext)

        ciphertext = (extended_plaintext ** 2) % self.k_pub

        return ciphertext

    # Input: Ciphertext
    # Output: All four possible plaintexts
    # Behavior: Decrypts the ciphertext using the private and the public key

    def decrypt(self, ciphertext: int) -> int:

        # prime numbers composing the private key

        p = self.k_pri[0]
        q = self.k_pri[1]

        # square roots modulo private key

        sq_p = ciphertext ** (Decimal('0.25') * (p + 1)) % p
        sq_q = ciphertext ** (Decimal('0.25') * (q + 1)) % q

        sq_p = int(sq_p)
        sq_q = int(sq_q)

        # bezout coefficients

        coef = extEuclideanAlgorithm(p, q)["coef"]

        coef_p = coef[0]
        coef_q = coef[1]

        # square roots

        plaintext_1 = (coef_p * p * sq_q + coef_q * q * sq_p) % self.k_pub
        plaintext_2 = self.k_pub - plaintext_1
        plaintext_3 = (coef_p * p * sq_q - coef_q * q * sq_p) % self.k_pub
        plaintext_4 = self.k_pub - plaintext_3

        plaintexts = [

            plaintext_1,
            plaintext_2,
            plaintext_3,
            plaintext_4

        ]

        return self.__getPlaintext(plaintexts)