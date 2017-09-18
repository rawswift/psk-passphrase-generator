#!/usr/bin/python

# -------------------------
# Written by Ryan Yonzon
# http://www.ryanyonzon.com/
# -------------------------

import sys
import getopt
import uuid
import os
from itertools import product

def main(argv):

    char_length = None
    prefix = ''
    output = str(uuid.uuid4())
    # Default iterables
    iterables = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Check parameters
    try:
        opts, args = getopt.getopt(argv, "hl:i:p:o:", ["help", "iterable=", "length=", "prefix=", "output="])
    except getopt.GetoptError:
        print ('psk-passphrase-generator.py -l <LENGTH> -p <PREFIX> -o <OUTPUT FILE> -i <ITERABLES>')
        sys.exit(2)

    # Get parameter values
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('psk-passphrase-generator.py -l <LENGTH> -p <PREFIX> -o <OUTPUT FILE> -i <ITERABLES>')
            sys.exit()
        elif opt in ("-l", "--length"):
            char_length = arg
        elif opt in ("-p", "--prefix"):
            prefix = arg
        elif opt in ("-o", "--output"):
            output = arg
        elif opt in ("-i", "--iterable"):
            iterables = arg

    # Character length is required
    if char_length is None:
        print ('psk-passphrase-generator.py -l <LENGTH> -p <PREFIX> -o <OUTPUT FILE> -i <ITERABLES>')
        sys.exit(2)
    else:
        # Prepare and write on file output
        output_file = open(output, 'wb')
        keywords = [''.join(i) for i in product(iterables, repeat=int(char_length))]
        for val in keywords:
            output_string = prefix + val + "\n"
            output_file.write(bytes(output_string, 'UTF-8'))

if __name__ == "__main__":

    try:
        arg1 = sys.argv[1]
    except IndexError:
        print('psk-passphrase-generator.py -l <LENGTH> -p <PREFIX> -o <OUTPUT FILE> -i <ITERABLES>')
        sys.exit(1)

    main(sys.argv[1:])
