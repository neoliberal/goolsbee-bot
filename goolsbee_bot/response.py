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
        return f"[{self.text}]({self.image})"

    def has_words(self: Response, words: List[str]) -> bool:
        """check if all words are found in trigger"""
        return any((trigger for trigger in self.triggers if trigger in words))
