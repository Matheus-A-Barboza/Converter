# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'entrar_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import app_v1_0_1.view.resource_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(410, 534)
        Dialog.setMaximumSize(410, 534)
        Dialog.setMinimumSize(410, 534)
        icon = QIcon()
        icon.addFile(u":/icon/Converte.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_2 = QWidget(Dialog)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"image: url(:/icon/Converte.ico);")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 291, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_2.addItem(self.verticalSpacer)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_cnpj_entrar = QLabel(self.widget)
        self.lbl_cnpj_entrar.setObjectName(u"lbl_cnpj_entrar")

        self.verticalLayout_2.addWidget(self.lbl_cnpj_entrar)

        self.txt_cnpj_entrar = QLineEdit(self.widget)
        self.txt_cnpj_entrar.setObjectName(u"txt_cnpj_entrar")
        self.txt_cnpj_entrar.setStyleSheet(u"Digite seu CNPJ...")

        self.verticalLayout_2.addWidget(self.txt_cnpj_entrar)

        self.lbl_senha_entrar = QLabel(self.widget)
        self.lbl_senha_entrar.setObjectName(u"lbl_senha_entrar")

        self.verticalLayout_2.addWidget(self.lbl_senha_entrar)

        self.txt_senha_entrar = QLineEdit(self.widget)
        self.txt_senha_entrar.setObjectName(u"txt_senha_entrar")

        self.verticalLayout_2.addWidget(self.txt_senha_entrar)

        self.btn_entrar = QPushButton(self.widget)
        self.btn_entrar.setObjectName(u"btn_entrar")

        self.verticalLayout_2.addWidget(self.btn_entrar)

        self.btn_cadastrar = QPushButton(self.widget)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")

        self.verticalLayout_2.addWidget(self.btn_cadastrar)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Entrar", None))
        self.lbl_cnpj_entrar.setText(QCoreApplication.translate("Dialog", u"CNPJ", None))
#if QT_CONFIG(tooltip)
        self.txt_cnpj_entrar.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Digite seu CNPJ</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.txt_cnpj_entrar.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.txt_cnpj_entrar.setText("")
        self.lbl_senha_entrar.setText(QCoreApplication.translate("Dialog", u"Senha", None))
        self.btn_entrar.setText(QCoreApplication.translate("Dialog", u"Entrar", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("Dialog", u"Cadastrar", None))
    # retranslateUi

