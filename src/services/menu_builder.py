from typing import Dict, List
from src.models.dish import Dish
from src.models.ingredient import restriction_map
from src.services.inventory_control import InventoryMapping
from src.services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str) -> None:
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 6
    def is_dish_available(self, dish: Dish) -> bool:
        for ingredient, quantity in dish.recipe.items():
            if (
                ingredient not in self.inventory.inventory
                or self.inventory.inventory[ingredient] < quantity
            ):
                return False
        return True

    # Req 4
    def get_main_menu(self, restriction: restriction_map = None) -> List[Dict]:
        main_menu = []
        for dish in self.menu_data.dishes:
            if (
                restriction is None
                or restriction not in dish.get_restrictions()
            ):
                if self.is_dish_available(dish):
                    dish_info = {
                        "dish_name": dish.name,
                        "ingredients": list(dish.recipe.keys()),
                        "price": dish.price,
                        "restrictions": dish.get_restrictions(),
                    }
                    main_menu.append(dish_info)
        return main_menu
