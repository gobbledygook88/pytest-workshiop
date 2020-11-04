import pytest

from chef import cook


def test_chef_can_cook_rice_noodles():
    ingredients = ["miso", "dashi stock", "seaweed", "tofu", "rice noodles"]

    dish = cook(ingredients)

    assert dish.type == "soup noodles"


def test_chef_can_cook_belt_noodles():
    ingredients = ["miso", "dashi stock", "seaweed", "tofu", "belt noodles"]

    dish = cook(ingredients)

    assert dish.type == "soup noodles"


def test_chef_can_cook_knife_cut_noodles():
    ingredients = ["miso", "dashi stock", "seaweed", "tofu", "knife cut noodles"]

    dish = cook(ingredients)

    assert dish.type == "soup noodles"
