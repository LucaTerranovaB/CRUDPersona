from person import Person

class Repositorio:
    def __init__ (self):
        self.human = dict()

    def agregar(self, person: Person()):
        if person.idd in self.human:
            pass
        else:    
            self.human[person.idd] = person

    def borrar(self, idd: int):
        if idd not in self.human:
            pass
        else:
            del self.human[idd]


    def actualizar(self,idd: int, nuevaPersona: Person, ):
        if idd not in self.human:
            pass
        self.human[idd] = nuevaPersona
        return self.human[idd]

    
    def buscarLast(self):
        list(self.human.values())[-1]

    def buscarDni(self, idd: int):
        if idd not in self.human:
            pass
        return self.human[idd]


    def buscarAll(self):
        return list(self.human.values())
    
   

    def escribirArchivo(self):
        with open ('persona.txt', 'w') as file:
            for person in self.human.values():
                file.write(f'{person.idd}, {person.nombre}, {person.apellido}, {person.mail};\n')

    def leerrchivo(self):
        with open('persona.txt', 'r') as file:
            for line in file:
                print(line)

if __name__ == '__main__':
    repository = Repositorio()
    print(repository)