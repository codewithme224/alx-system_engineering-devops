#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress"""

import requests
from sys import argv

if __name__ == "__main__":
    """script that, using this REST API, for a given employee ID"""
    url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    url2 = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            argv[1])
    response = requests.get(url)
    response2 = requests.get(url2)
    json_obj = response.json()
    json_obj2 = response2.json()
    name = json_obj.get('name')
    done_tasks = 0
    total_tasks = 0

    for task in json_obj2:
        if task.get('completed') is True:
            done_tasks += 1
        total_tasks += 1
    print("Employee {} is done with tasks({}/{}):".format(
        name, done_tasks, total_tasks))
    for task in json_obj2:
        if task.get('completed') is True:
            print("\t {}".format(task.get('title')))
