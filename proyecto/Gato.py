"""
Clase Gato.
:author: Jaime Rabasco Ronda.
"""
class Gato:
    def maullar(self):
        """
        FUnción que imprime el maullar de un gato
        """
        self.maulla = 'Miau'
        print(self.maulla)

g = Gato()
g.maullar()
