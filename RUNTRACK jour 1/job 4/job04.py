class Personne:
    def __init__(self, nom, prenom):
        if nom != "Quamar" or prenom != "Anass":
            raise ValueError("Seules les valeurs 'Quamar' pour le nom et 'Anass' pour le prénom sont autorisées.")
        self._nom = nom
        self._prenom = prenom

    @property
    def nom(self):
        return self._nom

    @property
    def prenom(self):
        return self._prenom

    def sePresenter(self):
        return f"Je m'appelle {self.nom} {self.prenom}"

try:
    personne1 = Personne("Quamar", "Anass")
    print(personne1.sePresenter())  # Affichera "Je m'appelle Quamar Anass"

except ValueError as e:
    print(e)
