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


class Window(QMainWindow):
    """Других вариантов нет, код идеален, Успех в любом случае"""
    def button_work_symm_click(self):
        main.work_sym_algoritm(16)
        QMessageBox.about(self, "Отчет", "Успех!")

    def button_work_asymm_click(self):
        main.work_asym_algoritm()
        QMessageBox.about(self, "Отчет", "Успех!")

    def button_work_hybrid_click(self):
        main.work_hybrid_algoritm()
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
        self.button_work_symm.setMinimumSize(220, 30)
        self.button_work_symm.move(425, 300)
        self.button_work_symm.setText("Запустить симметричный алгоритм")
        self.button_work_asymm.setMinimumSize(220, 30)
        self.button_work_asymm.move(425, 355)
        self.button_work_asymm.setText("Запустить асимметричный алгоритм")
        self.button_work_hybrid.setMinimumSize(220, 30)
        self.button_work_hybrid.move(425, 410)
        self.button_work_hybrid .setText("Запустить гибридный алгоритм")

    def __init__(self) -> None:
        """ "create a window object"""
        super(Window, self).__init__()
        self.qm = QMessageBox()
        self.button_work_symm = QtWidgets.QPushButton(self)
        self.button_work_asymm = QtWidgets.QPushButton(self)
        self.button_work_hybrid = QtWidgets.QPushButton(self)
        self.button_work_hybrid.hide()
        self.button_work_asymm.hide()
        self.button_work_symm.hide()
        self.button_work_symm.clicked.connect(self.button_work_symm_click)
        self.button_work_asymm.clicked.connect(self.button_work_asymm_click)
        self.button_work_hybrid.clicked.connect(self.button_work_hybrid_click)
        self.set_position()
        help_function.create_settings()
        self.ret = self.qm.question(self, '', "Хотите использовать директории по умолчанию?", self.qm.Yes | self.qm.No)
        if self.ret == self.qm.Yes:
            self.button_work_hybrid.show()
            self.button_work_asymm.show()
            self.button_work_symm.show()
        else:
            self.reset_settings()
            self.button_work_hybrid.show()
            self.button_work_asymm.show()
            self.button_work_symm.show()


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
