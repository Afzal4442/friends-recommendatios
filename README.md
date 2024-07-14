# Friends Recommendation System

This project implements a friends recommendation system based on the friends-of-friends algorithm. It uses SQLite for the database and Python for executing the SQL queries and processing the results.

## Database Schema

The database consists of two tables:

- `User`: stores user information.
- `Friend`: stores the friendship relationships between users.

## Tables

### Users Table

| Column    | Type         |
|-----------|--------------|
| user_id   | INT PRIMARY KEY |
| user_name | VARCHAR(100) |
| email     | VARCHAR(100) |
| age       | INT          |

### Friends Table

| Column    | Type |
|-----------|------|
| user_id   | INT  |
| friend_id | INT  |

## Inserted Dummy Data

The `Users` table is populated with 30 records and the `Friends` table is populated with friendship relationships between these users.

## Setup Instructions

### Prerequisites

- Python 3.x
- SQLite3

### Steps

1. Clone the repository or download the code files.
2. Create and populate the database with dummy data by running the provided Python script.
3. Use the script to get friends recommendations for a given user.

### Create and Populate the Database

python feed_data.py

### Run application

python main.py

