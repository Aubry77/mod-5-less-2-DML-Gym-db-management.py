# Gym Database Management System

## Overview
This project is a simple Gym Database Management System built using Python and SQLite. It allows you to manage members and workout sessions in a gym, including adding, updating, and deleting records.

## Features
- Add new members to the gym.
- Add new workout sessions for specific members.
- Update workout session times.
- Delete members who have canceled their membership.
- Handle errors gracefully to maintain data integrity.

## Requirements
- Python 3.x
- SQLite3

## Setup and Usage

### Install Dependencies
Ensure you have Python installed on your system. You can download it from [Python's official website](https://www.python.org/).

### Create and Initialize the Database
1. Open your terminal or command prompt.
2. Run the Python script to create the necessary tables and add some initial data:
    ```sh
    python gym_management.py
    ```

### Adding a Member
To add a new member, use the `add_member` function in the script:
```python
add_member(1, 'Jane Doe', 28)
