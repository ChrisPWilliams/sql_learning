from animals_sqlite_orm import AnimalORM
import animals as anm

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