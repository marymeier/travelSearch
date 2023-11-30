import pandas as pd
import sqlite3

# Global Variables
user_id = ""

def clean_country_list(file_name):
    europe_data = pd.read_csv(file_name)
    europe_data = europe_data[europe_data['continent'] == 'Europe']
    selected_columns = ['country', 'currency', 'capital_city', 'region', 'gdp', 'population', 'democracy_type']
    europe_data = europe_data[selected_columns]

    # Fixing democracy type on major basis
    democracy_mapping = {'Flawed democracy': 'Parliamentary democracy', 'Full democracy': 'Parliamentary democracy', 'Hybrid regime': 'Constitutional monarchy'}
    europe_data['democracy_type'] = europe_data['democracy_type'].replace(democracy_mapping)

    # Fixing democracy type
    europe_data.loc[europe_data['country'] == 'Bosnia and herzegovina', 'country'] = 'Presidential republic'
    europe_data.loc[europe_data['country'] == 'Turkey', 'democracy_type'] = 'Presidential republic'
    europe_data.loc[europe_data['country'] == 'Cyprus', 'democracy_type'] = 'Presidential republic'
    europe_data.loc[europe_data['country'] == 'Monaco', 'democracy_type'] = 'Constitutional monarchy'
    europe_data.loc[europe_data['country'] == 'San Marino', 'democracy_type'] = 'Parlimentary democracy'
    europe_data.loc[europe_data['country'] == 'Andorra', 'democracy_type'] = 'Parlimentary democracy'
    europe_data.loc[europe_data['country'] == 'Liechtenstein', 'democracy_type'] = 'Semi-constitutional monarchy'

    europe_data = europe_data.reset_index(drop=True)

    # Add new Countries:
    missing_countries_data = {'country': ['Armenia', 'Azerbaijan', 'Georgia', 'Kosovo', 'Turkey', 'Vatican City'],
                      'currency': ['Armenian Dram', 'Azerbaijani Manat', 'Tbilisi', 'Euro', 'Turkish lira', 'Euro'],
                      'capital_city': ['Yerevan', 'Baku', 'Tbilisi', 'Pristina', 'Ankara', 'Vatican City'],
                      'region': ['Eastern Europe', 'Eastern Europe', 'Eastern Europe', 'Southeast Europe', 'Southeast Europe', 'Southern Europe'],
                      'gdp': [58497000000, 192146000000, 82210000000, 27918000000, 3613000000000, 16195272],
                      'population': [3000756, 10353296, 3688647, 1761985, 85279553, 764],
                      'democracy_type': ['Parlimentary democracy', 'Presidential republic', 'Parlimentary democracy', 'Parlimentary democracy', 'Presidential republic', 'Monarchy']}
    
    missing_countries_df = pd.DataFrame(missing_countries_data)
    new_europe_data = pd.concat([europe_data, missing_countries_df], ignore_index=True)
    new_europe_data = new_europe_data.sort_values(by='country', ignore_index=True)

    return new_europe_data

def new_data(file_name):
    different_data = pd.read_csv(file_name)
    return different_data

def intro_message():
    print("\n\033[1;4m\t\tWelcome to the European Travel and Information Guide\033[0m\n")
    print("\tHere will be a travel guide that details information regarding a country\n\t" + 
          "and its capital city. In addition, the guide shoulde provide you with\n\t" +
          "information regarding the countries':")
    print("\t\t- Cuisine" +
         "\n\t\t- Transportation" +
         "\n\t\t- Climate" +
         "\n\t\t- Economy" +
         "\n\t\t- Tourist Attractions" +
         "\n\t\t- National Security Situation, as related to travel")


def print_command_list():
    print("\n{}, here is a list of commands you can type and what each command does".format(user_id))
    print("\n\033[1mCommands:\033[0m")
    print("\t\033[1mEnter 'E' or 'e'\033[0m" +
          "\n\t\t- to escape the command sequence and leave the travel guide")
    print("\t\033[1mEnter '1'\033[0m" +
          "\n\t\t- to receive the list of countries in the guide")
    print("\t\033[1mEnter '2'\033[0m" +
          "\n\t\t- to receive a list of information we offer for each country in" +
          "\n\t\tthe guide")
    print("\t\033[1mEnter '3 [country name]'\033[0m" +
          "\n\t\t- to view specific information regarding the country")
    print("\t\033[1mEnter '4 [country name] [country specific info]'\033[0m" +
          "\n\t\t- to view information in a specific sector of that country be" + 
          "\n\t\tit climate, economy, food, etc")
    print("\t\033[1mEnter '5 [country name] all'\033[0m" +
          "\n\t\t- To view everything regarding a country")


def set_user_id():
    print("\nLet's begin by making you an account!")
    
    user_first_name = input("Please enter your first name:\n")
    user_last_name = input("Please enter your last name:\n")

    global user_id
    user_id = user_first_name[0] + user_last_name

def connect_travelSearch():
    # Connect to sqlite and tableSearch database
    conn = sqlite3.connect('travelSearch.db')

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM travelSearch.Capital_City')
    conn.commit

def create_country_table_csv(european_data_frame, additional_europe_data_frame):
    europe_data_selected = european_data_frame[['country', 'democracy_type']]
    selected_columns_diff_db = ['country_name', 'most_common_religion', 'language', 'time_zone']
    working_db = additional_europe_data_frame[selected_columns_diff_db]

    country_table = pd.merge(europe_data_selected, working_db,left_on='country', right_on='country_name', how = 'inner')
    country_table.drop(columns=['country_name'], inplace=True)
    country_table.sort_values(by='country', inplace=True)

    desired_order = ['country', 'most_common_religion', 'language', 'democracy_type', 'time_zone']
    new_column_names = {'country': 'name', 'democracy_type': 'govt_struct'}
    country_table = country_table[desired_order]
    country_table = country_table.rename(columns=new_column_names)

    output_file_path = 'Country_table.csv'
    country_table.to_csv(output_file_path, index=False)
    return country_table

def create_economy_table_csv(european_data_frame, additional_europe_data_frame):
    europe_data_selected = european_data_frame[['country', 'currency', 'gdp']]
    selected_columns_diff_db = ['country_name', 'economic_world_ranking', 'economy_type', 'largest_industry']
    working_db = additional_europe_data_frame[selected_columns_diff_db]

    economy_table = pd.merge(europe_data_selected, working_db,left_on='country', right_on='country_name', how = 'inner')
    economy_table.drop(columns=['country_name'], inplace=True)
    economy_table.sort_values(by='economic_world_ranking', inplace=True)

    desired_order = ['country', 'economic_world_ranking', 'gdp', 'economy_type', 'currency', 'largest_industry']
    economy_table = economy_table[desired_order]

    output_file_path = 'Economy_table.csv'
    economy_table.to_csv(output_file_path, index=False)
    return economy_table

def create_capital_city_table_csv(european_data_frame, additional_europe_data_frame):
    europe_data_selected = european_data_frame[['country', 'population', 'capital_city']]
    selected_columns_diff_db = ['country_name', 'capital_city_region']
    working_db = additional_europe_data_frame[selected_columns_diff_db]

    capital_city_table = pd.merge(europe_data_selected, working_db,left_on='country', right_on='country_name', how = 'inner')
    capital_city_table.drop(columns=['country_name'], inplace=True)
    capital_city_table.sort_values(by='country', inplace=True)

    desired_order = ['country', 'capital_city', 'population', 'capital_city_region']
    capital_city_table = capital_city_table[desired_order]

    output_file_path = 'Capital_City_table.csv'
    capital_city_table.to_csv(output_file_path, index=False)
    return capital_city_table

def create_tourist_attraction_table_csv(european_data_frame, additional_europe_data_frame):
    europe_data_selected = european_data_frame[['country']]
    selected_columns_diff_db = ['country_name', 'capital_most_popular_nightlife_area', 'top_visited_tourist_attraction', 'capital_city_region']
    working_db = additional_europe_data_frame[selected_columns_diff_db]

    tourist_attraction_table = pd.merge(europe_data_selected, working_db,left_on='country', right_on='country_name', how = 'inner')
    tourist_attraction_table.drop(columns=['country_name'], inplace=True)
    tourist_attraction_table.sort_values(by='country', inplace=True)

    desired_order = ['country', 'capital_most_popular_nightlife_area', 'top_visited_tourist_attraction', 'capital_city_region']
    new_column_names = {'capital_most_popular_nightlife_area': 'most_popular_nightlife_area', 'capital_city_region': 'tourist_attraction_region'}
    tourist_attraction_table = tourist_attraction_table[desired_order]
    tourist_attraction_table = tourist_attraction_table.rename(columns=new_column_names)

    output_file_path = 'Tourist_Attraction_table.csv'
    tourist_attraction_table.to_csv(output_file_path, index=False)
    return tourist_attraction_table

def create_national_cuisine_table_csv(european_data_frame, additional_europe_data_frame):
    europe_data_selected = european_data_frame[['country']]
    selected_columns_diff_db = ['country_name', 'national_cuisine', 'food_classification', 'most_exported_food']
    working_db = additional_europe_data_frame[selected_columns_diff_db]

    national_cuisine_table = pd.merge(europe_data_selected, working_db,left_on='country', right_on='country_name', how = 'inner')
    national_cuisine_table.drop(columns=['country_name'], inplace=True)
    national_cuisine_table.sort_values(by='country', inplace=True)

    desired_order = ['country', 'national_cuisine', 'food_classification', 'most_exported_food']
    new_column_names = {'national_cuisine': 'dish_name'}
    national_cuisine_table = national_cuisine_table[desired_order]
    national_cuisine_table = national_cuisine_table.rename(columns=new_column_names)

    output_file_path = 'National_Cuisine_table.csv'
    national_cuisine_table.to_csv(output_file_path, index=False)
    return national_cuisine_table

def create_climate_table_csv(european_data_frame, additional_europe_data_frame):
    europe_data_selected = european_data_frame[['country']]
    selected_columns_diff_db = ['country_name', 'season_to_travel', 'type_of_climate', 'avg_days_of_sun', 'capital_city_region']
    working_db = additional_europe_data_frame[selected_columns_diff_db]

    climate_table = pd.merge(europe_data_selected, working_db,left_on='country', right_on='country_name', how = 'inner')
    climate_table.drop(columns=['country_name'], inplace=True)
    climate_table.sort_values(by='country', inplace=True)

    desired_order = ['country', 'capital_city_region', 'season_to_travel', 'type_of_climate', 'avg_days_of_sun']
    new_column_names = {'capital_city_region': 'region_of_climate'}
    climate_table = climate_table[desired_order]
    climate_table = climate_table.rename(columns=new_column_names)

    output_file_path = 'Climate_table.csv'
    climate_table.to_csv(output_file_path, index=False)
    return climate_table

def main():
    intro_message()

    set_user_id()
    print("\nHere is your unique User_ID: {}".format(user_id))

    european_data = clean_country_list("All_countries.csv")

    additional_europe_data_frame = new_data("data.csv")
    print(additional_europe_data_frame.columns)

    country_table_df = create_country_table_csv(european_data, additional_europe_data_frame)
    # print(Country_table_df)
    economy_table_df = create_economy_table_csv(european_data, additional_europe_data_frame)
    # print(economy_table_df)
    capital_city_table_df = create_capital_city_table_csv(european_data, additional_europe_data_frame)
    # print(capital_city_table_df)
    tourist_attraction_table_df = create_tourist_attraction_table_csv(european_data, additional_europe_data_frame)
    # print(tourist_attraction_table_df)
    national_cuisine_table_df = create_national_cuisine_table_csv(european_data, additional_europe_data_frame)
    # print(national_cuisine_table_df)
    climate_table_df= create_climate_table_csv(european_data, additional_europe_data_frame)
    print(climate_table_df)




    # for index, row in Country_table_df.iterrows():
    # # Print the values in each row
    #     print(f"Country: {row['name']}")
    #     print(f"Democracy Type: {row['govt_struct']}")
    #     print(f"Most Common Religion: {row['most_common_religion']}")
    #     print(f"Language: {row['language']}")
    #     print(f"Time Zone: {row['time_zone']}")
    #     print("\n")


    while True:
        break
        print_command_list()
        user_input = input("Please enter your next command: ")

        # each user_input should call a function that connects to the sql server
        # does the sql call that we need, retreives the table, flushes the data and
        # returns it in user friendly way
        if user_input.lower() == "e":
            break
        elif user_input == "1":
            print("add here connection to sql to retrieve country list")
        elif user_input == "2":
            print("add here connection to sql to retrieve entity list")
        elif user_input == "3":
            print("add here connection to sql to retrieve country info")
        elif user_input == "4":
            print("add here connection to sql to retrieve entity specific inof")
        elif user_input == "5":
            print("add here connection to sql to retrieve aggregate info on country")
        else:
            print("Your command did not match any of the acceptable ones...")
    
    print("\n\n\033[1;4m\t\tThank you for using our Travel Guide - Safe Travels\033[0m\n\n")    

if __name__ == "__main__":
    main()