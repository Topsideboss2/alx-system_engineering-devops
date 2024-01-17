#!/usr/bin/python3

""" Module that queries the Reddit API """

import requests
import sys

def recurse(subreddit, hot_list=[]):
    """ Function that queries the Reddit API and returns a list containing
        the titles of all hot articles for a given subreddit. If no results
        are found for the given subreddit, the function should return None. """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77\
               Safari/537.36"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        for post in response.json().get("data").get("children"):
            hot_list.append(post.get("data").get("title"))
            after = response.json().get("data").get("after")
        if after is not None:
            recurse(subreddit, hot_list)
        return hot_list
    else:
        return None