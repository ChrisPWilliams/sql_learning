class Animal:
    def __init__(self, name):
        self.name = name
        self.type = "generic"
        self.has_fur = False
        self.has_feathers = False
        self.has_scales = False
    
    def move(self):
        print(f"{self.name} moves in a strange way")

class Duck(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.type = "duck"
        self.has_feathers = True
    
    def move(self):
        print(f"{self.name} is swimming down the river")

class Snake(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.type = "snake"
        self.has_scales = True
    
    def move(self):
        print(f"{self.name} is slithering on the ground")   
        
class Squid(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.type = "squid"