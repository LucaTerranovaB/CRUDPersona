
import unittest
from person import Person
from repositorio import Repositorio
from service import Service

class TestPersonaService(unittest.TestCase):
   
    def testPerson(self):
        person = Person(39952739, 'Luca', 'Terranova', 'l.terranova')
        self.assertEqual(person.dni, 39952739)

  
    def testRepositorio(self):
        repository = Repositorio()
        self.assertEqual(len(repository.human), 0)

    
    def testService(self):
        service = Service()
        persona = Person(39952739, 'Luca', 'Terranova', 'l.terranova@alumno.um.edu.ar')
        service.agregar(persona)
        self.assertEqual(len(service.repository.human), 1)

    #Añadir mas de un valor al repositorio
    def testService2Añadir(self):
        service = Service()
        persona1 = Person(39952739, 'Rodrigo', 'Matamala', 'rodrigoM@gmail.com')
        service.agregar(persona1)

        persona2 = Person(39952740, 'Silvestre', 'Peña', 'silverpyl@gmail.com')
        service.agregar(persona2)
        

        self.assertEqual(len(service.repository.human), 2)

     #Actualizar un valor
    def testServiceActualizar(self):
        service = Service()
        persona1 = Person(39952739, 'Luca', 'Terranova', 'l.terranova@alumno.um.edu.ar')
        service.actualizar(persona1, 39952739)

        persona2 = Person(39952739, 'Juan', 'Gomez', 'jgomez@email.com')
        service.actualizar(persona2, 39952739)

        self.assertNotEqual(service.repository.human, persona2, 2)

    
    def testService(self):
        service = Service()
        person1 = Person(39952739, 'Luca', 'Terranova', 'l.terranova@alumno.um.edu.ar')
        service.agregar(person1)

        service.borrar(39952739)
        self.assertEqual(len(service.repository.human), 0)

   
    def testServicebuscarYVer(self):
        service = Service()
        persona1 = Person(39952739, 'Luca', 'Terranova', 'l.terranova@alumno.um.edu.ar')
        service.agregar(persona1)
        
        self.assertEqual(len(service.buscarAll()), 1)


if __name__=='__main__':
    unittest.main()