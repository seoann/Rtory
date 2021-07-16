from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import *
import sys, os
import aesrsa, steganographyModule

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 703)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 90, 1021, 591))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.tab)
        self.verticalScrollBar.setGeometry(QtCore.QRect(1000, 0, 16, 561))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(80, 40, 121, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(90, 90, 111, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(120, 150, 91, 41))
        self.label_4.setObjectName("label_4")
        self.lineEdit_sf_enc = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_sf_enc.setGeometry(QtCore.QRect(230, 40, 481, 25))
        self.lineEdit_sf_enc.setObjectName("lineEdit_sf_enc")
        self.lineEdit_ir_enc = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_ir_enc.setGeometry(QtCore.QRect(230, 100, 481, 25))
        self.lineEdit_ir_enc.setObjectName("lineEdit_ir_enc")
        self.lineEdit_st_enc = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_st_enc.setGeometry(QtCore.QRect(230, 160, 481, 25))
        self.lineEdit_st_enc.setObjectName("lineEdit_st_enc")
        self.buttonBox_enc = QtWidgets.QDialogButtonBox(self.tab)
        self.buttonBox_enc.setGeometry(QtCore.QRect(730, 470, 233, 34))
        self.buttonBox_enc.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox_enc.setObjectName("buttonBox_enc")
        self.pushButton_sf_enc = QtWidgets.QPushButton(self.tab)
        self.pushButton_sf_enc.setGeometry(QtCore.QRect(730, 40, 112, 34))
        self.pushButton_sf_enc.setObjectName("pushButton_sf_enc")
        self.pushButton_ir_enc = QtWidgets.QPushButton(self.tab)
        self.pushButton_ir_enc.setGeometry(QtCore.QRect(730, 100, 112, 34))
        self.pushButton_ir_enc.setObjectName("pushButton_ir_enc")
        self.pushButton_st_enc = QtWidgets.QPushButton(self.tab)
        self.pushButton_st_enc.setGeometry(QtCore.QRect(730, 160, 112, 34))
        self.pushButton_st_enc.setObjectName("pushButton_st_enc")
        self.line_2 = QtWidgets.QFrame(self.tab)
        self.line_2.setGeometry(QtCore.QRect(0, 230, 1001, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(0, 10, 1001, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_im_enc = QtWidgets.QLabel(self.tab)
        self.label_im_enc.setGeometry(QtCore.QRect(230, 260, 481, 281))
        self.label_im_enc.setText("")
        self.label_im_enc.setObjectName("label_im_enc")
        self.label_im_enc.setAlignment(QtCore.Qt.AlignCenter)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalScrollBar_2 = QtWidgets.QScrollBar(self.tab_2)
        self.verticalScrollBar_2.setGeometry(QtCore.QRect(1000, 0, 16, 561))
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(90, 160, 161, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(70, 30, 181, 41))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(120, 80, 81, 61))
        self.label_10.setObjectName("label_10")
        self.lineEdit_hi_dec = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_hi_dec.setGeometry(QtCore.QRect(230, 40, 481, 25))
        self.lineEdit_hi_dec.setObjectName("lineEdit_hi_dec")
        self.lineEdit_st_dec = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_st_dec.setGeometry(QtCore.QRect(230, 100, 481, 25))
        self.lineEdit_st_dec.setObjectName("lineEdit_st_dec")
        self.lineEdit_ir_dec = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_ir_dec.setGeometry(QtCore.QRect(230, 160, 481, 25))
        self.lineEdit_ir_dec.setObjectName("lineEdit_ir_dec")
        self.buttonBox_dec = QtWidgets.QDialogButtonBox(self.tab_2)
        self.buttonBox_dec.setGeometry(QtCore.QRect(730, 460, 233, 34))
        self.buttonBox_dec.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox_dec.setObjectName("buttonBox_dec")
        self.pushButton_ir_dec = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_ir_dec.setGeometry(QtCore.QRect(730, 160, 112, 34))
        self.pushButton_ir_dec.setObjectName("pushButton_ir_dec")
        self.line_3 = QtWidgets.QFrame(self.tab_2)
        self.line_3.setGeometry(QtCore.QRect(0, 10, 1001, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.tab_2)
        self.line_4.setGeometry(QtCore.QRect(0, 230, 1001, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.pushButton_hi_dec = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_hi_dec.setGeometry(QtCore.QRect(730, 40, 112, 34))
        self.pushButton_hi_dec.setObjectName("pushButton_hi_dec")
        self.pushButton_st_dec = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_st_dec.setGeometry(QtCore.QRect(730, 100, 112, 34))
        self.pushButton_st_dec.setObjectName("pushButton_st_dec")
        self.label_im_dec = QtWidgets.QLabel(self.tab_2)
        self.label_im_dec.setGeometry(QtCore.QRect(230, 260, 481, 281))
        self.label_im_dec.setText("")
        self.label_im_dec.setObjectName("label_im_dec")
        self.label_im_dec.setAlignment(QtCore.Qt.AlignCenter)
        self.tabWidget.addTab(self.tab_2, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, -10, 761, 71))
        self.label.setObjectName("label")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(0, 60, 1021, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.pushButton_sf_enc.clicked.connect(self.getFile_sf)
        self.pushButton_ir_enc.clicked.connect(self.getFile_ir_enc)
        self.pushButton_st_enc.clicked.connect(self.getFile_st_enc)
        self.buttonBox_enc.accepted.connect(self.encryption)
        self.pushButton_hi_dec.clicked.connect(self.getFile_hi_dec)
        self.pushButton_ir_dec.clicked.connect(self.getFile_ir_dec)
        self.pushButton_st_dec.clicked.connect(self.getFile_st_dec)
        self.buttonBox_dec.accepted.connect(self.decryption)
        self.buttonBox_enc.rejected.connect(sys.exit)
        self.buttonBox_dec.rejected.connect(sys.exit)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Steganosaurus"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-family: Consolas; font-weight:600; color:#5500ff;\">Secret File</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-family:Consolas; font-weight:600; color:#5500ff;\">Image Root</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-family:Consolas; font-weight:600; color:#5500ff;\">Save To</span></p></body></html>"))
        self.pushButton_sf_enc.setText(_translate("MainWindow", "Browse"))
        self.pushButton_ir_enc.setText(_translate("MainWindow", "Browse"))
        self.pushButton_st_enc.setText(_translate("MainWindow", "Browse"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Encryption"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-family:Consolas; font-weight:600; color:#5500ff;\">Image Root</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-family:Consolas; font-weight:600; color:#5500ff;\">Hidden Image</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-family:Consolas; font-weight:600; color:#5500ff;\">Save To</span></p></body></html>"))
        self.pushButton_ir_dec.setText(_translate("MainWindow", "Browse"))
        self.pushButton_hi_dec.setText(_translate("MainWindow", "Browse"))
        self.pushButton_st_dec.setText(_translate("MainWindow", "Browse"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Decryption"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt; font-family:Consolas; font-weight:600; color:#aa55ff;\">STEGANOSAURUS</span></p></body></html>"))
        
        
    def getFile_sf( self ):
        self.lineEdit_sf_enc.setText(self.browserSlot())
    def getFile_st_enc( self ):
        self.lineEdit_st_enc.setText(self.directorySlot())
    def getFile_ir_enc( self ):
        self.lineEdit_ir_enc.setText(self.browserSlotImage())
    def getFile_hi_dec( self ):
        self.lineEdit_hi_dec.setText(self.browserSlotImage())
    def getFile_st_dec( self ):
        self.lineEdit_st_dec.setText(self.directorySlot())
    def getFile_ir_dec( self ):
        self.lineEdit_ir_dec.setText(self.browserSlotImage()) 
        
    def browserSlot( self ):
        options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
                        None,
                        "FILE BROWSER",
                        "",
                        "All Files (*)",
                        options=options)    
        return fileName
    def browserSlotImage( self ):
        options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
                        None,
                        "IMAGE BROWSER",
                        "",
                        "Image Files (*bmp)",
                        options=options)    
        return fileName 
    def directorySlot( self ):
        folderName = QtWidgets.QFileDialog.getExistingDirectory(
                        None,
                        "SELECT DIRECTORY",
                        "",
                        QtWidgets.QFileDialog.ShowDirsOnly)
        return folderName
    def refresh( self ):
        self.lineEdit_hi_dec.setText("")
        self.lineEdit_ir_dec.setText("")
        self.lineEdit_st_dec.setText("")
        self.lineEdit_ir_enc.setText("")
        self.lineEdit_sf_enc.setText("")
        self.lineEdit_st_enc.setText("")
  
    def encryption( self ):        
        try:
            saveTo = open(self.lineEdit_st_enc.text()+"/encryption.bmp","w")
            saveTo.close()
            aesrsa.aes_en( self.lineEdit_sf_enc.text(), 'C:\\Users\\user\\Desktop\\CS\\project\\pri1', 'C:\\Users\\user\\Desktop\\CS\\project\\pub2')
            steganographyModule.hideFile(self.lineEdit_ir_enc.text(), 'C:\\Users\\user\\Desktop\\CS\\project\\cryaes',self.lineEdit_st_enc.text()+"/encryption.bmp")
            image = QtGui.QPixmap(self.lineEdit_st_enc.text()+"/encryption.bmp")
            image = image.scaled(481, 281, QtCore.Qt.KeepAspectRatio,QtCore.Qt.FastTransformation)
            self.label_im_enc.setPixmap(QtGui.QPixmap(image))
            self.refresh()
            Message = QtWidgets.QMessageBox()
            Action = QtWidgets.QMessageBox.information(Message, "Result", "Decryption Successed",QtWidgets.QMessageBox.Ok)
            if Action == QtWidgets.QMessageBox.Ok:
                self.label_im_enc.clear()
            
        except:
            image = QtGui.QPixmap('C:\\Users\\user\\Desktop\\CS\\project\\nope')
            image = image.scaled(481, 281, QtCore.Qt.KeepAspectRatio,QtCore.Qt.FastTransformation)
            self.label_im_enc.setPixmap(QtGui.QPixmap(image))
            Message = QtWidgets.QMessageBox()
            Action = QtWidgets.QMessageBox.information(Message, "Error", "Check The Input",QtWidgets.QMessageBox.Ok)
            if Action == QtWidgets.QMessageBox.Ok:
                self.label_im_enc.clear()
            
    def decryption( self ):           
        try:
            saveTo = open(self.lineEdit_st_dec.text()+"/tmp","w")
            saveTo.close()
            steganographyModule.desFile(self.lineEdit_ir_dec.text(), self.lineEdit_hi_dec.text(), self.lineEdit_st_dec.text()+"/tmp")
            aesrsa.aes_de(self.lineEdit_st_dec.text()+"/tmp", 'C:\\Users\\user\\Desktop\\CS\\project\\pub1', 'C:\\Users\\user\\Desktop\\CS\\project\\pri2')
            os.remove(self.lineEdit_st_dec.text()+"/tmp")
            image = QtGui.QPixmap(self.lineEdit_hi_dec.text())
            image = image.scaled(481, 281, QtCore.Qt.KeepAspectRatio,QtCore.Qt.FastTransformation)
            self.label_im_dec.setPixmap(QtGui.QPixmap(image))
            self.refresh()
            Message = QtWidgets.QMessageBox()
            Action = QtWidgets.QMessageBox.information(Message, "Result", "Decryption Successed",QtWidgets.QMessageBox.Ok)
            if Action == QtWidgets.QMessageBox.Ok:
                self.label_im_dec.clear()
        except:
            image = QtGui.QPixmap('C:\\Users\\user\\Desktop\\CS\\project\\nope')
            image = image.scaled(481, 281, QtCore.Qt.KeepAspectRatio,QtCore.Qt.FastTransformation)
            self.label_im_dec.setPixmap(QtGui.QPixmap(image))
            Message = QtWidgets.QMessageBox()
            Action = QtWidgets.QMessageBox.information(Message, "Error", "Check The Input",QtWidgets.QMessageBox.Ok)
            if Action == QtWidgets.QMessageBox.Ok:
                self.label_im_dec.clear()
        
        
                  

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

