#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -----------------------------------------
# Written by http://www.ryanyonzon.com/
# -----------------------------------------

import argparse
import uuid

from itertools import product

def main(args):

    char_length = args.length
    prefix = args.prefix
    output = args.output
    iterables = args.iterables

    if iterables is None:
        iterables = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ' # Default iterables    

    if prefix is None:
        prefix = ''

    if output is None:
        output = str(uuid.uuid4()) + '.lst'

    output_file = open(output, 'wb') # Prepare output file
    keywords = [''.join(i) for i in product(iterables, repeat=int(char_length))]
    for val in keywords:
        output_string = prefix + val + "\n"
        output_file.write(bytes(output_string, 'UTF-8'))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-l", "--length", help="Character length (Required)", required=True)
    parser.add_argument("-p", "--prefix", help="Prefix character or string", required=False)
    parser.add_argument("-o", "--output", help="Output file name", required=False)
    parser.add_argument("-i", "--iterables", help="Iterable characters (e.g. ABC123)", required=False)

    args = parser.parse_args()

    main(args)
