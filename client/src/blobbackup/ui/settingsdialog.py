# Form implementation generated from reading ui file 'src/blobbackup/ui/settingsdialog.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.resize(500, 350)
        SettingsDialog.setMinimumSize(QtCore.QSize(500, 350))
        self.verticalLayout = QtWidgets.QVBoxLayout(SettingsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(SettingsDialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.computer_name_line_edit = QtWidgets.QLineEdit(self.tab)
        self.computer_name_line_edit.setObjectName("computer_name_line_edit")
        self.verticalLayout_2.addWidget(self.computer_name_line_edit)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.backup_schedule_combo_box = QtWidgets.QComboBox(self.tab)
        self.backup_schedule_combo_box.setObjectName("backup_schedule_combo_box")
        self.backup_schedule_combo_box.addItem("")
        self.backup_schedule_combo_box.addItem("")
        self.verticalLayout_2.addWidget(self.backup_schedule_combo_box)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.max_upload_kibs_spin_box = QtWidgets.QSpinBox(self.tab)
        self.max_upload_kibs_spin_box.setMaximum(2147483647)
        self.max_upload_kibs_spin_box.setObjectName("max_upload_kibs_spin_box")
        self.verticalLayout_2.addWidget(self.max_upload_kibs_spin_box)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.inclusions_list_widget = QtWidgets.QListWidget(self.tab_2)
        self.inclusions_list_widget.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.inclusions_list_widget.setObjectName("inclusions_list_widget")
        item = QtWidgets.QListWidgetItem()
        self.inclusions_list_widget.addItem(item)
        self.horizontalLayout_2.addWidget(self.inclusions_list_widget)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.inclusions_add_button = QtWidgets.QPushButton(self.tab_2)
        self.inclusions_add_button.setObjectName("inclusions_add_button")
        self.verticalLayout_3.addWidget(self.inclusions_add_button)
        self.inclusions_remove_button = QtWidgets.QPushButton(self.tab_2)
        self.inclusions_remove_button.setObjectName("inclusions_remove_button")
        self.verticalLayout_3.addWidget(self.inclusions_remove_button)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.exclusions_list_widget = QtWidgets.QListWidget(self.tab_3)
        self.exclusions_list_widget.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.exclusions_list_widget.setObjectName("exclusions_list_widget")
        item = QtWidgets.QListWidgetItem()
        self.exclusions_list_widget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.exclusions_list_widget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.exclusions_list_widget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.exclusions_list_widget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.exclusions_list_widget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.exclusions_list_widget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.exclusions_list_widget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.exclusions_list_widget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.exclusions_list_widget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.exclusions_list_widget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.exclusions_list_widget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.exclusions_list_widget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.exclusions_list_widget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.exclusions_list_widget.addItem(item)
        self.horizontalLayout_3.addWidget(self.exclusions_list_widget)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.exclusions_add_button = QtWidgets.QPushButton(self.tab_3)
        self.exclusions_add_button.setObjectName("exclusions_add_button")
        self.verticalLayout_4.addWidget(self.exclusions_add_button)
        self.exclusions_remove_button = QtWidgets.QPushButton(self.tab_3)
        self.exclusions_remove_button.setObjectName("exclusions_remove_button")
        self.verticalLayout_4.addWidget(self.exclusions_remove_button)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.save_button = QtWidgets.QPushButton(SettingsDialog)
        self.save_button.setObjectName("save_button")
        self.horizontalLayout.addWidget(self.save_button)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(SettingsDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        SettingsDialog.setWindowTitle(_translate("SettingsDialog", "Blobbackup Settings"))
        self.label.setText(_translate("SettingsDialog", "Computer Name"))
        self.computer_name_line_edit.setText(_translate("SettingsDialog", "Bimbas-MacBook-Pro.local "))
        self.label_2.setText(_translate("SettingsDialog", "Backup Schedule"))
        self.backup_schedule_combo_box.setItemText(0, _translate("SettingsDialog", "Automatic"))
        self.backup_schedule_combo_box.setItemText(1, _translate("SettingsDialog", "Manual"))
        self.label_3.setText(_translate("SettingsDialog", "Max Upload KiB/s (0 = Unlimited)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("SettingsDialog", "General"))
        __sortingEnabled = self.inclusions_list_widget.isSortingEnabled()
        self.inclusions_list_widget.setSortingEnabled(False)
        item = self.inclusions_list_widget.item(0)
        item.setText(_translate("SettingsDialog", "/"))
        self.inclusions_list_widget.setSortingEnabled(__sortingEnabled)
        self.inclusions_add_button.setText(_translate("SettingsDialog", "Add Folder"))
        self.inclusions_remove_button.setText(_translate("SettingsDialog", "Remove"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("SettingsDialog", "Inclusions"))
        __sortingEnabled = self.exclusions_list_widget.isSortingEnabled()
        self.exclusions_list_widget.setSortingEnabled(False)
        item = self.exclusions_list_widget.item(0)
        item.setText(_translate("SettingsDialog", "/Applications"))
        item = self.exclusions_list_widget.item(1)
        item.setText(_translate("SettingsDialog", "/Library"))
        item = self.exclusions_list_widget.item(2)
        item.setText(_translate("SettingsDialog", "/Private"))
        item = self.exclusions_list_widget.item(3)
        item.setText(_translate("SettingsDialog", "/System"))
        item = self.exclusions_list_widget.item(4)
        item.setText(_translate("SettingsDialog", "/bin"))
        item = self.exclusions_list_widget.item(5)
        item.setText(_translate("SettingsDialog", "/dev"))
        item = self.exclusions_list_widget.item(6)
        item.setText(_translate("SettingsDialog", "/etc"))
        item = self.exclusions_list_widget.item(7)
        item.setText(_translate("SettingsDialog", "/net"))
        item = self.exclusions_list_widget.item(8)
        item.setText(_translate("SettingsDialog", "/sbin"))
        item = self.exclusions_list_widget.item(9)
        item.setText(_translate("SettingsDialog", "/usr"))
        item = self.exclusions_list_widget.item(10)
        item.setText(_translate("SettingsDialog", "/home"))
        item = self.exclusions_list_widget.item(11)
        item.setText(_translate("SettingsDialog", "*.vmc"))
        item = self.exclusions_list_widget.item(12)
        item.setText(_translate("SettingsDialog", "*.vhd"))
        item = self.exclusions_list_widget.item(13)
        item.setText(_translate("SettingsDialog", "*.iso"))
        self.exclusions_list_widget.setSortingEnabled(__sortingEnabled)
        self.exclusions_add_button.setText(_translate("SettingsDialog", "Add"))
        self.exclusions_remove_button.setText(_translate("SettingsDialog", "Remove"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("SettingsDialog", "Exclusions"))
        self.save_button.setText(_translate("SettingsDialog", "Save"))
