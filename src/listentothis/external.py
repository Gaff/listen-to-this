from praw import Reddit as PrawReddit
from listentothis import environment
from .data import RedditItem

class Reddit:
    def __init__(self, env=None):
        if env is None:
            env = environment.env

        self.reddit = PrawReddit(client_id=env.get("reddit-client"),
                                 client_secret=env.get("reddit-key"),
                                 user_agent="Listen To This script")

    def query_reddit(self, subreddit: str = "listentothis", time_filter: str = "week"):
        query = self.reddit.subreddit(subreddit).top(
            time_filter=time_filter, limit=100)

        return (RedditItem(
            title=x.title,
            url=x.url,
            score=x.score
        ) for x in query)
