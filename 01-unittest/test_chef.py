from unittest import TestCase
from chef import cook


class TestChefSkills(TestCase):
    def test_chef_can_prepare_ingredients(self):
        ingredients = ["carrots", "celery", "onion"]

        dish = cook(ingredients)

        self.assertEqual(dish.name, "soffritto")
        self.assertFalse(dish.cooked)
        self.assertListEqual(ingredients, dish.ingredients)

    def test_chef_can_bake_a_sponge_cake(self):
        ingredients = ["sugar", "flour", "eggs", "butter"]

        dish = cook(ingredients)

        self.assertEqual(dish.name, "sponge cake")
        self.assertTrue(dish.cooked)
        self.assertListEqual(ingredients, dish.ingredients)
