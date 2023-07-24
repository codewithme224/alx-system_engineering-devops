#!/usr/bin/python3
"""script to export data in the CSV format"""

import csv
import requests
from sys import argv


if __name__ == "__main__":
    """script to export data in the CSV format"""
    url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    url2 = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            argv[1])
    response = requests.get(url)
    response2 = requests.get(url2)
    json_obj = response.json()
    json_obj2 = response2.json()
    name = json_obj.get('username')

    with open("{}.csv".format(argv[1]), "w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in json_obj2:
            writer.writerow([argv[1], name, task.get('completed'), task.get('title')])
