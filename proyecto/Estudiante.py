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
    def __init__(self, nombre, apellidos, nif):
        """
        Permite instanciar un objeto en la clase persona
        :param nombre:  indica el nombre de la persona
        :param apellidos: indica el apellido de la persona
        :param nif: indica el dni de la persona
        """
        self.__nif = nif
        self.__nombre = nombre
        self.__apellidos = apellidos


class Estudiante(Persona, Persona):
    nif = "11111111Z"
    curso = "Primaria"
    nombre = "Nombre"
    apellidos = "Apellidos"

    def __init__(self, nif, curso, nombre, apellidos, dni):
        """
        Permite instanciar un objeto en la clase estudiante
        :param nif: dni del estudiante
        :param curso: curso actual de estudiante
        :param nombre: nombre del estudiante
        :param apellidos: apellidos del estudiante
        :param dni:
        """
        super().__init__(dni, nombre, apellidos)
        self.nif = nif
        self.curso = curso
        self.nombre = nombre
        self.apellidos = apellidos

    @property
    def nif(self):
        """

        :return: self.__nif devuelve el nif del estudiante
        """
        return self.__nif

    @nif.setter
    def nif(self, value):
        """
        Establece el nif con el parametro value
        :param value:
        """
        self.__nif = value

    @property
    def curso(self):
        """

        :return: delvuelve el curso del estudiante
        """
        return self.__curso

    @curso.setter
    def curso(self, value):
        """
        Asigna el valor value a el curso
        :param value:
        """
        self.__curso = value

    @property
    def nombre(self):
        """

        :return: devuelve el nombre del estudiantes
        """
        return self.__nombre

    @nombre.setter
    def nombre(self, value: int):
        """
        Asigan el valor al nombre
        :param value:
        """
        self.__nombre = value

    @property
    def apellidos(self):
        """

        :return: los apellidos de los estudiantes
        """
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, value):
        """

        :param value: asigna a los apellidos el valor como parametro
        """
        self.__apellidos = value
