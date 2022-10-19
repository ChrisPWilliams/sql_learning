from animals_sqlite_orm import AnimalORM
import animals as anm

"""
This is intended to be a demo of the capabilities of the ORM, see the 
animals_sqlite_orm and animals py files for a full list of methods
"""

my_orm = AnimalORM("test.db")

current_animals = my_orm.get_animals()

if current_animals:
    for animal in current_animals:
        print(f"Say hi to {animal.name}, who is a {animal.type}!")
        animal.move()

bob = anm.Duck("bob")

alice = anm.Snake("alice")

new_animals = [alice, bob]

for animal in new_animals:
    my_orm.add(animal)