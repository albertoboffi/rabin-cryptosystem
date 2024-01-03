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

    def __splitText(self, text:str, split_size:int) -> list:

        text_split = [
        
            text[i:i + split_size]

            for i in range(0, len(text), split_size)
        
        ]

        return text_split
    
    # Input: Integer
    # Output: Two-characters string
    # Behavior: Transforms the ciphertext into a text by using ascii encoding

    def __getTextFromCiphertext(self, ciphertext:int) -> str:

        s_ciphertext = str(ciphertext)

        fh = s_ciphertext[:len(s_ciphertext) // 2]
        sh = s_ciphertext[len(s_ciphertext) // 2 :]

        fchar = chr(int(fh))
        schar = chr(int(sh))

        text = fchar + schar

        return text

    # Input: Two-character string
    # Output: Integer
    # Behavior: Converts the text into the original ciphertext using ascii decoding

    def __getCiphertextFromText(self, text:str) -> tuple[int, int]:

        fciph = ord(text[0])
        sciph = ord(text[1])

        s_fciph = str(fciph)
        s_sciph = str(sciph)
        
        s_sciph = ("0" * (len(s_fciph) - len(s_sciph))) + s_sciph # adds possible leading zeros

        ciphertext = int(s_fciph + s_sciph)
        alt_ciphertext = int(s_fciph + "0" + s_sciph) # considering additional possible leading zero

        return ciphertext, alt_ciphertext
    
    # Input: Text
    # Output: Encrypted text
    # Behavior: Encrypts the text using the Rabin cryptosystem

    def encrypt(self, text:str) -> str:

        chars = self.__splitText(text, 1) # extracts each character from the text

        enc_text = ""

        for i in range(len(chars)):

            plaintext = ord(chars[i]) # converts each character in the corresponding ascii encoding
            ciphertext = self.crypsys.encrypt(plaintext)

            enc_text += self.__getTextFromCiphertext(ciphertext) # converts the integer ciphertext into a two-character text

        return enc_text
    
    # Input: Text
    # Output: Decrypted text
    # Behavior: Decrypts the text using the Rabin cryptosystem

    def decrypt(self, text:str) -> str:

        chars = self.__splitText(text, 2) # splits the text into groups of two characters

        dec_text = ""

        for i in range(len(chars)):
            
            ciphertext, alt_ciphertext = self.__getCiphertextFromText(chars[i]) # converts the string-format ciphertext into the corresponding integer
            plaintext = self.crypsys.decrypt(ciphertext)

            try:

                dec_text += chr(plaintext) # converts the integer-format plaintext into the corrisponding ascii character

            except TypeError: # the wrong ciphertext has been considered, switch
                
                plaintext = self.crypsys.decrypt(alt_ciphertext)
                dec_text += chr(plaintext)
        
        return dec_text

