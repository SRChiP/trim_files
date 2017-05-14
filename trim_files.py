#!/usr/bin/env python3

import argparse
import os


def parse_path_arg():
    parser = argparse.ArgumentParser(description="Application to automatically delete old files keeping 'n' "
                                                 "number of files left.")
    parser.add_argument('--path', required=True, dest="folder_path", help="Path of the directory to delete files.")
    parser.add_argument('--file_count', required=False, dest="file_keep_count", type=int, default=3,
                        help="Number of files to keep when deleting the rest of the files of the directory.")
    args = parser.parse_args()
    return os.path.abspath(args.folder_path), args.file_keep_count


def main(folder_path, file_keep_count):
    # Get a list of files in the dir
    file_list = os.listdir(folder_path)
    # Sort files alphabetically
    file_list.sort()
    # Count the number of files that needs to be removed
    number_of_files = len(file_list)
    number_of_files_to_remove = number_of_files - file_keep_count
    number_of_files_to_remove = 0 if number_of_files_to_remove < 0 else number_of_files_to_remove
    removed_file_count = 0
    # Remove files
    print("Found {} files in {}".format(number_of_files, folder_path))
    for i in range(number_of_files_to_remove):
        full_file_path = os.path.abspath(os.path.join(folder_path, file_list[i]))
        try:
            os.remove(full_file_path)
            removed_file_count += 1
        except OSError:
            print("Could not remove file {}".format(full_file_path))
    print("Removed {}/{} files.".format(removed_file_count, number_of_files_to_remove))
    print("At most {} files should be left.".format(file_keep_count))


if __name__ == "__main__":
    main(*parse_path_arg())
