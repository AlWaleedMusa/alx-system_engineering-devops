#!/usr/bin/python3
"""using task 0 extend your Python script to
export data in the json format with some requirements"""

import json
import requests
import sys


if __name__ == "__main__":
    """Prints the to-do list for all employees in json format."""

    api = "https://jsonplaceholder.typicode.com/"
    users = requests.get(api + "users").json()
    todos = requests.get(api + "todos").json()

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(
            {
                user.get("id"): [
                    {
                        "username": user.get("username"),
                        "task": t.get("title"),
                        "completed": t.get("completed"),
                    }
                    for t in todos
                    if t.get("userId") == user.get("id")
                ]
                for user in users
            },
            json_file,
        )
