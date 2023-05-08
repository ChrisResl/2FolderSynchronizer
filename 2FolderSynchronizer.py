import argparse
import os

def argparser():
    """Store user input and return as Namespace object"""
    parser = argparse.ArgumentParser(prog="2FolderSynchronizer", description="Synchronizing content of input folders")
    parser.add_argument("-s", "--source", required=True, help="Path of Source folder")
    parser.add_argument("-r", "--replica", required=True, help="Path of Replica folder")
    parser.add_argument("-i", "--interval", nargs="?", default=1, help="Synchronization interval")
    parser.add_argument("-l", "--log", required=True, help="Output file path to log file")

    args = parser.parse_args()
    return args

def check_directory_path(path):
    """Checking if directory exists
    :param path: string
    """
    if not os.path.isdir(path):
        print(path + " is not a directory.\nPlease provide a proper directory path.")
        exit()


def main():
    p = argparser()

    check_directory_path(p.source)
    check_directory_path(p.replica)


if __name__ == "__main__":
    main()
