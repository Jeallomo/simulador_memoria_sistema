import sys
from PyQt5.QtGui import QFont, QPixmap, QIcon, QMovie
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QBoxLayout, QVBoxLayout, QWidget,
                             QGroupBox, QLabel)

from EstaticaFija import EstaticaFija, tableWidget2
from EstaticaVariable import EstaticaVariable, tableWidget1
from DinamicaSinCompactacion import DinamicaSinCompactacion, tableWidget3
from DinamicaCompactacion import DinamicaCompactacion, tableWidget4

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(300, 320)
        QMainWindow.setWindowFlags(self,Qt.MSWindowsFixedSizeDialogHint|Qt.WindowCloseButtonHint)
        self.setWindowTitle("SIMULADOR")
        self.setStyleSheet("QGroupBox {background:rgba(245, 246, 250,.95)}")
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        
        self.VentanaFija = EstaticaFija()
        self.tablaVentanaFija = tableWidget2()
        
        self.VentanaVaraible = EstaticaVariable()
        self.tablaVentanaVaraible = tableWidget1()
        
        self.VentanaDsinCompactacion = DinamicaSinCompactacion()
        self.tablaVentanaDSinCompactacion = tableWidget3()
        
        self.VentanaDCompactacion= DinamicaCompactacion()
        self.tablaVentanaDCompactacion = tableWidget4()
        
        self.group = QGroupBox(self.centralWidget)
        self.gifLabel = QLabel(self.group)
        self.gifLabel.setGeometry(QRect(-200,20,500,600))
        
        font = QFont()
        font.setPointSize(10)
        self.btnEstaticaFija = QPushButton("ESTATICA FIJA",self.group)
        self.btnEstaticaFija.setGeometry(QRect(45,60,200,35))
        self.btnEstaticaFija.setFont(font)
        self.btnEstaticaVariable = QPushButton("ESTATICA VARIABLE",self.group)
        self.btnEstaticaVariable.setGeometry(QRect(45,110,200,35))
        self.btnEstaticaVariable.setFont(font)
        self.btnDinamicaSinCompactacion = QPushButton("DINAMICA SIN COMPACTACION",self.group)
        self.btnDinamicaSinCompactacion.setGeometry(QRect(45,160,200,35))
        self.btnDinamicaSinCompactacion.setFont(font)
        self.btnDinamicaCompactacion = QPushButton("DINAMICA CON COMPACTACION",self.group)
        self.btnDinamicaCompactacion.setGeometry(QRect(45,210,200,35))
        self.btnDinamicaCompactacion.setFont(font)
        Ventanal =QVBoxLayout()
        Ventanal.addWidget(self.group)
        self.centralWidget.setLayout(Ventanal)
        
        self.VentanaFija.btnRegresar.clicked.connect(self.regresarInicio)
        self.VentanaVaraible.btnRegresar.clicked.connect(self.regresarInicio)
        self.VentanaDsinCompactacion.btnRegresar.clicked.connect(self.regresarInicio)
        self.VentanaDCompactacion.btnRegresar.clicked.connect(self.regresarInicio)
        
        self.btnEstaticaFija.clicked.connect(self.MostrarFija)
        self.btnEstaticaVariable.clicked.connect(self.MostrarVariable)
        self.btnDinamicaSinCompactacion.clicked.connect(self.MostrarDsinCompactacion)
        self.btnDinamicaCompactacion.clicked.connect(self.MostarDCompactacion)
        
     
    def regresarInicio(self):
        self.VentanaFija.hide()
        self.tablaVentanaFija.hide()
        
        self.VentanaVaraible.hide()
        self.tablaVentanaVaraible.hide()
        
        self.VentanaDsinCompactacion.hide()
        self.tablaVentanaDSinCompactacion.hide()
        
        self.VentanaDCompactacion.hide()
        self.tablaVentanaDCompactacion.hide()
        self.show()

    def MostrarFija(self):
        self.hide()
        self.VentanaFija.show()
        self.tablaVentanaVaraible.show()
    
    def MostrarVariable(self):
        self.hide()
        self.VentanaVaraible.show()
        self.tablaVentanaVaraible.show()
        
        
    def MostrarDsinCompactacion(self):
        self.hide()
        self.VentanaDsinCompactacion.show()
        self.tablaVentanaDSinCompactacion.show()
    
    def MostarDCompactacion(self):
        self.hide()
        self.VentanaDCompactacion.show()
        self.tablaVentanaDCompactacion.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow= MainWindow()
    mainWindow.show()
    app.exec_()