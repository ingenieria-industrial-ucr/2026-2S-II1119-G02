from eii_utils import limpiar_consola, leer_entero, imprimir_error, imprimir_mensaje

dinero:int=0
estudiante:int=0

limpiar_consola()
estudiante = leer_entero("Cuanto estudiantes son")
dinero=leer_entero("Monto recolectado")

if dinero >= (estudiante * 500):
    imprimir_mensaje("Nos fuimos de fiesta (de la alegria)")
else:
    imprimir_error("Se devuelve el dinero")