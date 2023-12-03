#!/usr/bin/env python

from math import prod

__author__ = 'Alberto Boffi'
__deprecated__ = False

# Input: r0 = a, r1 = b such that a > b > 0
# Output: gcd, Bezout coefficients
# Bahvior: Performs the extended version of the Euclidean algorithm

def extEuclideanAlgorithm(r0: int, r1: int, s0 = 1, s1 = 0, t0 = 0, t1 = 1):

    q = r0 // r1

    r_new = r0 - q * r1
    s_new = s0 - q * s1
    t_new = t0 - q * t1

    if (r_new):
        
        return extEuclideanAlgorithm(r1, r_new, s1, s_new, t1, t_new)
    
    return {

        "gcd": r1, # greatest common divisor
        "coef": [s1, t1] # bezout coefficients

    }

# Input: List a of residues, list m of moduluses. It must holds that len(a) = len(m)
# Output: Result of the system
# Behavior: Solves the system using the Chinese Remainder Theorem

def chineseRemainderTheorem(a: list, m: list):

    x = 0

    for i in range(len(a)):

        M = prod(m) / m[i] # products of all the moduluses except m[i]

        coef = extEuclideanAlgorithm(M, m[i])["coef"]
        coef_M = coef[0] # coefficient of M

        x += M * coef_M * a[i] # add the solution of the single congruence to the overall solution

    return x

