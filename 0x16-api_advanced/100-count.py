#!/usr/bin/python3
"""Module for recursive function"""
import requests


def count_words(subreddit, word_list):
    """Queries the Reddit API, parses the title of all hot
    articles, and prints a sorted count of given keywords"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'My-User-Agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        for i in range(len(response.json().get('data').get('children'))):
            for word in word_list:
                if word.lower() in response.json().get('data').get('children')
                [i].get('data').get('title').lower():
                    print(word.lower())
    else:
        print(None)
