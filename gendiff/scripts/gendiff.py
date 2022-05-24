#!/usr/bin/env python

import argparse
from ..generate_diff import generate_diff


def main():
    gendiff_desc = 'Compares two configuration files and shows a difference.'
    parser = argparse.ArgumentParser(description=gendiff_desc)
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output',
                        default='stylish', choices=['plain', 'stylish', 'json'])
    args = parser.parse_args()
    result = generate_diff(args.first_file, args.second_file, args.format)
    print(result)


if __name__ == '__main__':
    main()
