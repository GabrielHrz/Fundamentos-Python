class BankAccount:
    def __init__(self, owner, initial_balance):
        self.owner= owner
        self.__balance = initial_balance #Encapsulamiento 
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def withdraw(self, amount):
        if amount > 0 and amount < self.__balance:
            self.__balance -= amount
        else :
            print("Saldo insuficiente o monto invalido")                