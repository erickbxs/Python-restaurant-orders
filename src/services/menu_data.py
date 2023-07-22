import csv
from typing import Dict, List, Tuple, Union, Set
from models.dish import Dish, Recipe
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes: Set[Dish] = set()
        self.ingredients: Set[Ingredient] = set()

        # Carrega os pratos e suas receitas a partir do arquivo CSV
        self._load_data_from_csv(source_path)

    def _load_data_from_csv(self, source_path: str) -> None:
        # Dicionário para armazenar temporariamente as receitas de cada prato
        dish_recipes: Dict[str, Recipe] = {}

        with open(source_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                dish_name = row["dish"]
                ingredient_name = row["ingredient"]
                recipe_amount = int(row["recipe_amount"])

                # Verifica se o prato já foi adicionado ao dicionário
                # de receitas
                if dish_name not in dish_recipes:
                    dish_price = float(row["price"])
                    dish = Dish(dish_name, dish_price)
                    self.dishes.add(dish)
                    dish_recipes[dish_name] = {}

                # Verifica se o ingrediente já foi adicionado ao conjunto
                # de ingredientes
                ingredient = Ingredient(ingredient_name)
                self.ingredients.add(ingredient)

                # Adiciona o ingrediente e sua quantidade à receita do prato
                dish_recipes[dish_name][ingredient] = recipe_amount

        # Relaciona as receitas com os pratos criados
        for dish in self.dishes:
            dish.recipe = dish_recipes[dish.name]
