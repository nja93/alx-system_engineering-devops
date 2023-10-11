#!/usr/bin/python3
"""
This script querries  the Reddit API and returns the number of subscribers
NOT  active users NOT  total subscribers for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the no of subscribers
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    """
    SEND get request to the subreddit api
    """
    response = requests.get(url, headers=headers, allow_redirects=False)

    try:
        data = response.json()["data"]
        subscribers = data["subscribers"]
        return subscribers
    except Exception as e:
        return 0
