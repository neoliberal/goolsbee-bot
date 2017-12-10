"""class for holding possible goolsbee responses"""
from typing import List, Dict, Any

from tabulate import tabulate

# pylint: disable=R0903
class Response(object):
    """hold response data"""

    def __init__(self, triggers: List[str], table: Dict[str, str]) -> None:
        self.triggers: List[str] = triggers
        self.table: Dict[str, Any] = table

    def __str__(self) -> str:
        """returns formatted table"""
        def vote(level: int) -> str:
            """converts voting number into string"""
            vote_dict: Dict[int, str] = {
                -2: "Strongly Disagree",
                -1: "Disagree",
                0: "Uncertain",
                1: "Agree",
                2: "Strongly Agree"
            }
            return vote_dict[level]

        return tabulate(
            [[
                vote(self.table["vote"]),
                self.table["confidence"],
                self.table["comment"]
            ]],
            headers=["Vote", "Confidence", "Comments"],
            tablefmt="pipe",
            numalign="left"
        )

    def has_words(self, words: List[str]) -> bool:
        """check if all words are found in trigger"""
        return all(trigger in self.triggers for trigger in words)
