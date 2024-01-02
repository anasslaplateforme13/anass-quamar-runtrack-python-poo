class Animal:
    def __init__(self):
        self._age = 0
        self._prenom = "Luna"

    @property
    def age(self):
        return self._age

    @property
    def prenom(self):
        return self._prenom

    def afficherAge(self):
        print(f"L'âge de l'animal est de {self.age} an(s).")

    def vieillir(self):
        self._age += 1

    def nommer(self, nom):
        if not isinstance(nom, str):
            raise ValueError("Le nom doit être une chaîne de caractères.")
        self._prenom = nom
        print(f"L'animal est nommé {self.prenom}.")

# Exemple d'utilisation :
monAnimal = Animal()
monAnimal.afficherAge()  # Affichera "L'âge de l'animal est de 0 an(s)."
monAnimal.vieillir()
monAnimal.afficherAge()  # Affichera "L'âge de l'animal est de 1 an(s)."

try:
    monAnimal.nommer("Luna")
    print(monAnimal.prenom)  # Affichera "Médor"
    monAnimal.nommer(123)  # Déclenchera une ValueError
except ValueError as e:
    print(e)
