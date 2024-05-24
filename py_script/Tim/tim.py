#!/usr/bin/python3

import os
import json
import shutil
from subprocess import PIPE, run
import sys

GAME_IDENTIFIER = "game"
GAME_EXTENSION = ".go"

def find_all_game_paths(source):
    '''This function is used to find only the directories with a certain word in their name and return all directories that match it'''

    game_paths = []
    
    for dirpath, dirname, filename in os.walk(source):
        for directory in dirname:
            # print(directory)
            if GAME_IDENTIFIER in directory.lower():
                path = os.path.join(source, directory)
                game_paths.append(path)

        break

    return game_paths

def create_dir(path):
    '''This function is used to create the target directory, if not present'''

    if not os.path.exists(path):
        os.mkdir(path)
        print(f"Created directory: {path}")
    else:
        print(f"Path {path} already exists, thus skipping ahead.")

def get_pathName(paths, stripName):
    '''This function is used to remove the word specified from each matching directories name and return it'''

    changed_dirname = []

    for path in paths:

        _, dir_name = os.path.split(path)
        changed_dirname_name = dir_name.replace(stripName, "")
        changed_dirname.append(changed_dirname_name)

    return changed_dirname

def copy_with_overwrite(source, dest):
    '''This function is used to copy the directories and files recursively which were in the find_all_game_paths directories and place them inside the target folder while copying those directories and files, and if they already exist in target, then remove them recursively'''

    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(source, dest)

def make_json_metadata_file(path, game_dir):
    data = {
        "Game directory names": game_dir,
        "Number of games": len(game_dir)
    }

    with open(path, "w") as f:      #with is used to open the file and also close it after the args end, thus avoiding memory leak or such issues. We use "w" to specify that the file is being opened for write action.
        json.dump(data, f)          #dump is being used to dump all the content of "data" dictionary into the file.

def list_go_files(path):
    files_list = []
    for dirpath, dirname, filename in os.walk(path):
        for file in filename:
            os.chdir(path)
            file_names_list = os.listdir(".")
            for file_name in file_names_list:
                if file_name.endswith(GAME_EXTENSION):
                    files_list.append(file_name)
            break
    if len(files_list) != 0:
        _, dir_name = os.path.split(path)
        print("Directory name: ", dir_name , "and go files in it:", files_list) 
    else:
        _, dir_name = os.path.split(path)
        print("No go files were found in directory:", dir_name)

def main(source, target):
    '''This is the main function'''

    cwd = os.getcwd()                       # Get current working directory
    source_path = os.path.join(cwd, source) # Use os.path.join instead of string concat as concat can lead to issues with different OS, due to the use of different path dividers.
    target_path = os.path.join(cwd, target) 

    game_paths = find_all_game_paths(source_path)

    create_dir(target_path)
    changed_dirname = get_pathName(game_paths, GAME_IDENTIFIER)

    for source, dest in zip(game_paths, changed_dirname):   #zip is used to make tuples of the matching indexes of 2 passed lists.
        dest_path = os.path.join(target_path, dest) 
        copy_with_overwrite(source,dest_path)
    
    for each_folder in changed_dirname:
        list_go_files(os.path.join(target_path, each_folder))

    json_path = os.path.join(target_path, "game_meta.json")
    make_json_metadata_file(json_path, changed_dirname)
    
if __name__ == "__main__":
    args=sys.argv
    if len(args) != 3: #Only accept 2 command line arguments
        raise Exception("Please enter the existing directory name and the target directory name!")
    
    source,target = args[1:]
    main(source, target)
