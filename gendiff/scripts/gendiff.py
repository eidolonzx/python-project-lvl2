#!/usr/bin/env python

import argparse
from gendiff.engine import generate_diff


def main():
    gendiff_desc = 'Compares two configuration files and shows a difference.'
    parser = argparse.ArgumentParser(description=gendiff_desc)
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output',
                        default='json', choices=['plain', 'text', 'json'])
    args = parser.parse_args()
    diff_list = generate_diff(args.first_file, args.second_file, args.format)
    print(diff_list)


if __name__ == '__main__':
    main()
