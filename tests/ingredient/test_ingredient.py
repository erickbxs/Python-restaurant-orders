from src.models.ingredient import Ingredient, Restriction


def test_ingredient():
    ingrediente1 = Ingredient("queijo mussarela")
    ingrediente2 = Ingredient("presunto")
    assert hash(ingrediente1) != hash(ingrediente2)

    ingrediente1 = Ingredient("queijo mussarela")
    ingrediente2 = Ingredient("queijo mussarela")
    assert ingrediente1 == ingrediente2

    ingrediente1 = Ingredient("queijo mussarela")
    ingrediente2 = Ingredient("presunto")
    assert not ingrediente1 == ingrediente2

    ingrediente = Ingredient("queijo mussarela")
    assert repr(ingrediente) == "Ingredient('queijo mussarela')"

    ingrediente = Ingredient("queijo mussarela")
    assert ingrediente.name == "queijo mussarela"

    ingrediente = Ingredient("queijo mussarela")
    assert ingrediente.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }

    ingrediente1 = Ingredient("queijo mussarela")
    ingrediente2 = Ingredient("queijo mussarela")
    assert hash(ingrediente1) == hash(ingrediente2)
    assert ingrediente1 == ingrediente2
    assert repr(ingrediente1) == "Ingredient('queijo mussarela')"
    assert ingrediente1.name == "queijo mussarela"
    assert ingrediente1.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }
