#!/usr/bin/env python
from sys import argv
import random

script, filename = argv

def make_chains(filename):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    # open the file
    filename = open("poem.txt", 'r')
    read_file = filename.read()
    # clean up the text to be strings in a list
    words = read_file.split()
   
    # FIXME remove commas in the string. do we keep punctuation?
    chains_dict = {}
    for index in range(len(words)-2):
        key = (words[index], words[index+1])
        value = words[index+2]
        if key in chains_dict:
            chains_dict[key].append(value)
        else:
            chains_dict[key] = [value]

    print chains_dict
    return chains_dict


def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    # create empty list
    make_text_list = []
    # test_list = make_chains()
    # # 1: append the first tuple key using get() so it's random to the empty list
    print random.choice(chains.keys())
        # Would you
    # 2: randomly select a value in the list in that key-value pair, rand(dictionary [key])
        # a
    # 3: take the second value in the first tuple key and create a new tuple with the second value being the randomly selected value from the list
    # append to empty list
        # (you, a)
    # 4: look for that tuple in the dictionary and randomly select the value (repeat step 2)
    # when to end: stop after a certain number of periods or certain number of words/characters or max char count
    # end: print list



def main():
    #args = sys.argv

    # Change this to read input_text from a file
    input_text = "Some text"

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text



if __name__ == "__main__":
    main()
