#!/usr/bin/python3
# Script that uses JSONPlaceholder to return information about his/her TODO list progress
# Requirements:
# You must use urllib or requests module
# The script must accept an integer as a parameter, which is the employee ID
# The script must display on the standard output the employee TODO list progress in this exact format:


import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    todo = requests.get(url + "todos", params={"userId": user_id}).json()
    completed = [task for task in todo if task.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todo)))
    for task in completed:
        print("\t {}".format(task.get("title")))