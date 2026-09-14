nombre:str = 'Mauricio'
apellido:str = 'Zamora'
cumple:str = '14 de mayo'

#"Hola, soy xxx xxx y cumplo el día xxxx"

print(f"Hola, soy {nombre} {apellido} y cumplo el día {cumple}")

costo:float = 123.344
utilidad:float = costo * 0.5
impuesto:float = (costo+utilidad)*0.13
total:float = costo + utilidad + impuesto

print(f"Costo {costo}")
print(f"Utilidad {utilidad}")
print(f"Impuesto {impuesto}")
print(f"Total {total}")
print('-'*10)
print("{:12} {:8.2f}".format("Costo",costo))
print("{:12} {:8.2f}".format("Utilidad",utilidad))
print("{:12} {:8.2f}".format("Impuesto",impuesto))
print("{:12} {:8.2f}".format("Total",total))