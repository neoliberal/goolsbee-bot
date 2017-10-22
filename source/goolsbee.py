#!/usr/bin/python3.6
"""not stupid"""
import json
import random
from typing import List, Dict, Any, Optional
import string

import praw

from .response import Response


class Goolsbot(object):
    """goolsbot class"""

    def __init__(self: Goolsbot) -> None:
        self.reddit: praw.Reddit = praw.Reddit('Goolsbee')
        with open("replied_comments.txt") as replied:
            self.commented: List[str] = replied.read().split()

        with open("data/responses.json") as responses:
            res_list: List[Dict[str, Any]] = json.loads(responses.read())["responses"]
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
                if str(comment) not in self.commented:
                    text: List[str] = str(comment.body).translate(punc_remover).lower().split()
                    combos: Optional[List[Response]] = [
                        response for response in self.responses for
                        word in text if word in response.triggers
                    ]
                    if combos:
                        self.write_comment(random.choice(combos), comment)
                    elif 'goolsbee' in text:
                        self.write_comment(
                            random.choice(self.responses), comment)

    def write_comment(self: Goolsbot, response: Response, comment: praw.models.Comment) -> None:
        """log comment and writes to file"""
        with open('replied_comments.txt', 'a') as file:
            file.write(str(comment))
            file.write(' ')

        if random.randint(1, 21) == 1:
            print("Comment passed")
            return

        comment.reply(str(response))
        print("Comment written")
        return

if __name__ == '__main__':
    Goolsbot()
