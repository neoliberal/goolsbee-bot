"""main entry point"""
import argparse
from os import environ

import praw

from .goolsbee import Goolsbot

def main() -> None:
    """main function"""
    args: argparse.Namespace = arguments().parse_args()
    reddit = praw.Reddit(
        client_id=args.client_id,
        client_secret=args.client_secret,
        refresh_token=args.refresh_token,
        user_agent="linux: goolsbee_bot 1.0.0 (by /u/CactusChocolate)"
    )
    bot: Goolsbot = Goolsbot(reddit, args.subreddits)
    while True:
        bot.run()

def arguments() -> argparse.ArgumentParser:
    """make argument parser"""
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="Goolsbee Bot"
    )
    parser.add_argument(
        "subreddits", metavar='S', type=str, nargs='+',
        help="Subreddits to browse"
    )
    parser.add_argument(
        "--client_id", dest="client_id", type=str, nargs='?',
        default=environ.get("goolsbot_client_id"),
        help="Client ID of reddit script"
    )
    parser.add_argument(
        "--client_secret", dest="client_secret", type=str, nargs='?',
        default=environ.get("goolsbot_client_secret"),
        help="Client secret of reddit script"
    )
    parser.add_argument(
        "--refresh_token", dest="refresh_token", type=str, nargs='?',
        default=environ.get("goolsbee_refresh_token"),
        help="Refresh token of reddit script"
    )
    return parser

if __name__ == "__main__":
    main()
