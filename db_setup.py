# Initializes SQLite DB
import sqlite3

def create_connection():
    return sqlite3.connect('db/lms_database.db')