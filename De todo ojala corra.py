#De todo ojala corra

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

categorias = {
    "Literatura colombiana": [("Cien años de soledad", 55300, 2), ("La María", 28800, 2), ("El olvido que seremos", 44800, 2),
                              ("Satanás", 44000, 2), ("El amor en los tiempos del cólera", 97000, 2)],

    "Ciencias exactas": [("La magia de las matemáticas", 163000, 2), ("Algebra de Baldor", 143000, 2), ("Cálculo de Leithold", 76000, 2),
                         ("Aritmética de Baldor", 86000, 2), ("El origen de las especies", 47900, 2)],

    "Ciencia ficción": [("La guerra de las galaxias", 41300), ("Harry Potter y la piedra filosofal", 52500, 2), ("La niebla", 32900, 2),
                        ("Harry Potter y la camara secreta", 52500, 2), ("Juan Salvador Gaviota", 34300, 2)],

    "Ciencias Sociales": [("Margarita va sola", 45500, 2), ("Conquistadores e indios", 45500, 2), ("El contrato social", 72000, 2),
                          ("El arte de la guerra", 31900, 2), ("Las 48 leyes del poder", 46000, 2)],

    "Poesía": [("Por los países de Colombia", 41300, 2), ("Soy vertical pero preferiría ser horizontal", 17500, 2), ("Oda a la vida", 10000, 2),
               ("Veinte poemas de amor y una canción desesperada", 22000, 2), ("Almas en pena, chapolas negras", 34300, 2)],

    "Novelas históricas": [("Crimen y castigo", 59900, 2), ("La Odisea", 59000, 2), ("Las mil y una noches", 59900, 2),
                           ("El Principito", 31900, 2),("Los miserables", 59900, 2)],

}


class MiApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.categoria_combo.addItems(categorias.keys())
        self.categoria_combo.currentIndexChanged.connect(self.actualizar_libros)

        self.boton_comprar.clicked.connect(self.realizar_compra)
        self.boton_ver_carrito.clicked.connect(self.mostrar_carrito)

        # Variable para almacenar la información de la compra actual
        self.compra_actual = {'categoria': '', 'libro': '', 'precio': 0, 'cantidad': 0, 'descuento': 0}

        # Lista para almacenar las compras realizadas (carrito de compras)
        self.carrito = []

    def actualizar_libros(self):
        categoria_seleccionada = self.categoria_combo.currentText()
        libros = [libro[0] for libro in categorias[categoria_seleccionada]]
        self.libro_combo.clear()
        self.libro_combo.addItems(libros)

    def realizar_compra(self):
        categoria = self.categoria_combo.currentText()
        libro = self.libro_combo.currentText()
        cantidad = self.cantidad_spin.value()

        precio = [libro[1] for libro in categorias[categoria] if libro[0] == libro][0]

        # Lógica para aplicar descuentos
        descuento = self.aplicar_descuentos(categoria, libro, cantidad)

        precio_total = precio * cantidad - descuento

        # Actualizar la información de la compra actual
        self.compra_actual = {'categoria': categoria, 'libro': libro, 'precio': precio, 'cantidad': cantidad,
                              'descuento': descuento}

        # Agregar la compra al carrito
        self.carrito.append(self.compra_actual)

        # Mostrar el resultado en la interfaz
        self.mostrar_resultados()

    def aplicar_descuentos(self, categoria, libro, cantidad):
        # Lógica para aplicar descuentos según las reglas establecidas
        # Aquí debes implementar las reglas específicas del ejercicio
        return 0

    def mostrar_resultados(self):
        # Lógica para mostrar los resultados en la interfaz
        # Aquí puedes utilizar los valores almacenados en self.compra_actual
        pass

    def mostrar_carrito(self):
        # Lógica para mostrar el carrito de compras
        carrito_texto = ""
        for compra in self.carrito:
            carrito_texto += f"{compra['categoria']} - {compra['libro']} - Cantidad: {compra['cantidad']} - Precio: {compra['precio']}\n"

        if carrito_texto:
            QMessageBox.information(self, "Carrito de Compras", carrito_texto)
        else:
            QMessageBox.information(self, "Carrito de Compras", "El carrito está vacío")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiApp()
    ventana.show()
    sys.exit(app.exec_())
