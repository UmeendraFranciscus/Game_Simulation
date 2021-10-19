#!/usr/bin/env python
# coding: utf-8

class Animal:
    def eat(self):
        return f"{self.name} Eating"
        
    def speak(self, sound):
        return f"{self.name} says {sound}"

class Cat(Animal):
    def __init__(self, name , sex, age):
        super().__init__()
        self.name = name
        self.sex = sex
        self.age = age

    # Instance methods
    def description(self):
        if(self.sex == "Male"):
            return f"{self.name} is {self.age} years old. {self.name} is male cat."
        else:
            return f"{self.name} is {self.age} years old. {self.name} is female cat. "
    
    def if_age_more(self, cutoff_age):
        return self.age > cutoff_age