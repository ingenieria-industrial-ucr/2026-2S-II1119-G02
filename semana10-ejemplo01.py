from eii_utils import leer_entero

x: int = 0
y: int = 0
plastico1: str = "4123-5555-6666-7777"
plastico2: str = "4123-5555-6666-"
plastico3: str = "4123-5555-6666-777a"
plastico4: str = "4123555566667777"
plastico5: str = "5123555566667777"


def contar_digitos(texto: str) -> int:
    contador: int = 0
    for caracter in texto:
        if (
            caracter == "1"
            or caracter == "2"
            or caracter == "3"
            or caracter == "4"
            or caracter == "5"
            or caracter == "6"
            or caracter == "7"
            or caracter == "8"
            or caracter == "9"
            or caracter == "0"
        ):
            contador += 1
    return contador


def es_numero_valido(plastico: str) -> bool:
    salida: bool = False
    plastico = plastico.strip()
    if plastico[0] == "4" and (len(plastico) == 16 or len(plastico) == 19):
        salida = True
    return salida


def obtener_mayor(a: int, b: int) -> int:
    if a > b:
        return a
    else:
        return b


if __name__ == "__main__":
    x, y = 23, 43
    # print(obtener_mayor(x, y))
    print(plastico1, es_numero_valido(plastico1))
    print(plastico2, es_numero_valido(plastico2))
    print(plastico3, es_numero_valido(plastico3))
    print(plastico4, es_numero_valido(plastico4))
    print(plastico5, es_numero_valido(plastico5))
