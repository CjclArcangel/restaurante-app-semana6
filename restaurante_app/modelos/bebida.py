"""
Módulo que define la clase Bebida, hija de Producto.

Representa una bebida disponible en Burger Cedeño, añadiendo atributos
propios que no aplican a un producto genérico ni a un platillo.
"""

from modelos.producto import Producto


class Bebida(Producto):
    """
    Clase hija que representa una bebida de Burger Cedeño.

    Hereda de Producto los atributos comunes (nombre, precio,
    disponibilidad) y agrega tres atributos específicos de la bebida:
    volumen en mililitros, tamaño del vaso y tipo de bebida.
    """

    def __init__(self, nombre, precio, volumen_ml, tamano, tipo_bebida, disponible=True):
        """
        Inicializa una bebida reutilizando el constructor de la clase
        padre mediante super() y añadiendo los atributos propios de la
        bebida.

        Args:
            nombre (str): Nombre de la bebida.
            precio (float): Precio de la bebida.
            volumen_ml (int): Volumen de la bebida, en mililitros.
            tamano (str): Tamaño del vaso (ej. Pequeño, Mediano, Grande).
            tipo_bebida (str): Categoría de la bebida (ej. Gaseosa, Malteada, Natural).
            disponible (bool): Disponibilidad de la bebida.
        """
        super().__init__(nombre, precio, disponible)
        self.volumen_ml = volumen_ml
        self.tamano = tamano
        self.tipo_bebida = tipo_bebida

    def mostrar_informacion(self):
        """
        Sobrescribe el método de la clase padre para mostrar información
        específica de una bebida (demostración de polimorfismo).
        """
        estado = "Disponible" if self.disponible else "No disponible"
        print(
            f"Bebida: {self.nombre} | Volumen: {self.volumen_ml} ml | "
            f"Tamaño: {self.tamano} | Tipo: {self.tipo_bebida} | "
            f"Precio: ${self.obtener_precio():.2f} | Estado: {estado}"
        )
