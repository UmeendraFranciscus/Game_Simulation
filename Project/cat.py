#!/usr/bin/env python
# coding: utf-8

# In[1]:


# sex
#  - Male
#  - Female

# personality (temperament)
#  - friendly
#  - aggressive


# In[2]:


class Animal:

    def __init__(self):
        print("--- Animal created ---")

    def eat(self):
        return f"{self.name} Eating"
        
    def speak(self, sound):
        return f"{self.name} says {sound}"

class Cat(Animal):
    def __init__(self, name, age, sex, personality):
        super().__init__()
        self.name = name
        self.age = age
        self.sex = sex
        self.personality = personality
        print("--- Cat created ---")

    # Instance methods
    def description(self):
        if(self.sex == "Male"):
            return f"{self.name} is {self.age} years old. his temperament is {self.personality}."
        else:
            return f"{self.name} is {self.age} years old. her temperament is {self.personality}. "
    
    def is_friendly(self):
        return self.personality == "friendly"
    
    def if_age_more(self, cutoff_age):
        return self.age > cutoff_age
    
    def stepChange(current, moves):
        nextgrid = np.zeros(current.shape, dtype="int16")

        for row in range(MAXROW):
            for col in range(MAXCOL):
                for g in range(current[row,col]):
                    nextrow = row + random.choice(moves)
                    nextcol = col + random.choice(moves)
                    #print("Newpos = ", nextrow, nextcol)
                    if nextrow < 0:
                        nextrow = 0
                    if nextcol < 0:
                        nextcol = 0
                    if nextrow >= MAXROW:
                        nextrow = MAXROW - 1
                    if nextcol >= MAXCOL:
                        nextcol = MAXCOL - 1
                    nextgrid[nextrow, nextcol] += 1
        return nextgrid


# In[ ]:




