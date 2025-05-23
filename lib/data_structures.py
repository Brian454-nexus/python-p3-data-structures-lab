spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    # Return a list of names from each spicy food dictionary
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    # Return a list of spicy foods with heat_level greater than 5
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    # Print each spicy food in the specified format with the correct number of 🌶 emojis
    for food in spicy_foods:
        # Multiply the emoji by the heat_level to show spiciness
        heat = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    # Return the first spicy food dictionary that matches the given cuisine
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    # Print only the spicy foods with heat_level greater than 5 using print_spicy_foods
    spiciest = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest)

def get_average_heat_level(spicy_foods):
    # Calculate the average heat_level of all spicy foods
    total_heat = sum(food["heat_level"] for food in spicy_foods)  # Sum all heat levels
    count = len(spicy_foods)  # Count the number of foods
    if count == 0:
        return 0  # Avoid division by zero
    return int(total_heat / count)  # Return the integer average

def create_spicy_food(spicy_foods, spicy_food):
    # Add the new spicy_food dictionary to the list and return the updated list
    spicy_foods.append(spicy_food)
    return spicy_foods
