class Human:

  MAX_ENERGY = 100

  def __init__(self):
    self.name = "Bob"
    self.age = 0
    self.energy = Human.MAX_ENERGY

  def __str__(self):
    return f"My name is {self.name}"

  def __repr__(self):
    return f"Human(name = {self.name}, age = {self.age}, energy = {self.energy})"

  def display(self):
    print(f"My name is {self.name}")

  def grow(self):
    self.age += 1

  def eat(self, ammount):
    self.energy += ammount
    if self.energy > Human.MAX_ENERGY:
      self.energy = Human.MAX_ENERGY

  def move(self, distance):
    self.energy -= distance
    if self.energy < 0:
      self.energy = 0



if (__name__ == "__main__"):
  human = Human()
  human.display()