class Person:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def work(self):
        return f"{self.nombre} esta trabajando duro"    
    
    
person1 = Person(nombre='Gabriel',edad=25)
print(person1.work())