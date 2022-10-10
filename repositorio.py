from person import Person

class Repositorio:
    def __init__ (self):
        self.human = dict()

    def agregar(self, person: Person()):
        if person.dni in self.human:
            raise Exception("Inexistente")
        else:    
            self.human[person.dni] = person

    def borrar(self, dni: int):
        if dni not in self.human:
            raise Exception("Inexistente")
        else:
            del self.human[dni]


    def actualizar(self,dni: int, nuevaPersona: Person, ):
        if dni not in self.human:
            raise Exception("Inexistente")
        self.human[dni] = nuevaPersona
        return self.human[dni]

    
    def buscarLast(self):
        list(self.human.values())[-1]

    def buscarDni(self, dni: int):
        if dni not in self.human:
            raise Exception("Inexistente")
        return self.human[dni]


    def buscarAll(self):
        return list(self.human.values())
    
   

    def escribirArchivo(self):
        with open ('persona.txt', 'w') as file:
            for person in self.human.values():
                file.write(f'{person.dni}, {person.nombre}, {person.apellido}, {person.mail};\n')

    def leerrchivo(self):
        with open('persona.txt', 'r') as file:
            for line in file:
                print(line)

if __name__ == '__main__':
    repository = Repositorio()
    print(repository)