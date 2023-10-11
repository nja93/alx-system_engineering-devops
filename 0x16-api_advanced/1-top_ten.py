#!/usr/bin/python3
"""
this script prints the titles of the first 10 hot posts
listed for a subreddit
"""
import requests


def top_ten(subreddit):
    """
    If not a valid subreddit, print None.'''
    this can be useed as an alternative to the codes below'''
    url = ('https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit))
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("None")
    else:
        try:
            data = response.json()["data"]
            count = 1
            for post in data["children"]:
                if count <= 10:
                    print(count, post["data"]["title"])
                count += 1
            return 0
        except Exception as e:
            print("None")
