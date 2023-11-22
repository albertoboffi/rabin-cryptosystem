#!/usr/bin/env python

from KeyGenerator import KeyGenerator

__author__ = 'Alberto Boffi'
__date__ = '2023-11-23'
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

    def encrypt(self, msg, key):
        pass

    def decrypt(self, msg, key):
        pass