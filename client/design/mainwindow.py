# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt6 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 350)
        MainWindow.setMinimumSize(QtCore.QSize(500, 350))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.logo_label = QtWidgets.QLabel(self.groupBox_3)
        self.logo_label.setText("")
        self.logo_label.setObjectName("logo_label")
        self.horizontalLayout_4.addWidget(self.logo_label)
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.email_label = QtWidgets.QLabel(self.groupBox_3)
        self.email_label.setObjectName("email_label")
        self.horizontalLayout_4.addWidget(self.email_label)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.computer_label = QtWidgets.QLabel(self.groupBox_2)
        self.computer_label.setText("")
        self.computer_label.setObjectName("computer_label")
        self.horizontalLayout_3.addWidget(self.computer_label)
        self.arrow_label = QtWidgets.QLabel(self.groupBox_2)
        self.arrow_label.setMinimumSize(QtCore.QSize(64, 0))
        self.arrow_label.setText("")
        self.arrow_label.setAlignment(QtCore.Qt.AlignCenter)
        self.arrow_label.setObjectName("arrow_label")
        self.horizontalLayout_3.addWidget(self.arrow_label)
        self.cloud_label = QtWidgets.QLabel(self.groupBox_2)
        self.cloud_label.setMinimumSize(QtCore.QSize(64, 0))
        self.cloud_label.setText("")
        self.cloud_label.setObjectName("cloud_label")
        self.horizontalLayout_3.addWidget(self.cloud_label)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3)
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_9.addWidget(self.label_4)
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_9.addWidget(self.label_8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem5)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_3.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_4.addWidget(self.pushButton_3)
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setTextFormat(QtCore.Qt.RichText)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setTextFormat(QtCore.Qt.RichText)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem6)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout.addWidget(self.groupBox_4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Blobbackup Control Panel"))
        self.label_2.setText(_translate("MainWindow", "Blobbackup"))
        self.email_label.setText(_translate("MainWindow", "Account: bimba@email.com"))
        self.label.setText(_translate("MainWindow", "You are backed up as of 5:30 pm on Jan 21, 2021"))
        self.pushButton.setText(_translate("MainWindow", "Backup Now"))
        self.pushButton_2.setText(_translate("MainWindow", "Restore Files"))
        self.label_3.setText(_translate("MainWindow", "Selected for Backup: "))
        self.label_7.setText(_translate("MainWindow", "246 GB "))
        self.label_4.setText(_translate("MainWindow", "Backup Schedule:"))
        self.label_8.setText(_translate("MainWindow", "Automatic"))
        self.label_5.setText(_translate("MainWindow", "Current Status:"))
        self.label_9.setText(_translate("MainWindow", "favorite-cat.jpg"))
        self.pushButton_3.setText(_translate("MainWindow", "Settings"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" text-decoration: underline; color:#0000ff;\">Data Privacy</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" text-decoration: underline; color:#0000ff;\">Contact Support</span></p></body></html>"))


class MainWindow(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        pixmap = QtGui.QPixmap("img/logo.png")
        pixmap = pixmap.scaled(20, 20)
        self.logo_label.setPixmap(pixmap)

        pixmap = QtGui.QPixmap("img/computer.png")
        pixmap = pixmap.scaled(32, 32)
        self.computer_label.setPixmap(pixmap)

        pixmap = QtGui.QPixmap("img/arrow.png")
        pixmap = pixmap.scaled(20, 20)
        self.arrow_label.setPixmap(pixmap)

        pixmap = QtGui.QPixmap("img/cloud.png")
        pixmap = pixmap.scaled(32, 32)
        self.cloud_label.setPixmap(pixmap)

app = QtWidgets.QApplication([])
app.setStyle("Fusion")
window = MainWindow()
window.show()
app.exec()