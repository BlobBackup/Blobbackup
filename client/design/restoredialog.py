# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'restoredialog.ui'
#
# Created by: PyQt6 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_RestoreDialog(object):
    def setupUi(self, RestoreDialog):
        RestoreDialog.setObjectName("RestoreDialog")
        RestoreDialog.resize(500, 350)
        RestoreDialog.setMinimumSize(QtCore.QSize(500, 350))
        self.verticalLayout = QtWidgets.QVBoxLayout(RestoreDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.snapshots_combo_box = QtWidgets.QComboBox(RestoreDialog)
        self.snapshots_combo_box.setObjectName("snapshots_combo_box")
        self.snapshots_combo_box.addItem("")
        self.verticalLayout.addWidget(self.snapshots_combo_box)
        self.snapshot_tree_widget = QtWidgets.QTreeWidget(RestoreDialog)
        self.snapshot_tree_widget.setHeaderHidden(True)
        self.snapshot_tree_widget.setObjectName("snapshot_tree_widget")
        self.snapshot_tree_widget.headerItem().setText(0, "1")
        self.verticalLayout.addWidget(self.snapshot_tree_widget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.restore_button = QtWidgets.QPushButton(RestoreDialog)
        self.restore_button.setObjectName("restore_button")
        self.horizontalLayout.addWidget(self.restore_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(RestoreDialog)
        QtCore.QMetaObject.connectSlotsByName(RestoreDialog)

    def retranslateUi(self, RestoreDialog):
        _translate = QtCore.QCoreApplication.translate
        RestoreDialog.setWindowTitle(_translate("RestoreDialog", "Restore Files - Blobbackup"))
        self.snapshots_combo_box.setItemText(0, _translate("RestoreDialog", "Jan 19 2022, 10:18:01 PM"))
        self.restore_button.setText(_translate("RestoreDialog", "Restore"))


class RestoreDialog(Ui_RestoreDialog, QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_RestoreDialog.__init__(self)
        self.setupUi(self)


app = QtWidgets.QApplication([])
app.setStyle("Fusion")
dialog = RestoreDialog()
dialog.exec()