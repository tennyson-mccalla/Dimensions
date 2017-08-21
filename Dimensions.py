#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Script to get the dimensions of images in a directory and list them"""

import sys
from os import listdir
from PIL import Image


folder = sys.argv[1]


def main():
    """Where the real fun begins"""
    pics = get_image_names_and_sizes(folder)
    for pic in sorts(pics):
        print(f'{pic[0]} {pic[1]} {pic[2]}')


def get_image_names_and_sizes(dir):
    """Gets the filenames and image sizes as a 3-tuple, returns a list"""
    lis = []
    for f in listdir(dir):
        if '.DS_Store' in f:
            continue
        try:
            im = Image.open(dir + f)
            lis.append((f, im.size, im.format))
        except OSError:
            continue
    return lis


def sorts(lis):
    """Present the options for sorting (H, W, or A) then print to bash"""
    option = input("Sort by height (H), width (W), or area (A)? ").upper()
    if option == 'H':
        return sorted(lis, key=lambda dim: dim[1][1])
    elif option == 'W':
        return sorted(lis, key=lambda dim: dim[1][0])
    elif option == 'A':
        return sorted(lis, key=lambda dim: dim[1][0] * dim[1][1])
    else:
        return lis


if __name__ == '__main__':
    sys.exit(main())
