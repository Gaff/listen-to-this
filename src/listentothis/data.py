from dataclasses import dataclass

@dataclass
class RedditItem:
    title: str
    url: str
    score: int
