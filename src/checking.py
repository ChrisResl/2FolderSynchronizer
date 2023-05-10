import os


def checking_procedure(source, replica, log):
    """Checking provided command line input paths if valid
    :param source: string of path to source directory
    :param replica: string of path to replica directory
    :param log: string of path to log output file
    """
    check_directory_path(source)
    check_directory_path(replica)
    check_log_path(log)


def check_directory_path(path):
    """Checking if directory exists
    :param path: string
    """
    if not os.path.isdir(path):
        print(path + " is not a directory.\nPlease provide a proper directory path.")
        exit()


def check_log_path(log):
    """Checking if log path is correct
    :param log: string of path to log output file
    """
    try:
        with open(log, "w") as f:
            f.close()
    except FileNotFoundError:
        print(log + " is an incorrect path.\nPlease provide a proper one.")
        exit()
