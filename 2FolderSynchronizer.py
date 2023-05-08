import argparse


def argparser():
    """Store user input and return as Namespace object"""
    parser = argparse.ArgumentParser(prog="2FolderSynchronizer", description="Synchronizing content of input folders")
    parser.add_argument("-s", "--source", required=True, help="Path of Source folder")
    parser.add_argument("-r", "--replica", required=True, help="Path of Replica folder")
    parser.add_argument("-l", "--log", required=True, help="Output file path to log file")

    args = parser.parse_args()
    return args


def main():
    p = argparser()


if __name__ == "__main__":
    main()
