class Operation:
    def __init__(self, nombre1=5, nombre2=10):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def __str__(self):
        return f"Nombre1: {self.nombre1}, Nombre2: {self.nombre2}"

# Instanciation de la classe Operation
operation_instance = Operation()

# Impression des valeurs des attributs nombre1 et nombre2 en utilisant __str__
print(operation_instance)

# Vous pouvez également utiliser str() pour obtenir la représentation sous forme de chaîne
print(str(operation_instance))


