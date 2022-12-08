from typing import List, Optional


class Pizza:
    MARGARITA = "Margarita"
    PEPPERONI = "Pepperoni"

    def __init__(self, ingredients: List[str]):
        self.ingredients = ingredients

    @classmethod
    def classic_flavours(
        cls, flavour: str, extra_ingredients: Optional[List[str]] = None
    ):
        """
        Create a pizza in a classic named flavour
        """
        extra_ingredients = extra_ingredients if extra_ingredients is not None else []
        ingredients = {
            Pizza.MARGARITA: ["Cheese"],
            Pizza.PEPPERONI: ["Cheese", "Pepperoni"],
        }.get(flavour, None)

        if ingredients is None:
            raise ValueError(f"{flavour} is not a valid classic flavour")

        return type(flavour, (Pizza,), {})(ingredients + extra_ingredients)
