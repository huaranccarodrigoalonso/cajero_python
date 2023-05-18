import unittest
from Persona import Persona
from deposito import depositar
from retirar import retirar
from datetime import datetime

class Test_atm(unittest.TestCase):

    #testearemos primero que los métodos de Persona funcionen como debería
    def test_persona(self):
        current = Persona("juan", "123", 0, 0, 100, "2023-05-18")
        self.assertEqual(current.getName(), "juan")
        self.assertEqual(current.getPassword(), "123")
        self.assertEqual(current.getRetiroTotal(), 0)
        self.assertEqual(current.getSaldo(), 100)

    def test_deposito(self):
        persona = Persona("juan", "123", 0, 0, 100, "2023-05-18")
        #negativos
        depositar.depositar(self, persona, -1)
        self.assertTrue(persona.getSaldo(), 100)
        #cero o valor mínimo
        depositar.depositar(self, persona, 0)
        self.assertTrue(persona.getSaldo(), 100)
        #deposito normal
        depositar.depositar(self, persona, 10)
        self.assertTrue(persona.getSaldo(), 110)
        self.assertTrue(persona.getDepositoTotal(), 10)
        self.assertEqual(persona.getRetiroTotal(), 0)
        #deposito excesivo
        depositar.depositar(self, persona, 3001)
        self.assertTrue(persona.getSaldo(), 100)
        self.assertEqual(persona.getDepositoTotal(), 10)
        self.assertEqual(persona.getRetiroTotal(), 0)

    def test_retiro(self):
        persona = Persona("juan", "123", 0, 0, 100, "2023-05-18")
        #negativos
        retirar.retirar(self, persona, -1)
        self.assertTrue(persona.getSaldo(), 100)
        #cero o valor mínimo
        retirar.retirar(self, persona, 0)
        self.assertTrue(persona.getSaldo(), 100)
        #retiro normal
        retirar.retirar(self, persona, 10)
        self.assertTrue(persona.getSaldo(), 90)
        self.assertEqual(persona.getDepositoTotal(), 0)
        self.assertEqual(persona.getRetiroTotal(), 10)
        #retiro excesivo al día
        retirar.retirar(self, persona, 3001)
        self.assertTrue(persona.getSaldo(), 100)
        self.assertEqual(persona.getDepositoTotal(), 0)
        self.assertEqual(persona.getRetiroTotal(), 10)
        #retiro más del saldo 
        retirar.retirar(self, persona, 101)
        self.assertTrue(persona.getSaldo(), 100)
        self.assertEqual(persona.getDepositoTotal(), 0)
        self.assertEqual(persona.getRetiroTotal(), 10)

    def test_ver(self):
        #debido a que solo es mirar los registros, sera combinado
        persona = Persona("juan", "123", 0, 0, 100, "2023-05-18")
        retirar.retirar(self, persona, 10)
        depositar.depositar(self, persona, 11)
        self.assertTrue(persona.getSaldo(), 101)
        self.assertEqual(persona.getDepositoTotal(), 11)
        self.assertEqual(persona.getRetiroTotal(), 10)

        #excediendo la suma deposito
        retirar.retirar(self, persona, 10)
        depositar.depositar(self, persona, 2990)
        self.assertTrue(persona.getSaldo(), 91)
        self.assertEqual(persona.getDepositoTotal(), 11)
        self.assertEqual(persona.getRetiroTotal(), 20)

        #excediendo el saldo de retiro
        retirar.retirar(self, persona, 92)
        depositar.depositar(self, persona, 2900)
        self.assertTrue(persona.getSaldo(), 2991)
        self.assertEqual(persona.getDepositoTotal(), 2911)
        self.assertEqual(persona.getRetiroTotal(), 20)

        #excediendo la suma retiro
        persona.setDepositoTotal(0)
        depositar.depositar(self, persona, 10) #3001
        retirar.retirar(self, persona, 3000)
        self.assertTrue(persona.getSaldo(), 3001)
        self.assertEqual(persona.getDepositoTotal(), 10)
        self.assertEqual(persona.getRetiroTotal(), 20)

unittest.main()