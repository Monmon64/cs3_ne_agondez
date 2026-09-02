class Starship:
    def __init__(self, base_weight, cargo_weight, final_fuel):
        self.base_weight = base_weight
        self.cargo_weight = cargo_weight
        self.final_fuel = final_fuel

    def calculate_fuel(self):
        final_fuel = 0
        base_ship_weight = 50000
        total_weight = self.base_weight + self.cargo_weight
        final_fuel = total_weight * 3

        return final_fuel

Starship(50000, 0, 0)
starship.load_cargo(1000)
starship.load_cargo(1000)
starship.load_cargo(1000)

print(f"Final fuel needed: {starship.calculate_fuel()}")

    

