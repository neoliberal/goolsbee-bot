#!/usr/bin/python3.6
"""not stupid"""
import json
import random
from typing import List, Dict, Any

import praw
from slack_python_logging import slack_logger

from .response import Response

class Goolsbot(object):
    """goolsbot class"""

    def __init__(self: Goolsbot, reddit: praw.Reddit, subreddits: List[str]) -> None:
        self.logger = slack_logger.initialize("goolsbee-bot")
        self.logger.debug("Intializing")

        self.logger.debug("Logging into reddit")
        self.reddit: praw.Reddit = reddit
        self.logger.debug("Logged into reddit")

        self.logger.debug("Validating subreddits")
        self.subreddits: List[praw.models.Subreddit] = []
        for subreddit in subreddits:
            try:
                self.subreddits.append(self.reddit.subreddit(subreddit))
            except praw.exceptions.APIException:
                self.logger.warning("\"%s\" is an invalid subreddit, skipping", subreddit)
        self.logger.debug("Validated subreddits")

        with open("replied_comments.txt") as replied:
            self.commented: List[str] = replied.read().split()

        self.logger.debug("Opening responses")
        with open("data/responses.json") as responses:
            res_list: List[Dict[str, Any]] = json.loads(responses.read())
            self.responses: List[Response] = [
                Response(item["image"], item["text"], item["triggers"]) for item in res_list
            ]
        self.logger.debug("Opened responses")
        self.logger.info("goolsbee-bot intialized successfully")
        return

    import string
    punc_remover = str.maketrans('', '', string.punctuation)
    def run(self: Goolsbot) -> None:
        """run the main code"""
        for subreddit in self.subreddits:
            for comment in subreddit.stream.comments():
                if not comment.author == self.reddit.user.me():
                    if str(comment) not in self.commented:
                        text: List[str] = comment.body.translate(self.punc_remover).lower().split()
                        combos: List[Response] = [
                            response for response in self.responses
                            if response.has_words(text)
                        ]
                        if combos:
                            self.write_comment(random.choice(combos), comment)
                        elif "goolsbee" in text:
                            self.write_comment(
                                random.choice(self.responses), comment
                            )

    # pylint: disable=R0201
    def write_comment(self: Goolsbot, response: Response, comment: praw.models.Comment) -> None:
        """log comment and writes to file"""
        with open('replied_comments.txt', 'a') as file:
            file.write(str(comment))
            file.write(' ')

        if random.randint(1, 21) == 1:
            try:
                comment.reply(str(response))
            except praw.exceptions.APIException as reddit_error:
                print(reddit_error)
                return
            print("Comment passed")
            return

        print("Comment written")
        return


if __name__ == '__main__':
    bot: Goolsbot = Goolsbot(praw.Reddit("Goolsbee"), ["neoliberal"])
    while True:
        bot.run()
