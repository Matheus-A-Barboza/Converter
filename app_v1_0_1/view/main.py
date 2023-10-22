import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtGui import QPalette, QColor, Qt

from app_v1_0_1.view.menu_ui import Ui_MainWindow
from app_v1_0_1.view.entrar_ui import Ui_Dialog
from app_v1_0_1.view.segmento_ui import Ui_Dialog
from app_v1_0_1.infra.config.connection import DBConnectionHandler

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        data_base = DBConnectionHandler

class Empresa(QMainWindow, Ui_Dialog):
    def __init__(self):
        super(Empresa, self).__init__()
        self.setupUi(self)

    def cadastrar_empresa(self):
        self.cadastro_dialog = EmpresaDialog()
        self.cadastro_dialog.show()

class EmpresaDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(EmpresaDialog, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication()
    window = EmpresaDialog()
    window.show()
    sys.exit(app.exec())