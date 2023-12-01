import sqlite3
import overall_country_queries

def query_all_users():
    connection = sqlite3.connect('travelSearch.db')
    cursor = connection.cursor()

    select_query = "SELECT * FROM Users;"
    cursor.execute(select_query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    connection.close()

def create_new_user(user_id):
    connection = sqlite3.connect('travelSearch.db')
    cursor = connection.cursor()
    
    # Check if a user with the same user_id already exists
    check_existing_user_query = f"SELECT * FROM Users WHERE user_id = '{user_id}'"
    cursor.execute(check_existing_user_query)

    existing_user = cursor.fetchone()

    if existing_user:
        print(f"A user with the user_id  \033[1m'{user_id}'\033[0m already exists")
        connection.close()
        return False
    else:
        # Insert a new user
        create_user_command = f"INSERT INTO Users (user_id) VALUES ('{user_id}')"
        cursor.execute(create_user_command)
        
    connection.commit()
    connection.close()

    print(f"\t\tYour new account's user_id is: \033[1m'{user_id}'\033[0m be sure to save it somewhere safe!")
    return True

def delete_user(user_id, country_name=None):
    connection = sqlite3.connect('travelSearch.db')
    cursor = connection.cursor()
    if country_name is not None:
        country_name = country_name.title()

    if country_name is None:
        # If no country_name is provided, delete all rows with the specified user_id
        delete_user_command = f"DELETE FROM Users WHERE user_id = '{user_id}'"
    else:
        # If country_name is provided, delete the specific row with matching user_id and country_name
        delete_user_command = f"DELETE FROM Users WHERE user_id = '{user_id}' AND country_name = '{country_name}'"
    
    cursor.execute(delete_user_command)

    connection.commit()
    connection.close()

def delete_all_users():
    connection = sqlite3.connect('travelSearch.db')
    cursor = connection.cursor()

    # Delete all rows from the Users table
    delete_command = "DELETE FROM Users"
    cursor.execute(delete_command)

    connection.commit()
    connection.close()

def user_exists(user_id):
    connection = sqlite3.connect('travelSearch.db')
    cursor = connection.cursor()

    # Check if a record with the given user_id exists
    check_existing_record_query = f"SELECT * FROM Users WHERE user_id = '{user_id}'"
    cursor.execute(check_existing_record_query)

    existing_record = cursor.fetchone()

    connection.close()

    return existing_record is not None

def insert_tourist_attraction_fun_fact(user_id, country_name, tourist_attraction_fun_fact):
    connection = sqlite3.connect('travelSearch.db')
    cursor = connection.cursor()
    country_name = country_name.title()

    available_countries = overall_country_queries.query_country_names()
    if country_name.title() not in available_countries:
        print(f"Error: {country_name} is not a valid country. Please enter a valid country")
        connection.close()
        return False

    # Check if a record with the same user_id and country_name already exists
    check_existing_record_query = f"SELECT * FROM Users WHERE user_id = '{user_id}' AND country_name = '{country_name}'"
    cursor.execute(check_existing_record_query)

    existing_record = cursor.fetchone()

    if existing_record:
        # If a record exists, check if tourist_attraction_fun_fact is already set
        if existing_record[2] is not None:
            # If tourist_attraction_fun_fact already exists, ask the user if they want to update it
            update_confirmation = input(f"A tourist attraction fun fact already exists for user {user_id} in {country_name}. Do you want to update it? (yes/no): ")
            
            if update_confirmation.lower() == 'yes':
                # Update existing tourist_attraction_fun_fact
                update_command = f"UPDATE Users SET tourist_attraction_fun_fact = '{tourist_attraction_fun_fact}' WHERE user_id = '{user_id}' AND country_name = '{country_name}'"
                cursor.execute(update_command)
                print("Tourist attraction fun fact updated successfully.")
            else:
                print("No changes made, original submission stands.")
        else:
            # Insert tourist_attraction_fun_fact if it doesn't exist
            update_command = f"UPDATE Users SET tourist_attraction_fun_fact = '{tourist_attraction_fun_fact}' WHERE user_id = '{user_id}' AND country_name = '{country_name}'"
            cursor.execute(update_command)
            print("Tourist attraction fun fact inserted successfully.")
    else:
        # If no record exists, insert a new record
        insert_command = f"UPDATE Users SET country_name = '{country_name}', tourist_attraction_fun_fact = '{tourist_attraction_fun_fact}' WHERE user_id = '{user_id}'"
        cursor.execute(insert_command)
        print("New Tourist Attraction Fun Fact inserted successfully.")

    connection.commit()
    connection.close()

    return True

def delete_tourist_attraction_fun_fact(user_id, country_name):
    connection = sqlite3.connect('travelSearch.db')
    cursor = connection.cursor()
    country_name = country_name.title()

    available_countries = overall_country_queries.query_country_names()
    if country_name not in available_countries:
        print(f"Error: {country_name} is not a valid country. Please enter a valid country")
        connection.close()
        return False

    # Check if a record with the given user_id and country_name exists
    check_existing_record_query = f"SELECT * FROM Users WHERE user_id = '{user_id}' AND country_name = '{country_name}'"
    cursor.execute(check_existing_record_query)

    existing_record = cursor.fetchone()

    if existing_record:
        # If a record exists, check if tourist_attraction_fun_fact is set
        if existing_record[2] is not None:
            # Delete existing tourist_attraction_fun_fact
            delete_command = f"UPDATE Users SET tourist_attraction_fun_fact = NULL WHERE user_id = '{user_id}' AND country_name = '{country_name}'"
            cursor.execute(delete_command)
            print("Your tourist attraction fun fact was deleted successfully.")
        else:
            print(f"No tourist attraction fun fact exists for your user_id: {user_id} in {country_name}.")
    else:
        print(f"No record found for user {user_id} in {country_name}.")

    connection.commit()
    connection.close()

    return True

def insert_economic_cost_of_stay(user_id, country_name, economic_cost_of_stay):
    connection = sqlite3.connect('travelSearch.db')
    cursor = connection.cursor()
    country_name = country_name.title()

    available_countries = overall_country_queries.query_country_names()
    if country_name.title() not in available_countries:
        print(f"Error: {country_name} is not a valid country. Please enter a valid country")
        connection.close()
        return False

    # Check if a record with the same user_id and country_name already exists
    check_existing_record_query = f"SELECT * FROM Users WHERE user_id = '{user_id}' AND country_name = '{country_name}'"
    cursor.execute(check_existing_record_query)

    existing_record = cursor.fetchone()

    if existing_record:
        # If a record exists, check if economic_cost_of_stay is already set
        if existing_record[3] is not None:
            # If economic_cost_of_stay already exists, ask the user if they want to update it
            update_confirmation = input(f"An estimated economic cost of stay for a week already exists for user {user_id} in {country_name}. Do you want to update it? (yes/no): ")
            
            if update_confirmation.lower() == 'yes':
                # Update existing economic_cost_of_stay
                update_command = f"UPDATE Users SET economic_cost_of_stay = '{economic_cost_of_stay}' WHERE user_id = '{user_id}' AND country_name = '{country_name}'"
                cursor.execute(update_command)
                print("Your estimated economic cost of stay for a week was updated successfully.")
            else:
                print("No changes made, original submission stands.")
        else:
            # Insert economic_cost_of_stay if it doesn't exist
            update_command = f"UPDATE Users SET economic_cost_of_stay = '{economic_cost_of_stay}' WHERE user_id = '{user_id}' AND country_name = '{country_name}'"
            cursor.execute(update_command)
            print("Your estimated economic cost of stay for a week was inserted successfully.")
    else:
        # If no record exists, insert a new record
        insert_command = f"UPDATE Users SET country_name = '{country_name}', economic_cost_of_stay = '{economic_cost_of_stay}' WHERE user_id = '{user_id}'"
        cursor.execute(insert_command)
        print("Your new Estimated economic cost of stay for a week was inserted successfully.")

    connection.commit()
    connection.close()

    return True

def delete_economic_cost_of_stay(user_id, country_name):
    connection = sqlite3.connect('travelSearch.db')
    cursor = connection.cursor()
    country_name = country_name.title()

    available_countries = overall_country_queries.query_country_names()
    if country_name not in available_countries:
        print(f"Error: {country_name} is not a valid country. Please enter a valid country")
        connection.close()
        return False

    # Check if a record with the given user_id and country_name exists
    check_existing_record_query = f"SELECT * FROM Users WHERE user_id = '{user_id}' AND country_name = '{country_name}'"
    cursor.execute(check_existing_record_query)

    existing_record = cursor.fetchone()

    if existing_record:
        # If a record exists, check if economic_cost_of_stay is set
        if existing_record[3] is not None:
            # Delete existing economic_cost_of_stay
            delete_command = f"UPDATE Users SET economic_cost_of_stay = NULL WHERE user_id = '{user_id}' AND country_name = '{country_name}'"
            cursor.execute(delete_command)
            print("Your estimated economic cost of stay for a week was deleted successfully.")
        else:
            print(f"No estimated economic cost of stay for a week exists for your user_id: {user_id} in {country_name}.")
    else:
        print(f"No record found for user {user_id} in {country_name}.")

    connection.commit()
    connection.close()

    return True

def insert_national_cuisine_rating(user_id, country_name, national_cuisine_rating):
    connection = sqlite3.connect('travelSearch.db')
    cursor = connection.cursor()
    country_name = country_name.title()

    available_countries = overall_country_queries.query_country_names()
    if country_name not in available_countries:
        print(f"Error: {country_name} is not a valid country. Please enter a valid country")
        connection.close()
        return False

    # Check if a record with the same user_id and country_name already exists
    check_existing_record_query = f"SELECT * FROM Users WHERE user_id = '{user_id}' AND country_name = '{country_name}'"
    cursor.execute(check_existing_record_query)

    existing_record = cursor.fetchone()

    if existing_record:
        # If a record exists, check if national_cuisine_rating is already set
        if existing_record[4] is not None:
            # If national_cuisine_rating already exists, ask the user if they want to update it
            update_confirmation = input(f"A national cuisine rating already exists for user {user_id} in {country_name}. Do you want to update it? (yes/no): ")
            
            if update_confirmation.lower() == 'yes':
                # Update existing national_cuisine_rating
                update_command = f"UPDATE Users SET national_cuisine_rating = '{national_cuisine_rating}' WHERE user_id = '{user_id}' AND country_name = '{country_name}'"
                cursor.execute(update_command)
                print("The National cuisine rating was updated successfully.")
            else:
                print("No changes made, original submission stands.")
        else:
            # Insert national_cuisine_rating if it doesn't exist
            update_command = f"UPDATE Users SET national_cuisine_rating = '{national_cuisine_rating}' WHERE user_id = '{user_id}' AND country_name = '{country_name}'"
            cursor.execute(update_command)
            print("The National cuisine rating was inserted successfully.")
    else:
        # If no record exists, insert a new record
        insert_command = f"UPDATE Users SET country_name = '{country_name}', national_cuisine_rating = '{national_cuisine_rating}' WHERE user_id = '{user_id}'"
        cursor.execute(insert_command)
        print("The National cuisine rating was inserted successfully.")

    connection.commit()
    connection.close()

    return True

def delete_national_cuisine_rating(user_id, country_name):
    connection = sqlite3.connect('travelSearch.db')
    cursor = connection.cursor()
    country_name = country_name.title()

    available_countries = overall_country_queries.query_country_names()
    if country_name not in available_countries:
        print(f"Error: {country_name} is not a valid country. Please enter a valid country")
        connection.close()
        return False

    # Check if a record with the given user_id and country_name exists
    check_existing_record_query = f"SELECT * FROM Users WHERE user_id = '{user_id}' AND country_name = '{country_name}'"
    cursor.execute(check_existing_record_query)

    existing_record = cursor.fetchone()

    if existing_record:
        # If a record exists, check if national_cuisine_rating is set
        if existing_record[4] is not None:
            # Delete existing national_cuisine_rating
            delete_command = f"UPDATE Users SET national_cuisine_rating = NULL WHERE user_id = '{user_id}' AND country_name = '{country_name}'"
            cursor.execute(delete_command)
            print("Your national cuisine rating was deleted successfully.")
        else:
            print(f"No national cuisine rating exists for your user_id: {user_id} in {country_name}.")
    else:
        print(f"No record found for user {user_id} in {country_name}.")

    connection.commit()
    connection.close()

    return True

# def main():
#     delete_user("bschneider")
#     query_all_users()

# if __name__ == "__main__":
#     main()