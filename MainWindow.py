import json
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
import Symmetric
import Hybrid

class Window(QMainWindow):
    """Других вариантов нет, код идеален, Успех в любом случае"""
    def button_1_click(self):
        main.work_sym_algoritm(16)
        QMessageBox.about(self, "Отчет", "Успех!")
    def button_2_click(self):
        main.work_asym_algoritm(16)
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
                "decrypted_file.txt": "C:/Users/Солнышко/PycharmProjects/isb-3/decrypted/dec_file.txt",
                "encrypted_file.yaml": "C:/Users/Солнышко/PycharmProjects/isb-3/encrypted/enc_file.yaml",
                "initial_file.txt": "C:/Users/Солнышко/PycharmProjects/isb-3/initial_file.txt",
                "public_key.pem": "C:/Users/Солнышко/PycharmProjects/isb-3/public_key/public_key.pem",
                "secret_key.pem": "C:/Users/Солнышко/PycharmProjects/isb-3/private_key/secret_key.pem",
                "symmetric_key.txt": "C:/Users/Солнышко/PycharmProjects/isb-3/symmetrical_key/key.txt",
                "enc_symmetric_key.txt": "C:/Users/Солнышко/PycharmProjects/isb-3/symmetrical_key/enc_key.txt"
            }
            for key in settings:
                path = QFileDialog.getExistingDirectory(self, key, ".")
                if path == "":
                    print("Ничего не выбрано")
                else:
                    settings[key] = path + "/" + key
                print(settings)
            json.dump(settings, fp)

    def position(self):
        self.button_1.setMinimumSize(150, 30)
        self.button_1.move(425, 300)
        self.button_1.setText("Генерация ключей")
        self.button_2.setMinimumSize(150, 30)
        self.button_2.move(425, 355)
        self.button_2.setText("Шифрование текста")
        self.button_3.setMinimumSize(150, 30)
        self.button_3.move(425, 410)
        self.button_3.setText("Дешифрование текста")

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
        self.position()
        self.ret = self.qm.question(self, '', "Хотите использовать директории по умолчанию?", self.qm.Yes | self.qm.No)
        if self.ret == self.qm.Yes:
            print("2")
            help_function.create_settings()
            self.button_3.show()
            self.button_2.show()
            self.button_1.show()
        else:
            print("1")
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
