#! /usr/bin/env python3
'''Module to setup desired Dune product. It set ups different configs
and environments to allow VSCode and other scripts work correctly

Returns:
    env files: can return different env files:
                .env-setup, .env-target
    output strings: can return different strings that allows
                to VSCode Prompts get them
'''
import sys
import argparse
import os

def check_lists(args):

    """
        Checks list arguments and it prints desired options if matching
        list command
        Args:
            args: arguments from the user
    """

    if args.list_families:
        print('family_1')
        print('family_2')

        sys.exit(0)
    if args.list_family_os:
        print('os_1_for_{}'.format(args.family))
        print('os_2_for_{}'.format(args.family))
        sys.exit(0)

def main(arguments):
    '''
    Main for setup.py
    Calls check_list method to check if any list option has been passed
    by argument
    Calls save_setup_session to persist setup done for Dune in .env-setup

    Args:
        arguments ([parameter]): [Given Arguments]
    '''

    args, remaining_args = arguments

    if args.list_family_os and not args.family:
        print("ERROR: --family argument must be provided")
        sys.exit(1)

    # Check if any list argument has been given. If yes print list options and exits
    check_lists(args)


    if (not args.family) or (not args.os):
        print("ERROR: --family <family> --os <os> arguments must be provided to complete the job")
        sys.exit(1)

    if ( args.family) and ( args.os):
        print("SUCCESS")
        sys.exit(0)

if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(os.path.basename(__file__))
    PARSER.add_argument('--family', '-f', help="Product Family")
    PARSER.add_argument('--os', '-o', default="ubuntu", help="Product's Target OS")
    list_family_opts = PARSER.add_mutually_exclusive_group(required=False)
    list_family_opts.add_argument('--list_families', action='store_true', help="Product Family")
    list_family_opts.add_argument('--list_family_os', action='store_true', help="Product's Target OS")


    sys.exit(main(PARSER.parse_known_args()))
