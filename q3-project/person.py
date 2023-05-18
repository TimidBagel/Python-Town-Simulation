from random import choice

sexes = ["male", "female"]

class Person:
    def __init__(self, name, health, food, backpack, capacity, morale):
        self.name = name
        self.health = health
        self.food = food
        self.backpack = backpack
        self.capacity = capacity
        self.morale = morale
        self.task_timer = 0
        self.condition = None
        self.condition_timer = 0
        self.sex = choice(sexes)

    def takeItems(self, newItem, capacity):
        if len(self.backpack) >= capacity:
            self.backpack.append(newItem)
            return True
        else:
            return False
        
    def execute_task(self):
        self.task_timer -= 1
        if self.task_timer <= 0:
            return "finished"
        else:
            return "unfinished"
        
    def execute_condition(self):
        if self.condition != None:
            if self.condition_timer <= 0:
                self.condition = None

            elif self.condition == "diseased":
                self.condition_timer -= 1
                self.health -= 1
            
    def hunger(self, rate):
        if self.health < 20:
            rate += 1
        self.food -= rate

    task = None