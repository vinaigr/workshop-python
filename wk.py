import scrapy as sc
import random as rd
def mult(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("ThreeFive")
        elif i % 3 == 0:
            print("Three")
        elif i % 5 == 0:
            print("Five")
        else:
            print(i)

#mult(16

def calculate(lst):
    if lst == list:
        print("False it's not a list")
    else:
        a = 0
        b = 0
        for i in range(len(lst)):
            if lst[i] <= '9' and lst[i] >= '0':
                a += int(lst[i])
            else:
                continue
    print(a)

#calculate(['1', '3', "tomato", '5'])

def generator():
    a = rd.randint(1, 100)
    print(a)
#generator()

class Villager():
    def __init__(self, name):
        self.hp = 100
        self.attack = 5
        self.stamina = 100
        self.name = name
    def attack(self):
        return self.stamina - 10
    def rest(self):
        self.stamina = 100
        return self.stamina
    def damage(self, hp_damage):
        if self.hp <= 0:
            print("I am dead")
        else:
            self.hp = hp_damage - self.hp
        return self.hp
    def speak(self):
        print("Hello my name is {}".format(self.name))


class knight(Villager):
    def __init__(self, name):
        super().__init__(name)
        self.hp = 150
        self.attack = 15
        self.stamina = 100
        self.armor = 50
        #self.name = name
    def damage(self, hp_damage):
        if self.hp <= 0:
            print("I am dead")
        else:
            hp_damage = hp_damage - self.armor
            super().damage(hp_damage)
    def special_attack(self):
        return self.stamina - 50
        
vl = Villager("jerem")
kg = knight("mesmer")
if __name__ == '__main__':
    print(vl.hp)
    print(kg.speak())

