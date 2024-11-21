print("Fco.Santiago.Cor.Car")
print(" ")

# Clase persona que almacena datos de una persona
class persona:
    # Constructor de la clase
    def __init__(self, nombre = "Santiago", edad = 16, dni = "nosequeesprofe"):
        # Inicializamos los atributos de la persona
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    # Setter para el nombre
    def set_nombre(self, nombre):
        if isinstance(nombre, str) and len(nombre) > 0:  # Validar que el nombre no esté vacío
            self.nombre = nombre

    # Getter para el nombre
    def get_nombre(self):
        return self.nombre

    # Setter para la edad
    def set_edad(self, edad):
        if isinstance(edad, int) and edad >= 0:  # Validar que la edad sea un número positivo
            self.edad = edad

    # Getter para la edad
    def get_edad(self):
        return self.edad

    # Setter para el dni
    def set_dni(self, dni):
        if isinstance(dni, str) and len(dni) > 0:  # Validar que el dni no esté vacío
            self.dni = dni

    # Getter para el dni
    def get_dni(self):
        return self.dni

    # Método para mostrar los datos de la persona
    def mostrar(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}")

    # Método que valida si la persona es mayor de edad
    def mayordeedad(self):
        if self.edad >= 18:
            return True
        return False

# Crear una instancia de la clase persona
persona1 = persona("Canelitas", 21, "Canelitas123")  # Puedes cambiar los valores por los que quieras

# Mostrar los datos de la persona
persona1.mostrar()

# Verificar si la persona es mayor de edad
if persona1.mayordeedad():
    print(f"{persona1.get_nombre()} es mayor de edad")
else:
    print(f"{persona1.get_nombre()} no es mayor de edad")
