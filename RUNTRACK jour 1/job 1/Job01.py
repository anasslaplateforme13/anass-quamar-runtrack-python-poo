class Operation:
    def __init__(self, nombre1=5, nombre2=10):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        return self.nombre1 + self.nombre2

    def soustraction(self):
        return self.nombre1 - self.nombre2

    def multiplication(self):
        return self.nombre1 * self.nombre2

    def division(self):
        if self.nombre2 != 0:
            return self.nombre1 / self.nombre2
        else:
            return "Division par zéro impossible"

print
operation_instance = Operation()


print("Addition :", operation_instance.addition())
print("Soustraction :", operation_instance.soustraction())
print("Multiplication :", operation_instance.multiplication())
print("Division :", operation_instance.division())

