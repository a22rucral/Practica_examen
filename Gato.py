"""
Clase Gato.
:author: Jaime Rabasco Ronda.
"""
class Gato:

    def __init__(self):
        """
        Inicializa un objeto de la clase gato
        """
        self.maulla = 'Miau'

    def maullar(self):
        """
        FUnción que imprime el maullar de un gato
        """
        print(self.maulla)

g = Gato()
g.maullar()
