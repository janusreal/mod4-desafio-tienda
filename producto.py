class Producto:
    def __init__(self, nombre, precio, stock = 0):
        self.nombre =nombre
        self.precio=precio
        if stock < 0:
            self.stock = 0
        else:
            self.stock = stock
            

#estamos hablando de una tienda en particular y no una tienda genérica
#cada producto es parte de una tienda. Son parte de ella y no están aparte


def __eq__(self, otro_prod):
    return self.nombre == otro_prod.nombre
