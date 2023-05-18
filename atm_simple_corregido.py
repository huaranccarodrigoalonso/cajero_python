"""
Created on Mon May 15 16:05:23 2023

@author: Huarancca Leon Rodrigo
"""

from os import system
from Persona import Persona
from datetime import datetime
import getpass
class Cajero:

    MAX_DEP = 3000
    MIN_DEP = 0
    MAX_RET = 3000
    MIN_RET = 1
    prendido = True
    logueado = False

    def __init__(self):        
        while(self.prendido):
            self.menuPrincipal()

    def menuPrincipal(self):
        opcion = "0"

        print("""Bienvenido al cajero
        ***Menú principal
        1 - Ingresar
        2 - Apagar
        """)

        opcion = input("Su opción es: ")

        if opcion == "1":
            aux_persona = self.loguearse()
        elif opcion == "2":
            self.prendido = False
        else:
            print("Opción inválida")

        if self.logueado:

            opcion = 0

            while not opcion == 4: 
                system("clear")
                print(""" Bienvenido al cajero automatico
                ******Menú******
                1 - Depositar
                2 - Retirar
                3 - Ver saldo
                4 - Cerrar sesión """)
                opcion = input("Su opción es: ")

                if opcion == "1" :
                    self.depositar(aux_persona)

                elif opcion == "2" :
                    self.retirar(aux_persona)

                elif opcion == "3":
                    self.ver(aux_persona)

                elif opcion == "4":
                    self.logueado = False
                    self.guardar(aux_persona)
                    print("Sesion cerrada ")
                    break

                else:
                    print("NO existe esa opción")



    def loguearse(self):
        intentos = 1

        aux_name = input("Ingrese su nombre o usuario: ")

        datos = open("usuarios.txt", "r")
        linea = ""

        while True:
            linea = datos.readline()
            if linea:
                datos_persona = linea.split(" ")
                aux_persona = Persona(datos_persona[0], datos_persona[1], datos_persona[2], datos_persona[3], datos_persona[4], datos_persona[5])

                if aux_name == aux_persona.getName():

                    while intentos <= 3:
                        aux_password = getpass.getpass("Ingrese contraseña: ")
                        if aux_password == aux_persona.getPassword():
                            if aux_persona.getDia() != datetime.now().date():
                                aux_persona.setDia(datetime.now().date())
                                aux_persona.setDepositoTotal(0)
                                aux_persona.setRetiroTotal(0)
                            self.logueado = True
                            datos.close()
                            return aux_persona
                        else:
                            print(f"Contraseña Incorrecta, le quedan {3 - intentos} intentos")
                            intentos += 1
            else:
                break
            
        if self.logueado != True:
            print("No se encontró el usuario\n")

    def depositar(self, persona, dep):
        dep = input("Ingrese el monto a depositar: ")
        if  self.MIN_DEP >= int(dep):
            print("Ingrese depositos mayores a los mínimos ")
        elif int(persona.getDepositoTotal())+int(dep) > self.MAX_DEP:
            print("Usted excede la cantidad máxima de deposito por día")
        else:
            persona.setSaldo(str(int(persona.getSaldo())+int(dep)))
            persona.setDepositoTotal(int(persona.getDepositoTotal())+int(dep))
            print("Su nuevo saldo es "+persona.getSaldo())
        input("Presione ENTER para continuar")

    def retirar(self, persona):
        ret = input("Ingrese el monto a retirar: ")
        if  self.MIN_RET >= int(ret):
            print("Ingrese retiros mínimos válidos ")
        elif int(ret) > int(persona.getSaldo()):
            print("Usted no puede retirar más del saldo disponible")
        elif int(persona.getRetiroTotal())+int(ret) > self.MAX_RET:
            print("Usted excede la cantidad máxima de retiro por día")
        else:
            persona.setSaldo(int(persona.getSaldo())-int(ret))
            persona.setRetiroTotal(int(persona.getRetiroTotal())+int(ret))
            print(f"Su nuevo saldo es {persona.getSaldo()}")   
        input("Presione ENTER para continuar")


    def ver(self, persona):
        print(f"Su saldo es: {persona.getSaldo()}")
        print(f"Hoy puede depositar hasta: {self.MAX_DEP-int(persona.getDepositoTotal())}")
        print(f"Hoy puede retirar hasta: {self.MAX_RET-int(persona.getRetiroTotal())}")
        input("Presione ENTER para continuar")
        
    def guardar(self, persona):

        datos = open("usuarios.txt", "r")
        datos_persona = []

        for linea in datos:
            datos_persona.append(linea)
        #buscar manera de abrir los archivos sin borrarlos
        datos.close()

        datos = open("usuarios.txt", "w")

        for linea in datos_persona:
            i = linea.split(" ")
            if (i[0] == persona.getName()):
                datos.write(str(persona.getName())+" "+str(persona.getPassword())+" "+str(persona.getDepositoTotal())+" "+str(persona.getRetiroTotal())+" "+str(persona.getSaldo())+" "+str(persona.getDia())+"\n")
            else:
                datos.write(" ".join(i))
        datos_persona.clear() #limpiando para evitar malos usos
        datos.close()

app = Cajero()