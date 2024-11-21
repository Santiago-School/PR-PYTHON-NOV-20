

print("Fco.Santiago.Car.Cor  0421")
print(" ")
# definimos la clase cuentajoven que hereda de cuenta
class cuentajoven(cuenta): # type: ignore
    # constructor con bonificacion adicional
    def __init__(self, titular, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    # obtener y dar para bonificacion
    def setbonificacion(self, bonificacion):
        if isinstance(bonificacion, (int, float)) and bonificacion >= 0:
            self.bonificacion = bonificacion

    def getbonificacion(self):
        return self.bonificacion

    # verificar si el titular es valido
    def es_titular_valido(self):
        return self.titular.es_mayor_de_edad() and self.titular.get_edad() < 25

    # retirar dinero solo si el titular es valido
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)

    # mostrar informacion de cuenta joven
    def mostrar(self):
        return f"cuenta joven, bonificacion: {self.bonificacion}%"
