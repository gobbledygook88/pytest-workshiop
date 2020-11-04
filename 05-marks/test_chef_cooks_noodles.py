import pytest

from chef import cook
from kitchen import utensils


@pytest.fixture
def pot():
    pot = utensils.Pot()
    pot.boil_water()

    yield pot


@pytest.fixture
def bowl():
    bowl = utensils.Bowl()
    bowl.warm()

    yield bowl


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
