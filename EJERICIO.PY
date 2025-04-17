## PO CON HERENCIAS
#clase padre o base
class vehiculo:
    def __init__(self,marca):
        self.marca=marca
    def describir(self):
        print(f"este vehiculos es de marca{self.marca}.")
class coche(vehiculo):
        #clase hija(heredada de vehiculo)
    def __init__(self,marca,modelo):
        # llama al constructor de la clase base (vehiculo)
        super().__init__(marca)
        self.modelo=modelo  # atributo especifico de coche
    def describir(self):
        # sobre escribir el metodo escribir para coche
        print(f"este coche es un {self.modelo} de la marca {self.marca}")
        # crear un objeto de la clase coche
mi_coche=coche("toyota","corolla")
mi_coche.describir()

# CREAR UN ALGORITMO POO DONDE INGRESE  NOMBRE DEL PACIENTE, EDAD, SEXO Y MUESTRE, (NOMBRE, EDAD)  Y HEREDE ESTOS VALORES Y  INCLUYAN LA ENFERMEDAD BASE 

class paciente:
    def __init__(self,nombre,edad,sexo):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
    def describir(self):
        print(f"Mi nombre es: {self.nombre} mi edad es: {self.edad} y mi sexo es: {self.sexo}")
class enfermedad_base(paciente):
    def __init__(self, nombre, edad, sexo, enfermedad):
        super().__init__(nombre, edad, sexo)
        self.enfermedad=enfermedad
    def describir(self):
        print(f"Mi nombre es: {self.nombre} mi edad es: {self.edad} y mi sexo es: {self.sexo} y mi enfermedad es: {self.enfermedad}")
paciente1=enfermedad_base("DANIEL", 23, "MASCULINO", "GASTRITIS")
paciente2=enfermedad_base("LAURA", 24, "FEMENINO", "NEUMONIA")
paciente1.describir()
paciente2.describir()       