from producto import Producto

# tipo puede ser super, farmacia o restaurant
# los tres metodos deben ser abstractos

class Tienda:
    
    def __init__(self, nombre, costo_delivery, tipo):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.productos = []
        self.tipo =tipo
        
    def ingresar_producto(self, nombre, precio, stock):
        nuevo_producto = Producto(nombre, precio, stock)
        #iterar para definir si existe producto
        for prod in self.productos:
            if prod == nuevo_producto:
                prod.stock += nuevo_producto.stock
                return
        #si llego a esta linea, quiere decir que nunca encontré
        #el producto
        self.productos.append(nuevo_producto)
        
    def listar_productos(self):
        pass
    
    def realizar_venta(self):
        pass
    
    
    
    