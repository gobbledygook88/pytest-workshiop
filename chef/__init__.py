from collections import namedtuple


Dish = namedtuple("Dish", ["name", "ingredients", "cooked"])


class UnknownDish(Exception):
    pass


def hash_ingredients(ingredients):
    return "-".join(sorted(set(ingredients)))


RECIPES = {
    hash_ingredients(dish.ingredients): dish
    for dish in [
        Dish("soffritto", ["carrots", "celery", "onion"], False),
        Dish("sponge cake", ["sugar", "flour", "eggs", "butter"], True),
    ]
}


def cook(ingredients):
    key = hash_ingredients(ingredients)

    try:
        return RECIPES[key]
    except KeyError:
        raise UnknownDish("No dish known for ingredients")
