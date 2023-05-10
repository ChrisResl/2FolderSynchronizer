import argparse

def argparser():
    """Store user input and return as Namespace object"""
    parser = argparse.ArgumentParser(prog="2FolderSynchronizer", description="Synchronizing content of input folders")
    parser.add_argument("-s", "--source", required=True, help="Path of Source folder")
    parser.add_argument("-r", "--replica", required=True, help="Path of Replica folder")
    parser.add_argument("-i", "--interval", nargs="?", default=10, type=int, help="Synchronization interval in seconds")
    parser.add_argument("-l", "--log", required=True, help="Output file path of log file")

    args = parser.parse_args()
    return args
