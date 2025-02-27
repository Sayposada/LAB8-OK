from BinaryTree import *
from BinarySearchTree import *

class Usuario:
    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion

    def __str__(self):
        return f"{self.nombre} ({self.identificacion})"
    
    def calcular_clave(self, identificacion):
        return sum(int(digito) for digito in str(identificacion))




# Crear el árbol binario de búsqueda
bst = BinarySearchTree()

# Crear los usuarios
usuarios = [
    Usuario("Pablo", 10001011),
    Usuario("Maria", 10101015),
    Usuario("Ana", 1010000),
    Usuario("Diana", 10111105),
    Usuario("Mateo", 10110005)
]

# Insertar los usuarios en el árbol
for usuario in usuarios:
    clave = usuario.calcular_clave(usuario.identificacion)
    bst.insert(clave, usuario)

# Mostrar el árbol
print("Árbol binario de búsqueda:")
bst.display()

# Recorrido inorder
print("\nRecorrido inorder:")
inorder = bst.inorder_traversal()
for clave in inorder:
    usuario = bst.find(clave).data
    print(f"Clave: {clave}, Usuario: {usuario}")

# Buscar un usuario
clave_busqueda = 8
usuario_buscado = bst.find(clave_busqueda)

if usuario_buscado is not None:
    print(f"\nUsuario con clave {clave_busqueda}: {usuario_buscado.data}")
else:
    print(f"\nClave {clave_busqueda} no encontrada en el árbol.")

# Encontrar mínimo y máximo
min_usuario = bst.find_min()
max_usuario = bst.find_max()

if min_usuario is not None:
    print(f"\nUsuario con clave mínima: {min_usuario}")
else:
    print("No hay usuarios en el árbol para encontrar la clave mínima.")

if max_usuario is not None:
    print(f"Usuario con clave máxima: {max_usuario}")
else:
    print("No hay usuarios en el árbol para encontrar la clave máxima.")

# Eliminar un usuario
clave_eliminar = 4
if bst.find(clave_eliminar) is not None:
    bst.remove(clave_eliminar)
    print("\nÁrbol después de eliminar a Pablo:")
else:
    print(f"\nClave {clave_eliminar} no encontrada en el árbol.")

bst.display()