from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


def test_dish():
    # Req 2.1
    dish = Dish("Lasanha", 25.99)
    assert dish.name == "Lasanha"

    # Req 2.2
    dish1 = Dish("Lasanha", 25.99)
    dish2 = Dish("Lasanha", 25.99)
    assert hash(dish1) == hash(dish2)

    # Req 2.3
    dish1 = Dish("Lasanha", 25.99)
    dish2 = Dish("Feijoada", 35.99)
    assert hash(dish1) != hash(dish2)

    # Req 2.4
    dish1 = Dish("Lasanha", 25.99)
    dish2 = Dish("Lasanha", 25.99)
    assert dish1 == dish2

    # Req 2.5
    dish1 = Dish("Lasanha", 25.99)
    dish2 = Dish("Feijoada", 35.99)
    assert not dish1 == dish2

    # Req 2.6
    dish = Dish("Lasanha", 25.99)
    assert repr(dish) == "Dish('Lasanha', R$25.99)"

    # Req 2.7
    with pytest.raises(TypeError):
        dish = Dish("Lasanha", "invalid_price")

    # Req 2.8
    with pytest.raises(ValueError):
        dish = Dish("Lasanha", -10.0)

    # Req 2.9
    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("tomate")
    dish = Dish("Pizza", 29.99)
    dish.add_ingredient_dependency(ingredient1, 2)
    dish.add_ingredient_dependency(ingredient2, 1)
    assert dish.recipe.get(ingredient1) == 2
    assert dish.recipe.get(ingredient2) == 1

    # Req 2.10
    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("tomate")
    dish = Dish("Pizza", 29.99)
    dish.add_ingredient_dependency(ingredient1, 2)
    dish.add_ingredient_dependency(ingredient2, 1)
    assert dish.get_restrictions() == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }

    # Req 2.11
    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("tomate")
    dish = Dish("Pizza", 29.99)
    dish.add_ingredient_dependency(ingredient1, 2)
    dish.add_ingredient_dependency(ingredient2, 1)
    assert dish.get_ingredients() == {ingredient1, ingredient2}

    # Req 2.12
    dish1 = Dish("Lasanha", 25.99)
    dish2 = Dish("Lasanha", 25.99)
    assert hash(dish1) == hash(dish2)
    assert dish1 == dish2
    assert repr(dish1) == "Dish('Lasanha', R$25.99)"
    assert dish1.name == "Lasanha"
    assert dish1.price == 25.99
    assert dish1.recipe == {}
