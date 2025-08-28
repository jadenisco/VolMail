import logging
import argparse

# Files
root_files = './files/'

# Log files
log_file = root_files + 'log.txt'

# Debug
dry_run = False

'''
Send an email
'''
def send_mail(args):
    print("Send mail")
    return 0


def _v_mail(args):
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    logging.FileHandler(log_file)

    if args.dry_run:
        dry_run = True

    if args.func:
        return args.func(args)
    else:
        return 0


def setup_debug(): 
    logger = logging.getLogger("")
    logging.basicConfig(level=logging.DEBUG)
    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter("%(asctime)s %(levelname)s : %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='VolMail',
                                        description='These function allow the user to send an email',
                                        epilog='See "%(prog)s help COMMAND" for help on a specific command.')
    parser.add_argument('--debug', '-d', action='count', help='Print debug output')
    parser.add_argument('--dry-run', '-dr', action='count', help='Execute a dry run')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    send_parser = subparsers.add_parser('send', help='Send an email')
    send_parser.set_defaults(func=send_mail)

    args = parser.parse_args()

    if args.debug:
        setup_debug()

    if args.dry_run:
        dry_run = True

    if args.command:
        args.func(args)
    else:
        parser.print_help()





#    _v_mail(main_args)
