import csv
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="weareP$U24",
    database="travelSearch"
)

# Only needs to be run once:
# cursor.execute("CREATE DATABASE travelSearch")

def create_users_table():
    cursor = mydb.cursor()

    # Start us with a clean slate and rebuilds a User table if it already exists
    cursor.execute('DROP TABLE IF EXISTS Users')
    create_users_table = """CREATE TABLE Users (
                            user_id VARCHAR(50) NOT NULL,
                            country_name VARCHAR(100),
                            tourist_attraction_fun_fact VARCHAR(300) DEFAULT NULL,
                            economic_cost_of_stay FLOAT DEFAULT NULL,
                            national_cuisine_rating FLOAT DEFAULT NULL,
                            PRIMARY KEY(user_id, country_name)
                            );
                            """
    # create_users_table = """CREATE TABLE Users (
    #                     user_id VARCHAR(50) NOT NULL,
    #                     country_name VARCHAR(100),
    #                     tourist_attraction_fun_fact VARCHAR(300) DEFAULT NULL,
    #                     economic_cost_of_stay FLOAT DEFAULT NULL,
    #                     national_cuisine_rating FLOAT DEFAULT NULL,
    #                     PRIMARY KEY(user_id, country_name),
    #                     FOREIGN KEY (country_name)
    #                         REFERENCES Country(name)
    #                     );
    #                     """
    cursor.execute(create_users_table)

    mydb.commit()
    cursor.close()

def create_and_populate_country_table():
    # Cursor object
    cursor = mydb.cursor()

    cursor.execute('SET FOREIGN_KEY_CHECKS=0')

    # Start us with a clean slate and rebuilds a Country table if it already exists
    cursor.execute('DROP TABLE IF EXISTS Country')
    create_country_table = """CREATE TABLE Country (
                            name VARCHAR(100) NOT NULL,
                            most_common_religion VARCHAR(100),
                            official_language VARCHAR(100),
                            government_struct VARCHAR(100),
                            time_zone VARCHAR(100),
                            PRIMARY KEY(name)
                            );
                            """
    cursor.execute(create_country_table)

    with open('Country_table.csv') as file:
        contents = csv.reader(file)
        
        # Skip the header row
        next(contents)
        
        insert_records = "INSERT INTO Country (name, most_common_religion, official_language, government_struct, time_zone) VALUES (%s,%s,%s,%s,%s)"
        contents = [tuple(inner_list) for inner_list in contents]
        cursor.executemany(insert_records, contents)

    cursor.execute('SET FOREIGN_KEY_CHECKS=1')

    mydb.commit()
    cursor.close()
        
def create_and_populate_capital_city_table():
    # Cursor object
    cursor = mydb.cursor()

    cursor.execute('SET FOREIGN_KEY_CHECKS=0')

    # Start us with a clean slate and rebuilds a Capital_City table if it already exists
    cursor.execute('DROP TABLE IF EXISTS Capital_City')
    create_capital_city_table = """CREATE TABLE Capital_City (
                            country VARCHAR(100),
                            capital_city VARCHAR(75) NOT NULL,
                            population INT,
                            capital_city_region VARCHAR(100),
                            PRIMARY KEY(capital_city),
                            FOREIGN KEY (country)
                                REFERENCES Country(name)
                            );
                            """
    cursor.execute(create_capital_city_table)

    with open('Capital_City_table.csv') as file:
        contents = csv.reader(file)
        
        # Skip the header row
        next(contents)
        
        insert_records = "INSERT INTO Capital_City (country,capital_city,population,capital_city_region) VALUES (%s,%s,%s,%s)"
        contents = [tuple(inner_list) for inner_list in contents]
        cursor.executemany(insert_records, contents)

    cursor.execute('SET FOREIGN_KEY_CHECKS=1')

    mydb.commit()
    cursor.close()

def create_and_populate_public_transportation_table():
    # Cursor object
    cursor = mydb.cursor()

    cursor.execute('SET FOREIGN_KEY_CHECKS=0')

    # Start us with a clean slate and rebuilds a Public_Transportation table if it already exists
    cursor.execute('DROP TABLE IF EXISTS Public_Transportation')
    create_public_transportation_table = """CREATE TABLE Public_Transportation (
                                country_name VARCHAR(100),
                                most_used VARCHAR(100),
                                owned_by VARCHAR(100) NOT NULL,
                                avg_price_of_ticket FLOAT,
                                types_available VARCHAR(100) NOT NULL,
                                PRIMARY KEY (types_available, owned_by),
                                FOREIGN KEY (country_name)
                                    REFERENCES Country(name)
                            );
                            """
    cursor.execute(create_public_transportation_table)

    with open('Public_Transportation_table.csv') as file:
        contents = csv.reader(file)
        
        # Skip the header row
        next(contents)
        
        insert_records = "INSERT INTO Public_Transportation (country_name,most_used,owned_by,avg_price_of_ticket,types_available) VALUES (%s,%s,%s,%s,%s)"
        contents = [tuple(inner_list) for inner_list in contents]
        cursor.executemany(insert_records, contents)

    cursor.execute('SET FOREIGN_KEY_CHECKS=1')

    mydb.commit()
    cursor.close()

def create_and_populate_national_cuisine_table():
    # Cursor object
    cursor = mydb.cursor()

    cursor.execute('SET FOREIGN_KEY_CHECKS=0')

    # Start us with a clean slate and rebuilds a National_Cuisine table if it already exists
    cursor.execute('DROP TABLE IF EXISTS National_Cuisine')
    create_national_cuisine_table = """CREATE TABLE National_Cuisine (
                                country_name VARCHAR(100),
                                dish_name VARCHAR(70) NOT NULL,
                                food_classification VARCHAR(80),
                                most_exported_food VARCHAR(900),
                                PRIMARY KEY(dish_name),
                                FOREIGN KEY (country_name)
                                    REFERENCES Country(name)
                            );
                            """
    cursor.execute(create_national_cuisine_table)

    with open('National_Cuisine_table.csv') as file:
        contents = csv.reader(file)
        
        # Skip the header row
        next(contents)
        
        insert_records = "INSERT INTO National_Cuisine (country_name,dish_name,food_classification,most_exported_food) VALUES (%s,%s,%s,%s)"
        contents = [tuple(inner_list) for inner_list in contents]
        cursor.executemany(insert_records, contents)

    cursor.execute('SET FOREIGN_KEY_CHECKS=1')

    mydb.commit()
    cursor.close()

def create_and_populate_economy_table():
    # Cursor object
    cursor = mydb.cursor()

    cursor.execute('SET FOREIGN_KEY_CHECKS=0')

    # Start us with a clean slate and rebuilds a Economy table if it already exists
    cursor.execute('DROP TABLE IF EXISTS Economy')
    create_economy_table = """CREATE TABLE Economy (
                        country_name VARCHAR(100),
                        economic_world_ranking INT NOT NULL,
                        gdp FLOAT,
                        type VARCHAR(75),
                        currency VARCHAR(50),
                        largest_industry VARCHAR(80),
                        PRIMARY KEY (economic_world_ranking),
                        FOREIGN KEY (country_name)
                            REFERENCES Country(name)
                    );
                    """
    cursor.execute(create_economy_table)

    with open('Economy_table.csv') as file:
        contents = csv.reader(file)
        
        # Skip the header row
        next(contents)
        
        insert_records = "INSERT INTO Economy (country_name,economic_world_ranking,gdp,type,currency,largest_industry) VALUES (%s,%s,%s,%s,%s,%s)"
        contents = [tuple(inner_list) for inner_list in contents]
        cursor.executemany(insert_records, contents)

    cursor.execute('SET FOREIGN_KEY_CHECKS=1')

    mydb.commit()
    cursor.close()

def create_and_populate_national_security_table():
    # Cursor object
    cursor = mydb.cursor()

    cursor.execute('SET FOREIGN_KEY_CHECKS=0')

    # Start us with a clean slate and rebuilds a National_Security table if it already exists
    cursor.execute('DROP TABLE IF EXISTS National_Security')
    create_economy_table = """CREATE TABLE National_Security (
                        economic_world_ranking INT NOT NULL,
                        homicide_rate FLOAT,
                        global_peace_index INT,
                        avg_larceny FLOAT,
                        police_force VARCHAR(80),
                        PRIMARY KEY (economic_world_ranking),
                        FOREIGN KEY (economic_world_ranking)
                            REFERENCES Economy(economic_world_ranking)
                    );
                    """
    cursor.execute(create_economy_table)

    with open('National_Security_table.csv') as file:
        contents = csv.reader(file)
        
        # Skip the header row
        next(contents)
        
        insert_records = "INSERT INTO National_Security (economic_world_ranking,homicide_rate,global_peace_index,avg_larceny,police_force) VALUES (%s,%s,%s,%s,%s)"
        contents = [tuple(inner_list) for inner_list in contents]
        cursor.executemany(insert_records, contents)

    cursor.execute('SET FOREIGN_KEY_CHECKS=1')

    mydb.commit()
    cursor.close()

def create_and_populate_tourist_attractions_table():
    # Cursor object
    cursor = mydb.cursor()

    cursor.execute('SET FOREIGN_KEY_CHECKS=0')

    # Start us with a clean slate and rebuilds a Tourist_Attractions table if it already exists
    cursor.execute('DROP TABLE IF EXISTS Tourist_Attractions')
    create_economy_table = """CREATE TABLE Tourist_Attractions (
                        city_name VARCHAR(75),
                        most_popular_nightlife_area VARCHAR(100) NOT NULL,
                        top_visited VARCHAR(100),
                        tourist_attraction_region VARCHAR(100),
                        PRIMARY KEY (most_popular_nightlife_area),
                        FOREIGN KEY (city_name)
                            REFERENCES Capital_City(capital_city)
                    );
                    """
    cursor.execute(create_economy_table)

    with open('Tourist_Attraction_table.csv') as file:
        contents = csv.reader(file)
        
        # Skip the header row
        next(contents)
        
        insert_records = "INSERT INTO Tourist_Attractions (city_name,most_popular_nightlife_area,top_visited,tourist_attraction_region) VALUES (%s,%s,%s,%s)"
        contents = [tuple(inner_list) for inner_list in contents]
        cursor.executemany(insert_records, contents)

    cursor.execute('SET FOREIGN_KEY_CHECKS=1')

    mydb.commit()
    cursor.close()

def create_and_populate_climate_table():
    # Cursor object
    cursor = mydb.cursor()

    cursor.execute('SET FOREIGN_KEY_CHECKS=0')
    # Start us with a clean slate and rebuilds a Climate table if it already exists
    cursor.execute('DROP TABLE IF EXISTS Climate')
    create_economy_table = """CREATE TABLE Climate (
                        city_name VARCHAR(75),
                        region_of_climate VARCHAR(80) NOT NULL,
                        season_to_travel VARCHAR(40),
                        climate_type VARCHAR(80),
                        avg_days_of_sun INT,
                        PRIMARY KEY (region_of_climate),
                        FOREIGN KEY (city_name)
                            REFERENCES Capital_City(capital_city)
                    );
                    """
    cursor.execute(create_economy_table)

    with open('Climate_table.csv') as file:
        contents = csv.reader(file)
        
        # Skip the header row
        next(contents)
        
        insert_records = "INSERT INTO Climate (city_name,region_of_climate,season_to_travel,climate_type,avg_days_of_sun) VALUES (%s,%s,%s,%s,%s)"
        contents = [tuple(inner_list) for inner_list in contents]
        cursor.executemany(insert_records, contents)
    
    cursor.execute('SET FOREIGN_KEY_CHECKS=1')
    
    mydb.commit()
    cursor.close()

# Private function
def _initialize_sql_tables():
    create_and_populate_country_table()
    create_users_table()
    create_and_populate_capital_city_table()
    create_and_populate_public_transportation_table()
    create_and_populate_national_cuisine_table()
    create_and_populate_economy_table()
    create_and_populate_national_security_table()
    create_and_populate_tourist_attractions_table()
    create_and_populate_climate_table()


def main():
    _initialize_sql_tables()
    mydb.close()

if __name__ == "__main__":
    main()