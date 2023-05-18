from Persona import Persona

class retirar:
     def retirar(self, persona, ret):
        if  0 >= int(ret):
            print("")
        elif int(ret) > int(persona.getSaldo()):
            print("")
        elif int(persona.getRetiroTotal())+int(ret) > 3000:
            print("")
        else:
            persona.setSaldo(int(persona.getSaldo())-int(ret))
            persona.setRetiroTotal(int(persona.getRetiroTotal())+int(ret))