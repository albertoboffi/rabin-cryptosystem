#!/usr/bin/env python

#---------------------------------------------------#
#--------------- Prepare for import ----------------#
#---------------- IGNORE THIS PART -----------------#
#---------------------------------------------------#

import os, sys
sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
            )
        )
    )

from src.RabinCryptosystem import RabinCryptosystem

#---------------------------------------------------#
#--------------- Possible messages -----------------#
#----------- CHANGE WITH YOUR OWN MESAGE -----------#
#---------------------------------------------------#

msg = 741

#---------------------------------------------------#
#--------------- Body of the script ----------------#
#------------------ DO NOT TOUCH -------------------#
#---------------------------------------------------#

def main(msg):

    # encryption

    cryptosystem = RabinCryptosystem()

    ciphertext = cryptosystem.encrypt(msg)
    plaintexts = cryptosystem.decrypt(ciphertext)

    # log

    print("Original message >> ", msg)
    print("Encrypted message >> ", ciphertext)
    print("Decrypted message >> ", plaintexts)


if __name__ == '__main__':

    main(msg)