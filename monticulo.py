import heapq

class Llamada:
    def __init__(self, nombre, edad, direccion, motivo, gravedad):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.motivo = motivo
        self.gravedad = gravedad

    def __lt__(self, other):
        if self.gravedad == other.gravedad:
            return self.edad < other.edad
        return self.gravedad < other.gravedad

class ColaPrioridad:
    def __init__(self):
        self.cola = []
        self.contador = 0
        
    def infiltArriba(self, i):
        while i // 2 > 0:
            if self.cola[i][3] < self.cola[i // 2][3]:
                self.cola[i], self.cola[i // 2] = self.cola[i // 2], self.cola[i]
            elif self.cola[i][3] == self.cola[i // 2][3]:
                if self.cola[i][0] < self.cola[i // 2][0]:
                    self.cola[i], self.cola[i // 2] = self.cola[i // 2], self.cola[i]
                else:
                    break
            else:
                break
            i = i // 2

    def ingresar_llamada(self, nombre, edad, direccion, motivo, gravedad):
        llamada = Llamada(nombre, edad, direccion, motivo, gravedad)
        heapq.heappush(self.cola, (llamada.nombre, llamada.edad, llamada.direccion, llamada.motivo, llamada.gravedad, self.contador))
        self.contador += 1
        self.infiltArriba(len(self.cola) - 1)
        print(f"Llamada de {nombre} ingresada. Posición en cola: {len(self.cola)}")
        
    def pasar_siguiente_solicitud(self):
        if self.cola:
            nombre, edad, direccion, motivo, gravedad, _ = heapq.heappop(self.cola)
            print("Siguiente solicitud en ser atendida:")
            print(f"Nombre: {nombre}")
            print(f"Edad: {edad}")
            print(f"Dirección: {direccion}")
            print(f"Motivo: {motivo}")
            print(f"Gravedad: {gravedad}")
        else:
            print("No hay más solicitudes en espera.")
            
    def mostrar_cola(self):
        print("Cola de atención:")
        for _, edad, _, _, gravedad, _ in self.cola:
            print(f"Nombre: {_} - Edad: {edad} - Gravedad: {gravedad}")

cola_prioridad = ColaPrioridad()

while True:
    print("\nMenú:")
    print("1. Ingresar Llamada")
    print("2. Pasar siguiente solicitud")
    print("3. Mostrar la cola")
    print("4. Salir")
    
    opcion = input("Ingrese la opción deseada: ")
    
    if opcion == "1":
        nombre = input("Nombre Completo: ")
        edad = int(input("Edad: "))
        direccion = input("Dirección: ")
        motivo = input("Motivo de la llamada: ")
        gravedad = int(input("Gravedad (1-5): "))
        cola_prioridad.ingresar_llamada(nombre, edad, direccion, motivo, gravedad)
    elif opcion == "2":
        cola_prioridad.pasar_siguiente_solicitud()
    elif opcion == "3":
        cola_prioridad.mostrar_cola()
    elif opcion == "4":
        break
    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")