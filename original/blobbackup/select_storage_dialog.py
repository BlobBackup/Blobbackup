from PySide2.QtWidgets import QDialog
from blobbackup.ui_select_storage_dialog import Ui_SelectStorageDialog


class SelectStorageDialog(QDialog, Ui_SelectStorageDialog):
    def __init__(self):
        QDialog.__init__(self)
        Ui_SelectStorageDialog.__init__(self)

        self.setupUi(self)
        self.location = None

        self.local_directory_button.pressed.connect(
            lambda: self.select_generic("Local Directory"))
        self.amazon_aws_button.pressed.connect(
            lambda: self.select_generic("Amazon AWS"))
        self.backblaze_b2_button.pressed.connect(
            lambda: self.select_generic("Backblaze B2"))
        self.microsoft_azure_button.pressed.connect(
            lambda: self.select_generic("Microsoft Azure"))
        self.google_cloud_button.pressed.connect(
            lambda: self.select_generic("Google Cloud"))
        self.s3_storage_button.pressed.connect(
            lambda: self.select_generic("S3 Storage"))
        self.sftp_button.pressed.connect(lambda: self.select_generic("SFTP"))

    def select_generic(self, location):
        self.location = location
        self.accept()