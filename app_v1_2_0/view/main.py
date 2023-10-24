import os.path

import pandas as pd
import xmltodict as xml
import openpyxl
import sys

from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QLabel, QMessageBox, QFileDialog, QListWidget

from code_test.view.menu_ui import Ui_Menu
from code_test.view.segmento_ui import Ui_Segmento
from code_test.view.entrar_ui import Ui_Login
from code_test.view.cadastrar_ui import Ui_Cadastro


class MainWindow(QMainWindow, Ui_Login):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.btn_entrar.clicked.connect(self.entrar)
        self.btn_cadastrar.clicked.connect(self.cadastrar)


    def entrar(self):
        self.close()
        self.entrarUi = EntrarUi()
        self.entrarUi.show()

    def cadastrar(self):
        self.close()
        self.cadastrarUi = CadastrarUi()
        self.cadastrarUi.show()


class CadastrarUi(QDialog, Ui_Cadastro):

    def __init__(self, parent=None):
        super(CadastrarUi, self).__init__(parent)
        self.setupUi(self)

        self.btn_cadastrar_empresa.clicked.connect(self.proximo)
        self.btn_voltar_entrar.clicked.connect(self.voltar)

    def proximo(self):
        self.close()
        self.proximoUi = SegmentoUi()
        self.proximoUi.show()

    def voltar(self):
        self.close()
        self.menuUi = MainWindow()
        self.menuUi.show()


class SegmentoUi(QDialog, Ui_Segmento):
    def __init__(self, parent=None):
        super(SegmentoUi, self).__init__(parent)
        self.setupUi(self)

        self.btn_cadastrar_segmento.clicked.connect(self.cadastrarSegmento)
        self.btn_cancelar.clicked.connect(self.cancelarSegmento)

    def cadastrarSegmento(self):
        self.close()
        self.cadastrar_segmento = EntrarUi()
        self.cadastrar_segmento.show()

    def cancelarSegmento(self):
        self.close()
        self.cancelar_cadastro = MainWindow()
        self.cancelar_cadastro.show()


class EntrarUi(QDialog, Ui_Menu):
    def __init__(self, parent=None):
        super(EntrarUi, self).__init__(parent)
        self.setupUi(self)
        self.model = model

        self.xml_files = []
        self.lst_xml = self.list_arquivos

        self.btn_selecionar_arquivos.clicked.connect(self.adicionar_xml)
        self.btn_excel.clicked.connect(self.converter_notas)

        self.model = QStandardItemModel()
        self.list_arquivos.setModel(self.model)

    def adicionar_xml(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        files, _ = QFileDialog.getOpenFileNames(self, 'Selecionar Arquivos XML', '',
                                                'Arquivos XML (*.xml);;Todos os Arquivos (*)', options=options)

        if files:
            self.model.clear()
            for file in files:
                item = QStandardItem(file)
                self.model.appendRow(item)

    def converter_notas(self):
        if self.model.rowCount() == 0:
            QMessageBox.warning(self, "Nenhum Arquivo Selecionado", "Nenhum arquivo foi selecionado.")
            return

        valores = []
        for row in range(self.model.rowCount()):
            item = self.model.item(row, 0)
            arquivo = item.text()
            self.pegar_infos(arquivo, valores)

        colunas = ['numeroNota', 'empresaEmissora', 'nomeCliente', 'logradouro', 'bairro', 'municipio', 'uf',
                   'peso', 'valorNota', 'valorICMS', 'valorImposto', 'valorDesconto', 'COFINS',
                   'qntProd']

        tabela = pd.DataFrame(columns=colunas, data=valores)

        desktop_path = os.path.expanduser("~/Desktop")
        excel_file_path = os.path.join(desktop_path, 'NotasFiscais.xlsx')

        tabela.to_excel(excel_file_path, index=False)

        QMessageBox.information(self, "Conversão Concluída",
                                "Notas fiscais convertidas com sucesso para 'NotasFiscais.xlsx'.")

        os.system(f'start excel "{excel_file_path}"')

    def pegar_infos(self, nome_arquivo, valores):
        with open(nome_arquivo, 'rb') as arquivo_xml:
            dic_arquivo = xml.parse(arquivo_xml)
            if 'NFe' in dic_arquivo:
                infos_nf = dic_arquivo['NFe']['infNFe']
            else:
                infos_nf = dic_arquivo['nfeProc']['NFe']['infNFe']
            numeroNota = infos_nf['@Id']
            empresaEmissora = infos_nf['emit']['xNome']
            nomeCliente = infos_nf['dest']['xNome']
            logradouro = infos_nf['dest']['enderDest']['xLgr']
            bairro = infos_nf['dest']['enderDest']['xBairro']
            municipio = infos_nf['dest']['enderDest']['xMun']
            uf = infos_nf['dest']['enderDest']['UF']
            valorNota = infos_nf['total']['ICMSTot']['vBC']
            valorICMS = infos_nf['total']['ICMSTot']['vICMS']
            valorDesconto = infos_nf['total']['ICMSTot'].get('vDesc', '0.0')

            if 'vTotTrib' in infos_nf['total']:
                valorImposto = infos_nf['total']['ICMSTot']['vTotTrib']
            else:
                valorImposto = '0.0'

            if 'COFINS' in infos_nf['det']:
                COFINS = infos_nf['det']['imposto']['COFINS']['COFINSAliq']['vBC']
            else:
                COFINS = 'Nao Informado'

            if 'prod' in infos_nf['det']:
                qntProd = infos_nf['det']['prod']['qCom']
            else:
                qntProd = 'Nao Informado'

            if 'vol' in infos_nf['transp']:
                peso = infos_nf['transp']['vol']['pesoB']
            else:
                peso = 'Não Informado'

        valores.append([numeroNota, empresaEmissora, nomeCliente, logradouro, bairro, municipio, uf,
                        peso, valorNota, valorICMS, valorImposto, valorDesconto, COFINS, qntProd])

        return None


if __name__ == '__main__':
    app = QApplication()
    model = QStandardItemModel()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
