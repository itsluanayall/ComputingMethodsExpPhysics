"""Assignment N.1 
Luana Michela Modafferi 
 30th September 2019
 """

import argparse
import os
import string
import time
import matplotlib.pyplot as plt
import numpy
import logging
logging.basicConfig(level=logging.INFO)



_description = "Measure the relative frequencies of letter in a text"



def load_file(file_path):
    """Read text (.txt format). 
    """
    #Basic sanity check.
    assert file_path.endswith('.txt')
    assert os.path.isfile(file_path)
    
    #Good to go--open the input file.
    logging.info('Opening file %s...', file_path)
    with open(file_path, 'r') as input_file:
        data = input_file.read()    #file closes automatically. Use this from now on!   
    logging.info('Done.')   #use logging instead of print to detect bugs
    return data              #and to see what the code is doing.


def letter_counter(data):
    """Associates to each letter in the alphabet its frequency in the book (data).
    Returns a dictionary which keys are single letters, and values are the relative frequencies.
    """
    # Create a dictionary for letter counting.
    dict_alphabet = dict( (key, 0) for key in string.ascii_lowercase ) 

    # Iterate through the book and calcutate the total elapsed time.
    start_time = time.time()
    for char in data.lower():
        if char in dict_alphabet.keys():
            dict_alphabet[char] += 1
    end_time = time.time()
    elapsed_time = total_elapsed_time(start_time,end_time)
    logging.info('Total Elapsed Time: {} seconds'.format(elapsed_time))

    # Normalize the occurences.
    total_letters = float(sum(dict_alphabet.values()))
    for k in dict_alphabet.keys():
        dict_alphabet[k] /= total_letters
    
    #Print the frequencies legibly.
    logging.info("Writing relative frequencies...")
    for char, freq in dict_alphabet.items():
        print('{}, {:.3f}%'.format(char, freq * 100))
    logging.info("Done.")

    return dict_alphabet


def total_elapsed_time(start, end):
    """Simple sottraction to calculate a time interval.
    """
    return end - start


def horizontal_hist(y, counts, title):
    """Makes a horizontal histogram. Note that you can choose the title,
    so this piece of code can really come in handy.
    """
    logging.info("Making histogram...")
    plt.rcdefaults()
    fig, ax = plt.subplots()
    y_pos = numpy.arange(len(y))
    ax.barh(y_pos, counts, edgecolor='black')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(y)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Frequency')
    ax.set_title(title)
    plt.tight_layout()
    logging.info("Plot ready.")
    plt.show()
 

def split_text(data, token, i):
    """ The split method returns an array of sub-strings separated by the token. 
    This function returns the i-th element of this array.
    """
    return data.split(token)[i]


def word_counter(data):
    """Since every word is separated by a space,
    we use the split method with the token set to ' '.
    """
    return len(data.split(' '))


def line_counter(data):
    """Since every line is separated by a \n, 
    we use the split method with the token set to '\n'.
    """
    return len(data.split('\n'))





if __name__ == '__main__': 

    # Handle the command-line interface.
    parser = argparse.ArgumentParser(description=_description)
    parser.add_argument("infile", help="path to the input text file")
    parser.add_argument("--hist", help="plots the bar chart of the frequecies", action="store_true")
    parser.add_argument("--ign", help="ignores preamble and license", action="store_true")
    parser.add_argument("--stats", help="prints out the basic book stats", action="store_true")
    args = parser.parse_args()

    # Upload data.
    data = load_file(args.infile)

    # Here we ignore the preamble and the license, if the user typed --ign.
    if args.ign:
        data = split_text(data, "***", 2)

    #Finally process the data.
    dict_alphabet = letter_counter(data)

    #If the user type --stats, show the basic statistics of the book.
    if args.stats:
        logging.info("Printing basic stats...")
        print("{} total characters. {} total words. {} total lines.".format(len(data), word_counter(data), line_counter(data)))

    # If the user typed --hist, make a histogram of the occurencies.
    if args.hist:
        title_plot = 'Letter occurencies from "Of The Nature of Things" by Lucretius'
        horizontal_hist(dict_alphabet.keys(), dict_alphabet.values(), title_plot)