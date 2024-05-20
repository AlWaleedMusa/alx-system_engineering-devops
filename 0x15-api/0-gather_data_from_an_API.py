#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""

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
    print(
        "Employee {} is done with tasks({}/{}):".format(
            user.get("name"), len(completed), len(todos)
        )
    )
    [print("\t {}".format(c)) for c in completed]
