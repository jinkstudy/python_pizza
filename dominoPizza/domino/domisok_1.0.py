# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dominsok_1.0.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


#from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5.QtCore, PyQt5.QtGui, PyQt5.QtWidgets
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(984, 842)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = PyQt5.QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = PyQt5.QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(PyQt5.QtCore.QRect(310, 80, 671, 601))
        font = PyQt5.QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(PyQt5.QtGui.QCursor(PyQt5.QtCore.Qt.PointingHandCursor))
        self.tabWidget.setMouseTracking(True)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tabWidget.setTabPosition(PyQt5.QtWidgets.QTabWidget.East)
        self.tabWidget.setTabShape(PyQt5.QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setObjectName("tabWidget")
        self.pizzaTab = PyQt5.QtWidgets.QWidget()
        self.pizzaTab.setObjectName("pizzaTab")
        for i in range(0,3):
            for j in range(0,3):
                # pizzaName
                self.pizzaName = PyQt5.QtWidgets.QLabel(self.pizzaTab)
                self.pizzaName.setGeometry(PyQt5.QtCore.QRect(181*i+10, 230*j+10, 181, 31))
                sizePolicy = PyQt5.QtWidgets.QSizePolicy(PyQt5.QtWidgets.QSizePolicy.Fixed, PyQt5.QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.pizzaName.sizePolicy().hasHeightForWidth())
                self.pizzaName.setSizePolicy(sizePolicy)
                font = PyQt5.QtGui.QFont()
                font.setFamily("KoPubWorldDotum")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)

                self.pizzaName.setFont(font)
                self.pizzaName.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.pizzaName.setObjectName("pizzaName")
                # pizzaImg
                self.pizzaImg = PyQt5.QtWidgets.QPushButton(self.pizzaTab)
                self.pizzaImg.setGeometry(PyQt5.QtCore.QRect(181*i+10, 230*j+50, 181, 171))
                sizePolicy = PyQt5.QtWidgets.QSizePolicy(PyQt5.QtWidgets.QSizePolicy.Fixed, PyQt5.QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(1)
                sizePolicy.setVerticalStretch(1)
                sizePolicy.setHeightForWidth(self.pizzaImg.sizePolicy().hasHeightForWidth())
                self.pizzaImg.setSizePolicy(sizePolicy)
                self.pizzaImg.setMouseTracking(True)
                self.pizzaImg.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.pizzaImg.setObjectName("pizzaImg")
                self.pizzaPrice = PyQt5.QtWidgets.QLabel(self.pizzaTab)

                # pizzaPrice
                self.pizzaPrice.setGeometry(PyQt5.QtCore.QRect(181*i+10, 230*j+230, 181, 31))
                sizePolicy = PyQt5.QtWidgets.QSizePolicy(PyQt5.QtWidgets.QSizePolicy.Fixed, PyQt5.QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.pizzaPrice.sizePolicy().hasHeightForWidth())
                self.pizzaPrice.setSizePolicy(sizePolicy)
                font = PyQt5.QtGui.QFont()
                font.setFamily("KoPubWorldDotum")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.pizzaPrice.setFont(font)
                self.pizzaPrice.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.pizzaPrice.setObjectName("pizzaPrice")
                self.tabWidget.addTab(self.pizzaTab, "")
        self.sideTab = PyQt5.QtWidgets.QWidget()
        self.sideTab.setObjectName("sideTab")
        self.tabWidget.addTab(self.sideTab, "")
        self.beverageTab = PyQt5.QtWidgets.QWidget()
        self.beverageTab.setObjectName("beverageTab")
        self.tabWidget.addTab(self.beverageTab, "")
        self.topFrame = PyQt5.QtWidgets.QFrame(self.centralwidget)
        self.topFrame.setGeometry(PyQt5.QtCore.QRect(10, 0, 971, 81))
        self.topFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.topFrame.setFrameShape(PyQt5.QtWidgets.QFrame.StyledPanel)
        self.topFrame.setFrameShadow(PyQt5.QtWidgets.QFrame.Raised)
        self.topFrame.setObjectName("topFrame")
        self.menuLabel = PyQt5.QtWidgets.QLabel(self.topFrame)
        self.menuLabel.setGeometry(PyQt5.QtCore.QRect(460, 30, 351, 51))
        font = PyQt5.QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.menuLabel.setFont(font)
        self.menuLabel.setTextFormat(PyQt5.QtCore.Qt.AutoText)
        self.menuLabel.setObjectName("menuLabel")
        self.graphBt = PyQt5.QtWidgets.QPushButton(self.topFrame)
        self.graphBt.setGeometry(PyQt5.QtCore.QRect(910, 40, 31, 31))
        font = PyQt5.QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.graphBt.setFont(font)
        self.graphBt.setCursor(PyQt5.QtGui.QCursor(PyQt5.QtCore.Qt.PointingHandCursor))
        self.graphBt.setAutoFillBackground(False)
        self.graphBt.setText("")
        icon = PyQt5.QtGui.QIcon()
        icon.addPixmap(PyQt5.QtGui.QPixmap("C:/Users/Playdata/Desktop/graphico.png"), PyQt5.QtGui.QIcon.Normal, PyQt5.QtGui.QIcon.Off)
        self.graphBt.setIcon(icon)
        self.graphBt.setAutoDefault(False)
        self.graphBt.setDefault(False)
        self.graphBt.setFlat(False)
        self.graphBt.setObjectName("graphBt")
        self.logoBt = PyQt5.QtWidgets.QPushButton(self.topFrame)
        self.logoBt.setGeometry(PyQt5.QtCore.QRect(10, 0, 271, 81))
        self.logoBt.setLayoutDirection(PyQt5.QtCore.Qt.LeftToRight)
        self.logoBt.setAutoFillBackground(False)
        self.logoBt.setText("")
        icon1 = PyQt5.QtGui.QIcon()
        icon1.addPixmap(PyQt5.QtGui.QPixmap("../Py_Workspace/dominsuk/pizza/logo1.PNG"), PyQt5.QtGui.QIcon.Normal, PyQt5.QtGui.QIcon.Off)
        self.logoBt.setIcon(icon1)
        self.logoBt.setIconSize(PyQt5.QtCore.QSize(250, 300))
        self.logoBt.setAutoDefault(True)
        self.logoBt.setFlat(True)
        self.logoBt.setObjectName("logoBt")
        self.checkFrame = PyQt5.QtWidgets.QFrame(self.centralwidget)
        self.checkFrame.setGeometry(PyQt5.QtCore.QRect(10, 80, 291, 601))
        self.checkFrame.setFrameShape(PyQt5.QtWidgets.QFrame.StyledPanel)
        self.checkFrame.setFrameShadow(PyQt5.QtWidgets.QFrame.Raised)
        self.checkFrame.setObjectName("checkFrame")
        self.label = PyQt5.QtWidgets.QLabel(self.checkFrame)
        self.label.setGeometry(PyQt5.QtCore.QRect(0, 10, 291, 51))
        font = PyQt5.QtGui.QFont()
        font.setFamily("KoPubWorldDotum")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.label.setFrameShape(PyQt5.QtWidgets.QFrame.StyledPanel)
        self.label.setObjectName("label")
        self.label_2 = PyQt5.QtWidgets.QLabel(self.checkFrame)
        self.label_2.setGeometry(PyQt5.QtCore.QRect(0, 350, 291, 51))
        font = PyQt5.QtGui.QFont()
        font.setFamily("KoPubWorldDotum")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.label_2.setFrameShape(PyQt5.QtWidgets.QFrame.StyledPanel)
        self.label_2.setObjectName("label_2")
        self.checkBt = PyQt5.QtWidgets.QPushButton(self.checkFrame)
        self.checkBt.setGeometry(PyQt5.QtCore.QRect(10, 470, 271, 61))
        font = PyQt5.QtGui.QFont()
        font.setFamily("KoPubWorld돋움체 Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkBt.setFont(font)
        self.checkBt.setCursor(PyQt5.QtGui.QCursor(PyQt5.QtCore.Qt.PointingHandCursor))
        self.checkBt.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.checkBt.setCheckable(False)
        self.checkBt.setObjectName("checkBt")
        self.cancelBt = PyQt5.QtWidgets.QPushButton(self.checkFrame)
        self.cancelBt.setGeometry(PyQt5.QtCore.QRect(10, 540, 271, 61))
        font = PyQt5.QtGui.QFont()
        font.setFamily("KoPubWorld돋움체 Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.cancelBt.setFont(font)
        self.cancelBt.setCursor(PyQt5.QtGui.QCursor(PyQt5.QtCore.Qt.PointingHandCursor))
        self.cancelBt.setStyleSheet("font: 75 12pt \"KoPubWorld돋움체 Bold\";\n"
"background-color: rgb(255, 85, 127);")
        self.cancelBt.setCheckable(False)
        self.cancelBt.setObjectName("cancelBt")
        self.totalLcd = PyQt5.QtWidgets.QLCDNumber(self.checkFrame)
        self.totalLcd.setGeometry(PyQt5.QtCore.QRect(10, 410, 241, 51))
        self.totalLcd.setObjectName("totalLcd")
        self.label_3 = PyQt5.QtWidgets.QLabel(self.checkFrame)
        self.label_3.setGeometry(PyQt5.QtCore.QRect(260, 430, 21, 31))
        font = PyQt5.QtGui.QFont()
        font.setFamily("KoPubWorldDotum")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.checkTable = PyQt5.QtWidgets.QTableWidget(self.checkFrame)
        self.checkTable.setGeometry(PyQt5.QtCore.QRect(0, 60, 291, 291))
        sizePolicy = PyQt5.QtWidgets.QSizePolicy(PyQt5.QtWidgets.QSizePolicy.Preferred, PyQt5.QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkTable.sizePolicy().hasHeightForWidth())
        self.checkTable.setSizePolicy(sizePolicy)
        self.checkTable.setObjectName("checkTable")
        self.checkTable.setColumnCount(2)
        self.checkTable.setRowCount(0)
        item = PyQt5.QtWidgets.QTableWidgetItem()
        self.checkTable.setHorizontalHeaderItem(0, item)
        item = PyQt5.QtWidgets.QTableWidgetItem()
        self.checkTable.setHorizontalHeaderItem(1, item)
        self.bottomFrame = PyQt5.QtWidgets.QFrame(self.centralwidget)
        self.bottomFrame.setGeometry(PyQt5.QtCore.QRect(10, 690, 951, 111))
        self.bottomFrame.setFrameShape(PyQt5.QtWidgets.QFrame.StyledPanel)
        self.bottomFrame.setFrameShadow(PyQt5.QtWidgets.QFrame.Raised)
        self.bottomFrame.setObjectName("bottomFrame")
        self.bannerLabel = PyQt5.QtWidgets.QLabel(self.bottomFrame)
        self.bannerLabel.setGeometry(PyQt5.QtCore.QRect(3, 0, 951, 111))
        self.bannerLabel.setText("")
        self.bannerLabel.setPixmap(PyQt5.QtGui.QPixmap("../Py_Workspace/dominsuk/pizza/pizza.png"))
        self.bannerLabel.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
        self.bannerLabel.setObjectName("bannerLabel")
        self.bottomFrame.raise_()
        self.tabWidget.raise_()
        self.topFrame.raise_()
        self.checkFrame.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = PyQt5.QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(PyQt5.QtCore.QRect(0, 0, 984, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        PyQt5.QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = PyQt5.QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pizzaName.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">pizzaName</p></body></html>"))
        self.pizzaImg.setText(_translate("MainWindow", "pizzaImg"))
        self.pizzaPrice.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">pizzaPrice</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pizzaTab), _translate("MainWindow", "PIZZA"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sideTab), _translate("MainWindow", "SIDE"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.beverageTab), _translate("MainWindow", "BERVERAGE"))
        self.menuLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">PIZZA</p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">총 주문 내역</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">TOTAL</span></p></body></html>"))
        self.checkBt.setText(_translate("MainWindow", "결 제 하 기"))
        self.cancelBt.setText(_translate("MainWindow", "취 소 하 기"))
        self.label_3.setText(_translate("MainWindow", "원"))
        item = self.checkTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "메뉴"))
        item = self.checkTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "가격"))


if __name__ == "__main__":
    import sys
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    MainWindow = PyQt5.QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

