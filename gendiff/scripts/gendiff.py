#!/usr/bin/env python

import argparse
from gendiff.engine import generate_diff
from gendiff.render import render_diff_result


def main():
    gendiff_desc = 'Compares two configuration files and shows a difference.'
    parser = argparse.ArgumentParser(description=gendiff_desc)
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output',
                        default='json', choices=['plain', 'text', 'json'])
    args = parser.parse_args()
    diff_list = generate_diff(args.first_file, args.second_file)
    result = render_diff_result(diff_list, args.format)
    print(result)


if __name__ == '__main__':
    main()
