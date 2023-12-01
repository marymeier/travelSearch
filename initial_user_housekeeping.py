import user_db_commands

# Global Variables
user_id = ""

def get_user_id():
    global user_id
    return user_id

# Introduction message for a new or existing user once they enter our guide
def intro_message():
    print("\n\n\n\033[1;4m\t\tWelcome to the European Travel and Information Guide\033[0m\n")
    print("\tHere will be a travel guide that details information regarding European\n\t" + 
          "countries. In addition, the guide shoulde provide you with information\n\t" +
          "regarding the countries':")
    print("\t\t- Cuisine" +
         "\n\t\t- Transportation" +
         "\n\t\t- Climate" +
         "\n\t\t- Economy" +
         "\n\t\t- Tourist Attractions" +
         "\n\t\t- National Security Situation, as related to travel\n")

# Check if the user inputed user_id information is only alphabetical letters
def is_alphabetical(input_str):
    return input_str.isalpha()

def user_log_in_message():
    global user_id
    print("\n\n\033[1;4m\t\tBefore you enter our guide we need to validate your account\033[0m\n")
    
    while True:
        user_input = input("\n\t\tAre you an existing user? [Y/N or Yes/No] \033[1m(not case sensitive)\033[0m\n\t").lower()

        # Verifies that user is an existing id through a query
        if user_input in ['y', 'yes']:
            print("\n\t\tGreat, you are an existing user. Let's verify your user_id.")
            user_inputted_id = input("\t\tPlease enter your user_id:\n\t")

            while not is_alphabetical(user_inputted_id):
                print("\n\t\t\033[1mInvalid input.\033[0m Your user_id must only include alphabetical letters.")
                user_inputted_id = input("\t\tPlease enter a valid user_id:\n\t")

            # All user_id's are lowercased
            user_inputted_id.lower()
            # Verifies if user_id exists, if it does sets global user_id var to it
            # If not returns message to user
            if user_db_commands.user_exists(user_inputted_id):
                user_id = user_inputted_id
                print(f"\n\t\tWelcome back \033[1m{user_id}!\033[0m")
                break
            else:
                print(f"\n\t\tUser '\033[1m{user_inputted_id}\033[0m' does not exist, double check the spelling or create a new user.")
        elif user_input in ['n', 'no']:
            print("\n\t\tWelcome new user!")
            set_user_id()
            break
        else:
            print("\n\t\tSorry you entered an invalid input. Please enter 'Y' or 'N' or 'Yes' or 'No'. \033[1m(not case sensitive)\033[0m")

# Sequence of messages and operations to create a user_id for a new user
def set_user_id():
    global user_id
    print("\n\t\tLet's begin by making you an account!")
    print("\t\t\033[1mYour user name must only include alphabetical letters and nothing else!\033[0m\n")
    
    # Verifies that user input is valid for both first and last name
    user_first_name = input("\n\t\tPlease enter your first name:\n\t")
    while not is_alphabetical(user_first_name):
        print("\t\t\033[1mInvalid input.\033[0m Your first name must only include alphabetical letters.")
        user_first_name = input("Please enter your first name:\n\t")

    user_last_name = input("\n\t\tPlease enter your last name:\n\t")
    while not is_alphabetical(user_last_name):
        print("\n\t\t\033[1mInvalid input.\033[0m Your last name must only include alphabetical letters.")
        user_last_name = input("\n\t\tPlease enter your last name:\n\t")
    
    temp_user_id = user_first_name[0] + user_last_name
    temp_user_id = temp_user_id.lower()

    # Checks if the inputed id is available, if it already exists asks if user wants to log in with that id
    while user_db_commands.user_exists(temp_user_id):
        print(f"\n\t\tSorry, the user_id: \033[1m'{temp_user_id}'\033[0m already exists.")

        # Ask the user if they want to log in with the existing id or enter a new one
        user_input = input("\n\t\tDo you want to log in with this user_id? [Y/N or Yes/No] \033[1m(not case sensitive)\033[0m\n\t").lower()

        if user_input in ['y', 'yes']:
            print("\n\t\tGreat! Logging in with existing user_id.")
            user_id = temp_user_id
            break
        elif user_input in ['n', 'no']:
            print("\n\t\tOkay, well let's try creating you a new user_id.")
            set_user_id()
            break
        else:
            print("\n\t\tInvalid input. Please enter 'Y' or 'N' or 'Yes' or 'No'. \033[1m(not case sensitive)\033[0m")
    # If id does not exist in database creates new user based on given ID
    if not user_db_commands.user_exists(temp_user_id):
        print(f"\n\t\tUser_id {temp_user_id} is available.\n")
        if user_db_commands.create_new_user(temp_user_id):
            user_id = temp_user_id
        # Should never reach here but just incase reloops to log-in
        else:
            print("Let's try that again")
            user_log_in_message