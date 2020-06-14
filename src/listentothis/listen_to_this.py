from praw import Reddit

class ListenToThis:
    def __init__(self, env):
        self.reddit = Reddit(client_id=env.get("reddit-client"),
                     client_secret=env.get("reddit-key"),
                     user_agent="Listen To This script")

    def queryReddit(self, subreddit):
        return ""
