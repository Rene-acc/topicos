from PyQt5.QtWidgets import QTableWidgetItem, QFileDialog, QMessageBox
from vista import *
from modelo import *
from neuronal import *
#plt.rcParams['font.family'] = 'sans-serif'
#plt.rcParams['font.sans-serif'] = ['Malgun Gothic', 'DejaVu Sans', 'cmr10','Code2000']

class controlador(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self) 
        
        self.csv = modelo()

        self.botonAbrir.clicked.connect(self.abrirArchivo)
        self.botonGuardar.clicked.connect(self.guardarArchivo)
        self.botonFiltrar.clicked.connect(self.filtrarArchivo)
        self.botonNube.clicked.connect(self.crearNube)
        self.botonHistograma.clicked.connect(self.crearHistograma)
        self.botonMostrarTodos.clicked.connect(self.mostrarTodos)


    def abrirArchivo(self):
        abrirFile = QFileDialog.getOpenFileName(self,"Abrir Archivo CSV", "","CSV files (*.csv);;All files (*.*)")
        self.direccionAbrir = abrirFile[0]
        try:
            self.csv.set_archivo(self.direccionAbrir)
            self.verArchivo()
        except Exception:
            self.verificarArchivo()
            return None
        
    def guardarArchivo(self):
        guardarFile = QFileDialog.getSaveFileName(self,"Guardar Archivo CSV", "","CSV files (*.csv);;All files (*.*)")
        self.direccionGuardar = guardarFile[0]
        try:
            self.csv.get_archivo().to_csv(self.direccionGuardar)
        except Exception:
            self.verificarArchivo()
            return None

    def filtrarArchivo(self):
        try:
            texto = self.editarTexto.text()
            sentimiento = self.editarSentimiento.text()
            idioma = self.editarIdioma.text()
            self.csv.filtrarCSV(texto, sentimiento, idioma)
            self.verArchivo()
        except Exception:
            self.verificarArchivo()
            return None

    def crearNube(self):
        try:
            self.csv.nubePalabras()
        except Exception:
            self.verificarArchivo()

    def crearHistograma(self):
        try:
            self.csv.histograma()
        except Exception:
            self.verificarArchivo()
            
    def mostrarTodos(self):
        self.csv.archivoCompleto()
        self.verArchivo()

    def verArchivo(self):
        self.tabla.setColumnCount(self.csv.get_x())
        self.tabla.setRowCount(self.csv.get_y())
        for j in range(self.csv.get_x()):
            encabezado = QtWidgets.QTableWidgetItem(self.csv.get_encabezado()[j])
            self.tabla.setHorizontalHeaderItem(j, encabezado)
            for i in range(self.csv.get_y()):
                dato = str(self.csv.get_datos()[i][j])
                self.tabla.setItem(i,j, QTableWidgetItem(dato))
        self.tabla.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.tabla.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def verificarArchivo(self):
        QMessageBox.about (self,'Advertencia', 'Archivo erroneo')  

##Borrar al finalizar
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = controlador()
    window.show()
    app.exec_()