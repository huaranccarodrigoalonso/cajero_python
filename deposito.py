from Persona import Persona

class depositar:
    def depositar(self, persona, dep):
        #dep = input("Ingrese el monto a depositar: ")
        if  0 >= int(dep):
            print("")
        elif int(persona.getDepositoTotal())+int(dep) > 3000:
            print("")
        else:
            persona.setSaldo(str(int(persona.getSaldo())+int(dep)))
            persona.setDepositoTotal(int(persona.getDepositoTotal())+int(dep))