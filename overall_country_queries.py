import sqlite3

def format_country_name(user_inputted_country_name):
    return user_inputted_country_name.lower().title()

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


def query_country_overview(user_inputted_country_name):
    connection = sqlite3.connect('travelSearch.db')
    cursor = connection.cursor()

    country_name = format_country_name(user_inputted_country_name)

    select_query = """SELECT
                        city_name,
                        region_of_climate,
                        climate_type,
                        avg_days_of_sun,
                        season_to_travel
                    FROM Climate
                    WHERE city_name = (
                        SELECT capital_city
                        FROM Capital_City
                        WHERE country = ?
                    );
                    """
    cursor.execute(select_query, (country_name,))

    result = cursor.fetchone()
    
    if result:
        user_output = {"Country Name": country_name,
                    "City": result[0].title(),
                    "Region of Climate": result[1].title(),
                    "Climate Type": result[2].title(),
                    "Average Days of Sun in the Year": f"{result[3]} days",
                    "Season to Travel": result[4].title()
                    }
    else:
        user_output = {"Country Name": "Invalid country name. Country was either mispelled or is not in Europe, (not case sensitive)"}
    
    connection.close()

    return user_output


def main():
    print(f"country names:\n{', '.join(query_country_names())}")

if __name__ == "__main__":
    main()