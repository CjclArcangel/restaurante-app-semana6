"""
Módulo que define la clase Platillo, hija de Producto.

Representa una comida preparada que se ofrece en Burger Cedeño, añadiendo
atributos propios que no aplican a un producto genérico ni a una bebida.
"""

from modelos.producto import Producto


class Platillo(Producto):
    """
    Clase hija que representa un platillo de Burger Cedeño.

    Hereda de Producto los atributos comunes (nombre, precio,
    disponibilidad) y agrega tres atributos específicos del platillo:
    tipo de platillo, tiempo de preparación y calorías aproximadas.
    """

    def __init__(self, nombre, precio, tipo_platillo, tiempo_preparacion_minutos, calorias, disponible=True):
        """
        Inicializa un platillo reutilizando el constructor de la clase
        padre mediante super() y añadiendo los atributos propios del
        platillo.

        Args:
            nombre (str): Nombre del platillo.
            precio (float): Precio del platillo.
            tipo_platillo (str): Categoría del platillo (ej. plato fuerte, acompañante).
            tiempo_preparacion_minutos (int): Tiempo estimado de preparación, en minutos.
            calorias (int): Cantidad aproximada de calorías del platillo.
            disponible (bool): Disponibilidad del platillo.
        """
        super().__init__(nombre, precio, disponible)
        self.tipo_platillo = tipo_platillo
        self.tiempo_preparacion_minutos = tiempo_preparacion_minutos
        self.calorias = calorias

    def mostrar_informacion(self):
        """
        Sobrescribe el método de la clase padre para mostrar información
        específica de un platillo (demostración de polimorfismo).
        """
        estado = "Disponible" if self.disponible else "No disponible"
        print(
            f"Platillo: {self.nombre} | Tipo: {self.tipo_platillo} | "
            f"Tiempo de preparación: {self.tiempo_preparacion_minutos} min | "
            f"Calorías: {self.calorias} kcal | "
            f"Precio: ${self.obtener_precio():.2f} | Estado: {estado}"
        )
