# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'doutores.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import icons_rc

class Ui_Doutores(object):
    def setupUi(self, Doutores):
        if not Doutores.objectName():
            Doutores.setObjectName(u"Doutores")
        Doutores.resize(712, 266)
        Doutores.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.267045 rgba(0, 152, 151, 225), stop:1 rgba(10, 42, 15, 224));")
        self.verticalLayout = QVBoxLayout(Doutores)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Doutores)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: none;")
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
        self.btndr1 = QPushButton(self.frame_2)
        self.btndr1.setObjectName(u"btndr1")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btndr1.sizePolicy().hasHeightForWidth())
        self.btndr1.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/icons/Icons/doutor1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btndr1.setIcon(icon)
        self.btndr1.setIconSize(QSize(132, 200))

        self.verticalLayout_2.addWidget(self.btndr1)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btndr2 = QPushButton(self.frame_3)
        self.btndr2.setObjectName(u"btndr2")
        sizePolicy.setHeightForWidth(self.btndr2.sizePolicy().hasHeightForWidth())
        self.btndr2.setSizePolicy(sizePolicy)
        icon1 = QIcon()
        icon1.addFile(u":/icons/Icons/doutor2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btndr2.setIcon(icon1)
        self.btndr2.setIconSize(QSize(132, 200))

        self.verticalLayout_3.addWidget(self.btndr2)


        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btdr3 = QPushButton(self.frame_4)
        self.btdr3.setObjectName(u"btdr3")
        sizePolicy.setHeightForWidth(self.btdr3.sizePolicy().hasHeightForWidth())
        self.btdr3.setSizePolicy(sizePolicy)
        icon2 = QIcon()
        icon2.addFile(u":/icons/Icons/doutor3.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btdr3.setIcon(icon2)
        self.btdr3.setIconSize(QSize(132, 200))

        self.verticalLayout_4.addWidget(self.btdr3)


        self.horizontalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.btndr4 = QPushButton(self.frame_5)
        self.btndr4.setObjectName(u"btndr4")
        sizePolicy.setHeightForWidth(self.btndr4.sizePolicy().hasHeightForWidth())
        self.btndr4.setSizePolicy(sizePolicy)
        icon3 = QIcon()
        icon3.addFile(u":/icons/Icons/doutor4.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btndr4.setIcon(icon3)
        self.btndr4.setIconSize(QSize(132, 200))

        self.verticalLayout_5.addWidget(self.btndr4)


        self.horizontalLayout.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Doutores)

        QMetaObject.connectSlotsByName(Doutores)
    # setupUi

    def retranslateUi(self, Doutores):
        Doutores.setWindowTitle(QCoreApplication.translate("Doutores", u"Form", None))
        self.btndr1.setText("")
        self.btndr2.setText("")
        self.btdr3.setText("")
        self.btndr4.setText("")
    # retranslateUi

