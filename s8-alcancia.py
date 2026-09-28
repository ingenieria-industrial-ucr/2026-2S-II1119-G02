from eii_utils import (
    limpiar_consola,
    imprimir_titulo_decorado,
    pausar,
    mostrar_menu,
    imprimir_error,
    imprimir_advertencia,
    imprimir_mensaje,
    leer_flotante
)

opciones:list[str] = ["Ver Saldo","Depositar","Retirar"]
opcion:int = -1
saldo:float = 0
dinero:float = 0

while not(opcion == 0):
    opcion = mostrar_menu(opciones=opciones, titulo_menu="Menu principal")
    if opcion == 0:
        print("Muchas gracias por su visita")
    elif opcion == 1:
        limpiar_consola()
        print(f"Saldo {saldo:.2f}")
        pausar()
    elif opcion == 2:
        limpiar_consola()
        dinero = leer_flotante("Digite el dinero a depositar")
        saldo += dinero
    elif opcion == 3:
        limpiar_consola()
        dinero = leer_flotante("Digite el dinero a retirar")
        saldo -= dinero