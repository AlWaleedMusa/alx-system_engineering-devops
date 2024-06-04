#!/usr/bin/python3
"""Query the Reddit API and returns subscribers"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers"""

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    else:
        return 0
