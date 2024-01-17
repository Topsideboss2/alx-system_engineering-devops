#!/usr/bin/python3

""" Module to query the Reddit API """

import sys
import requests

def top_ten(subreddit):
    """ Function that queries the Reddit API and prints the titles of the
        first 10 hot posts listed for a given subreddit. If not a valid
        subreddit, print None. """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77\
               Safari/537.36"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        for post in response.json().get("data").get("children"):
            print(post.get("data").get("title"))
    else:
        print(None)