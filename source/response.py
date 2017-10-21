"""class for handling possible goolsbee responses"""
import json
from typing import List, Dict, Any


class Response(object):
    """hold response data"""

    def __init__(self: Response, image: str, text: str, triggers: List[str]) -> None:
        self.image = image
        self.text = text
        self.triggers = triggers

    def has_word(self: Response, words: List[str]) -> bool:
        """check if any words are in trigger"""
        return any((True for word in words if word in self.triggers))

    def __str__(self: Response) -> str:
        """returns formatted link"""
        return "[{1}]({2})".format(self.text, self.image)