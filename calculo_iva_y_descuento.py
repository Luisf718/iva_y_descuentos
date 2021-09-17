import random

# Aqui puedes importar o hacer los diccionarios que quieras para calcularles el descuento y el iva, en las llaves va el precio de los productos y en los valores va el descuento o el iva 
compras_descuento = {
    3000: 30,
    6000: 27,
    4000: 30,
    6000: 40,
    70000: 50,
    }
compras_iva = {
    6000: 16,
    5000: 16,
    3000: 20,
    3050: 20,
    6500: 20

}

# Creamos una función para calcular el producto con el iva 
def calculo_iva(precio, iva):
    iva_decimal = iva / 100
    iva_precio = precio * iva_decimal
    precio_con_iva = precio + iva_precio
    print(f"El producto con iva cuesta {precio_con_iva}")
    
# Creamos una función para calcular el producto con el descuento
def descuento_function(precio_2, descuento):
    descuento_decimal = descuento / 100
    descuento_real = precio_2 * descuento_decimal
    producto_con_descuento = precio_2 - descuento_real
    print(f"El producto con descuento cuesta {producto_con_descuento} pesos")
    
# Creamos una función para que imprima todos los productos ya con el descuento y el iva 
def lista_de_compras():
    print("Esta es la lista de compras con descuento: ")
    for precio in compras_descuento.keys():
        for des in compras_descuento.values():
            descuento_function(precio, des)
    
    print("Esta es la lista de compras con iva: ")
    for precio in compras_iva.keys():
        for iva in compras_iva.values():
            calculo_iva(precio, iva)
        
    
if __name__ == "__main__":
    lista_de_compras()