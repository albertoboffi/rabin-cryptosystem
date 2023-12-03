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

    # Input: -
    # Output: -
    # Behavior: Generates a key pair

    def generateKeys(self):

        keys = self.key_generator.generateKeys()
        self.k_pri = keys["private"]
        self.k_pub = keys["public"]

    """
    # Input: string
    # Output: integer produced through a bijective function
    def __fromStringToInt(s: str):
        s_bytes = s.encode("utf-8")
        s_int = int.from_bytes(s_bytes, byteorder = "big")
        return s_int
    """

    # Input: plaintext
    # Output: ciphertext
    # Behavior: Encrypts the plaintext using the public key

    def encrypt(self, plaintext: int) -> int:

        ciphertext = (plaintext ** 2) % self.k_pub

        return ciphertext

    # Input: ciphertext
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

        return [

            plaintext_1,
            plaintext_2,
            plaintext_3,
            plaintext_4

        ]