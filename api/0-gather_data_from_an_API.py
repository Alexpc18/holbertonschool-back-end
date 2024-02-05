#!/usr/bin/python3

import requests
import sys

def get_employee_todo_progress(employee_id):
    # Base URL for the TODO API
    base_url = "https://jsonplaceholder.typicode.com/users"

    # Make a request to get employee details
    employee_response = requests.get(f"{base_url}/{employee_id}")
    employee_data = employee_response.json()

    # Make a request to get TODO list for the employee
    todo_response = requests.get(f"{base_url}/{employee_id}/todos")
    todo_data = todo_response.json()

    # Calculate progress
    total_tasks = len(todo_data)
    completed_tasks = sum(task['completed'] for task in todo_data)

    # Display information
    print(f"Employee {employee_data['name']} is done with tasks ({completed_tasks}/{total_tasks}):")
    print(f"\t{employee_data['name']}:", end=" ")
    print(f"number of done tasks: {completed_tasks}", end=", ")
    print(f"total number of tasks: {total_tasks}")

    # Display titles of completed tasks
    print("Completed tasks:")
    for task in todo_data:
        if task['completed']:
            print(f"\t- {task['title']}")

if __name__ == "__main__":
    # Check if an employee ID is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Call the function with the provided employee ID
    get_employee_todo_progress(employee_id)

