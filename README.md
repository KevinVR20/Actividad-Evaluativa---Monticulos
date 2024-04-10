# Actividad-Evaluativa---Monticulos

Kevin Yesid Vargas Ravelo. 2211253

Descripción del planteamiento del problema:

El problema consiste en diseñar un programa en Python que simule la gestión de una cola de prioridad para la atención de llamadas de emergencia en una unidad de policía. Cada llamada se registra con los siguientes datos: nombre completo, edad, dirección, motivo de la llamada y gravedad. La gravedad se evalúa en una escala del 1 al 5, donde 1 es la mayor gravedad. Además, se establece una prioridad en la atención de las llamadas de acuerdo a la gravedad y la edad del solicitante, priorizando a niños menores de 12 años, adultos mayores de 65 años y, en caso de empate en la gravedad, se considera la edad para desempatar. Se deben implementar funciones para ingresar una llamada a la cola de prioridad, pasar a la siguiente solicitud en ser atendida y mostrar la cola actual.

Análisis realizado:

Se identificaron los requisitos del problema, incluyendo la estructura de datos a utilizar (cola de prioridad), los datos necesarios para cada llamada y las reglas de priorización.

Se diseñó una clase Llamada para representar cada llamada, con atributos para almacenar nombre, edad, dirección, motivo y gravedad.

Se adaptó una implementación de montículo binario (heap) para manejar la cola de prioridad. Se modificaron los métodos para insertar y eliminar elementos, teniendo en cuenta la prioridad según las especificaciones del problema.

Se implementó un menú interactivo para permitir al usuario ingresar llamadas, pasar a la siguiente solicitud en ser atendida, mostrar la cola actual y salir del programa.

Se realizó una prueba del programa con diferentes escenarios para asegurar su correcto funcionamiento, incluyendo casos de llamadas con la misma gravedad y la misma edad para validar el desempate.
