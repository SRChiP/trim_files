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


def main(dir, file_keep_count):
    # Get a list of files in the dir
    file_list = os.listdir(dir)
    # Sort files alphabetically
    file_list.sort()
    # Count the number of files that needs to be removed
    number_of_files = len(file_list)
    number_of_files_to_remove = number_of_files - file_keep_count
    number_of_files_to_remove = 0 if number_of_files_to_remove < 0 else number_of_files_to_remove
    removed_file_count = 0
    # Remove files
    for i in range(number_of_files_to_remove):
        full_file_path = os.path.abspath(os.path.join(dir, file_list[i]))
        try:
            os.remove(full_file_path)
            removed_file_count += 1
        except OSError:
            print(f"Could not remove file {full_file_path}")
    print(f"Removed {removed_file_count}/{number_of_files_to_remove} files.")
    print(f"At most {file_keep_count} files should be left.")


if __name__ == "__main__":
    main(*parse_path_arg())
