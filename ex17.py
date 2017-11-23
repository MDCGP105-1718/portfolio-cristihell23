class Car(object):
    def __init__(self, wheels, doors, engine):
        self.wheels=wheels
        self.doors=doors
        self.engine=engine

    def __str__(self, wheels, doors, engine):
        return str (self.wheels, self.doors, self.engine)

    def change_engine(self, engine):
        self.engine = engine

panda_trueno = Car(4, 4, '4A-GEU 16v')

print(panda_trueno.wheels)

panda_trueno.change_engine("4A-GEU 20v")
print(panda_trueno.engine)
