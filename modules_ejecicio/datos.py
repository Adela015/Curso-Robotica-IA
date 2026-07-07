## from datos import base_datos

## print(base_datos)

from base import base_datos as db

clientes = db.base_datos["clientes"]
empleados = db.base_datos["empleados"]

print(f"Clientes: {db.base_datos['clientes']} \n")
print(f"Empleados: {db.base_datos['empleados']} \n")
