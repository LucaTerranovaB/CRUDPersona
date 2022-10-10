
import unittest
from person import Person
from repositorio import Repositorio
from service import Service

class TestPersonaService(unittest.TestCase):
    #Test comprobacion creacion del objeto
    def testPerson(self):
        person = Person(123, 'Abel', 'Carrizo', 'acarrizo@email.com')
        self.assertEqual(person.dni, 123)

    #Test repositorio inicial
    def testRepositorio(self):
        repository = Repositorio()
        self.assertEqual(len(repository.human), 0)

    #Test Servicio
    #Añadir un valor al repositorio
    def testService(self):
        service = Service()
        persona = Person(123, 'Abel', 'Carrizo', 'acarrizo@email.com')
        service.agregar(persona)
        self.assertEqual(len(service.repository.human), 1)

    #Añadir mas de un valor al repositorio
    def testService2Añadir(self):
        service = Service()
        persona1 = Person(123, 'Rodrigo', 'Matamala', 'rodrigoM@gmail.com')
        service.agregar(persona1)

        persona2 = Person(345, 'Silvestre', 'Peña', 'silverpyl@gmail.com')
        service.agregar(persona2)
        

        self.assertEqual(len(service.repository.human), 2)

     #Actualizar un valor
    def testServiceactuallizar(self):
        service = Service()
        persona1 = Person(123, 'Abel', 'Carrizo', 'acarrizo@email.com')
        service.agregar(persona1)

        persona2 = Person(123, 'Juan', 'Gomez', 'jgomez@email.com')
        service.update(persona2, 123)

        self.assertNotEqual(service.repository.human, persona2)

    #Borrar un valor
    def testService5(self):
        service = Service()
        person1 = Person(123, 'Abel', 'Carrizo', 'acarrizo@email.com')
        service.agregar(person1)

        service.borrar(123)
        self.assertEqual(len(service.repository.people), 0)

    #Ver todo
    def testServicebuscarYVer(self):
        service = Service()
        persona1 = Person(123, 'Abel', 'Carrizo', 'acarrizo@email.com')
        service.agregar(persona1)
        
        self.assertEqual(len(service.buscarAll()), 1)


if __name__=='__main__':
    unittest.main()