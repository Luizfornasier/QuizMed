# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pacientes.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)
import icons_rc

class Ui_Pacientes(object):
    def setupUi(self, Pacientes):
        if not Pacientes.objectName():
            Pacientes.setObjectName(u"Pacientes")
        Pacientes.resize(702, 287)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Pacientes.sizePolicy().hasHeightForWidth())
        Pacientes.setSizePolicy(sizePolicy)
        Pacientes.setMaximumSize(QSize(1646, 614))
        Pacientes.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.267045 rgba(0, 152, 151, 225), stop:1 rgba(10, 42, 15, 224));")
        self.verticalLayout = QVBoxLayout(Pacientes)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Pacientes)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: none;\n"
"\n"
"color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_2.addWidget(self.label_7)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setTextFormat(Qt.PlainText)
        self.label.setPixmap(QPixmap(u":/icons/Icons/paciente3.png"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)

        self.verticalLayout_2.addWidget(self.label)

        self.lblalt1 = QLabel(self.frame_2)
        self.lblalt1.setObjectName(u"lblalt1")

        self.verticalLayout_2.addWidget(self.lblalt1)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_3.addWidget(self.label_8)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u":/icons/Icons/paciente1.png"))
        self.label_3.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.label_3)

        self.lblalt2 = QLabel(self.frame_3)
        self.lblalt2.setObjectName(u"lblalt2")

        self.verticalLayout_3.addWidget(self.lblalt2)


        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_4.addWidget(self.label_9)

        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setPixmap(QPixmap(u":/icons/Icons/paciente2.png"))
        self.label_5.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.label_5)

        self.lblalt3 = QLabel(self.frame_4)
        self.lblalt3.setObjectName(u"lblalt3")

        self.verticalLayout_4.addWidget(self.lblalt3)


        self.horizontalLayout.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Pacientes)

        QMetaObject.connectSlotsByName(Pacientes)
    # setupUi

    def retranslateUi(self, Pacientes):
        Pacientes.setWindowTitle(QCoreApplication.translate("Pacientes", u"Form", None))
        self.label_7.setText(QCoreApplication.translate("Pacientes", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Paciente 1</span></p></body></html>", None))
        self.label.setText("")
        self.lblalt1.setText(QCoreApplication.translate("Pacientes", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Alternativa: 1</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Pacientes", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Paciente 2</span></p></body></html>", None))
        self.label_3.setText("")
        self.lblalt2.setText(QCoreApplication.translate("Pacientes", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Alternativa: 1</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Pacientes", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Paciente 3</span></p></body></html>", None))
        self.label_5.setText("")
        self.lblalt3.setText(QCoreApplication.translate("Pacientes", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Alternativa: 1</span></p></body></html>", None))
    # retranslateUi

