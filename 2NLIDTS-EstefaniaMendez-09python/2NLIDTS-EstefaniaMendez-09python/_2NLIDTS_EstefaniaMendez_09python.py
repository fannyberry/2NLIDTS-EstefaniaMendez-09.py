MAX_TAM = 10 

def ingresar_valores(frente, final, cola, contador):
    # Usamos el contador para saber si está llena de forma exacta
    if contador == MAX_TAM:
        print("Desbordamiento de la cola (Cola llena)")
        return frente, final, cola, contador
        
    elemento = int(input("Ingrese un elemento para la cola: "))
    cola[final] = elemento
    final = (final + 1) % MAX_TAM
    contador += 1
    print("Elemento agregado a la cola:", elemento)
    return frente, final, cola, contador

def eliminar_elemento(frente, final, contador):
    if contador == 0:
        print("La cola está vacía, no se puede eliminar")
        return frente, contador
        
    frente = (frente + 1) % MAX_TAM
    contador -= 1
    print("Elemento eliminado de la cola.")
    return frente, contador

def imprimir(frente, cola, contador):
    if contador == 0:
        print("La cola está vacía.")
        return
        
    print("Elementos de la cola en el orden de ingreso:")
    idx = frente
    for _ in range(contador):
        print(cola[idx], end=" ")
        idx = (idx + 1) % MAX_TAM
    print("\n")

def main():
    cola = [0] * MAX_TAM
    contador = 0
    frente = 0
    final = 0
    
    respuesta = input("¿Desea agregar elementos a la cola? (s/n): ").lower()
    while respuesta == "s" and contador < MAX_TAM:
        frente, final, cola, contador = ingresar_valores(frente, final, cola, contador)
        if contador < MAX_TAM:
            respuesta = input("¿Desea agregar más elementos a la cola? (s/n): ").lower()
            
    if contador == 0:
        print("La cola está vacía.")
        return
        
    primer_elemento = cola[frente]
    print("El primer elemento de la cola es:", primer_elemento)
    
    frente, contador = eliminar_elemento(frente, final, contador)
    imprimir(frente, cola, contador)

if __name__ == "__main__":
    main()
