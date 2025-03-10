from Pelicula import Pelicula

# Creamos una clase llamada Catalogo

class Catalogo:
    def __init__(self, peliculas=None):
        if peliculas is None:
            peliculas = []
        self.peliculas = peliculas

    def agregar(self, pelicula):
        self.peliculas.append(pelicula)

    def mostrar(self):
        for pelicula in self.peliculas:
            print(pelicula)