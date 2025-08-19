#!/usr/bin/env python3
"""
MySQLServer.py
Creates the database 'alx_book_store' if it does not exist.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    cursor = None
    try:
        # Connect to MySQL server (adjust user/password if needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rootpassword"   # change to your MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close cursor and connection safely
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
            # print("MySQL connection is closed")  # optional

if __name__ == "__main__":
    create_database()
