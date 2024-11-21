print("Fco.Santiago.Cor.Car")
print(" ")

class cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad

    def obtener_titular(self):
        return self.titular

    def establecer_titular(self, titular):
        self.titular = titular

    def obtener_cantidad(self):
        return self.cantidad

    def establecer_cantidad(self, cantidad):
        self.cantidad = cantidad

    def mostrar(self):
        print(f"Titular: {self.titular}, Cantidad: {self.cantidad}")

class cuenta_joven(cuenta):
    def __init__(self, titular, cantidad, bonificacion):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    def obtener_bonificacion(self):
        return self.bonificacion

    def establecer_bonificacion(self, bonificacion):
        self.bonificacion = bonificacion

    def es_titular_valido(self):
        if 18 <= self.titular['edad'] < 25:
            return True
        return False

    def mostrar(self):
        print(f"Cuenta Joven: Bonificacion: {self.bonificacion}%")
        
    def retirar_dinero(self, cantidad_retirar):
        if self.es_titular_valido():
            if self.obtener_cantidad() >= cantidad_retirar:
                self.establecer_cantidad(self.obtener_cantidad() - cantidad_retirar)
                print(f"Retiro de {cantidad_retirar} exitoso")
            else:
                print("No hay suficiente cantidad para retirar")
        else:
            print("Titular no valido para retiro")

# Ejemplo de uso
titular = {'nombre': 'Juan', 'edad': 22}
cuenta_juan = cuenta_joven(titular, 5000, 2)

cuenta_juan.mostrar()
cuenta_juan.retirar_dinero(1000)
cuenta_juan.mostrar()
