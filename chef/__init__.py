from collections import namedtuple


Dish = namedtuple("Dish", ["name", "ingredients", "cooked", "type"])


class UnknownDish(Exception):
    pass


def hash_ingredients(ingredients):
    return "-".join(sorted(set(ingredients)))


RECIPES = {
    hash_ingredients(dish.ingredients): dish
    for dish in [
        Dish("soffritto", ["carrots", "celery", "onion"], False, "base"),
        Dish("sponge cake", ["sugar", "flour", "eggs", "butter"], True, "dessert"),
        Dish(
            "rice noodles",
            ["miso", "dashi stock", "seaweed", "tofu", "rice noodles"],
            True,
            "soup noodles",
        ),
        Dish(
            "belt noodles",
            ["miso", "dashi stock", "seaweed", "tofu", "belt noodles"],
            True,
            "soup noodles",
        ),
        Dish(
            "knife cut noodles",
            ["miso", "dashi stock", "seaweed", "tofu", "knife cut noodles"],
            True,
            "soup noodles",
        ),
    ]
}


def cook(ingredients):
    key = hash_ingredients(ingredients)

    try:
        return RECIPES[key]
    except KeyError:
        raise UnknownDish("No dish known for ingredients")
