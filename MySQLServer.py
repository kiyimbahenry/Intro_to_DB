#!/usr/bin/env python3
"""
MySQL Server Connection Script
Creates the alx_book_store database
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    """Create alx_book_store database if it doesn't exist"""
    try:
        # Connect to MySQL server without specifying a database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Kiyimba7!"
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            print("Database 'alx_book_store' created successfully!")
            
    except mysql.connector.Error as e:  # CHANGED THIS LINE
        print(f"Error: {e}")
        
    finally:
        # Close connection properly
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Execute the function
if __name__ == "__main__":
    create_database()
