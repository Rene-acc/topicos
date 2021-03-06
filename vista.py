# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vistaSinEdit.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 619)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 791, 26))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 240, 781, 351))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabla = QtWidgets.QTableWidget(self.layoutWidget1)
        self.tabla.setObjectName("tabla")
        self.tabla.setColumnCount(0)
        self.tabla.setRowCount(0)
        self.verticalLayout.addWidget(self.tabla)
        self.botonMostrarTodos = QtWidgets.QPushButton(self.layoutWidget1)
        self.botonMostrarTodos.setObjectName("botonMostrarTodos")
        self.verticalLayout.addWidget(self.botonMostrarTodos)
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setGeometry(QtCore.QRect(10, 30, 781, 202))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.botonAbrir = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.botonAbrir.setFont(font)
        self.botonAbrir.setObjectName("botonAbrir")
        self.botonGuardar = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.botonGuardar.setFont(font)
        self.botonGuardar.setObjectName("botonGuardar")
        self.opciones = QtWidgets.QToolBox(self.splitter_2)
        self.opciones.setObjectName("opciones")
        self.opcionesFiltrar = QtWidgets.QWidget()
        self.opcionesFiltrar.setGeometry(QtCore.QRect(0, 0, 610, 121))
        self.opcionesFiltrar.setObjectName("opcionesFiltrar")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.opcionesFiltrar)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.editarTexto = QtWidgets.QLineEdit(self.opcionesFiltrar)
        self.editarTexto.setObjectName("editarTexto")
        self.gridLayout.addWidget(self.editarTexto, 0, 1, 1, 1)
        self.botonFiltrar = QtWidgets.QPushButton(self.opcionesFiltrar)
        self.botonFiltrar.setObjectName("botonFiltrar")
        self.gridLayout.addWidget(self.botonFiltrar, 3, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.opcionesFiltrar)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.opcionesFiltrar)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.editarSentimiento = QtWidgets.QLineEdit(self.opcionesFiltrar)
        self.editarSentimiento.setObjectName("editarSentimiento")
        self.gridLayout.addWidget(self.editarSentimiento, 1, 1, 1, 1)
        self.editarIdioma = QtWidgets.QLineEdit(self.opcionesFiltrar)
        self.editarIdioma.setObjectName("editarIdioma")
        self.gridLayout.addWidget(self.editarIdioma, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.opcionesFiltrar)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.opciones.addItem(self.opcionesFiltrar, "")
        self.opcionesFrecuencia = QtWidgets.QWidget()
        self.opcionesFrecuencia.setGeometry(QtCore.QRect(0, 0, 610, 121))
        self.opcionesFrecuencia.setObjectName("opcionesFrecuencia")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.opcionesFrecuencia)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.botonNube = QtWidgets.QPushButton(self.opcionesFrecuencia)
        self.botonNube.setObjectName("botonNube")
        self.gridLayout_5.addWidget(self.botonNube, 0, 0, 1, 1)
        self.botonHistograma = QtWidgets.QPushButton(self.opcionesFrecuencia)
        self.botonHistograma.setObjectName("botonHistograma")
        self.gridLayout_5.addWidget(self.botonHistograma, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_5)
        self.opciones.addItem(self.opcionesFrecuencia, "")
        self.opcionesRed = QtWidgets.QWidget()
        self.opcionesRed.setGeometry(QtCore.QRect(0, 0, 610, 121))
        self.opcionesRed.setObjectName("opcionesRed")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.opcionesRed)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.botonEntrenar = QtWidgets.QPushButton(self.opcionesRed)
        self.botonEntrenar.setObjectName("botonEntrenar")
        self.gridLayout_3.addWidget(self.botonEntrenar, 0, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.opcionesRed)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)
        self.editarRed = QtWidgets.QLineEdit(self.opcionesRed)
        self.editarRed.setObjectName("editarRed")
        self.gridLayout_3.addWidget(self.editarRed, 1, 1, 1, 1)
        self.botonRed = QtWidgets.QPushButton(self.opcionesRed)
        self.botonRed.setObjectName("botonRed")
        self.gridLayout_3.addWidget(self.botonRed, 2, 0, 1, 2)
        self.opciones.addItem(self.opcionesRed, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.opciones.setCurrentIndex(2)
        self.opciones.layout().setSpacing(6)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "EQUIPO 5"))
        self.botonMostrarTodos.setText(_translate("MainWindow", "Mostrar Todos"))
        self.botonAbrir.setText(_translate("MainWindow", "Abrir"))
        self.botonGuardar.setText(_translate("MainWindow", "Guardar"))
        self.botonFiltrar.setText(_translate("MainWindow", "Filtrar"))
        self.label_4.setText(_translate("MainWindow", "Idioma:"))
        self.label_3.setText(_translate("MainWindow", "Sentimiento"))
        self.label_2.setText(_translate("MainWindow", "Texto:"))
        self.opciones.setItemText(self.opciones.indexOf(self.opcionesFiltrar), _translate("MainWindow", "Opciones de filtrado"))
        self.botonNube.setText(_translate("MainWindow", "Crear nube de palabras"))
        self.botonHistograma.setText(_translate("MainWindow", "Crear histograma"))
        self.opciones.setItemText(self.opciones.indexOf(self.opcionesFrecuencia), _translate("MainWindow", "Opciones de frecuencia de palabras"))
        self.botonEntrenar.setText(_translate("MainWindow", "Entrenar red neuronal"))
        self.label_5.setText(_translate("MainWindow", "Preguntar a la red neuronal"))
        self.botonRed.setText(_translate("MainWindow", "Preguntar a la red neuronal"))
        self.opciones.setItemText(self.opciones.indexOf(self.opcionesRed), _translate("MainWindow", "Opciones de red neuronal"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
