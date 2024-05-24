#!/usr/bin/python3

import os
import sys
import shutil

def store_filename(path):
    '''This is a function to store filenames inside a specified directory and return the list'''
    path_filenames = []

    for dirpath, dirname, filename in os.walk(path):
        for file in filename:
            path_filenames.append(file)
    return path_filenames

def main(source, target):
    '''This is the main function'''
    cwd = os.getcwd()
    source_path = os.path.join(cwd, source)
    target_path = os.path.join(cwd, target)

    source_files_list = store_filename(source_path)
    target_files_list = store_filename(target_path)

    print(set(source_files_list) & set(target_files_list))



if __name__ == "__main__":
    args=sys.argv
    if len(args) != 3:
        raise Exception("Please provide the source and destination folder!")
    
    source, target = args[1:]

    main(source, target)
