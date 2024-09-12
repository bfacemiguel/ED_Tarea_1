class Nodo_listaSE:
    def __init__(self, dato):
        self.dato = dato
        self.sig = None

    def __str__(self):
        return f"{self.dato}"

