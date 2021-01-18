import argparse
from .organizer import Organizer


def main():

    parser = argparse.ArgumentParser(
        prog="pythod",
        description="Load CLI flags for the Pythod organizer.",
        usage="pythod --dir /absolute/path/to/directory/for/organizing"
    )

    parser.add_argument(
        "--config",
        nargs="?",
        type=str,
        help="Path to your custom configuration file. If no passed, will load the default one.",
    )

    parser.add_argument(
        "--dir",
        type=str,
        help="Path to the directory that will be organized.",
        required=True
    )

    cli_arguments = parser.parse_args()

    if cli_arguments.config == None:
        print('>>> Default configuration will be loaded.')

    organizer = Organizer(cli_arguments.dir, cli_arguments.config)
    organizer.organize()
