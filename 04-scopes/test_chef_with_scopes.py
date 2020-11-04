from chef import cook


class TestChefSkills:
    def test_chef_can_prepare_ingredients(self):
        ingredients = ["carrots", "celery", "onion"]

        dish = cook(ingredients)

        assert dish.name == "soffritto"
        assert not dish.cooked
        assert ingredients == dish.ingredients

    def test_chef_can_bake_a_sponge_cake(self):
        ingredients = ["sugar", "flour", "eggs", "butter"]

        dish = cook(ingredients)

        assert dish.name == "sponge cake"
        assert dish.cooked
        assert ingredients == dish.ingredients
