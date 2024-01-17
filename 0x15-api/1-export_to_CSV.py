#!/usr/bin/python3


""" Script that uses JSONPlaceholder to return information
        about his/her TODO list progress
        Requirements:
        You must use urllib or requests module
        The script must accept an integer as a parameter, which is the employee ID
        """

import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    todo = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo:
            writer.writerow([user_id, user.get("username"),
                            task.get("completed"), task.get("title")])
