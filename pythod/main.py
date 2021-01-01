import argparse
from .organizer import Organizer


def main():

    parser = argparse.ArgumentParser(
        description="Load CLI flags for the Pythod organizer.")

    parser.add_argument(
        "--config",
        type=str,
        help="Path to your custom configuration file. If no passed, will load the default one.",
    )

    parser.add_argument(
        "--dir",
        nargs="?",
        type=str,
        help="Path to the directory that will be organized.",
    )

    cli_arguments = parser.parse_args()

    if cli_arguments.config == None:
        print('>>> Default configuration will be loaded.')

    organizer = Organizer(cli_arguments.dir, cli_arguments.config)
    organizer.organize()
