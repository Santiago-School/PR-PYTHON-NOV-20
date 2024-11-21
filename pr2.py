print("Fco.Santiago.Cor.Car")
print(" ")

# clase cuenta que almacena una cuenta bancaria
class cuenta:
    # constructor de la clase
    def __init__(self, titular, cantidad = 0.0):
        # el titular es obligatorio, cantidad opcional
        self.titular = titular
        self.cantidad = cantidad

    # setter para la cantidad
    def set_cantidad(self, cantidad):
        if cantidad >= 0:  # solo aceptar cantidades positivas
            self.cantidad = cantidad

    # getter para la cantidad
    def get_cantidad(self):
        return self.cantidad

    # metodo para mostrar los datos de la cuenta
    def mostrar(self):
        print(f"Titular: {self.titular}, Cantidad: {self.cantidad}")

    # metodo para ingresar dinero en la cuenta
    def ingresar(self, cantidad):
        if cantidad > 0:  # solo se puede ingresar dinero positivo
            self.cantidad += cantidad

    # metodo para retirar dinero de la cuenta
    def retirar(self, cantidad):
        if cantidad > 0:  # solo se puede retirar dinero positivo
            self.cantidad -= cantidad

# Crear una cuenta con titular "Juan Lom" y cantidad inicial 1000
cuenta1 = cuenta("Juan Lom", 1000)

# Mostrar la información de la cuenta
cuenta1.mostrar()

# Ingresar dinero a la cuenta
cuenta1.ingresar(500)
print("Despues de ingresar 500:")
cuenta1.mostrar()

# Retirar dinero de la cuenta
cuenta1.retirar(200)
print("Despues de retirar 200:")
cuenta1.mostrar()
