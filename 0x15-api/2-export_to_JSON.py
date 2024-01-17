#!/usr/bin/python3

""" Script that uses JSONPlaceholder to return information
        about his/her TODO list progress
        Requirements:
        You must use urllib or requests module
        The script must accept an integer as a parameter,
        which is the employee ID
        """

import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    todo = requests.get(url + "todos", params={"userId": user_id}).json()
    tasks = []
    for task in todo:
        tasks.append({"task": task.get("title"),
                      "completed": task.get("completed"),
                      "username": user.get("username")})
    jsonfile = {}
    jsonfile[user_id] = tasks
    with open("{}.json".format(user_id), "w") as f:
        json.dump(jsonfile, f)
