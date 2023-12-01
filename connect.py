import sqlite3
import csv

def create_and_populate_country_table():
    # Connect to sqlite and connect to tableSearch database
    connection = sqlite3.connect('travelSearch.db')
    # Cursor object
    cursor = connection.cursor()
    # Start us with a clean slate and rebuilds a Country table if it already exists
    cursor.execute('DROP TABLE IF EXISTS Country')
    create_country_table = """CREATE TABLE Country (
                            name VARCHAR(50) NOT NULL,
                            govt_struct VARCHAR(50),
                            language VARCHAR(50),
                            most_common_religion VARCHAR(50),
                            time_zone VARCHAR(50),
                            PRIMARY KEY(name)
                            );
                            """
    cursor.execute(create_country_table)
    file = open('Country_table.csv')
    contents = csv.reader(file)

    insert_records = "INSERT INTO Country (name, most_common_religion, language, govt_struct, time_zone) VALUES (?,?,?,?,?)"
        
    cursor.executemany(insert_records, contents)

    # This is just to validate we have the country correctly:
    select_all = "SELECT * FROM Country"
    rows = cursor.execute(select_all).fetchall()
    for r in rows:
        print(r)

    connection.commit()
    connection.close()
        
def create_and_populate_capital_city_table():
    # Connect to sqlite and 
    # Connect to tableSearch database
    connection = sqlite3.connect('travelSearch.db')
    # Cursor object
    cursor = connection.cursor()
     # Start us with a clean slate and rebuilds a Capital_City table if it already exists
    cursor.execute('DROP TABLE IF EXISTS Capital_City')
    create_capital_city_table = """CREATE TABLE Capital_City (
                            country VARCHAR(50),
                            capital_city VARCHAR(50) NOT NULL,
                            population INT,
                            capital_city_region VARCHAR(50),
                            PRIMARY KEY(capital_city),
                            FOREIGN KEY (country)
                                REFERENCES Country(name)
                            );
    """
    cursor.execute(create_capital_city_table)
    file = open('Capital_City_table.csv')
    contents = csv.reader(file)

    insert_records = "INSERT INTO Capital_City (country,capital_city,population,capital_city_region) VALUES (?,?,?,?)"
        
    cursor.executemany(insert_records, contents)

    select_all = "SELECT * FROM Capital_City"
    rows = cursor.execute(select_all).fetchall()
    for r in rows:
        print(r)

    connection.commit()
    connection.close()

def create_and_populate_public_transportation_table():
    # Connect to sqlite and 
    # Connect to tableSearch database
    connection = sqlite3.connect('travelSearch.db')
    # Cursor object
    cursor = connection.cursor()
     # Start us with a clean slate and rebuilds a Public_Transportation table if it already exists
    cursor.execute('DROP TABLE IF EXISTS Public_Transportation')
    create_public_transportation_table = """CREATE TABLE Public_Transportation (
                                country_name VARCHAR(50),
                                type VARCHAR(50) NOT NULL,
                                owned_by VARCHAR(50) NOT NULL,
                                most_used VARCHAR(50),
                                avg_price FLOAT,
                                PRIMARY KEY (type, owned_by),
                                FOREIGN KEY (country_name)
                                    REFERENCES Country(name)
                            );
    """
    cursor.execute(create_public_transportation_table)
    file = open('Public_Transportation_table.csv')
    contents = csv.reader(file)

    insert_records = "INSERT INTO Public_Transportation (country_name,type,owned_by,most_used,avg_price) VALUES (?,?,?,?,?)"
        
    cursor.executemany(insert_records, contents)

    select_all = "SELECT * FROM Public_Transportation"
    rows = cursor.execute(select_all).fetchall()
    for r in rows:
        print(r)

    connection.commit()
    connection.close()

def create_and_populate_national_cuisine_table():
    # Connect to sqlite and 
    # Connect to tableSearch database
    connection = sqlite3.connect('travelSearch.db')
    # Cursor object
    cursor = connection.cursor()
     # Start us with a clean slate and rebuilds a National_Cuisine table if it already exists
    cursor.execute('DROP TABLE IF EXISTS National_Cuisine')
    create_national_cuisine_table = """CREATE TABLE National_Cuisine (
                                country_name VARCHAR(50),
                                dish_name VARCHAR(70) NOT NULL,
                                classification VARCHAR(40),
                                most_exported VARCHAR(50),
                                PRIMARY KEY(dish_name),
                                FOREIGN KEY (country_name)
                                    REFERENCES Country(name)
                            );
    """
    cursor.execute(create_national_cuisine_table)
    file = open('National_Cuisine_table.csv')
    contents = csv.reader(file)

    insert_records = "INSERT INTO National_Cuisine (country_name,dish_name,classification,most_exported) VALUES (?,?,?,?)"
        
    cursor.executemany(insert_records, contents)

    select_all = "SELECT * FROM National_Cuisine"
    rows = cursor.execute(select_all).fetchall()
    for r in rows:
        print(r)

    connection.commit()
    connection.close()

def create_and_populate_economy_table():
    # Connect to sqlite and 
    # Connect to tableSearch database
    connection = sqlite3.connect('travelSearch.db')
    # Cursor object
    cursor = connection.cursor()
     # Start us with a clean slate and rebuilds a Economy table if it already exists
    cursor.execute('DROP TABLE IF EXISTS Economy')
    create_economy_table = """CREATE TABLE Economy (
                        country_name VARCHAR(50),
                        world_ranking INT NOT NULL,
                        gdp FLOAT,
                        type VARCHAR(50),
                        currency VARCHAR(30),
                        largest_industry VARCHAR(50),
                        PRIMARY KEY (world_ranking),
                        FOREIGN KEY (country_name)
                            REFERENCES Country(name)
                    );
    """
    cursor.execute(create_economy_table)
    file = open('Economy_table.csv')
    contents = csv.reader(file)

    insert_records = "INSERT INTO Economy (country_name,world_ranking,gdp,type,currency,largest_industry) VALUES (?,?,?,?,?,?)"
        
    cursor.executemany(insert_records, contents)

    select_all = "SELECT * FROM Economy"
    rows = cursor.execute(select_all).fetchall()
    for r in rows:
        print(r)

    connection.commit()
    connection.close()

def main():
    print("Country Table:")
    create_and_populate_country_table()
    print("\n\n\ncapital_city Table:")
    create_and_populate_capital_city_table()
    print("\n\n\npublic_transportation Table:")
    create_and_populate_public_transportation_table()
    print("\n\n\nNational_Cuisine Table:")
    create_and_populate_national_cuisine_table()
    print("\n\n\nEconomy Table:")
    create_and_populate_economy_table()

if __name__ == "__main__":
    main()