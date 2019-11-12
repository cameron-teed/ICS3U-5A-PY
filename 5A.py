#!/usr/bin/env python3

# Created by: Cameron Teed
# Created on: Oct 2019
# This is a program

import math


def main():

    word = input("Please put in a word: ")
    neword = ""
    vord = ""

    while True:

        try:

            number = int(input("Please put in how many letters you would like"
                               ". "))
            counter1 = int(input("Please put in how many how many time you "
                                 "would like the letters to repeat. "))
            lenght = (len(word))

            if lenght < number:
                print("")
                print("please put in a valid number of how many letters you"
                      " would like. ")
                break

            for counter in range(counter1):
                word3 = (word[1:number])
                vord = (word[0:1])
                vord = (vord.upper())
                wordies = (vord+word3)
                neword = neword + wordies

            print("")
            print(neword)
            break

        except ValueError:
            print("")
            print("Please put in a integer. ")


if __name__ == "__main__":
    main()
