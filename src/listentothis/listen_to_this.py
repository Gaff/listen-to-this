from praw import Reddit
from listentothis import environment


class ListenToThis:
    def __init__(self, env=None):
        if env is None:
            env = environment.env

        self.reddit = Reddit(client_id=env.get("reddit-client"),
                             client_secret=env.get("reddit-key"),
                             user_agent="Listen To This script")

    def query_reddit(self, _subreddit):
        return self.reddit

    def another_public_method(self):
        # pylint is harsh!
        return self.reddit
