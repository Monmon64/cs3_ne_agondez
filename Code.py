class Plant:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def is_alive(self):
        return self.health > 0

    def attack(self, zombie, turn):
        if self.is_alive() and zombie.is_alive():

            if self.name == "Kernel Pult" and turn % 5 == 0:
                print(f"{self.name} uses Butter!")
                zombie.buttered = True

            zombie.health -= self.damage

            print(f"{self.name} attacks the Zombie for {self.damage} damage.")

class Zombie:
    def __init__(self, name, health, damage, distance):
        self.name = name
        self.health = health
        self.damage = damage
        self.distance = distance
        self.buttered = False

    def is_alive(self):
        return self.health > 0

    def move(self):
        if self.buttered:
            print(
                f"{self.name} is stunned."
            )
            self.buttered = False

        elif self.distance > 0:
            self.distance -= 1
            print(
                f"{self.name} moves closer. "
                f"Distance: {self.distance}"
            )

    def attack(self, plant):
        if self.is_alive() and plant.is_alive():
            plant.health -= self.damage

            print(
                f"{self.name} attacks {plant.name} "
                f"for {self.damage} damage."
            )

plant1 = Plant("Peashooter", 20, 10)
plant2 = Plant("Kernel Pult", 20, 5)
zombie = Zombie("Zombie", 100, 5, 9)
turn = 1

print("PvZ ni Agondez and Aldep")

while True:
    print(f"\nTurn {turn}")

    if plant1.is_alive():
        plant1.attack(zombie, turn)

        if not zombie.is_alive():
            print("\nYour plants win. The lawn is safe.")
            break

    if plant2.is_alive():
        plant2.attack(zombie, turn)

        if not zombie.is_alive():
            print("\nYour plants win. The lawn is safe.")
            break

    if zombie.buttered:
        zombie.move()

    elif zombie.distance > 0:
        zombie.move()

    else:
 
        if plant1.is_alive():
            zombie.attack(plant1)

        elif plant2.is_alive():
            zombie.attack(plant2)

    print("\nStatus:")
    print(f"{plant1.name} health: {plant1.health}")
    print(f"{plant2.name} health: {plant2.health}")
    print(f"{zombie.name} health: {zombie.health}")
    print(f"{zombie.name} distance: {zombie.distance}")

    if not plant1.is_alive() and not plant2.is_alive():
        print("\n[Insert music and Dave screaming] THE ZOMBIES ATE YOUR BRAIN!")
        break

    turn += 1