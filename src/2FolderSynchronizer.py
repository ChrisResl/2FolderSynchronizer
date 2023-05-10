import argumentParser
import checking
import synchro


def main():

    p = argumentParser.argparser()

    checking.checking_procedure(p.source, p.replica, p.log)

    synchro.synchronization(p.source, p.replica, p.interval, p.log)


if __name__ == "__main__":
    main()
