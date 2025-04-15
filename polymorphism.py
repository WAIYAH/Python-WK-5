# Task 2: Polymorphism Challenge with Driving and Flying actions

# Parent class to define the action interface
class Action:
    # Method to be overridden by child classes (polymorphism)
    def move(self):
        pass

# Child class for Driving action
class Driving(Action):
    # Override the move method to define driving behavior
    def move(self):
        return "Car...move(): Vroom! The car speeds down the highway."

# Child class for Flying action
class Flying(Action):
    # Override the move method to define flying behavior
    def move(self):
        return "Plane...move(): Whoosh! The plane soars through the sky."

# Function to demonstrate polymorphism
def perform_action(action):
    print(action.move())

# Testing the polymorphic behavior
if __name__ == "__main__":
    # Create instances of Driving and Flying
    car = Driving()
    plane = Flying()

    # Use the same method call to get different behaviors
    perform_action(car)   # Output: Car...move(): Vroom! The car speeds down the highway.
    perform_action(plane) # Output: Plane...move(): Whoosh! The plane soars through the sky.