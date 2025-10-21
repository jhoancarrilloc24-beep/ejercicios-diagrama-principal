# Clase Usuario

class Usuario:
    # constructor de usuario

    def __init__(self, nombre, apellido, n_cuenta, direccion, login, password):
        self.nombre = nombre
        self.apellido = apellido
        self.n_cuenta = n_cuenta
        self.direccion = direccion
        self.login = login
        self.password = password
        print(f"Usuario creado: {self.nombre} {self.apellido}, cuenta N° {self.n_cuenta}.")

# imprimir texto

    def enviar_sugerencia(self):
        print(f"{self.nombre} ha enviado una sugerencia al sistema ➡️.")

    def leer(self):
        print(f"{self.nombre} está leyendo un producto del catálogo 📦.")

    def comprar(self):
        print(f"{self.nombre} ha realizado una compra 💰.")

    def vender(self):
        print(f"{self.nombre} ha vendido un producto ✉️.")

    def realizar_reclamacion(self):
        print(f"{self.nombre} ha realizado una reclamación ➡️.")


# Clase Producto

class Producto:
    # constructor de producto

    def __init__(self, precio, titulo, autor, editorial, anio_edicion, preferencias):
        self.precio = precio
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.anio_edicion = anio_edicion
        self.preferencias = preferencias

# texto a mostrar

    def vender(self):
        print(f"Producto '{self.titulo}' vendido con éxito ✅.")

    def comprar(self):
        print(f"Producto '{self.titulo}' comprado correctamente ✅.")

    def ver_catalogo(self):
        print(f"Mostrando información del producto: {self.titulo}")



# Subclases de Producto

class Libro(Producto):
    # constructor de libro


    def __init__(self, precio, titulo, autor, editorial, anio_edicion, preferencias, genero):
        super().__init__(precio, titulo, autor, editorial, anio_edicion, preferencias)
        self.genero = genero

# subclass de revista

class Revista(Producto):
    #constructor de revista

    def __init__(self, precio, titulo, autor, editorial, anio_edicion, preferencias, categoria):
        super().__init__(precio, titulo, autor, editorial, anio_edicion, preferencias)
        self.categoria = categoria


# subclass de articulo segunda mano

class ArticuloSegundaMano(Producto):
    # constructor de articulo segunda mano

    def __init__(self, precio, titulo, autor, editorial, anio_edicion, preferencias, clasificacion, tema, vendedor):
        super().__init__(precio, titulo, autor, editorial, anio_edicion, preferencias)
        self.clasificacion = clasificacion
        self.tema = tema
        self.vendedor = vendedor

# subclass de novedades

class Novedades(Producto):
    # constructor de novedades

    def __init__(self, precio, titulo, autor, editorial, anio_edicion, preferencias, clasificacion, tema):
        super().__init__(precio, titulo, autor, editorial, anio_edicion, preferencias)
        self.clasificacion = clasificacion
        self.tema = tema

    def cambiar_clasificacion(self, nueva):
        # texto
        print(f"Novedad '{self.titulo}' cambió su clasificación de {self.clasificacion} a {nueva}.")
        self.clasificacion = nueva

# subclass articulo online

class ArticuloOnline(Producto):
    # constructor de articulo online

    def __init__(self, precio, titulo, autor, editorial, anio_edicion, preferencias, tema):
        super().__init__(precio, titulo, autor, editorial, anio_edicion, preferencias)
        self.tema = tema
# texto

    def publicar(self):
        print(f"Artículo online '{self.titulo}' publicado en la web.")


# Clase Editorial

class Editorial:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
# texto

    def vender(self):
        print(f"La editorial '{self.nombre}' ha vendido un producto 📦.")


# Clase Servidor

class Servidor:
    # textos a imprimir

    def muestra_pagina(self):
        print("Servidor: https://accounts.google.com/v3/signin")

    def envia_sugerencia(self):
        print("Servidor: Enviando sugerencia al administrador 💻.")

    def envia_datos_de_compra(self):
        print("Servidor: Enviando datos de compra al procesador ♻️.")

    def envia_datos_de_venta(self):
        print("Servidor: Enviando datos de venta al procesador 💰.")


# Clase Indexador

class Indexador:
    # textos A imprimir

    def actualiza_almacen(self):
        print("Indexador: Actualizando el almacén de productos 🫙.")

    def envia_resultado_busqueda(self):
        print("Indexador: Enviando resultado de la búsqueda 🔎.")


# Clase Procesador

class Procesador:
    # texto a imprimir

    def mandar_datos_de_venta(self):
        print("Procesador: Mandando datos de venta al servidor 💸.")

    def mandar_articulo_online(self):
        print("Procesador: Mandando artículo online al sistema ➡️.")

    def envia_sugerencia_administrador(self):
        print("Procesador: Enviando sugerencia al administrador 👨‍💻.")

    def modificar_stock(self):
        print("Procesador: Modificando el stock de productos 📦.")

    def realizar_cobro(self):
        print("Procesador: Realizando el cobro al cliente 💰.")

    def realizar_pago(self):
        print("Procesador: Procesando el pago al vendedor 💸.")

    def actualiza_catalogo(self):
        print("Procesador: Actualizando catálogo de productos ♻️.")

    def realiza_busqueda(self):
        print("Procesador: Realizando búsqueda de productos 🔎.")


# Clase Recolector

class Recolector:
    # texto a imprimir
    def envia_novedades(self):
        print("Recolector: Enviando novedades al procesador ✉️.")


# Clase Hilo

class Hilo:
    #texto a mostrar 

    def busca_novedades(self):
        print("Hilo: Buscando novedades en el sistema 🔍.")


# Función principal

# codigo principal

def main():
    print("=== SISTEMA DE PRODUCTOS ===\n")

    usuario = Usuario("jhoan", "carrillo", 2314, "Calle 10", "anaL", "12345")
    producto = Libro(50000, "El Principito", "Antoine", "Planeta", 2020, "Infantil", "Fantasía")
    print(f"Producto creado: {producto.titulo} 📖")
    print("")
    servidor_inicio = Servidor()
    procesador = Procesador()
    indexador = Indexador()
    editorial = Editorial("Norma", "Cra 7", "3001234567")
    recolector = Recolector()
    hilo = Hilo()

    print("zona de Servidor ")
    servidor_inicio.muestra_pagina()
    servidor_inicio.envia_sugerencia()
    servidor_inicio.envia_datos_de_compra()
    servidor_inicio.envia_datos_de_venta()
    print("")
    print("zona de usuario")
    usuario.enviar_sugerencia()
    usuario.leer()
    usuario.comprar()
    usuario.vender()
    usuario.realizar_reclamacion()
    print("")
    print("zona de procesador")
    procesador.mandar_datos_de_venta()
    procesador.mandar_articulo_online()
    procesador.envia_sugerencia_administrador()
    procesador.modificar_stock()
    procesador.realizar_cobro()
    procesador.realizar_pago()
    procesador.actualiza_catalogo()
    procesador.realiza_busqueda()
    print("")
    print("zona de producto")
    producto.vender()
    producto.comprar()
    producto.ver_catalogo()
    print("")
    print("zona de iditorial")
    editorial.vender()
    print("")
    print("zona de recolector")
    recolector.envia_novedades()
    print("")
    print("zona de hilo")
    hilo.busca_novedades()
    print("")

# zona de ejecucion

if __name__ == "__main__":
    main()