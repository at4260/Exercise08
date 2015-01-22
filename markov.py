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
   
    # HELP! remove commas in the string. do we keep punctuation?
    # create the tuple
    new_tuples = []
    count1 = 0
    
    for word in words:
        while count1 < len(words) - 1:
            count2 = count1 + 1
            string_to_tuple = (words[count1], words[count2])
            new_tuples.append(string_to_tuple)
            count1 = count1 + 1    
            # print string_to_tuple
    #print new_tuples
    #turn tuples into keys
    #assign value to key, then turn k,v pair into dictionary
    for ind_tuple in new_tuples:
        new_dict = {ind_tuple:'0'}
        print new_dict

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
