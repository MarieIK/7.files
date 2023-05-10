from pprint import pprint


def open_file():
    with open('recipes.txt', encoding='utf-8') as file:
        cook_book = {}
        for line in file:
            dish_name = line.strip()
            ingredients_count = int(file.readline())
            ingredients = []
            for _ in range(ingredients_count):
                ingredient, quantity, measure = file.readline().strip().split(' | ')
                recipe = {
                    'ingredient_name': ingredient,
                    'quantity': quantity,
                    'measure': measure
                }
                ingredients.append(recipe)
            file.readline()
            cook_book[dish_name] = ingredients
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in (cook_book := open_file()):
            for ingredient in cook_book[dish]:
                try:
                    shop_list[ingredient['ingredient_name']]['quantity'] += int(ingredient['quantity']) * int(
                        person_count)
                except KeyError:
                    shop_list.update({ingredient['ingredient_name']: {'measure': ingredient['measure'],
                                                                      'quantity': int(ingredient['quantity']) * int(
                                                                          person_count)}})

    return shop_list


pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 10), sort_dicts=False)

