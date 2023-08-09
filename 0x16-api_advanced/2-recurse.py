#!/usr/bin/python3
"""Module for a recursive function"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """Queries the Reddit API and returns a list containing the
    titles of all hot articles for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'My-User-Agent'}
    params = {'count': count, 'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        for i in range(len(response.json().get('data').get('children'))):
            hot_list.append(response.json().get('data').get('children')
                            [i].get('data').get('title'))
        after = response.json().get('data').get('after')
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after, params.get(cont))
    else:
        return None
