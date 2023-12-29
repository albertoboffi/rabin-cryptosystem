#!/usr/bin/env python

from .RabinCryptosystem import RabinCryptosystem

__author__ = 'Alberto Boffi'
__deprecated__ = False

class RabinTextManager:

    # Input: -
    # Output: -
    # Behavior: Initializes the Rabin cryptosystem

    def __init__(self):

        self.crypsys = RabinCryptosystem()

    # Input: Text
    # Output: List of characters of the strings
    # Behavior: Splits the text in each character composing it

    def __splitText(self, text:str, split_size:int):

        text_split = [
        
            text[i:i + split_size]

            for i in range(0, len(text), split_size)
        
        ]

        return text_split
    
    def __getTextFromCiphertext(self, ciphertext:int):

        s_ciphertext = str(ciphertext)

        fh = s_ciphertext[:len(s_ciphertext) // 2]
        sh = s_ciphertext[len(s_ciphertext) // 2 :]

        fchar = chr(int(fh))
        schar = chr(int(sh))

        text = fchar + schar

        return text

    # Input: List of chars
    # Output: Single string
    # Behavior: Merges all the characters in the list in a unique string

    def __mergeTexts(self, text_split:list):

        text = "".join(text_split)

        return text
    
    def encrypt(self, text:str):

        chars = self.__splitText(text, 1)

        enc_text = ""

        for i in range(len(chars)):

            plaintext = ord(chars[i]) # ascii char
            ciphertext = self.crypsys.encrypt(plaintext)

            enc_text += self.__getTextFromCiphertext(ciphertext)
        
        return enc_text