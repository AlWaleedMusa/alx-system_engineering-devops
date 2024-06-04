#!/usr/bin/python3
"""Query the Reddit API and returns a list of titles for all hot articles to a given subreddit"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of titles for all hot articles to a given subreddit"""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        for post in response.json().get("data").get("children"):
            hot_list.append(post.get("data").get("title"))

        after = response.json().get("data").get("after")
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
