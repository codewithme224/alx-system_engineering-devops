#!/usr/bin/python3
"""Module for Reddit API quering"""
import requests


def top_ten(subreddit):
    """Queries the Reddit API and returns the top 10
    hot posts    of the subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'My-User-Agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        for i in range(10):
            print(response.json().get('data').get('children')
                  [i].get('data').get('title'))
    else:
        print(None)
