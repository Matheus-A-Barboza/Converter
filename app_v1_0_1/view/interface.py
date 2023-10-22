from PySide6 import QtGui
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QPushButton, QListWidget, QVBoxLayout, QLabel, QWidget, QFileDialog, \
    QHBoxLayout, QMessageBox
import sys
import xmltodict as xml
import pandas as pd
import app_v1_0_0.control.connection as cn

class AppXMLtoExcel(QWidget):
    def __init__(self):
        super().__init__()

        # self.criarBanco()

        self.xml_files = []

        self.setWindowIcon(QtGui.QIcon('Converte.ico'))
        self.setWindowTitle("Icon")

        self.setWindowTitle('ConversorNFs')
        self.setGeometry(100, 100, 400, 600)

        self.txt_logo = QLabel('ConversorNFs')
        self.txt_logo.setAlignment(Qt.AlignCenter)  # Centralizar o texto

        self.btn_selecionar = QPushButton('Selecionar Arquivos XML')
        self.btn_selecionar.clicked.connect(self.adicionar_xml)

        self.btn_converter = QPushButton('Converter para Excel')
        self.btn_converter.clicked.connect(self.converter_notas)

        self.btn_converter_pdf = QPushButton('Converter para PDF')
        # self.btn_converter_pdf.clicked.connect(self.converter_pdf)

        self.lst_xml = QListWidget()

        layout = QVBoxLayout()

        # Criar um layout horizontal para centralizar elementos
        horizontal_layout = QHBoxLayout()
        horizontal_layout.addWidget(self.txt_logo)
        layout.addLayout(horizontal_layout)

        layout.addWidget(self.btn_selecionar)
        layout.addWidget(self.btn_converter)
        layout.addWidget(self.btn_converter_pdf)
        layout.addWidget(self.lst_xml)

        self.setLayout(layout)

    def adicionar_xml(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        files, _ = QFileDialog.getOpenFileNames(self, 'Selecionar Arquivos XML', '',
                                                'Arquivos XML (*.xml);;Todos os Arquivos (*)', options=options)

        if files:
            self.xml_files.extend(files)
            self.lst_xml.clear()
            self.lst_xml.addItems(files)

    def converter_notas(self):
        if not self.xml_files:
            QMessageBox.warning(self, "Nenhum Arquivo Selecionado", "Nenhum arquivo foi selecionado.")
            return

        valores = []
        for arquivo in self.xml_files:
            self.pegar_infos(arquivo, valores)

        colunas = ['numeroNota', 'empresaEmissora', 'nomeCliente', 'logradouro', 'bairro', 'municipio', 'uf',
                   'peso', 'valorNota', 'valorICMS', 'valorImposto', 'valorDesconto', 'COFINS',
                   'qntProd']

        tabela = pd.DataFrame(columns=colunas, data=valores)
        tabela.to_excel('NotasFiscais.xlsx', index=False)

        QMessageBox.information(self, "Conversão Concluída",
                                "Notas fiscais convertidas com sucesso para 'NotasFiscais.xlsx'.")

    # def converter_pdf(self):
    #     if not self.xml_files:
    #         QMessageBox.warning(self, "Nenhum Arquivo Selecionado", "Nenhum arquivo foi selecionado.")
    #         return
    #
    #     for arquivo in self.xml_files:
    #         pdf_filename = self.converter_xml_para_pdf(arquivo)
    #         if pdf_filename:
    #             webbrowser.open(pdf_filename)

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

    # def converter_xml_para_pdf(self, nome_arquivo, res=None):
        # license = pdf.License()
        # license.set_license("Aspose.Total.lic")
        # #
        # # lic = new
        # # aspose.pdf.license()
        # # lic.setlicense("mergedapi.aspose.total.product.family.lic")
        # # lic.embedded = True
        #
        # # lic = new
        # # Aspose.Pdf.License()
        # # lic.SetLicense("MergedAPI.Aspose.Total.Product.Family.lic");
        # # lic.Embedded = True
        #
        # # aspose.pdf.License lic = new
        # # Aspose.P
        #
        # documento = pdf.Document()
        # documento.bind_xml("input.xml")
        #
        # documento.save("XMLtoPDF.pdf")
        #
        # QMessageBox.information(self, 'Aviso','Convertido')
        #
        # try:
        #     with open(nome_arquivo, 'rb') as xml_file:
        #         # Crie um dicionário com os parâmetros da solicitação
        #         # pxv = pv('xYdDLCArSF3Ps0Zemazay0UZIYkpVBrHXJ5dtlWRdfZTHuXyYizAHNXUiIFsLhfQ')
        #
        #         options = dict(template='supported_languages', output='pdf')
        #
        #         xml = '''<?xml version="1.0" encoding="UTF-8"?>
        #         <languages>
        #           <lang code="en">English</lang>
        #           <lang code="es">Español</lang>
        #           <lang code="fr">Français</lang>
        #           <lang code="pt-br">Portuguese</lang>
        #         </languages>'''
        #
        #         file = 'test.pdf'
        #
        #         try:
        #             # res = pxv.sendXML(xml, options)
        #
        #             with open(file, 'wb') as f:
        #                 f.write(res['file'])
        #                 f.close()
        #
        #             print(
        #             'File created:', file)
        #         except Exception as e:
        #             print(e)
        #
        #         params = {
        #             'template': 'xmltopdf',  # Substitua 'template-name' pelo nome do seu modelo na PrexView
        #             'output': 'pdf',  # Pode ser 'pdf', 'html', 'image', etc., dependendo do formato desejado
        #             # 'options': {
        #             #     'key1': 'value1',  # Parâmetros adicionais específicos do modelo, se necessário
        #             #     'key2': 'value2',
        #             # },
        #         }
        #         # headers = {'Authorization': 'xYdDLCArSF3Ps0Zemazay0UZIYkpVBrHXJ5dtlWRdfZTHuXyYizAHNXUiIFsLhfQ'}  # Substitua 'API_KEY' pela sua chave de API
        #
        #         # Faça a solicitação HTTP POST para a API da PrexView
        #         response = requests.post('https://api.prexview.com/v1/transform', files={'xml': xml_file}, data=params,
        #                                  )
        #
        #         if response.status_code == 200:
        #             # Verifique se a resposta parece ser um PDF válido
        #             if response.headers.get('Content-Type', '').lower() == 'application/pdf':
        #                 # Salve o conteúdo no arquivo temporário
        #                 with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as pdf_temp_file:
        #                     pdf_temp_file.write(response.content)
        #                     pdf_temp_file.close()
        #                     QMessageBox.information(self, "Conversão Concluída",
        #                                             "Notas fiscais convertidas com sucesso para PDF.")
        #
        #                     # Retorne o nome do arquivo PDF salvo
        #                     return pdf_temp_file.name
        #             else:
        #                 QMessageBox.warning(self, "Erro na Conversão", "A conversão não gerou um PDF válido.")
        #         else:
        #             QMessageBox.warning(self, "Erro na Conversão",
        #                                 f"O serviço retornou um status de erro: {response.status_code}")
        #
        # except Exception as e:
        #     QMessageBox.warning(self, "Erro na Conversão", f"Ocorreu um erro ao converter o XML para PDF: {str(e)}")
        xmlpdf = "/nfs"
        print(xmlpdf)

        return None


if __name__ == '__main__':
    app = QApplication()
    app_lista_tarefas = AppXMLtoExcel()
    app_lista_tarefas.show()
    sys.exit(app.exec())