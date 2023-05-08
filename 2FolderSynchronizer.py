import argparse
import os
import shutil
import datetime


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


def write_to_log(log, message):
    with open(log, "a+") as f:
        f.write(message)
        f.close()


def deletion(source, replica, log):

    source_structure = dict.fromkeys(os.listdir(source))
    replica_structure = dict.fromkeys(os.listdir(replica))

    for rel_path in replica_structure:
        if rel_path not in source_structure:
            abs_path = os.path.join(replica, rel_path)
            if os.path.isdir(abs_path):
                shutil.rmtree(abs_path)
                print("Directory " + rel_path + " was deleted")
                write_to_log(log, "Directory " + rel_path + " was deleted\n")
            else:
                os.remove(abs_path)
                print("File " + rel_path + " was deleted")
                write_to_log(log, "File " + rel_path + " was deleted\n")


def backup(source, replica, log):
    source_structure = dict.fromkeys(os.listdir(source))
    replica_structure = dict.fromkeys(os.listdir(replica))

    if len(source_structure) == 0:
        return
    else:
        for rel_path in source_structure:
            abs_path_source = os.path.join(source, rel_path)
            abs_path_replica = os.path.join(replica, rel_path)

            # in case file/directory is only present in source
            if rel_path not in replica_structure:
                if os.path.isfile(abs_path_source):
                    shutil.copy2(abs_path_source, abs_path_replica)
                    print("File " + rel_path + " was created")
                    write_to_log(log, "File " + rel_path + " was created\n")
                else:
                    os.makedirs(abs_path_source)
                    print("Directory " + rel_path + " was created")
                    write_to_log(log, "Directory " + rel_path + " was created\n")
                    backup(abs_path_source, abs_path_replica, log)
            # in case file/directory is present in both
            else:
                if os.path.isfile(abs_path_source):
                    shutil.copy2(abs_path_source, abs_path_replica)
                    print("File " + rel_path + " was copied")
                    write_to_log(log, "File " + rel_path + " was copied\n")
                else:
                    print("Directory " + rel_path + " was copied")
                    write_to_log(log, "Directory " + rel_path + " was copied\n")
                    backup(abs_path_source, abs_path_replica, log)


def synchronization(source, replica, interval, log):
    write_to_log(log, "Synchronization between folder " +source + " and folder "+ replica + " performed at " + str(datetime.datetime.now()) + "\n")

    # deleting files in replica
    deletion(source, replica, log)
    # creating and copying (to) files/directories in replica
    backup(source, replica, log)


def main():
    p = argparser()

    check_directory_path(p.source)
    check_directory_path(p.replica)

    synchronization(p.source, p.replica, p.interval, p.log)


if __name__ == "__main__":
    main()
