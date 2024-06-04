#!/usr/bin/python3
"""Query the Reddit API and returns the top 10 posts"""

import requests


def top_ten(subreddit):
    """Returns the top 10 posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        for post in response.json().get("data").get("children"):
            print(post.get("data").get("title"))
    else:
        print(None)
