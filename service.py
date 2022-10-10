
from repositorio import Repositorio
from person import Person

class Service:
    def __init__(self) -> None:
        self.repository = Repositorio()

    def agregar(self, person: Person):
        try:
            return self.repository.agregar(person)
        except Exception as e:
            print(e)

    def borrar(self, dni: int):
        try:
            person = self.repository.buscarDni(dni)
            self.repository.delete(person.dni)
            return person
        except Exception as e:
            print(e)

    def actualizar(self, nuevaPersona: Person, dni):
        try:
            return self.repository.actualizar(nuevaPersona, dni)
        except Exception as e:
            print(e)

    def buscarDni(self):
        try:
            return self.repository.buscarDni()
        except KeyError as e:
            print(e)

    
    def buscarAll(self):
        return self.repository.buscarAll()
    
    def BuscarLast(self):
        return self.repository.buscarLast()


    
if __name__ == '__main__':
    pass