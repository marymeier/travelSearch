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

def main():
    intro_message()

    set_user_id()
    print("\nHere is your unique User_ID: {}".format(user_id))

    european_data = clean_country_list("All_countries.csv")
    # print(european_data)

    # country_table = {'country': european_data['country'].tolist()}


    # print(country_table)

    diff_db = new_data("data.csv")
    headers = diff_db.columns
    print(diff_db)

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