#!/usr/bin/python3
"""using task 0 extend your Python script to
export data in the json format"""

import json
import requests
import sys


if __name__ == "__main__":
    """Prints the to-do list for a given employee ID."""

    if len(sys.argv) != 2:
        print("Usage: <{}> <employee_id>".format(sys.argv[0]))
        sys.exit()

    api = "https://jsonplaceholder.typicode.com/"
    user = requests.get(api + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(api + "todos", params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in todos if t.get("completed")]
    with open("{}.json".format(sys.argv[1]), "w") as json_file:
        json.dump(
            {
                sys.argv[1]: [
                    {
                        "task": t.get("title"),
                        "completed": t.get("completed"),
                        "username": user.get("username"),
                    }
                    for t in todos
                ]
            },
            json_file,
        )
