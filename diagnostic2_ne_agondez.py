def calculate_fuel(cargo_weight):
    total_cargo_weight = 0

    while True:
        cargo = input("Enter the cargo to be added to the starship (satellite, rover, supplies, or launch): ")

        if cargo == "satellite":
            print("\nA satellite has been added to the starship!\n")
            total_cargo_weight += 1000
        elif cargo == "rover":
            print("\nA rover has been added to the starship!\n")
            total_cargo_weight += 2500
        elif cargo == "supplies":
            print("\nSupplies have been added to the starship!\n")
            total_cargo_weight += 500
        elif cargo == "launch":
            print()
            break
        elif total_cargo_weight > 10000:
            print("\nMAX WEIGHT REACHED\n")
            break
        else:
            print("\nThe item is not approved for the mission.\n")

    return (total_cargo_weight + cargo_weight) * 3

cargo_weight = 50000
print(f"The required fuel is: {calculate_fuel(cargo_weight)}")


