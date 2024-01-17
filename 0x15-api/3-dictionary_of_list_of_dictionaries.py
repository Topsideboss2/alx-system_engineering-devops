#!/usr/bin/python3

""" Script that uses JSONPlaceholder to return information
        about his/her TODO list progress
        Requirements:
        You must use urllib or requests module
        The script must export data in the JSON format
        """
        
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    jsonfile = {}
    for user in users:
        user_id = user.get("id")
        todo = requests.get(url + "todos", params={"userId": user_id}).json()
        tasks = []
        for task in todo:
            tasks.append({"username": user.get("username"),
                          "task": task.get("title"),
                          "completed": task.get("completed")})
        jsonfile[user_id] = tasks
    with open("todo_all_employees.json", "w") as f:
        json.dump(jsonfile, f)
