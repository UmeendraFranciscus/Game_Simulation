class Animal:
    # Instance methods
    def eat(self):
        return f"{self.name} Eating"
        
    def speak(self, sound):
        return f"{self.name} says {sound}"

class Cat(Animal):
    def __init__(self, name, sex, personality):
        super().__init__()
        self.name = name
        self.sex = sex
        self.personality = personality

    # Instance methods
    def description(self):
        if(self.sex == "Male"):
            return f"{self.name}. his temperament is {self.personality}."
        elif(self.sex == "Female"):
            return f"{self.name}. her temperament is {self.personality}. "
        else:
            return "OUT OF RANGE"
    
    def is_friendly(self):
        return self.personality == "Friendly"

class Team_A(Cat):
    def __init__(self, name, sex, personality):
        super().__init__(name, sex, personality)


class Team_B(Cat):
    def __init__(self, name, sex, personality):
        super().__init__(name, sex, personality)