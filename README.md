# Burger Cedeño — Sistema de productos en Python (POO)

**Datos generales:**
1. Estudiante: Carlos Javier Cedeño Leiton
2. Asignatura: Programación Orientada a Objetos
3. Actividad: Semana 6 — Taller Práctico de organización modular de un sistema OOP en Python

---

## Descripción del sistema

Este proyecto implementa una versión mejorada del sistema `restaurante_app` para
**Burger Cedeño**, una hamburguesería y restaurante de comida rápida, aplicando los
principios fundamentales de la Programación Orientada a Objetos: **herencia**,
**encapsulación** y **polimorfismo**. El sistema representa los productos disponibles
mediante una clase padre `Producto` y dos clases hijas especializadas, `Platillo` y
`Bebida`. Un servicio `Restaurante` administra la lista de productos registrados y permite
mostrar el menú completo en consola.

A diferencia de una versión mínima, en este proyecto cada clase hija agrega **tres**
atributos propios en lugar de uno solo, para reforzar la idea de que un platillo y una
bebida necesitan información distinta a la de un producto genérico. El programa crea dos
platillos y dos bebidas propios de una hamburguesería, los registra en el restaurante y
muestra su información utilizando el mismo método (`mostrar_informacion()`), evidenciando
cómo cada tipo de objeto responde de forma distinta a la misma llamada.

## Estructura del proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py      # Clase padre Producto
│   ├── platillo.py       # Clase hija Platillo
│   └── bebida.py         # Clase hija Bebida
├── servicios/
│   ├── __init__.py
│   └── restaurante.py    # Clase de servicio Restaurante
└── main.py                # Punto de arranque del programa
```

- **`modelos/producto.py`**: define la clase `Producto`, con los atributos comunes a
  cualquier producto del restaurante: `nombre`, `__precio` (encapsulado) y `disponible`.
- **`modelos/platillo.py`**: define la clase `Platillo`, que hereda de `Producto` y agrega
  los atributos propios `tipo_platillo`, `tiempo_preparacion_minutos` y `calorias`.
- **`modelos/bebida.py`**: define la clase `Bebida`, que hereda de `Producto` y agrega los
  atributos propios `volumen_ml`, `tamano` y `tipo_bebida`.
- **`servicios/restaurante.py`**: define la clase `Restaurante`, encargada de almacenar los
  productos en una lista y mostrar el menú completo.
- **`main.py`**: crea los objetos, los registra en el restaurante y muestra los resultados
  en consola.

## Relación de herencia aplicada

Se aplicó una relación de herencia simple entre una clase general y dos clases
especializadas:

```
Producto
├── Platillo
└── Bebida
```

`Platillo` y `Bebida` heredan de `Producto` los atributos `nombre`, `__precio` y
`disponible`, reutilizándolos mediante `super().__init__()` en sus respectivos
constructores, y cada una agrega únicamente los atributos que le son propios, razonando qué
información pertenece a la clase padre (común a cualquier producto de la hamburguesería) y
cuál es exclusiva de cada clase hija (propia de un platillo o de una bebida).

## Atributo encapsulado

El atributo `__precio` de la clase `Producto` está encapsulado (nombre con doble guion
bajo). No se accede ni se modifica directamente desde fuera de la clase; en su lugar se
utilizan los métodos:

- `obtener_precio()`: devuelve el valor actual del precio.
- `cambiar_precio(nuevo_precio)`: valida que el nuevo precio sea mayor a cero antes de
  asignarlo; si no lo es, rechaza el cambio y muestra un mensaje de error.

## Método utilizado para demostrar polimorfismo

El método `mostrar_informacion()`, definido inicialmente en `Producto`, es sobrescrito en
`Platillo` y en `Bebida` para mostrar información específica de cada tipo de producto. En
`servicios/restaurante.py`, el método `mostrar_menu()` recorre la lista de productos
registrados y llama a `producto.mostrar_informacion()` sobre cada uno; aunque la llamada es
la misma para todos los objetos, cada uno ejecuta su propia versión del método según su
clase real (Platillo o Bebida), lo que evidencia el polimorfismo.

## Reflexión

Adaptar este sistema al contexto de una hamburguesería me permitió comprobar que la
Programación Orientada a Objetos no limita la cantidad de atributos que una clase hija
puede agregar: un platillo de comida rápida necesita tanto su tipo, como su tiempo de
preparación y sus calorías, mientras que una bebida necesita volumen, tamaño y tipo. La
herencia evitó repetir el nombre, precio y disponibilidad en cada clase; la encapsulación
del precio me obligó a validar cualquier cambio antes de aplicarlo, protegiendo la
integridad del dato; y el polimorfismo permitió que el restaurante mostrara el menú
completo llamando a un único método, sin importar si el objeto era un platillo o una
bebida. En conjunto, estos tres principios hacen que el sistema sea más ordenado, seguro y
fácil de escalar si en el futuro se agregan nuevos tipos de productos.

## Ejecución del programa

Desde la carpeta raíz del proyecto:

```bash
cd restaurante_app
python3 main.py
```
