#!/usr/bin/python3
"""
This script queries the Reddit API and
returns a list containing
the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit, the
function should return None.
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Fn returns a list containing the titles of all hot
    articles for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    if after:
        headers["after"] = after
        url = f"{url}?after={after}"
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json()["data"]
            after = data.get("after", None)
            for post in data["children"]:
                hot_list.append(post["data"]["title"])
            if after:
                recurse(subreddit, hot_list, after)
                return hot_list
            return hot_list
        except Exception as e:
            return None
    else:
        return None
