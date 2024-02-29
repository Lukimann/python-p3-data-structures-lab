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
    spicy_list = []
    for food in spicy_foods:
        spicy_list.append(food["name"])
    return spicy_list
    

def get_spiciest_foods(spicy_foods):
    return  [food for food in spicy_foods if food["heat_level"] > 5]
    


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
     name = food["name"]
     cuisine = food["cuisine"]
     heat_level = food["heat_level"]
     emoji_heat = "🌶" * heat_level
     print(f"{name} ({cuisine}) | Heat Level: {emoji_heat}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"].lower() == cuisine.lower():
            return food

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        emoji_heat = "🌶" * heat_level
        if food["heat_level"] > 5:
            print(f"{name} ({cuisine}) | Heat Level: {emoji_heat}")

def get_average_heat_level(spicy_foods):
    total_heat = 0
    for food in spicy_foods:
        total_heat += food['heat_level']
        average = total_heat / len(spicy_foods)
    return average
    

def create_spicy_food(spicy_foods, spicy_food):
     spicy_food = {
         "name" : "Griot",
         "cuisine" : "Haitian",
         "heat_level" : 10,
     }
     spicy_foods.append(spicy_food)
     return spicy_foods
     