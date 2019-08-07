if __name__ == "main":
    a = "a"
    b = "b"


def agregar(Grafo_simple):
    grafo = Grafo()
    agregar(grafo, a)
    agregar(grafo, b)

print("agregar")

def relaciona(Grafo_simple):
    relacionar(grafo, a, b, 1)
    relacionar(grafo, b, 2)
    relacionar(grafo, a, 3)
    relacionar(grafo, a, b, 4)
print ("relaciona")



numerograph = int(input("digite un numerograph:"))
if numerograph == 1:
    print("el numerograph es dirigido a, b")
elif numero == 1:
    print("el numeronodo no es dirigido a, b")


numerograph = int(input("digite un numerograph:"))
if numerograph == 3:
    print("el numerograph es dirigido a, ")
elif numero == 3:
    print("el numeronodo no es dirigido a, b")

numerograph = int(input("digite un numerograph:"))
if numerograph == 2:
    print("el numerograph es dirigido b, ")
elif numero == 2:
    print("el numeronodo no es dirigido a, b")

numerograph = int(input("digite un numerograph:"))
if numerograph == 4:
    print("el numerograph es dirigido a, b")
elif numero == 4:
    print("el numeronodo no es dirigido a, b")

