import random
from datetime import datetime, timedelta
import pycountry
import json

def load_countries_data():
    with open('countries_data.json', 'r', encoding='utf-8') as file:
        countries_data = json.load(file)
    return countries_data


def generate_daily_diet(country_data):
    # Get lists for different meal and snack options from country data
    breakfast_options = country_data.get("breakfast", [])
    lunch_options = country_data.get("lunch", [])
    dinner_options = country_data.get("dinner", [])
    snack_options = country_data.get("snack", [])

    # Function to randomly pick an option from a list
    def get_random_option(options):
        return random.choice(options)

    # Generate a random daily diet including breakfast, lunch, dinner, and snack
    breakfast = get_random_option(breakfast_options)
    lunch = get_random_option(lunch_options)
    dinner = get_random_option(dinner_options)
    snack = get_random_option(snack_options)

    return f"Breakfast: {breakfast}\nLunch: {lunch}\nDinner: {dinner}\nSnack: {snack}"

# Load countries data from the JSON file
countries_data = load_countries_data()

# Get a list of all countries
all_countries = list(countries_data.keys())

# Print the names of all countries
print("Select a country:")
for idx, country in enumerate(all_countries, start=1):
    print(f"{idx}. {country}")

# Get user input for selecting a country
selected_index = int(input("Enter the number corresponding to your country: "))
selected_country = all_countries[selected_index - 1]

# Get today's date
today = datetime.now().date()

# Calculate the date one week from today
one_week_from_today = today + timedelta(days=7)

# Print the dates for the next week with a random daily diet including snacks for the selected country
current_date = today
while current_date < one_week_from_today:
    print(f"\nYour Daily Diet for {selected_country} - {current_date.strftime('%d-%m-%y1')}:")
    print(generate_daily_diet(countries_data[selected_country]))
    current_date += timedelta(days=1)


input('Press ENTER to exit')