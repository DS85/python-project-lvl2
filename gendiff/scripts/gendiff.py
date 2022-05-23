#!/usr/bin/env python

from gendiff.cmd_parser import parser
from gendiff.generate_diff import generate_diff


def main():
    file1, file2, format = parser()
    result = generate_diff(file1, file2, format)
    print(result)


if __name__ == '__main__':
    main()
