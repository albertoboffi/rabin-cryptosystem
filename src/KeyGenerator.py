#!/usr/bin/env python

import secrets
from primality import primality

__author__ = 'Alberto Boffi'
__deprecated__ = False

class KeyGenerator:
    
    # Input: Prime p
    # Output: True if p ≡ 3 mod 4, False otherwise

    def __isValidPrime(self, p: int) -> bool:

        if (p % 4 == 3): return True
        return False
    
    # Input: -
    # Output: Random number n, st the generated prime will be at least the n-th prime

    def __getRandomSeed(self) -> int:

        seed_range = range(1000, 10000)
        seed = secrets.choice(seed_range)

        return seed
    
    # Input: -
    # Output: Random large prime p such that p ≡ 3 mod 4

    def __generatePrime(self, q = 0) -> int:

        seed = self.__getRandomSeed()

        p = primality.nthprime(seed)

        i = 0
        while (not(self.__isValidPrime(p) or (p == q))):
           p = primality.nthprime(seed + i)
           i += 1

        return p

    # Input: -
    # Output: Key pair for the Rabin cryptosystem

    def generateKeys(self) -> dict:

        q = self.__generatePrime()
        p = self.__generatePrime(q)

        k_pri = (p, q)
        k_pub = p * q

        return {

            "private": k_pri,
            "public": k_pub
            
        }
