# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'segmento_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QVBoxLayout, QWidget)
import app_v1_0_1.view.resource_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(362, 510)
        Dialog.setMinimumSize(QSize(362, 510))
        Dialog.setMaximumSize(QSize(362, 510))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_2 = QWidget(Dialog)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"image: url(:/icon/Converte.ico);")

        self.verticalLayout.addWidget(self.widget_2)

        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.rdbtn_alimenticio = QRadioButton(self.widget)
        self.rdbtn_alimenticio.setObjectName(u"rdbtn_alimenticio")

        self.verticalLayout_2.addWidget(self.rdbtn_alimenticio)

        self.radioButton_4 = QRadioButton(self.widget)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.verticalLayout_2.addWidget(self.radioButton_4)

        self.rdbtn_eletronico = QRadioButton(self.widget)
        self.rdbtn_eletronico.setObjectName(u"rdbtn_eletronico")

        self.verticalLayout_2.addWidget(self.rdbtn_eletronico)

        self.radioButton_5 = QRadioButton(self.widget)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.verticalLayout_2.addWidget(self.radioButton_5)

        self.radioButton_3 = QRadioButton(self.widget)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout_2.addWidget(self.radioButton_3)

        self.radioButton_6 = QRadioButton(self.widget)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.verticalLayout_2.addWidget(self.radioButton_6)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_2.addWidget(self.pushButton_2)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Seja Bem Vindo, &lt;nome&gt;!</span></p><p align=\"center\"><span style=\" font-weight:600;\">Selecione abaixo qual segmento da sua empresa!</span></p></body></html>", None))
        self.rdbtn_alimenticio.setText(QCoreApplication.translate("Dialog", u"Alimenticio", None))
        self.radioButton_4.setText(QCoreApplication.translate("Dialog", u"RadioButton", None))
        self.rdbtn_eletronico.setText(QCoreApplication.translate("Dialog", u"Eletronico", None))
        self.radioButton_5.setText(QCoreApplication.translate("Dialog", u"RadioButton", None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog", u"RadioButton", None))
        self.radioButton_6.setText(QCoreApplication.translate("Dialog", u"RadioButton", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Cadastrar", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Voltar", None))
    # retranslateUi

