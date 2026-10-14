class Person:
    
    especies = "Humano"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @classmethod   
    def nueva_especie(cls, nuevaEspecie):
        cls.especies = nuevaEspecie
        
            
    @staticmethod
    def is_older(age):
         return age > 18   
        
person1 = Person("Gabiel",25)

person2 = Person("Alex",25)
                
person1.nueva_especie("Reptiliano")
print(person1.especies)

Person.nueva_especie("Hominidos")
print(person1.especies)