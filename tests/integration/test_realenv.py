import pytest
from listentothis import env, Reddit



env.setup_gcloud_json("allsecretsjson")
assert env.get("id") == "allsecretsjson"

def test_reddit():
    ltt = Reddit()
    data = ltt.query_reddit()
    data = list(data)
    assert len(data) > 50
