class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def afficherLesPoints(self):
        print(f"Coordonnées du point : ({self.x}, {self.y})")

    def afficherX(self):
        print(f"Coordonnée horizontale (x) : {self.x}")

    def afficherY(self):
        print(f"Coordonnée verticale (y) : {self.y}")

    def changerX(self, nouvelle_valeur_x):
        self._x = nouvelle_valeur_x

    def changerY(self, nouvelle_valeur_y):
        self._y = nouvelle_valeur_y

# Exemple d'utilisation :
point = Point(3, 5)
point.afficherLesPoints()  # Affichera "Coordonnées du point : (3, 5)"
point.afficherX()  # Affichera "Coordonnée horizontale (x) : 3"
point.afficherY()  # Affichera "Coordonnée verticale (y) : 5"

point.changerX(8)
point.changerY(10)

point.afficherLesPoints()  # Affichera "Coordonnées du point : (8, 10)"
