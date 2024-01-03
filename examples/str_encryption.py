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

from src.RabinTextManager import RabinTextManager

#---------------------------------------------------#
#--------------- Possible messages -----------------#
#----------- CHANGE WITH YOUR OWN MESAGE -----------#
#---------------------------------------------------#

msg = "Hello world! What a beautiful day :)"

#---------------------------------------------------#
#--------------- Body of the script ----------------#
#------------------ DO NOT TOUCH -------------------#
#---------------------------------------------------#

def main(msg):

    # encryption

    text_manager = RabinTextManager()

    ciphertext = text_manager.encrypt(msg)
    plaintexts = text_manager.decrypt(ciphertext)

    # log

    print("Original message >> ", msg)
    print("Encrypted message >> ", ciphertext)
    print("Decrypted message >> ", plaintexts)


if __name__ == '__main__':

    main(msg)