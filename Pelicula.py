class Pelicula:
    def __init__(self, titulo, duracion, anio):
        self.titulo = titulo
        self.duracion = duracion
        self.anio = anio
        print(f"Se ha creado la película: {self.titulo}")

    def __str__(self):
        return f"{self.titulo} ({self.anio})"