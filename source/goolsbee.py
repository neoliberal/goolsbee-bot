#!/usr/bin/python3.6
"""not stupid"""
import json
import random
from typing import List, Dict, Any
import string

import praw

from .response import Response

class Goolsbot(object):
    """goolsbot class"""

    def __init__(self: Goolsbot) -> None:
        """initialize"""
        self.reddit: praw.Reddit = praw.Reddit('Goolsbee')
        self.commented: List[str] = open("replied_comments.txt").read().split()
        with open("data/responses.json") as responses_file:
            res_list: List[Dict[str, Any]] = json.loads(responses_file.read())["responses"]
            self.responses: List[Response] = [
                Response(item["image"], item["text"], item["triggers"]) for item in res_list
                ]

        while True:
            self.run()

    def run(self: Goolsbot) -> None:
        """run the main code"""
        punc_remover = str.maketrans('', '', string.punctuation)
        for comment in self.reddit.subreddit('neoliberal').stream.comments():
            if not comment.author == self.reddit.user.me():
                text: List[str] = str(comment.body).translate(punc_remover).lower().split()
                if str(comment) not in self.commented:

                    if 'bitcoin' in text:
                        self.write_comment(16, comment)

                    elif 'anime' in text:
                        self.write_comment(5, comment)

                    elif 'democracy' in text:
                        self.write_comment(27, comment)

                    elif 'stupid' in text:
                        self.write_comment(26, comment)

                    elif 'tax' in text and 'cuts' in text:
                        self.write_comment(20, comment)

                    elif 'cut' in text and 'taxes' in text:
                        self.write_comment(20, comment)

                    elif 'cutting' in text and 'taxes' in text:
                        self.write_comment(20, comment)

                    elif 'tea' in text and 'party' in text:
                        self.write_comment(20, comment)

                    elif 'gold' in text and 'standard' in text:
                        self.write_comment(0, comment)

                    elif 'bernie' in text and 'would' in text and 'have' in text and 'won':
                        self.write_comment(25, comment)

                    elif 'coal' in text and 'miners' in text:
                        self.write_comment(2, comment)

                    elif 'goolsbee' in text:
                        rint: int = random.randint(0, 24)
                        self.write_comment(rint, comment)

    def write_comment(self: Goolsbot, i: int, comment: praw.models.Comment) -> None:
        """writes comment to user"""
        responses: List[str] = open("Replies.txt").read().split("\n")
        response: str = responses[i]
        self.log_comment(comment)
        if random.randint(1, 11) == 1:
            comment.reply(response)
            print('Comment written')
            return

        print('Comment passed')
        return

    def log_comment(self: Goolsbot, comment: praw.models.Comment) -> None:
        """log comment to file"""
        with open('replied_comments.txt', 'a') as file:
            file.write(str(comment))
            file.write(' ')


if __name__ == '__main__':
    Goolsbot()
