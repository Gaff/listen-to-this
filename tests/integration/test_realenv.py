import pytest
from listentothis import env, listen_to_this


def test_env():
    env.setup_gcloud_json("allsecretsjson")
    assert env.get("id") == "allsecretsjson"

def test_listentothis():
    ltt = listen_to_this.ListenToThis()
