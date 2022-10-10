
class Person():

    def __init__(self, idd=None, nombre='', apellido='', mail=''):
        self.idd = idd
        self.apellido = apellido
        self.nombre = nombre
        self.mail = mail

    def __repr__(self):
        return f'{self.idd}, {self.nombre}, {self.apellido}, {self.mail}'

    @property
    def mail(self):
        return self._mail

    @mail.setter
    def mail(self, Valor):
        self._mail = Valor

    @property
    def idd(self):
        return self._idd

    @idd.setter
    def idd(self, Valor):
        self._idd = Valor

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, Valor):
        self._apellido = Valor

    @property
    def idd(self):
        return self._idd

    @idd.setter
    def idd(self, Valor):
        self._idd = Valor

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, Valor):
        self._nombre = Valor


        
if __name__ == '__main__':
    persona = Person(999 , 'Luca', 'Terranova', 'l.terranova@alumno.um.edu.ar')
 