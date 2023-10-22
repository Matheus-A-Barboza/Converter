# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'controle.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1111, 851)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.txt_nome = QLabel(self.widget_2)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setGeometry(QRect(60, 100, 201, 31))
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.txt_nome.setFont(font)
        self.txt_preco = QLabel(self.widget_2)
        self.txt_preco.setObjectName(u"txt_preco")
        self.txt_preco.setGeometry(QRect(60, 170, 201, 31))
        self.txt_preco.setFont(font)
        self.lbl_fornecedor = QLabel(self.widget_2)
        self.lbl_fornecedor.setObjectName(u"lbl_fornecedor")
        self.lbl_fornecedor.setGeometry(QRect(60, 450, 201, 31))
        self.lbl_fornecedor.setFont(font)
        self.lbl_categoria = QLabel(self.widget_2)
        self.lbl_categoria.setObjectName(u"lbl_categoria")
        self.lbl_categoria.setGeometry(QRect(60, 380, 201, 31))
        self.lbl_categoria.setFont(font)
        self.lbl_dtVal = QLabel(self.widget_2)
        self.lbl_dtVal.setObjectName(u"lbl_dtVal")
        self.lbl_dtVal.setGeometry(QRect(60, 310, 201, 31))
        self.lbl_dtVal.setFont(font)
        self.lbl_qnt = QLabel(self.widget_2)
        self.lbl_qnt.setObjectName(u"lbl_qnt")
        self.lbl_qnt.setGeometry(QRect(60, 240, 201, 31))
        self.lbl_qnt.setFont(font)
        self.lbl_nome = QLineEdit(self.widget_2)
        self.lbl_nome.setObjectName(u"lbl_nome")
        self.lbl_nome.setGeometry(QRect(60, 130, 391, 22))
        self.lbl_preco = QLineEdit(self.widget_2)
        self.lbl_preco.setObjectName(u"lbl_preco")
        self.lbl_preco.setGeometry(QRect(60, 210, 391, 22))
        self.lbl_preco.setInputMethodHints(Qt.ImhPreferNumbers)
        self.txt_qnt = QLineEdit(self.widget_2)
        self.txt_qnt.setObjectName(u"txt_qnt")
        self.txt_qnt.setGeometry(QRect(60, 270, 391, 22))
        self.txt_qnt.setInputMethodHints(Qt.ImhPreferNumbers)
        self.txt_dtVal_2 = QLineEdit(self.widget_2)
        self.txt_dtVal_2.setObjectName(u"txt_dtVal_2")
        self.txt_dtVal_2.setGeometry(QRect(60, 340, 391, 22))
        self.txt_dtVal_2.setInputMethodHints(Qt.ImhDate)
        self.txt_categoria_2 = QLineEdit(self.widget_2)
        self.txt_categoria_2.setObjectName(u"txt_categoria_2")
        self.txt_categoria_2.setGeometry(QRect(60, 410, 391, 22))
        self.txt_fornecedor = QLineEdit(self.widget_2)
        self.txt_fornecedor.setObjectName(u"txt_fornecedor")
        self.txt_fornecedor.setGeometry(QRect(60, 480, 391, 22))
        self.btn_editar = QPushButton(self.widget_2)
        self.btn_editar.setObjectName(u"btn_editar")
        self.btn_editar.setGeometry(QRect(30, 630, 221, 28))
        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(270, 630, 211, 28))
        self.btn_cadastrar = QPushButton(self.widget_2)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setGeometry(QRect(80, 580, 361, 28))
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 40, 271, 31))
        font1 = QFont()
        font1.setFamilies([u"Eras Demi ITC"])
        font1.setPointSize(15)
        self.label.setFont(font1)

        self.horizontalLayout.addWidget(self.widget_2)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.tableWidget = QTableWidget(self.widget)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.tableWidget.rowCount() < 5):
            self.tableWidget.setRowCount(5)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem11)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(5, 11, 531, 811))
        self.tableWidget.verticalHeader().setVisible(False)

        self.horizontalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.txt_nome.setText(QCoreApplication.translate("MainWindow", u"Nome do Produto", None))
        self.txt_preco.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o do Produto", None))
        self.lbl_fornecedor.setText(QCoreApplication.translate("MainWindow", u"Fornecedor", None))
        self.lbl_categoria.setText(QCoreApplication.translate("MainWindow", u"Categoria", None))
        self.lbl_dtVal.setText(QCoreApplication.translate("MainWindow", u"Data de Validade", None))
        self.lbl_qnt.setText(QCoreApplication.translate("MainWindow", u"Quantidade do Produto", None))
        self.btn_editar.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Remover", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Controle de Estoque", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Validade", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Categoria", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Fornecedor", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"5", None));
    # retranslateUi

