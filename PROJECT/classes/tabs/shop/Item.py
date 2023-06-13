import csv

class Polozka:
    all = []
    def __init__(self, name: str, item_type: str=None, price: float=None, quantity: float=None, units: str=None):
        # Run validation to the received arguments
        if name is None:
            raise ValueError('Jméno položky musí být vyplněno.')
        
        if price is not None:
            if not isinstance(price, (int, float)):
                raise ValueError(f"Cena: {price} musí být celé nebo desetinné číslo.")
            else:
                if price < 0:
                    raise ValueError(f"Cena: {price} musí být číslo větší 0.")

        if quantity is not None:
            if not isinstance(quantity, (int, float)):
                raise ValueError(f"Množství: {price} musí být celé nebo desetinné číslo.")
            else:
                if quantity <= 0:
                    raise ValueError(f"Množství: {quantity} musí být číslo větší 0.")

        # Assing to self object
        self.name = name
        self.item_type = item_type
        self.price = price
        self.quantity = quantity
        self.units = units
        
        # Actions to execute
        Polozka.all.append(self)
        print(f"Byla vytvořena instance třídy Polozka: {self.name}")

    @classmethod

    def instantiate_from_csv(cls, csv_path: str):
        with open("pridat_polozky.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        print(items)

        for item in items:
            Polozka(
                name=item.get("name").strip() if item.get("name").strip() else None,
                item_type=item.get("item_type").strip() if item.get("item_type").strip() else None,
                price=float(item.get("price").strip()) if item.get("price").strip() else None,
                quantity=float(item.get("quantity").strip()) if item.get("quantity").strip() else None,
                units=item.get("units").strip() if item.get("units").strip() else None
                )

    def __str__(self):
        return f"Class: {self.__class__.__name__}, name: {self.name}, item_type: {self.item_type}, price: {self.price}, quantity: {self.quantity}, uom: {self.units}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.item_type}, {self.price}, {self.quantity}, {self.units})"