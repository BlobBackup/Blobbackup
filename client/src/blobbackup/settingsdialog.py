from PyQt6.QtWidgets import QDialog, QFileDialog, QInputDialog
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

from blobbackup.ui.settingsdialog import Ui_SettingsDialog
from blobbackup.config import config, save_config
from blobbackup.api import update_computer
from blobbackup.util import get_password_from_keyring, LOGO_PATH


class SettingDialog(QDialog, Ui_SettingsDialog):
    def __init__(self):
        QDialog.__init__(self)
        Ui_SettingsDialog.__init__(self)
        self.setupUi(self)

        self.setWindowIcon(QIcon(LOGO_PATH))

        self.populate_settings()

        self.inclusions_add_button.pressed.connect(self.inclusions_add)
        self.inclusions_remove_button.pressed.connect(self.inclusions_remove)
        self.exclusions_add_button.pressed.connect(self.exclusions_add)
        self.exclusions_remove_button.pressed.connect(self.exclusions_remove)
        self.save_button.pressed.connect(self.accept)

    def populate_settings(self):
        self.computer_name_line_edit.setText(config["general"]["computer_name"])
        self.backup_schedule_combo_box.setCurrentText(
            config["general"]["backup_schedule"]
        )
        self.inclusions_list_widget.clear()
        for path in config["inclusions"]["paths"].split(","):
            if path:
                self.inclusions_list_widget.addItem(path)
        self.exclusions_list_widget.clear()
        for path in config["exclusions"]["paths"].split(","):
            if path:
                self.exclusions_list_widget.addItem(path)

    def inclusions_add(self):
        path = QFileDialog.getExistingDirectory()
        if path and not self.inclusions_list_widget.findItems(path, Qt.MatchFlag.MatchExactly):
            self.inclusions_list_widget.addItem(path)

    def inclusions_remove(self):
        item = self.inclusions_list_widget.currentItem()
        if item:
            row = self.inclusions_list_widget.row(item)
            self.inclusions_list_widget.takeItem(row)

    def exclusions_add(self):
        exclusion, okay = QInputDialog.getText(self, "Add exclusion", "Path or pattern")
        exists = self.exclusions_list_widget.findItems(exclusion, Qt.MatchFlag.MatchExactly)
        if okay and exclusion and not exists:
            self.exclusions_list_widget.addItem(exclusion)

    def exclusions_remove(self):
        item = self.exclusions_list_widget.currentItem()
        if item:
            row = self.exclusions_list_widget.row(item)
            self.exclusions_list_widget.takeItem(row)

    def accept(self):
        computer_name = self.computer_name_line_edit.text().strip()
        backup_schedule = self.backup_schedule_combo_box.currentText()

        config["general"]["computer_name"] = computer_name
        config["general"]["backup_schedule"] = backup_schedule
        config["inclusions"]["paths"] = ",".join(
            self.inclusions_list_widget.item(i).text()
            for i in range(self.inclusions_list_widget.count())
        )
        config["exclusions"]["paths"] = ",".join(
            self.exclusions_list_widget.item(i).text()
            for i in range(self.exclusions_list_widget.count())
        )

        save_config()
        self.update_computer_name_online(computer_name)

        super().accept()

    def update_computer_name_online(self, computer_name):
        computer_id = config["meta"]["computer_id"]
        email = config["meta"]["email"]
        password = get_password_from_keyring()
        update_computer(email, password, computer_id, {"name": computer_name})