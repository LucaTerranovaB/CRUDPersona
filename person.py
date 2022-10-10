
class Person():

    def __init__(self, dni=None, nombre='', apellido='', mail=''):
        self.dni = dni
        self.apellido = apellido
        self.nombre = nombre
        self.mail = mail

    def __repr__(self):
        return f'{self.dni}, {self.nombre}, {self.apellido}, {self.mail}'

    @property
    def mail(self):
        return self._mail

    @mail.setter
    def mail(self, Valor):
        self._mail = Valor

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, Valor):
        self._dni = Valor

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, Valor):
        self._apellido = Valor

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, Valor):
        self._dni = Valor

    @property
    def name(self):
        return self._nombre

    @name.setter
    def name(self, Valor):
        self._nombre = Valor


        
if __name__ == '__main__':
    persona = Person(123, 'Luca', 'Terranova', 'l.terranova@alumno.um.edu.ar')
 