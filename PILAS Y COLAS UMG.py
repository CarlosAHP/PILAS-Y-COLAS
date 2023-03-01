import random
import time

class Pila:
    def __init__(self):
        self.items = []
    
    def esta_vacia(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

class Cola:
    def __init__(self):
        self.items = []
    
    def esta_vacia(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0,item)
    
    def dequeue(self):
        return self.items.pop()

def generar_numeros():
    numeros = []
    for i in range(1000000):
        numeros.append(random.randint(-10000000,10000000))
    return numeros

def guardar_en_pila(numeros):
    pila = Pila()
    start_time = time.time()
    for numero in numeros:
        pila.push(numero)
    end_time = time.time()
    tiempo = end_time - start_time
    return pila, tiempo

def guardar_en_cola(numeros):
    cola = Cola()
    start_time = time.time()
    for numero in numeros:
        cola.enqueue(numero)
    end_time = time.time()
    tiempo = end_time - start_time
    return cola, tiempo

opcion = 0
while opcion != 3:
    print("Seleccione una opción:")
    print("1. Generar números aleatorios y guardarlos en una pila.")
    print("2. Generar números aleatorios y guardarlos en una cola.")
    print("3. Salir.")
    opcion = int(input())

    if opcion == 1:
        numeros = generar_numeros()
        pila, tiempo = guardar_en_pila(numeros)
        print(f"Se han insertado los números en la pila en {tiempo} segundos.")
        
    elif opcion == 2:
        numeros = generar_numeros()
        cola, tiempo = guardar_en_cola(numeros)
        print(f"Se han insertado los números en la cola en {tiempo} segundos.")
    
    elif opcion == 3:
        print("Saliendo del programa...")
    
    else:
        print("Opción inválida. Intente nuevamente.")
