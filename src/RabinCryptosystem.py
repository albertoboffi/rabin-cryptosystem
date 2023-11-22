#!/usr/bin/env python

from KeyGenerator import KeyGenerator

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
    def encrypt(self, plaintext: int):

        ciphertext = (plaintext ** 2) % self.k_pub

        return ciphertext


    def decrypt(self, ciphertext: int):

        pass