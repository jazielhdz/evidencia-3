import re, json, csv

class Vehiculo:
    def __init__(self, unidad, marca, modelo, km):
        self.unidad = unidad
        self.marca = marca
        self.modelo = modelo
        self.km = km

def validar_datos():
    while True:
        unidad = input("Unidad (XX-123): ")
        if re.match(r"^[A-Za-z0-9]{2}-[A-Za-z0-9]{3}$", unidad):
            return unidad, input("Marca: "), int(input("Modelo (2020-2024): ")), int(input("Km: "))
        print("Formato inválido")

def guardar(unidades, tipo="json"):
    if tipo == "json":
        json.dump([vars(v) for v in unidades], open("unidades.json", "w"))
    else:
        with open("unidades.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(['unidad', 'marca', 'modelo', 'km'])
            writer.writerows([[v.unidad, v.marca, v.modelo, v.km] for v in unidades])

def cargar(tipo="json"):
    try:
        if tipo == "json":
            return [Vehiculo(**v) for v in json.load(open("unidades.json"))]
        with open("unidades.csv") as f:
            return [Vehiculo(*row) for row in list(csv.reader(f))[1:]]
    except: return []

def main():
    unidades = []
    while True:
        op = input("\n1.Agregar 2.Mostrar 3.Guardar JSON 4.Cargar JSON 5.Guardar CSV 6.Cargar CSV 7.Salir\nOpción: ")
        if op == "1": unidades.append(Vehiculo(*validar_datos()))
        elif op == "2": [print(f"{i+1}. {v.unidad}, {v.marca}, {v.modelo}, {v.km}km") for i,v in enumerate(unidades)]
        elif op == "3": guardar(unidades, "json")
        elif op == "4": unidades = cargar("json")
        elif op == "5": guardar(unidades, "csv")
        elif op == "6": unidades = cargar("csv")
        elif op == "7": break

if __name__ == "__main__":
    main()