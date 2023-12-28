#!/usr/bin/env python

__author__ = 'Alberto Boffi'
__deprecated__ = False

class RabinTextManager:

    def __init__(self):

        self.text = "hello world"

    # Input: Text
    # Output: List of two-characters strings
    # Behavior: Splits the text in groups of two characters

    def splitText(self, text:str):

        split_len = 2   # number of characters in each split

        text_split = [
        
            text[i:i + split_len]

            for i in range(0, len(text), split_len)
        
        ]

        return text_split
    
    # Input: List of strings
    # Output: Single string
    # Behavior: Merges all the strings in the list in a unique string

    def mergeTexts(self, text_split:list):

        text = "".join(text_split)

        return text

    # Input: Text
    # Output: Integer number
    # Behavior: Converts a string into an integer through a bijective function

    def encodeText(self, text:str):

        text_bytes = text.encode("utf-8")
        text_int = int.from_bytes(text_bytes, byteorder = "big")
        
        return text_int
    
    # Input: Integer number
    # Output: Text
    # Behavior: Converts the integer produced through a bijective function into the original string
    
    def decodeNumber(self, num:int):

        num_bytes = num.to_bytes(
        
            (num.bit_length() + 7) // 8,
            byteorder="big"

        )

        num_string = num_bytes.decode("utf-8")

        return num_string
