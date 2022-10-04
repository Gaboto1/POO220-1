class UnaClase: 
    atributo= 123
    atributo2= 246
objeto1= UnaClase()
objeto2= UnaClase()
objeto1.atributo= 999
objeto2.atributo= 888
class Persona:
    edad=""
    nombre= ""
    def mostrarnombre(self):
        print("El nombre es: "+self.nombre)
    def setEdad(self,edad):
        self.edad= edad
    def getedad(self):
        return(self.edad)
    def mostradatos(self):
        print("la persona se llama "+str(self.nombre)+" y tiene "+str(self.edad)+" años")
    def __init__(self,nombre="",edad=0):
        self.nombre = nombre
        self.edad = 0
    
    
    
persona1 = Persona()
persona1.nombre= "Benjamin"
persona2 = Persona()
persona2.nombre= "Miguel"
print("existen 2 personas: "+persona1.nombre+" y "+persona2.nombre)
print("La edad de la persona 1 es: "+str(persona1.edad))
print("La edad de la persona 2 es: "+str(persona2.edad))


persona1.mostrarnombre()
persona2.mostrarnombre()
persona1.mostradatos()
persona2.mostradatos()