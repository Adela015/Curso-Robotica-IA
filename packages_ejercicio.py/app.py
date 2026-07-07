# Importamos la carpeta .\clientes\ y el archivo busqueda.py (sin el .py)
# Seguido importamos la función (def) que necesitamos en este caso buscar_cliente
from clientes.busqueda import buscar_cliente

def main():
    nombre_cliente = input("Ingrese el nombre del cliente: ")

    cliente = buscar_cliente(nombre_cliente)
    
    if cliente:
        print(f"Cliente encontrado: {cliente}")
    else:
        print("Cliente no encontrado")

main()
