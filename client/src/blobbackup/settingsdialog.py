from PyQt6.QtWidgets import QDialog, QFileDialog, QInputDialog, QMessageBox
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

from blobbackup.ui.settingsdialog import Ui_SettingsDialog
from blobbackup.choosecomputerdialog import ChooseComputerDialog
from blobbackup.restoredialog import RestoreDialog
from blobbackup.logindialog import verify_password
from blobbackup.config import config, save_config
from blobbackup.api import update_computer, get_computer, delete_computer
from blobbackup.util import get_password_from_keyring, is_windows, LOGO_PATH
from blobbackup.logger import get_logger


class SettingsDialog(QDialog, Ui_SettingsDialog):
    def __init__(self, main_window):
        QDialog.__init__(self)
        Ui_SettingsDialog.__init__(self)
        self.setupUi(self)

        self.logger = get_logger()
        self.main_window = main_window

        self.setWindowIcon(QIcon(LOGO_PATH))

        self.populate_settings()

        self.inclusions_add_button.pressed.connect(self.inclusions_add)
        self.inclusions_remove_button.pressed.connect(self.inclusions_remove)
        self.exclusions_add_button.pressed.connect(self.exclusions_add)
        self.exclusions_remove_button.pressed.connect(self.exclusions_remove)
        self.restore_different_computer_label.linkActivated.connect(
            self.restore_different_computer
        )
        self.inherit_backup_history_label.linkActivated.connect(
            self.inherit_backup_history
        )
        self.save_button.pressed.connect(self.accept)

        if is_windows():
            self.backup_connected_file_systems_label.setVisible(False)
            self.backup_connected_file_systems_combo_box.setVisible(False)

        self.logger.info("Settings dialog displayed.")

    def populate_settings(self):
        self.computer_name_line_edit.setText(config["general"]["computer_name"])
        self.backup_schedule_combo_box.setCurrentText(
            config["general"]["backup_schedule"]
        )
        self.max_upload_kibs_spin_box.setValue(
            int(config["general"]["max_upload_kibs"])
        )
        self.backup_connected_file_systems_combo_box.setCurrentText(
            config["general"]["backup_connected_file_systems"]
        )
        self.number_of_backup_threads_spin_box.setValue(
            int(config["general"]["num_backup_threads"])
        )
        self.inclusions_list_widget.clear()
        for path in config["inclusions"]["paths"].split(","):
            if path:
                self.inclusions_list_widget.addItem(path)
        self.exclusions_list_widget.clear()
        for path in config["exclusions"]["paths"].split(","):
            if path:
                self.exclusions_list_widget.addItem(path)
        self.logger.info("Settings populated.")

    def inclusions_add(self):
        path = QFileDialog.getExistingDirectory()
        if path and not self.inclusions_list_widget.findItems(
            path, Qt.MatchFlag.MatchExactly
        ):
            self.inclusions_list_widget.addItem(path)
            self.logger.info("Inclusion added.")

    def inclusions_remove(self):
        item = self.inclusions_list_widget.currentItem()
        if item:
            row = self.inclusions_list_widget.row(item)
            self.inclusions_list_widget.takeItem(row)
            self.logger.info("Inclusion removed.")

    def exclusions_add(self):
        exclusion, okay = QInputDialog.getText(self, "Add exclusion", "Path or pattern")
        exists = self.exclusions_list_widget.findItems(
            exclusion, Qt.MatchFlag.MatchExactly
        )
        if okay and exclusion and not exists:
            self.exclusions_list_widget.addItem(exclusion)
            self.logger.info("Exclusion added.")

    def exclusions_remove(self):
        item = self.exclusions_list_widget.currentItem()
        if item:
            row = self.exclusions_list_widget.row(item)
            self.exclusions_list_widget.takeItem(row)
            self.logger.info("Exclusion removed.")

    def restore_different_computer(self):
        email = config["meta"]["email"]
        if verify_password(email):
            password = get_password_from_keyring()
            choose_computer_dialog = ChooseComputerDialog(
                email,
                password,
                "Choose the computer you want to restore from.",
            )
            if choose_computer_dialog.exec():
                computer_id = choose_computer_dialog.computer_id
                dialog = RestoreDialog(email, password, computer_id)
                dialog.exec()

    def inherit_backup_history(self):
        email = config["meta"]["email"]
        if verify_password(email):
            password = get_password_from_keyring()
            choose_computer_dialog = ChooseComputerDialog(
                email,
                password,
                "Choose the computer to inherit backup history from.",
            )
            if choose_computer_dialog.exec():
                computer_id = choose_computer_dialog.computer_id
                computer = get_computer(email, password, computer_id)
                computer_name = computer["name"]
                reply = QMessageBox.information(
                    self,
                    "Inherit Backup History?",
                    f"You are about to inherit the backup history of the computer '{computer_name}'. This is an irreversible operation. Continue?",
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                    QMessageBox.StandardButton.No,
                )
                if reply == QMessageBox.StandardButton.Yes:
                    current_computer_id = config["meta"]["computer_id"]
                    delete_computer(email, password, current_computer_id)
                    config["meta"]["computer_id"] = str(computer_id)
                    save_config()
                    self.main_window.stop_backup()
                    QMessageBox.information(
                        self,
                        "Inherited Backup History",
                        "Successfully inherited backup history.",
                    )
                    self.reject()

    def accept(self):
        computer_name = self.computer_name_line_edit.text().strip()
        backup_schedule = self.backup_schedule_combo_box.currentText()
        max_upload_kibs = str(self.max_upload_kibs_spin_box.value())
        backup_connected_file_systems = (
            self.backup_connected_file_systems_combo_box.currentText()
        )
        num_backup_threads = str(self.number_of_backup_threads_spin_box.value())

        config["general"]["computer_name"] = computer_name
        config["general"]["backup_schedule"] = backup_schedule
        config["general"]["max_upload_kibs"] = max_upload_kibs
        config["general"]["num_backup_threads"] = num_backup_threads
        config["general"][
            "backup_connected_file_systems"
        ] = backup_connected_file_systems
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

        self.logger.info("Settings saved.")
        super().accept()

    def update_computer_name_online(self, computer_name):
        computer_id = config["meta"]["computer_id"]
        email = config["meta"]["email"]
        password = get_password_from_keyring()
        update_computer(email, password, computer_id, {"name": computer_name})
