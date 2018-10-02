# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import genKeys
import spartan
import os
import time

class Ui_Dialog(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = menu()
        self.ui.setupUi(self.window)
        Dialog.hide()
        self.window.show()

    def bypass(self):
        self.username1 = self.lineEdit_2.text()
        self.password1 = self.lineEdit.text()
        u = "spartan"
        p = "admin"

        if(self.username1 == u and self.password1 == p):
            print("User Found !")
            self.openWindow()
                #display warning for invalid username and password
             
        else:
            print("User Not Found !")

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(913, 549)
        Dialog.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(190, 370, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(0, 193, 150);\n"
"border: 2px solid rgb(0, 193, 150);\n"
"border-color: rgb(0, 193, 150);\n"
"padding: 10px;\n"
"border-radius: 25px;\n"
"")
        self.pushButton.setObjectName("pushButton")

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(70, 300, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: rgb(0, 193, 150);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 190, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("color: rgb(0, 193, 150);\n"
"")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(200, 140, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 193, 150);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(200, 250, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 193, 150);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(510, 80, 351, 331))
        self.label_3.setStyleSheet("image: url(SpartanIDS_official_logo.png);\n"
"height: 100px;\n"
"width: 500px;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(600, 400, 171, 51))
        self.label_4.setStyleSheet("image: url(SpartanIDS Text.png);\n"
"height: 100px;\n"
"width: 500px;")
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 430, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(0, 193, 150);\n"
"border: 2px solid rgb(35, 35, 35);\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton.clicked.connect(self.bypass)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Sign In"))
        self.label.setText(_translate("Dialog", "Username"))
        self.label_2.setText(_translate("Dialog", "Password"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_2.setText(_translate("Dialog", "Forgot Password ?"))

class menu(object):
    def key(self):
        genKeys.main()
    def base(self):
        os.system('python3 genBase.py')
        time.sleep(3)
        print("Base genrated")
    def spartan(self):
        os.system('python3 spartan.py')
        time.sleep(3)
        
    def setupUi(self, menu_sc):
        menu_sc.setObjectName("menu_sc")
        menu_sc.resize(912, 547)
        menu_sc.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.pushButton = QtWidgets.QPushButton(menu_sc)
        self.pushButton.setGeometry(QtCore.QRect(120, 110, 291, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(0, 193, 150);\n"
"border: 2px solid rgb(0, 193, 150);\n"
"border-color: rgb(0, 193, 150);\n"
"padding: 10px;\n"
"border-radius: 25px;\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.key)
        self.pushButton_2 = QtWidgets.QPushButton(menu_sc)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 210, 291, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(0, 193, 150);\n"
"border: 2px solid rgb(0, 193, 150);\n"
"border-color: rgb(0, 193, 150);\n"
"padding: 10px;\n"
"border-radius: 25px;\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.base)
        self.pushButton_3 = QtWidgets.QPushButton(menu_sc)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 310, 291, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("color: rgb(0, 193, 150);\n"
"border: 2px solid rgb(0, 193, 150);\n"
"border-color: rgb(0, 193, 150);\n"
"padding: 10px;\n"
"border-radius: 25px;\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.spartan)
        self.pushButton_4 = QtWidgets.QPushButton(menu_sc)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 470, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("color: rgb(0, 193, 150);\n"
"border: 2px solid rgb(0, 193, 150);\n"
"border-color: rgb(0, 193, 150);\n"
"padding: 10px;\n"
"border-radius: 25px;\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(menu_sc)
        self.pushButton_5.setGeometry(QtCore.QRect(750, 470, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("color: rgb(0, 193, 150);\n"
"border: 2px solid rgb(0, 193, 150);\n"
"border-color: rgb(0, 193, 150);\n"
"padding: 10px;\n"
"border-radius: 25px;\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_2 = QtWidgets.QLabel(menu_sc)
        self.label_2.setGeometry(QtCore.QRect(590, 380, 171, 71))
        self.label_2.setStyleSheet("image: url(SpartanIDS Text.png);\n"
"height: 100px;\n"
"width: 500px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(menu_sc)
        self.label.setGeometry(QtCore.QRect(490, 70, 361, 331))
        self.label.setStyleSheet("image: url(SpartanIDS_official_logo.png);\n"
"height: 100px;\n"
"width: 500px;")
        self.label.setObjectName("label")

        self.retranslateUi(menu_sc)
        QtCore.QMetaObject.connectSlotsByName(menu_sc)

    def retranslateUi(self, menu_sc):
        _translate = QtCore.QCoreApplication.translate
        menu_sc.setWindowTitle(_translate("menu_sc", "menu_sc"))
        self.pushButton.setText(_translate("menu_sc", "Generate Key"))
        self.pushButton_2.setText(_translate("menu_sc", "Generate Base"))
        self.pushButton_3.setText(_translate("menu_sc", "Check For Intrusion"))
        self.pushButton_4.setText(_translate("menu_sc", "Help"))
        self.pushButton_5.setText(_translate("menu_sc", "Exit"))
        self.label.setText(_translate("menu_sc", "<html><head/><body><p><br/></p></body></html>"))

        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

    app = QtWidgets.QApplication(sys.argv)
    menu = QtWidgets.QDialog()
    ui = menu()
    ui.setupUi(menu_sc)
    sys.exit(app.exec_())
