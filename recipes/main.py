from pprint import pprint


with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        ingredients_count = int(file.readline())
        ingredients = []
        for _ in range(ingredients_count):
            ingredient, count, measure = file.readline().strip().split(' | ')
            recipe = {
                'ingredient_name': ingredient,
                'quantity': count,
                'measure': measure
            }
            ingredients.append(recipe)
        file.readline()
        cook_book[dish_name] = ingredients

    pprint(cook_book, sort_dicts=False)
    

