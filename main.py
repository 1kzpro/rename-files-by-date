import sys
import argparse
import os
from pathlib import Path, PurePath

def rename_files_by_date(working_directory: str, prefix: str, index: int = 1) -> None:
    paths = sorted(Path(working_directory).iterdir(), key=os.path.getctime)
    for i, path in enumerate(paths):
        new_filename = prefix + " " + str(i + index) + path.suffix
        new_file_path = PurePath(path.parent, new_filename)
        path.rename(new_file_path)

if __name__ == '__main__':
    # Initialize parser
    parser = argparse.ArgumentParser()
    
    # Adding optional argument
    parser.add_argument("-d", "--Directory", help = "Working Directory")
    parser.add_argument("-p", "--Prefix", help = "File prefix")
    parser.add_argument("-i", "--Index", help = "Starting index")
    
    # Read arguments from command line
    args = parser.parse_args()
    
    if not args.Directory:
        print("Specify a directory")
        sys.exit()
    working_directory = args.Directory

    if not args.Prefix:
        print("Specify a Prefix")
        sys.exit()
    prefix = args.Prefix

    if args.Index:
        index = int(args.Index)
    else:
        print("Starting index is not specified, therefore defaulting to 1")
        index = 1
    
    print("Executing command...")
    rename_files_by_date(working_directory, prefix, index)
    print("Success.")