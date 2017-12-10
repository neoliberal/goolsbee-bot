"""class for holding possible goolsbee responses"""
from typing import List

# pylint: disable=R0903
class Response(object):
    """hold response data"""

    def __init__(self: Response, image: str, text: str, triggers: List[str]) -> None:
        self.image = image
        self.text = text
        self.triggers = triggers

    def __str__(self: Response) -> str:
        """returns formatted link"""
        return "[{1}]({2})".format(self.text, self.image)

    def has_words(self: Response, words: List[str]) -> bool:
        """check if all words are found in trigger"""
        return any((x for x in self.triggers if x in words))
