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
    chains_dict = {}
    # count1 = 0
    for index in range(len(words)-2):
        key = (words[index], words[index+1])
        value = words[index+2]
        if key in chains_dict:
            chains_dict[key].append(value)
        else:
            chains_dict[key] = [value]

    print chains_dict

    
    # for word in words:
    #     while count1 < len(words) - 1:
    #         count2 = count1 + 1
    #         string_to_tuple = (words[count1], words[count2])
    #         new_tuples.append(string_to_tuple)
    #         count1 = count1 + 1    
    #         # print string_to_tuple
    # #print new_tuples
    # #turn tuples into keys
    # #assign value to key, then turn k,v pair into dictionary
    # for ind_tuples in new_tuples:
    #     new_dicts = {ind_tuples:'0'}
    # #   print new_dicts

    # super_dict = {}
    # for d in new_dicts:
    #     for k,v in d.items():
    #         super_dict[k].append(v)
    #         print super_dict

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
