"""
Punto de arranque del sistema restaurante_app de Burger Cedeño.

Crea instancias de Platillo y Bebida propias de una hamburguesería y
comida rápida, las registra en el servicio Restaurante y muestra la
información resultante en consola, demostrando herencia, encapsulación
y polimorfismo.
"""

from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante


def main():
    """Función principal que ejecuta el flujo del programa."""

    # Creamos el servicio principal del restaurante
    restaurante = Restaurante("Burger Cedeño")

    # Creación de objetos Platillo (clase hija de Producto)
    hamburguesa_doble = Platillo(
        nombre="Hamburguesa doble carne",
        precio=6.50,
        tipo_platillo="Plato fuerte",
        tiempo_preparacion_minutos=15,
        calorias=750
    )

    papas_con_queso = Platillo(
        nombre="Papas fritas con queso",
        precio=3.50,
        tipo_platillo="Acompañante",
        tiempo_preparacion_minutos=10,
        calorias=480
    )

    # Creación de objetos Bebida (clase hija de Producto)
    batido_vainilla = Bebida(
        nombre="Batido de vainilla",
        precio=3.00,
        volumen_ml=400,
        tamano="Grande",
        tipo_bebida="Malteada"
    )

    gaseosa_cola = Bebida(
        nombre="Gaseosa Cola",
        precio=1.50,
        volumen_ml=350,
        tamano="Mediano",
        tipo_bebida="Gaseosa"
    )

    # Registramos los productos en el restaurante
    restaurante.agregar_producto(hamburguesa_doble)
    restaurante.agregar_producto(papas_con_queso)
    restaurante.agregar_producto(batido_vainilla)
    restaurante.agregar_producto(gaseosa_cola)

    # Mostramos el menú completo (demostración de polimorfismo)
    restaurante.mostrar_menu()

    # Demostración de encapsulación: obtener_precio() y cambiar_precio()
    # controlan el acceso al atributo privado __precio
    print("\n--- Prueba de encapsulación sobre el precio ---")
    print(f"Precio actual de '{hamburguesa_doble.nombre}': ${hamburguesa_doble.obtener_precio():.2f}")

    hamburguesa_doble.cambiar_precio(7.00)
    print(f"Nuevo precio de '{hamburguesa_doble.nombre}': ${hamburguesa_doble.obtener_precio():.2f}")

    # Intento de asignar un precio inválido (debe ser rechazado)
    hamburguesa_doble.cambiar_precio(-5)


if __name__ == "__main__":
    main()
