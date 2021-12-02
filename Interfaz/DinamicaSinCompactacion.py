import sys
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import (QWidget, QApplication, QDialog, QMenu, QAction, QActionGroup, 
                             QMessageBox, QMainWindow, QPushButton, QLabel, QGroupBox,
                            QVBoxLayout, QHBoxLayout,QTableWidget,QTableWidgetItem,
                            QAbstractItemView, QGridLayout, QComboBox, QFrame, QLineEdit
                            )

class DinamicaSinCompactacion(QMainWindow):
    def __init__(self,sql=None):
        QMainWindow.__init__(self)
        QMainWindow.setWindowFlags(self,Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowIcon(QIcon(""))
        self.setWindowTitle("Simulador de memoria")
        self.resize(650,350)
        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.setStyleSheet("QGroupBox {background:rgba(245, 246, 250,.95)}")

        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QRect(0, 0, 400, 370))
        self.label.setScaledContents(True)
        
        self.groupMainWindow()
        
    
    def groupMainWindow(self):
            
        self.etiqueta1 = QLabel("DINAMICA SIN COMPACTACION")
        self.groupControl = QGroupBox()
        
        self.groupControl = QGroupBox()
        self.etiqueta2 = QLabel("Metodo")
        self.seleccionarDivisionDeMemoria = QComboBox()
        self.seleccionarDivisionDeMemoria.addItem("MEJOR AJUSTE")
        self.seleccionarDivisionDeMemoria.addItem("PRIMER AJUSTE")
        self.seleccionarDivisionDeMemoria.addItem("PEOR AJUSTE")
        print(self.seleccionarDivisionDeMemoria.currentText())
        h1 = QHBoxLayout()
        h1.addWidget(self.etiqueta2)
        h1.addWidget(self.seleccionarDivisionDeMemoria)

        
        self.etiqueta4 = QLabel("Nombre")
        self.lineEdit1 = QLineEdit()
        self.lineEdit1.setPlaceholderText("Nombre del proceso")
        h2 = QHBoxLayout()
        h2.addWidget(self.etiqueta4)
        h2.addWidget(self.lineEdit1)

        self.etiqueta5 = QLabel("Tamaño")
        self.lineEdit2 = QLineEdit()
        self.lineEdit2.setPlaceholderText("Tamaño Codigo en Bytes")
        h3 = QHBoxLayout()
        h3.addWidget(self.etiqueta5)
        h3.addWidget(self.lineEdit2)
        
        self.etiqueta6 = QLabel("Tamaño")
        self.lineEdit3 = QLineEdit()
        self.lineEdit3.setPlaceholderText("Tamaño datos inicializados en Bytes")
        h4 = QHBoxLayout()
        h4.addWidget(self.etiqueta6)
        h4.addWidget(self.lineEdit3)
        
        self.etiqueta7 = QLabel("Tamaño")
        self.lineEdit4 = QLineEdit()
        self.lineEdit4.setPlaceholderText("Tamaño datos sin inicializar en Bytes")
        h5 = QHBoxLayout()
        h5.addWidget(self.etiqueta7)
        h5.addWidget(self.lineEdit4)

        self.ptCargar = QPushButton("Crear")
        h6 = QHBoxLayout()
        h6.addWidget(self.ptCargar)

        v1 = QVBoxLayout()
        v1.addWidget(self.etiqueta1)
        v1.addLayout(h1)
        v1.addLayout(h2)
        v1.addLayout(h3)
        v1.addLayout(h4)
        v1.addLayout(h5)
        v1.addLayout(h6)
        v1.addSpacing(170)
        self.groupControl.setLayout(v1)

        self.groupSimulator = QGroupBox()
        self.line=QFrame()            #marco hereda el espacio del QMainWindow
        self.line.setFrameShape(QFrame.VLine)           #forma linea en este caso
        self.line.setFrameShadow(QFrame.Raised)         #sombra

        self.tablaBitacora = QTableWidget()
        self.tablaBitacora.setColumnCount(1)    #Establecer numero de columna
        self.tablaBitacora.setMaximumWidth(150) #Establecer ancho maximo

        self.label = QLabel(self.groupControl)
        self.label.setGeometry(QRect(0,260,280,80))
        self.label.setScaledContents(True)
        self.btnRegresar = QPushButton("Regresar",self.groupControl)
        self.btnRegresar.setGeometry(QRect(5,325,90,25))

        nombrecolumnas=("16MB",)
        self.tablaBitacora.setHorizontalHeaderLabels(nombrecolumnas)#nombre de columna

        self.tablaBitacora.setAutoScroll(True)
        self.tablaBitacora.setAlternatingRowColors(True)
        self.tablaBitacora.verticalHeader().setDefaultSectionSize(20)       #alturas celda
        self.tablaBitacora.setColumnWidth(0,150)                            #anchura celda
        self.tablaBitacora.setRowHeight(0,10)
        self.tablaBitacora.setRowHeight(1,50)
        self.tablaBitacora.setRowHeight(2,90)

        self.tablaBitacora.setEditTriggers(QAbstractItemView.NoEditTriggers)#Desabilitar editar celdas
        self.tablaBitacora.setSortingEnabled(False)#desabilita el ordenamiento
        self.tablaBitacora.verticalHeader().setVisible(False)#ocultar header verticales

        v2  = QVBoxLayout()
        v2.addWidget(self.tablaBitacora)
        self.groupSimulator.setLayout(v2)

        self.grid = QGridLayout()
        self.grid.addWidget(self.groupControl,0,0,1,1)
        self.grid.addWidget(self.line,0,1,2,1)
        self.grid.addWidget(self.groupSimulator,0,2,1,4)

        self.centralwidget.setLayout(self.grid)

class tableWidget3(QDialog):
    def __init__(self, parent=None):
        super(tableWidget3, self).__init__(parent)
        
        self.setWindowTitle("LISTA DE PROCESOS")
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(740,348)
        
        self.initUI()
    
    def initUI(self):
        self.tabla = QTableWidget(self)
        self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla.setDragDropOverwriteMode(False)
        self.tabla.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabla.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabla.setTextElideMode(Qt.ElideRight)
        self.tabla.setWordWrap(False)
        self.tabla.setSortingEnabled(False)
        self.tabla.setColumnCount(4)
        self.tabla.setRowCount(0)
        self.tabla.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter)
        self.tabla.horizontalHeader().setHighlightSections(False)
        self.tabla.horizontalHeader().setStretchLastSection(True)
        self.tabla.verticalHeader().setVisible(False)
        self.tabla.setAlternatingRowColors(True)
        self.tabla.verticalHeader().setDefaultSectionSize(20)
        
        nombreColumnas = ("PID","Nombre","Tamaño","Estado")
        self.tabla.setHorizontalHeaderLabels(nombreColumnas)
        
        
        
        for indice, ancho in enumerate((80, 120, 120, 110, 150), start=0):
            self.tabla.setColumnWidth(indice, ancho)
        
        self.tabla.resize(700,240)
        self.tabla.move(20,56)
        
        botonMostrarDatos = QPushButton("Mostrar datos", self)
        botonMostrarDatos.setFixedWidth(140)
        botonMostrarDatos.move(20, 20)
        
        menu = QMenu()
        for indice, columna in enumerate(nombreColumnas, start=0):
            accion = QAction(columna, menu)
            accion.setCheckable(True)
            accion.setChecked(True)
            accion.setData(indice)
            
            menu.addAction(accion)
        
        
        botonEliminarFila = QPushButton("Eliminar Proceso", self)
        botonEliminarFila.setFixedWidth(100)
        botonEliminarFila.move(530, 20)
        
        botonEliminarFila.clicked.connect(self.eliminarFila)
        botonMostrarDatos.clicked.connect(self.datosTabla)
     
    def datosTabla(self):
        datos = [("1", "word", "1213", "Activo"),
                 ("2", "excel", "1213", "Listo"),
                 ("3", "asus", "8912", "Listo")]

        self.tabla.clearContents()

        row = 0
        for endian in datos:
            self.tabla.setRowCount(row + 1)
            
            idDato = QTableWidgetItem(endian[0])
            idDato.setTextAlignment(4)
            
            self.tabla.setItem(row, 0, idDato)
            self.tabla.setItem(row, 1, QTableWidgetItem(endian[1]))
            self.tabla.setItem(row, 2, QTableWidgetItem(endian[2]))
            self.tabla.setItem(row, 3, QTableWidgetItem(endian[3]))

            row += 1
       
    def eliminarFila(self):
        filaSeleccionada = self.tabla.selectedItems()
        if filaSeleccionada:
            fila = filaSeleccionada[0].row()
            self.tabla.removeRow(fila)

            self.tabla.clearSelection()
        else:
            QMessageBox.critical(self, "Eliminar fila", "Seleccione una fila.   ",
                                QMessageBox.Ok)            

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = DinamicaSinCompactacion()
    table = tableWidget3()
    main.show()
    table.show()
    app.exec_()