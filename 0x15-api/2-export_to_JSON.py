#!/usr/bin/python3
"""script to export data in the JSON format"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    """script to export data in the JSON format"""
    url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    url2 = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            argv[1])
    response = requests.get(url)
    response2 = requests.get(url2)
    json_obj = response.json()
    json_obj2 = response2.json()
    name = json_obj.get('username')
    json_dict = {}
    json_dict[argv[1]] = []

    for task in json_obj2:
        json_dict[argv[1]].append({"task": task.get('title'), "completed":
                                   task.get('completed'), "username": name})

    with open("{}.json".format(argv[1]), "w") as jsonfile:
        json.dump(json_dict, jsonfile)
