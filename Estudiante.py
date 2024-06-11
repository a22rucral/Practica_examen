"""
Clase Estudiante base para el Examen Convocatoria Ordinaria de la UD4
:author: Jaime Rabasco
Refactorización
Extrae una superclase con los campos
	nombre
	apellidos
	nif
"""


class Persona:
    def __init__(self, dni, nombre, apellidos):
        """
        Inicializa un objeto en la clase persona
        :param dni:
        :param nombre:
        :param apellidos:
        """
        self.__nif = dni
        self.__nombre = nombre
        self.__apellidos = apellidos


class Estudiante(Persona):
    nif = "11111111Z"
    curso = "Primaria"
    nombre = "Nombre"
    apellidos = "Apellidos"

    def __init__(self, nif, curso, nombre, apellidos, dni):
        """
        Inicializa un objeto en la clase estudiante
        :param nif:
        :param curso:
        :param nombre:
        :param apellidos:
        """
        super().__init__(dni, nombre, apellidos)
        self.nif = nif
        self.curso = curso
        self.nombre = nombre
        self.apellidos = apellidos

    @property
    def nif(self):
        """

        :return: el dni de la persona
        """
        return self.__nif

    @nif.setter
    def nif(self, value):
        """

        :param value: adjudica el valor al dni
        """
        self.__nif = value

    @property
    def curso(self):
        """

        :return: el curso en el que se encuentra
        """
        return self.__curso

    @curso.setter
    def curso(self, value):
        """

        :param value: asigna el valor al curso
        """
        self.__curso = value

    @property
    def nombre(self):
        """

        :return: el nombre de la persona
        """
        return self.__nombre

    @nombre.setter
    def nombre(self, value: int):
        """

        :param value: asigna un valor al nombre
        """
        self.__nombre = value

    @property
    def apellidos(self):
        """

        :return: los apellidos
        """
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, value):
        """

        :param value: asiga el valor al apellido
        """
        self.__apellidos = value
