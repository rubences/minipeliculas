from Pelicula import Pelicula
from Catalogo import Catalogo

def main():
    p = Pelicula("El Padrino", 175, 1972)
    c = Catalogo([p])  # Añado una lista con una película desde el principio
    c.mostrar()
    c.agregar(Pelicula("El Padrino: Parte 2", 202, 1974))  # Añadimos otra
    c.mostrar()


if __name__ == "__main__":
    main()
