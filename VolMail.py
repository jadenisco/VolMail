import logging
import argparse

# Files
root_files = './files'

# Log files
log_file = root_files + 'log.txt'

# Debug
dry_run = False

'''
Send an email
'''
def send(args):
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


def setup_debug(debug=False): 
    logger = logging.getLogger("")
    if debug == True:
        logging.basicConfig(level=logging.DEBUG)
    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter("%(asctime)s %(levelname)s : %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)


if __name__ == '__main__':
    main_parser = argparse.ArgumentParser(
    prog='va_utils',
        description='These utilities support the volunteer app.',
        epilog='See "%(prog)s help COMMAND" for help on a specific command.')
    main_parser.add_argument('--debug', '-d', action='count', help='Print debug output')
    main_parser.add_argument('--dry-run', '-dr', action='count', help='Execute a dry run')
    sub_parsers = main_parser.add_subparsers()

    cr_parser = sub_parsers.add_parser('send', help='Send an email')
    cr_parser.set_defaults(func=send)

    main_args = main_parser.parse_args()
    _v_mail(main_args)
