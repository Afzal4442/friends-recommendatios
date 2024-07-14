
import sqlite3 
  

def get_db_connection():
    # Connecting to sqlite 
    conn = sqlite3.connect('social.db') 
    
    # Creating a cursor object using the  
    # cursor() method 
    cursor = conn.cursor() 
    return cursor,conn