class Animal:
    alive = []

    def __init__(self, name : str, health : int = 100, hidden : bool = False)\
            -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        self.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health},"
                f" Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other_animal : "Herbivore | Carnivore") -> None:
        if ((other_animal.hidden is False)
                and not (isinstance(other_animal, Carnivore))):
            other_animal.health -= 50
            if other_animal.health <= 0:
                Animal.alive.remove(other_animal)
