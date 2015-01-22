#!/usr/bin/env python
from sys import argv

script, filename = argv

def make_chains(filename):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    # open the file
    filename = open("poem.txt", 'r')
    read_file = filename.read()
    # clean up the text to be strings in a list
    words = read_file.split()
    print words
   
    # HELP! remove commas in the string. do we keep punctuation?
    # create the tuple
    new_tuples = []
    count1 = 0
    while count1 < len(words):
        for word in range(0,len(words)):
            count2 = count1 + 1
            string_to_tuple = (words[count1], words[count2])
            new_tuples.append(string_to_tuple)
            count1 = count1 + 1    
            print string_to_tuple

    # convert that to a dictionary version of markov chains

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    return "Here's some random text."

def main():
    #args = sys.argv

    # Change this to read input_text from a file
    input_text = "Some text"

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text



if __name__ == "__main__":
    main()
