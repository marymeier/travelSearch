import sqlite3
import csv

def query_country_names():
    connection = sqlite3.connect('travelSearch.db')
    cursor = connection.cursor()

    select_query = "SELECT name as country_names FROM Country"
    cursor.execute(select_query)

    rows = cursor.fetchall()

    available_countries = []
    for row in rows:
        available_countries.append(row[0])
    
    connection.close()

    return available_countries

def format_country_name(user_inputted_country_name):
    return user_inputted_country_name.lower().title()

def query_country_attributes(user_inputted_country_name):
    connection = sqlite3.connect('travelSearch.db')
    cursor = connection.cursor()

    country_name = format_country_name(user_inputted_country_name)

    select_query = """SELECT
                        name AS country_name,
                        government_struct AS government_structure,
                        most_common_religion,
                        time_zone,
                        official_language
                    FROM Country
                    WHERE name = ?;
                    """
    cursor.execute(select_query, (country_name,))

    result = cursor.fetchone()
    
    if result:
        user_output = {"Country Name": result[0],
                    "Government Structure": result[1],
                    "Most Common Religion": result[2],
                    "Time Zone": result[3],
                    "Official Language": result[4]
                    }
    else:
        user_output = {"Country Name": "Invalid country name. Country was either mispelled or is not in Europe, (not case sensitive)"}
    
    connection.close()

    return user_output


def main():
    # query_country_names()
    # query_country_attributes("Some name")
    print("hello world")

if __name__ == "__main__":
    main()