import initial_user_housekeeping
import overall_country_queries
import database_queries
import user_db_commands

entity_list = ['capital city', 'capital_city', 'capital', 'public transportation', 'transportation', 'public_transportation',
               'transport', 'national cuisine', 'cuisine', 'national_cuisine', 'food', 'economy', 'econ', 'climate', 'weather',
               'tourist attractions', 'tourism', 'attractions', 'tourist_attractions', 'national security',
               'security', 'national_security']

def print_command_list():
    print(f"\n\n\t\t\033[1m'{initial_user_housekeeping.get_user_id()}'\033[0m, here is a list of commands you can type and what each command does:\n")
    print(f"\t\t\033[1mReminder NOTHING is Case Sensitive but it is Spelling Sensitive\033[0m\n")
    print("\t\033[1mEnter 'E' or 'e'\033[0m" +
          "\n\t\t- Escapes the command sequence and leaves the travel guide")
    print("\t\033[1mEnter 'Help', 'help', 'H', or 'h'\033[0m"+
          "\n\t\t- Prints this command list again at any time!")
    print("\t\033[1mEnter '1 or countries'\033[0m" +
          "\n\t\t- Receive a list of countries covered in guide")
    print("\t\033[1mEnter '2'\033[0m" +
          "\n\t\t- Receive a list of information we offer about each country")
    print("\t\033[1mEnter '[country name]'\033[0m" +
          "\n\t\t- to view specific information regarding a country" +
          "\n\t\t- Example: 'Denmark'")
    print("\t\033[1mEnter '[country name] [country specific info]'\033[0m" +
          "\n\t\t- to view information in a specific sector of that country be it climate, economy, food, etc" + 
          "\n\t\t- Example: 'Denmark Economy'")
    print("\t\033[1mEnter '[country name] all'\033[0m" +
          "\n\t\t- To view everything regarding a country" +
          "\n\t\t- Example 'Denmark all'")
    print("\t\033[1mCommands For User Ratings/ Inputs:\033[0m")
    print("\t\033[1mEnter 'add fun fact'\033[0m" +
          "\n\t\t- You can add a tourist attraction fun fact you have and want to save" +
          "\n\t\t- Example 'add fun fact'")
    print("\t\033[1mEnter 'delete fun fact'\033[0m" +
          "\n\t\t- Removes a previously added tourist fun fact" +
          "\n\t\t- Example 'delete fun fact'")
    print("\t\033[1mEnter 'add econ cost'\033[0m" +
          "\n\t\t- You can your estimated economic cost of stay for a week based on past experience" +
          "\n\t\t- Example 'add econ cost'")
    print("\t\033[1mEnter 'delete econ cost'\033[0m" +
          "\n\t\t- Removes a previously added economic estimate" +
          "\n\t\t- Example 'delete econ cost'")
    print("\t\033[1mEnter 'add cuisine rating'\033[0m" +
          "\n\t\t- You can your national cuisine rating based on past experience" +
          "\n\t\t- Example 'add cuisine rating'")
    print("\t\033[1mEnter 'delete cuisine rating'\033[0m" +
          "\n\t\t- Removes a previously added national cuisine rating" +
          "\n\t\t- Example 'delete cuisine rating'\n")

def print_country_list(country_list):
    print("\nList of Countries:\n")
    num_columns = 5

    # Calculate number of rows
    num_rows = -(-len(country_list) // num_columns)

    # Print the formatted list
    for i in range(num_rows):
        for j in range(num_columns):
            index = i + j * num_rows
            if index < len(country_list):
                print(f"{index + 1:2d}. {country_list[index]:<23}", end="")
        print()


def print_entity_list():
    print("\n\t\tEach country has the following country specific information offered about it:"+
        "\n\t\tYou can simply type the \033[1m'Country_name any_of_the_following'\033[0m to get specific info."
        "\n\t\t\t- Country" +
        "\n\t\t\t- Capital City, capital_city, or capital" +
        "\n\t\t\t- Public Transportation, transportation, public_transportation, or transport" +
        "\n\t\t\t- National Cuisine, cuisine, national_cuisine, or food" +
        "\n\t\t\t- Economy or econ" +
        "\n\t\t\t- Climate or weather" +
        "\n\t\t\t- Tourist Attractions, tourism, attractions, or tourist_attractions" +
        "\n\t\t\t- National Security, security, national_security" +
        "\n\t\t\t- Example: \033[1m'Italy Economy'\033[0m, \033[1m'Norway Climate'\033[0m, or \033[1m'Russia econ'\033[0m")

def print_country_specific_info(user_input):
    country = user_input.split()[0].title()
    if len(user_input.split()) == 2:
        specific_table = user_input.split()[1].lower()
    if len(user_input.split()) == 3:
        specific_table = user_input.split()[1].lower() + " " + user_input.split()[2].lower()

    if specific_table in ['capital city', 'capital_city', 'capital']:
        print("\n\t\tcapital city attributes:\n")
        for key, value in database_queries.query_capital_city_attributes(country).items():
            print(f"\t\t{key:25}{value}")
    elif specific_table in ['public transportation', 'transportation', 'public_transportation']:
        print("\n\t\tpublic transportation attributes:\n")
        for key, value in database_queries.query_public_transportation_attributes(country).items():
            print(f"\t\t{key:35}{value}")
    elif specific_table in ['national cuisine', 'cuisine', 'national_cuisine', 'food']:
        print("\n\t\tnational cuisine attributes:\n")
        for key, value in database_queries.query_national_cuisine_attributes(initial_user_housekeeping.get_user_id(), country).items():
            print(f"\t\t{key:45}{value}")
    elif specific_table in ['economy', 'econ']:
        print("\n\t\tEconomy attributes:\n")
        for key, value in database_queries.query_economy_attributes(initial_user_housekeeping.get_user_id(), country).items():
            print(f"\t\t{key:55}{value}")
    elif specific_table in ['climate', 'weather']:
        print("\n\t\tClimate:\n")
        for key, value in database_queries.query_climate_attributes(country).items():
            print(f"\t\t{key:35}{value}")
    elif specific_table in ['tourist attractions', 'tourism', 'attractions', 'tourist_attractions']:
        print("\n\t\tTourist Attractions:\n")
        for key, value in database_queries.query_tourist_attractions_attributes(initial_user_housekeeping.get_user_id(), country).items():
            print(f"\t\t{key:40}{value}")
    else:
        print("\n\t\tNational Security:\n")
        for key, value in database_queries.query_national_security_attributes(country).items():
            print(f"\t\t{key:40}{value}")
            
def add_fun_fact():
    country_name = input("\n\t\tLet's add your fun fact! First, which country do you want to add a fun fact about? \n\t")
    fun_fact = input("\n\t\tWhat is your fun fact? \n\t")
    
    user_input = input("\n\t\tAre you sure you want to add this fact? [y/n]\n\t")
    user_input.lower()
    if user_input in ['y', 'yes']:
        user_db_commands.insert_tourist_attraction_fun_fact(initial_user_housekeeping.get_user_id(), country_name, fun_fact)
    else:
        print("Okay, it will not be added. You can add another at any time.")
        
def delete_fun_fact():
    country_name = input("\n\t\tWhat country was your fun fact about?\n\t")
    
    user_input = input("\n\t\tAre you sure you want to delete? [y/n]\n\t")
    user_input.lower()
    if user_input in ['y', 'yes']:
        user_db_commands.delete_tourist_attraction_fun_fact(initial_user_housekeeping.get_user_id(), country_name)
    else:
        print("Okay, it will not be deleted. You can come back to delete it at any time.")
        
def add_econ_cost():
    country_name = input("\n\t\tWhat country do you want to add your estimated cost of stay to?\n\t")
    cost_of_stay = input("\n\t\tHow much is it? Please only enter a number.\n\t")
    
    user_input = input("\n\t\tAre you sure you want to add this cost of stay? [y/n]\n\t")
    user_input.lower()
    if user_input in ['y', 'yes']:
        user_db_commands.insert_economic_cost_of_stay(initial_user_housekeeping.get_user_id(), country_name, cost_of_stay)
    else:
        print("Okay, it will not be added. You can add another at any time.")
        
def delete_econ_cost():
    country_name = input("\n\t\tWhat country do you want to delete your estimated cost of stay from?\n\t")

    user_input = input("\n\t\tAre you sure you want to delete your estimated cost of stay for this country? [y/n]\n\t")
    user_input.lower()
    if user_input in ['y', 'yes']:
        user_db_commands.delete_economic_cost_of_stay(initial_user_housekeeping.get_user_id(), country_name)
    else:
        print("Okay, it will not be deleted. You can come back to delete it at any time.")
        
def add_cuisine_rating():
    country_name = input("\n\t\tWhat country do you want to add your rating of their national cuisine to?\n\t")
    rating = input("\n\t\tWhat is your rating on a scale of 1-10 (1 being the worst and 10 being the best)\n\t")
    
    user_input = input("\n\t\tAre you sure you want to add this rating? [y/n]\n\t")
    user_input.lower()
    if user_input in ['y', 'yes']:
        user_db_commands.insert_national_cuisine_rating(initial_user_housekeeping.get_user_id(), country_name, rating)
    else:
        print("Okay, it will not be added. You can add another at any time.")

def delete_cuisine_rating():
    country_name = input("\n\t\tWhat country was the rating for?\n\t")
    
    user_input = input("\n\t\tAre you sure you want to delete this rating? [y/n]\n\t")
    user_input.lower()
    if user_input in ['y', 'yes']:
        user_db_commands.delete_national_cuisine_rating(initial_user_housekeeping.get_user_id(), country_name)
    else:
        print("Okay, it will not be deleted. You can come back to delete it at any time.")

def user_command_loop():
    country_list = overall_country_queries.query_country_names()
    print_command_list()
    while True:        
        user_input = input("\n\t\tPlease enter your next command, type \033[1m'h'\033[0m for the list of commands:\n\t")
        user_input = user_input.lower()

        if user_input in ['e', 'exit']:
            break
        elif user_input in ['h', 'help']:
            print_command_list()
        elif user_input in ['1', 'countries']:
            print_country_list(country_list)
        elif user_input == "2":
            print_entity_list()
        elif user_input.title() in country_list:
            print("\n\n\t\tCountry Attributes:")
            for key, value in database_queries.query_country_attributes(user_input.title()).items():
                print(f"\t\t{key:25}{value:}")
        elif user_input.split()[0].title() in country_list and user_input.split()[1] == 'all':
            print("\n\t\tCountry Overview:\n")
            for key, value in overall_country_queries.query_country_overview(user_input.split()[0].title()).items():
                print(f"\t\t{key:40}{value}")
        elif user_input.split()[0].title() in country_list and (user_input.split()[1] in entity_list or (user_input.split()[1] + " " + user_input.split()[2]) in entity_list):
            print_country_specific_info(user_input)
        elif user_input in ['add fun fact', 'fun fact', 'fact']:
            add_fun_fact()
        elif user_input in ['delete fun fact']:
            delete_fun_fact()
        elif user_input in ['add econ cost', 'econ cost', 'add cost of stay']:
            add_econ_cost()
        elif user_input in ['delete econ cost']:
            delete_econ_cost()
        elif user_input in ['add cuisine rating', 'cuisine rating', 'rate']:
            add_cuisine_rating()
        elif user_input in ['delete cuisine rating']:
            delete_cuisine_rating()
        else:
            print("\n\t\tYour command did not match any of the acceptable ones...")
            print("\n\t\tYou may have mispelled a country or request.")
