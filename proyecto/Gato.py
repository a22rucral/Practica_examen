"""
Clase Gato.
:author: Jaime Rabasco Ronda.
"""

class Gato:
    def maullar(self):
        """
        Funcion que imprime el maullido del gato
        """
        self.maulla = 'Miau'
        print(self.maulla)

g = Gato()
g.maullar()
