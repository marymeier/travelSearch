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
                        Country.name AS country_name,
                        Country.official_language,
                        Country.government_struct AS government_structure,
                        Country.most_common_religion,
                        Capital_City.capital_city,
                        Capital_City.population AS capital_city_population,
                        Public_Transportation.types_available AS public_transportation_options,
                        Public_Transportation.avg_price_of_ticket,
                        National_Cuisine.dish_name AS national_dish,
                        National_Cuisine.most_exported_food,
                        Economy.type,
                        Economy.economic_world_ranking,
                        Economy.gdp AS gross_domestic_product,
                        Economy.currency
                    FROM Country
                    JOIN Capital_City ON Country.name = Capital_City.country
                    JOIN Public_Transportation ON Country.name = Public_Transportation.country_name
                    JOIN National_Cuisine ON Country.name = National_Cuisine.country_name
                    JOIN Economy ON Country.name = Economy.country_name
                    WHERE Country.name = ?;
                    """
    cursor.execute(select_query, (country_name,))

    result = cursor.fetchone()
    
    if result:
        user_output = {"Country Name": result[0],
                    "Official Language/s": result[1].title(),
                    "Government Structure": result[2].title(),
                    "Most Common Religion": result[3],
                    "Capital City": result[4],
                    "City Population": '{:,}'.format(result[5]),
                    "Public Transportation Options": result[6].title(),
                    "Average Price of Ticket": result[7],
                    "National Dish": result[8].title(),
                    "Most Exported Food": result[9],
                    "Type of Economy": result[10].title(),
                    "Economic World Ranking": result[11],
                    "Total Gross Domestic Product, GDP": '${:,}'.format(result[12]),
                    "Currency": result[13]
                    }
    else:
        user_output = {"Country Name": "Invalid country name. Country was either mispelled or is not in Europe, (not case sensitive)"}
    
    connection.close()

    return user_output