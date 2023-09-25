#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    """
    defines the base URL of the REST API that the script will interact with
    """
    url = "https://jsonplaceholder.typicode.com/"
    """
    makes another HTTP GET request to the /todos endpoint, passing
    the userId parameter with the employee ID obtained from the
    command-line argument.
    """
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    """
    list comprehension to create a list called completed. It iterates
    through the TODO items (todos) and selects the "title" of each item
    for which the "completed" key is True
    """

    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]
