#!/usr/bin/env python3

'''
Author: <Name>
Date: <Date>
Description: <Description>
Parameters:
    Inputs:
        <Input 1>
    Outputs:
        <Output 1>
Notes: <Notes>
Examples:
    <Example 1>

    <Example 2>
'''

import os
import sys
import argparse


def main(arguments):

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('infile', help="Input file", type=argparse.FileType('r'))
    parser.add_argument('-o', '--outfile', help="Output file",
                        default=sys.stdout, type=argparse.FileType('w'))

    args = parser.parse_args(arguments)

    print(args)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
