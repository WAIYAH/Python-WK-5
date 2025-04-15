# Task 1: Design a Superhero class with attributes, methods, and inheritance

# Parent class for all superheroes
class Superhero:
    # Constructor to initialize superhero attributes
    def __init__(self, name, power, strength, speed):
        self.name = name          # Name of the superhero
        self.power = power        # Superpower (e.g., "flight", "super strength")
        self.strength = strength  # Strength level (1-100)
        self.speed = speed        # Speed level (1-100)
    
    # Method to describe the superhero's abilities
    def describe(self):
        return f"{self.name} has the power of {self.power}, with strength {self.strength} and speed {self.speed}."
    
    # Method to simulate using their power
    def use_power(self):
        return f"{self.name} uses {self.power} to save the day!"

# Child class inheriting from Superhero with unique encapsulation
class EnhancedSuperhero(Superhero):
    def __init__(self, name, power, strength, speed, secret_weapon):
        # Call the parent class constructor to initialize inherited attributes
        super().__init__(name, power, strength, speed)
        # Encapsulated attribute (using double underscore for name mangling)
        self.__secret_weapon = secret_weapon
    
    # Method to reveal the secret weapon (getter for encapsulated attribute)
    def reveal_secret_weapon(self):
        return f"{self.name}'s secret weapon is {self.__secret_weapon}!"

# Testing the classes
if __name__ == "__main__":
    # Create a basic superhero
    hero1 = Superhero("Captain Thunder", "lightning control", 85, 70)
    print(hero1.describe())      # Output: Captain Thunder has the power of lightning control, with strength 85 and speed 70.
    print(hero1.use_power())     # Output: Captain Thunder uses lightning control to save the day!

    # Create an enhanced superhero with a secret weapon
    hero2 = EnhancedSuperhero("Shadow Hawk", "invisibility", 60, 90, "stealth dagger")
    print(hero2.describe())      # Output: Shadow Hawk has the power of invisibility, with strength 60 and speed 90.
    print(hero2.use_power())     # Output: Shadow Hawk uses invisibility to save the day!
    print(hero2.reveal_secret_weapon())  # Output: Shadow Hawk's secret weapon is stealth dagger!