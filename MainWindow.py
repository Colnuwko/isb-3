import json
import os
import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QFileDialog,
)
import help_function
import main
import Hybrid


class Window(QMainWindow):
    """Других вариантов нет, код идеален, Успех в любом случае"""
    def button_1_click(self):
        main.work_sym_algoritm(16)
        QMessageBox.about(self, "Отчет", "Успех!")

    def button_2_click(self):
        main.work_asym_algoritm()
        QMessageBox.about(self, "Отчет", "Успех!")

    def button_3_click(self):
        keys = Hybrid.create_keys()
        Hybrid.save_keys(keys)
        Hybrid.load_keys()
        Hybrid.encrypt_text()
        Hybrid.decrypt_text()
        QMessageBox.about(self, "Отчет", "Успех!")

    def reset_settings(self):
        with open('settings.json', 'w') as fp:
            settings = {
                "path_to_dec_key_asym": "files/dec_asym_key.txt",
                "path_to_enc_key_asym": "files/enc_asym_key .txt",
                "path_to_decrypted_file": "files/dec_file.txt",
                "path_to_encrypted_file": "files/enc_file.txt",
                "path_to_initial_file": "files/initial_file.txt",
                "path_to_public_key": "files/public_key.pem",
                "path_to_secret_key": "files/secret_key.pem",
                "path_to_sym_key": "files/key.txt",
                "path_to_enc_sym_key": "files/enc_key.txt"
            }
            for key in settings:
                path = QFileDialog.getExistingDirectory(self, key, ".")
                if path == "":
                    print("Ничего не выбрано")
                else:
                    settings[key] = path + "/" + settings[key][6:]
            while not os.path.isfile(settings["path_to_initial_file"]):
                path = QFileDialog.getOpenFileName(self, "Выберите шифруемый файл", ".", "*.txt")
                if path == "":
                    print("Ничего не выбрано")
                else:
                    settings["path_to_initial_file"] = path[0]
            json.dump(settings, fp)

    def set_position(self):
        self.button_1.setMinimumSize(220, 30)
        self.button_1.move(425, 300)
        self.button_1.setText("Запустить симметричный алгоритм")
        self.button_2.setMinimumSize(220, 30)
        self.button_2.move(425, 355)
        self.button_2.setText("Запустить асимметричный алгоритм")
        self.button_3.setMinimumSize(220, 30)
        self.button_3.move(425, 410)
        self.button_3.setText("Запустить гибридный алгоритм")

    def __init__(self) -> None:
        """ "create a window object"""
        super(Window, self).__init__()
        self.qm = QMessageBox()
        self.button_1 = QtWidgets.QPushButton(self)
        self.button_2 = QtWidgets.QPushButton(self)
        self.button_3 = QtWidgets.QPushButton(self)
        self.button_3.hide()
        self.button_2.hide()
        self.button_1.hide()
        self.button_1.clicked.connect(self.button_1_click)
        self.button_2.clicked.connect(self.button_2_click)
        self.button_3.clicked.connect(self.button_3_click)
        self.set_position()
        help_function.create_settings()
        self.ret = self.qm.question(self, '', "Хотите использовать директории по умолчанию?", self.qm.Yes | self.qm.No)
        if self.ret == self.qm.Yes:
            self.button_3.show()
            self.button_2.show()
            self.button_1.show()
        else:
            self.reset_settings()
            self.button_3.show()
            self.button_2.show()
            self.button_1.show()


def application() -> None:
    app = QApplication(sys.argv)
    window = Window()
    window.setObjectName("MainWindow")
    window.setWindowIcon(QtGui.QIcon("files/phon.png"))
    window.setMinimumSize(1000, 800)
    window.setMaximumSize(1024, 720)
    window.setStyleSheet("#MainWindow{border-image:url(files/phon.png)}")
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
