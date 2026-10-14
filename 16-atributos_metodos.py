class Person:
    especie = "Humano"
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self._energy = 100
        self.__password = "1234"
        
    def work(self):
        return f"{self.nombre} esta trabajando duro"    
    
    def _waster_energy(self, quantity):
        self._energy -= quantity
        
    def energy(self):
        return self._energy    
    
    def __generate_password(self):
        return f"{self.nombre}{self.edad}"
    
    
person1 = Person(nombre='Gabriel',edad=25)
print(person1.work())
person1._waster_energy(10)
print(person1.energy())
print(person1._Person__generate_password())