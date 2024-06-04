#!/usr/bin/python3
"""Query the Reddit API and returns the number of times a word appears in the titles of hot articles for a given subreddit"""

import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    """Counts the number of times a word appears in the titles of hot articles for a given subreddit"""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        for post in response.json().get("data").get("children"):
            title = post.get("data").get("title")
            for word in word_list:
                if word.lower() in title.lower():
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1

        after = response.json().get("data").get("after")
        if after is not None:
            return count_words(subreddit, word_list, word_count, after)

        if len(word_count) == 0:
            return None

        for word in sorted(word_count.keys()):
            print(f"{word}: {word_count[word]}")
    else:
        print(None)
