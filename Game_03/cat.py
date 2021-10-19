class Cat():
    # Attributes
    def __init__(self, sex, age, personality):
        self.sex = sex
        self.age = age
        self.personality = personality
        print("--- Cat Class Added ---")

    # Methods
    def __str__(self):
        return f"Age group -- {self.age}, Gender -- {self.sex}, Personality -- {self.personality}"

    def eat(self):
        return f"Eating"
    
    def sleep(self):
        return f"Sleeping"