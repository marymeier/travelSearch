import sqlite3

def connect_travelSearch():
    # Connect to sqlite and 
    # Connect to tableSearch database
    connection = sqlite3.connect('travelSearch.db')
    # Cursor object
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS COUNTRY')
    table = """CREATE TABLE Country (
govt_struct VARCHAR(20), 
language VARCHAR(20), 
religion VARCHAR(20), 
time_zone VARCHAR(30),
name VARCHAR(50) NOT NULL, 
PRIMARY KEY(name)
);
 """
    cursor.execute(table)
    connection.close()
    # conn.commit