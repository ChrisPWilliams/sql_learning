import sqlite3
import animals

class AnimalORM:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()

        self.cur.execute("""CREATE TABLE IF NOT EXISTS animal_types(
                            type_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name VARCHAR(20) NOT NULL UNIQUE,
                            fur INTEGER,
                            feathers INTEGER,
                            scales INTEGER
                            );""")

        self.cur.execute("""CREATE TABLE IF NOT EXISTS animals(
                            animal_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name VARCHAR(20) NOT NULL,
                            type_id INTEGER NOT NULL,
                            FOREIGN KEY (type_id) REFERENCES animal_types(type_id)
                            );""")
        print(f"DB connection initialised at file {db_name}")

    def add(self, animal):
        self.cur.execute(f"""INSERT OR IGNORE INTO animal_types (name, fur, feathers, scales)
                            VALUES ('{animal.type}', {animal.has_fur}, {animal.has_feathers}, {animal.has_scales});""")
        self.cur.execute(f"""INSERT INTO animals (name, type_id) 
                            VALUES ('{animal.name}', (
                                SELECT type_id FROM animal_types WHERE (animal_types.name = '{animal.type}')
                                )
                            );""")
        print(f"Added animal {animal.name}")
    
    def get_animals(self):
        self.cur.execute(f"""SELECT animals.name, animal_types.name
                            FROM animal_types
                            INNER JOIN animals ON animal_types.type_id=animals.type_id;""")
        animals_list = []
        for animal_data in self.cur.fetchall():
            this_animal = 0
            if animal_data[1] == "duck":      # this pattern is bad but in practice we would probably not use subclasses like this
                this_animal = animals.Duck(animal_data[0])
            elif animal_data[1] == "snake":
                this_animal = animals.Snake(animal_data[0])
            elif animal_data[1] == "squid":
                this_animal = animals.Squid(animal_data[0])
            else:
                this_animal = animals.Animal(animal_data[0])
            animals_list.append(this_animal)
        return animals_list
    
    def delete(self, animal):
        self.cur.execute(f"""DELETE FROM animals
                            WHERE name = '{animal.name}';""")
        self.cur.execute(f"""DELETE FROM animal_types
                            WHERE NOT EXISTS(
                                SELECT animals.name FROM animals
                                INNER JOIN animal_types ON animals.type_id=animal_types.type_id
                                WHERE animal_types.name = '{animal.type}'
                            ) AND animal_types.name = '{animal.type}';""")
        print(f"Deleted animal {animal.name}")
    
    def __del__(self):
        self.conn.commit()
        self.conn.close()
    
    def test(self):
        self.cur.execute("SELECT * FROM animals")
        results = self.cur.fetchall()
        for i in results:
            print(i)
        self.cur.execute("SELECT * FROM animal_types")
        results = self.cur.fetchall()
        for i in results:
            print(i)