#!/usr/bin/env python
from sys import argv
import random
import string

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

    return chains_dict


def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    # create empty list
    make_text_list = []
    
    # initializer: append the first tuple key using get() so it's random to the empty list
    first_chain = random.choice(chains.keys())
    make_text_list.append(first_chain[0])
    make_text_list.append(first_chain[1])
    #get random value from initial tuple
    chain_val = random.choice(chains[first_chain])
    make_text_list.append(chain_val)   
    #print make_text_list 

    #max char length = 140
    #while the length of make_test_list is 
    while len(string.join(make_text_list)) < 140:
        new_tuple = (make_text_list[-2], make_text_list[-1])
    # look up new tuple in chains dictionary and choose random value
        new_val = random.choice(chains[new_tuple])    
    # append value to list
        make_text_list.append(new_val)
        if make_text_list[-2] == 'I' and make_text_list[-1] == 'Am?':
            break

    print string.join(make_text_list)
    
def main():
    #args = sys.argv

    # Change this to read input_text from a file
    input_text = "Some text"

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text



if __name__ == "__main__":
    main()
