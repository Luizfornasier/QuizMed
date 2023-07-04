# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'answerandquestion.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QCommandLinkButton, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QTabWidget,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(771, 560)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.267045 rgba(0, 152, 151, 225), stop:1 rgba(10, 42, 15, 224));")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Pages = QStackedWidget(self.centralwidget)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setStyleSheet(u"")
        self.inicio_pg = QWidget()
        self.inicio_pg.setObjectName(u"inicio_pg")
        self.verticalLayout_4 = QVBoxLayout(self.inicio_pg)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.inicio_pg)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/icons/Icons/Pergunta e Respostas.jpg"))
        self.label.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.label)

        self.frame = QFrame(self.inicio_pg)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(0,17,35);\n"
"color:rgb(255,255,255);\n"
"border-color: rgb(255,255,255);\n"
"border-radius:15px;\n"
"border: 1px solid white\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"background-color: rgb(0,71,149);\n"
"\n"
"\n"
"}\n"
"\n"
"QFrame{\n"
"\n"
"background-color: none;\n"
"\n"
"\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btnjogar = QPushButton(self.frame)
        self.btnjogar.setObjectName(u"btnjogar")
        self.btnjogar.setMinimumSize(QSize(300, 31))
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.btnjogar.setFont(font)
        self.btnjogar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnjogar.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.btnjogar, 0, Qt.AlignHCenter)

        self.btncadastrar = QPushButton(self.frame)
        self.btncadastrar.setObjectName(u"btncadastrar")
        self.btncadastrar.setMinimumSize(QSize(300, 31))
        self.btncadastrar.setFont(font)
        self.btncadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btncadastrar.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.btncadastrar, 0, Qt.AlignHCenter)

        self.btnsair = QPushButton(self.frame)
        self.btnsair.setObjectName(u"btnsair")
        self.btnsair.setMinimumSize(QSize(300, 31))
        self.btnsair.setFont(font)
        self.btnsair.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnsair.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.btnsair, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addWidget(self.frame)

        self.Pages.addWidget(self.inicio_pg)
        self.game_pg = QWidget()
        self.game_pg.setObjectName(u"game_pg")
        self.verticalLayout_8 = QVBoxLayout(self.game_pg)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_2 = QFrame(self.game_pg)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(0, 100))
        self.label_2.setStyleSheet(u"background-color: rgb(0,17,35);\n"
"border-radius:15px;\n"
"border: 2px solid white;\n"
"color:rgb(255,255,255);\n"
"\n"
"\n"
"")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.label_3.setFont(font1)
        self.label_3.setTabletTracking(False)
        self.label_3.setStyleSheet(u"background-color: none;\n"
"color: white;")
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(True)

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout_8.addWidget(self.frame_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_4 = QFrame(self.game_pg)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setStyleSheet(u"QCommandLinkButton{\n"
"\n"
"background-color: rgb(0,17,35); \n"
"color:rgb(255,255,255);\n"
"border-color: rgb(255,255,255);\n"
"border-radius:15px;\n"
"border: 1px solid white\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QCommandLinkButton:hover{\n"
"\n"
"background-color: rgb(0,71,149);\n"
"\n"
"\n"
"}\n"
"\n"
"QFrame{\n"
"\n"
"background-color: none;\n"
"\n"
"\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.btn_resp1 = QCommandLinkButton(self.frame_4)
        self.btn_resp1.setObjectName(u"btn_resp1")
        self.btn_resp1.setMaximumSize(QSize(16777215, 40))
        self.btn_resp1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_resp1.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/Icons/estetoscopio2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_resp1.setIcon(icon)

        self.verticalLayout_5.addWidget(self.btn_resp1)

        self.btn_resp2 = QCommandLinkButton(self.frame_4)
        self.btn_resp2.setObjectName(u"btn_resp2")
        self.btn_resp2.setMaximumSize(QSize(16777215, 40))
        self.btn_resp2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_resp2.setIcon(icon)

        self.verticalLayout_5.addWidget(self.btn_resp2)

        self.btn_resp4 = QCommandLinkButton(self.frame_4)
        self.btn_resp4.setObjectName(u"btn_resp4")
        self.btn_resp4.setMaximumSize(QSize(16777215, 40))
        self.btn_resp4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_resp4.setIcon(icon)

        self.verticalLayout_5.addWidget(self.btn_resp4)

        self.btn_resp3 = QCommandLinkButton(self.frame_4)
        self.btn_resp3.setObjectName(u"btn_resp3")
        self.btn_resp3.setMaximumSize(QSize(16777215, 40))
        self.btn_resp3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_resp3.setIcon(icon)

        self.verticalLayout_5.addWidget(self.btn_resp3)


        self.horizontalLayout_5.addWidget(self.frame_4)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_3 = QFrame(self.game_pg)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(350, 265))
        self.frame_3.setStyleSheet(u"QFrame{\n"
"\n"
"color:rgb(255,255,255);\n"
"border-color: rgb(255,255,255);\n"
"border-radius: 15px;\n"
"border:1px solid white;\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"\n"
"color:rgb(255,255,255);\n"
"border-color: rgb(255,255,255);\n"
"border-radius: 15px;\n"
"border:1px solid white;\n"
"\n"
"}\n"
"\n"
"QPushButton:Hover{\n"
"\n"
"color: #fff;\n"
"background-color: rgb(0,17,35); \n"
"\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.label_7)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_convidados = QPushButton(self.frame_3)
        self.btn_convidados.setObjectName(u"btn_convidados")
        self.btn_convidados.setMinimumSize(QSize(0, 50))
        self.btn_convidados.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_convidados.setAutoDefault(False)
        self.btn_convidados.setFlat(False)

        self.horizontalLayout_3.addWidget(self.btn_convidados)

        self.btn_cartas = QPushButton(self.frame_3)
        self.btn_cartas.setObjectName(u"btn_cartas")
        self.btn_cartas.setMinimumSize(QSize(0, 50))
        self.btn_cartas.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.btn_cartas)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_pular = QPushButton(self.frame_3)
        self.btn_pular.setObjectName(u"btn_pular")
        self.btn_pular.setMinimumSize(QSize(0, 50))
        self.btn_pular.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.btn_pular)

        self.btn_pular1 = QPushButton(self.frame_3)
        self.btn_pular1.setObjectName(u"btn_pular1")
        self.btn_pular1.setMinimumSize(QSize(0, 50))
        self.btn_pular1.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.btn_pular1)

        self.btn_pular2 = QPushButton(self.frame_3)
        self.btn_pular2.setObjectName(u"btn_pular2")
        self.btn_pular2.setMinimumSize(QSize(0, 50))
        self.btn_pular2.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.btn_pular2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.btnparar = QPushButton(self.frame_3)
        self.btnparar.setObjectName(u"btnparar")
        self.btnparar.setMinimumSize(QSize(0, 31))
        font2 = QFont()
        font2.setPointSize(11)
        self.btnparar.setFont(font2)
        self.btnparar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnparar.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(0,17,35);\n"
"color:rgb(255,255,255);\n"
"border-color: rgb(255,255,255);\n"
"border-radius:15px;\n"
"border: 1px solid white\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"background-color: rgb(0,71,149);\n"
"\n"
"\n"
"}\n"
"\n"
"QFrame{\n"
"\n"
"background-color: none;\n"
"\n"
"\n"
"}")

        self.verticalLayout_6.addWidget(self.btnparar)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(350, 95))
        self.frame_5.setStyleSheet(u"QFrame{\n"
"color:rgb(255,255,255);\n"
"border-color:rgb(255,255,255);\n"
"border-radius:15px;\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QLabel{\n"
"\n"
"background-color:none;\n"
"color:rgb(255,255,127);\n"
"\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_errar = QLabel(self.frame_5)
        self.lbl_errar.setObjectName(u"lbl_errar")

        self.horizontalLayout_2.addWidget(self.lbl_errar)

        self.lbl_acertar = QLabel(self.frame_5)
        self.lbl_acertar.setObjectName(u"lbl_acertar")

        self.horizontalLayout_2.addWidget(self.lbl_acertar)

        self.lbl_parar = QLabel(self.frame_5)
        self.lbl_parar.setObjectName(u"lbl_parar")

        self.horizontalLayout_2.addWidget(self.lbl_parar)


        self.verticalLayout_6.addWidget(self.frame_5)


        self.verticalLayout_7.addWidget(self.frame_3)

        self.frame_10 = QFrame(self.game_pg)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(0,17,35);\n"
"color:rgb(255,255,255);\n"
"border-color: rgb(255,255,255);\n"
"border-radius:15px;\n"
"border: 1px solid white\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"background-color: rgb(0,71,149);\n"
"\n"
"\n"
"}\n"
"\n"
"QFrame{\n"
"\n"
"background-color: none;\n"
"\n"
"\n"
"}")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.btn_backmenu = QPushButton(self.frame_10)
        self.btn_backmenu.setObjectName(u"btn_backmenu")
        self.btn_backmenu.setMinimumSize(QSize(0, 31))
        self.btn_backmenu.setFont(font2)

        self.horizontalLayout_13.addWidget(self.btn_backmenu)


        self.verticalLayout_7.addWidget(self.frame_10)


        self.horizontalLayout_5.addLayout(self.verticalLayout_7)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.btn_novojogo = QPushButton(self.game_pg)
        self.btn_novojogo.setObjectName(u"btn_novojogo")
        self.btn_novojogo.setMinimumSize(QSize(120, 31))
        self.btn_novojogo.setFont(font)
        self.btn_novojogo.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(0,17,35);\n"
"color:rgb(255,255,255);\n"
"border-color: rgb(255,255,255);\n"
"border-radius:15px;\n"
"border: 1px solid white\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"background-color: rgb(0,71,149);\n"
"\n"
"\n"
"}\n"
"\n"
"QFrame{\n"
"\n"
"background-color: none;\n"
"\n"
"\n"
"}")

        self.verticalLayout_8.addWidget(self.btn_novojogo, 0, Qt.AlignLeft)

        self.Pages.addWidget(self.game_pg)
        self.page_cadastrar = QWidget()
        self.page_cadastrar.setObjectName(u"page_cadastrar")
        self.page_cadastrar.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.267045 rgba(0, 152, 151, 225), stop:1 rgba(10, 42, 15, 224));")
        self.verticalLayout_9 = QVBoxLayout(self.page_cadastrar)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.tabWidget = QTabWidget(self.page_cadastrar)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_12 = QVBoxLayout(self.tab)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_6 = QFrame(self.tab)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background-color: none;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(40, 40))
        self.label_4.setPixmap(QPixmap(u":/icons/Icons/estetoscopio2.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(40, 40))
        self.label_5.setPixmap(QPixmap(u":/icons/Icons/estetoscopio2.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_7)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(40, 40))
        self.label_6.setPixmap(QPixmap(u":/icons/Icons/estetoscopio2.png"))
        self.label_6.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label_6)


        self.horizontalLayout_7.addWidget(self.frame_7)

        self.btn_back = QPushButton(self.frame_6)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setMinimumSize(QSize(120, 31))
        font3 = QFont()
        font3.setPointSize(12)
        self.btn_back.setFont(font3)
        self.btn_back.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_back.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(0,17,35);\n"
"color:rgb(255,255,255);\n"
"border-color: rgb(255,255,255);\n"
"border-radius:15px;\n"
"border: 1px solid white\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"background-color: rgb(0,71,149);\n"
"\n"
"\n"
"}\n"
"\n"
"QFrame{\n"
"\n"
"background-color: none;\n"
"\n"
"\n"
"}")

        self.horizontalLayout_7.addWidget(self.btn_back, 0, Qt.AlignRight)


        self.verticalLayout_12.addWidget(self.frame_6)

        self.frame_8 = QFrame(self.tab)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color:none;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_8)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_8 = QLabel(self.frame_8)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_10.addWidget(self.label_8)

        self.txt_question = QLineEdit(self.frame_8)
        self.txt_question.setObjectName(u"txt_question")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.txt_question.sizePolicy().hasHeightForWidth())
        self.txt_question.setSizePolicy(sizePolicy2)

        self.verticalLayout_10.addWidget(self.txt_question)


        self.verticalLayout_12.addWidget(self.frame_8)

        self.cb_level = QComboBox(self.tab)
        self.cb_level.addItem("")
        self.cb_level.addItem("")
        self.cb_level.addItem("")
        self.cb_level.setObjectName(u"cb_level")
        self.cb_level.setFont(font3)
        self.cb_level.setStyleSheet(u"background-color:none;")

        self.verticalLayout_12.addWidget(self.cb_level)

        self.frame_9 = QFrame(self.tab)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"QLabel{\n"
"\n"
"background-color:none;\n"
"color:rgb(255,255,255);\n"
"	font: 12pt \"MS Shell Dlg 2\";\n"
"\n"
"}\n"
"\n"
"QLineEdit{\n"
"\n"
"background-color:none;\n"
"\n"
"\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_9)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_9 = QLabel(self.frame_9)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_8.addWidget(self.label_9)

        self.txt_answer1 = QLineEdit(self.frame_9)
        self.txt_answer1.setObjectName(u"txt_answer1")
        self.txt_answer1.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_8.addWidget(self.txt_answer1)


        self.verticalLayout_11.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_10 = QLabel(self.frame_9)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_9.addWidget(self.label_10)

        self.txt_answer2 = QLineEdit(self.frame_9)
        self.txt_answer2.setObjectName(u"txt_answer2")
        self.txt_answer2.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_9.addWidget(self.txt_answer2)


        self.verticalLayout_11.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_11 = QLabel(self.frame_9)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_10.addWidget(self.label_11)

        self.txt_answer3 = QLineEdit(self.frame_9)
        self.txt_answer3.setObjectName(u"txt_answer3")
        self.txt_answer3.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_10.addWidget(self.txt_answer3)


        self.verticalLayout_11.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_12 = QLabel(self.frame_9)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_11.addWidget(self.label_12)

        self.txt_answer4 = QLineEdit(self.frame_9)
        self.txt_answer4.setObjectName(u"txt_answer4")
        self.txt_answer4.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_11.addWidget(self.txt_answer4)


        self.verticalLayout_11.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_13 = QLabel(self.frame_9)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_12.addWidget(self.label_13)

        self.cb_right_answer = QComboBox(self.frame_9)
        self.cb_right_answer.addItem("")
        self.cb_right_answer.addItem("")
        self.cb_right_answer.addItem("")
        self.cb_right_answer.addItem("")
        self.cb_right_answer.setObjectName(u"cb_right_answer")
        self.cb_right_answer.setFont(font3)
        self.cb_right_answer.setStyleSheet(u"background-color: none;\n"
"")

        self.horizontalLayout_12.addWidget(self.cb_right_answer)


        self.verticalLayout_11.addLayout(self.horizontalLayout_12)


        self.verticalLayout_12.addWidget(self.frame_9)

        self.btn_register = QPushButton(self.tab)
        self.btn_register.setObjectName(u"btn_register")
        self.btn_register.setMinimumSize(QSize(300, 35))
        self.btn_register.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_register.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(0,17,35);\n"
"color:rgb(255,255,255);\n"
"border-color: rgb(255,255,255);\n"
"border-radius:15px;\n"
"border: 1px solid white\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"background-color: rgb(0,71,149);\n"
"\n"
"\n"
"}\n"
"\n"
"QFrame{\n"
"\n"
"background-color: none;\n"
"\n"
"\n"
"}")
        self.btn_register.setAutoDefault(False)

        self.verticalLayout_12.addWidget(self.btn_register, 0, Qt.AlignHCenter)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_9.addWidget(self.tabWidget)

        self.Pages.addWidget(self.page_cadastrar)
        self.home_pg = QWidget()
        self.home_pg.setObjectName(u"home_pg")
        self.verticalLayout_2 = QVBoxLayout(self.home_pg)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.imglogo = QLabel(self.home_pg)
        self.imglogo.setObjectName(u"imglogo")
        self.imglogo.setEnabled(True)
        self.imglogo.setPixmap(QPixmap(u":/icons/Icons/Pergunta e Respostas.jpg"))
        self.imglogo.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.imglogo)

        self.btninicio = QPushButton(self.home_pg)
        self.btninicio.setObjectName(u"btninicio")
        self.btninicio.setMinimumSize(QSize(300, 35))
        self.btninicio.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(0,17,35);\n"
"color:rgb(255,255,255);\n"
"border-color: rgb(255,255,255);\n"
"border-radius:15px;\n"
"border: 1px solid white\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"background-color: rgb(0,71,149);\n"
"\n"
"\n"
"}\n"
"\n"
"QFrame{\n"
"\n"
"background-color: none;\n"
"\n"
"\n"
"}")

        self.verticalLayout_2.addWidget(self.btninicio, 0, Qt.AlignHCenter)

        self.Pages.addWidget(self.home_pg)

        self.verticalLayout.addWidget(self.Pages)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(3)
        self.btn_convidados.setDefault(False)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.btnjogar.setText(QCoreApplication.translate("MainWindow", u"Come\u00e7ar jogo", None))
        self.btncadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Perguntas", None))
        self.btnsair.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">Clique em novo jogo para Iniciar</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:12pt; font-weight:600;\">Perguntas e Respostas</span></p><p align=\"right\"><span style=\" font-size:12pt; font-weight:600;\">Medicina</span></p></body></html>", None))
        self.btn_resp1.setText("")
        self.btn_resp2.setText("")
        self.btn_resp4.setText("")
        self.btn_resp3.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">AJUDA</span></p></body></html>", None))
        self.btn_convidados.setText(QCoreApplication.translate("MainWindow", u"Pacientes", None))
        self.btn_cartas.setText(QCoreApplication.translate("MainWindow", u"Doutores", None))
        self.btn_pular.setText(QCoreApplication.translate("MainWindow", u"PULAR", None))
        self.btn_pular1.setText(QCoreApplication.translate("MainWindow", u"PULAR", None))
        self.btn_pular2.setText(QCoreApplication.translate("MainWindow", u"PULAR", None))
        self.btnparar.setText(QCoreApplication.translate("MainWindow", u"QUERO PARAR", None))
        self.lbl_errar.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">00</p><p align=\"center\">PARAR</p></body></html>", None))
        self.lbl_acertar.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">00</p><p align=\"center\">PARAR</p></body></html>", None))
        self.lbl_parar.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">00</p><p align=\"center\">PARAR</p></body></html>", None))
        self.btn_backmenu.setText(QCoreApplication.translate("MainWindow", u"Voltar ao Menu", None))
        self.btn_novojogo.setText(QCoreApplication.translate("MainWindow", u"Novo Jogo", None))
        self.label_4.setText("")
        self.label_5.setText("")
        self.label_6.setText("")
        self.btn_back.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Pergunta:</span></p></body></html>", None))
        self.cb_level.setItemText(0, QCoreApplication.translate("MainWindow", u"F\u00e1cil", None))
        self.cb_level.setItemText(1, QCoreApplication.translate("MainWindow", u"M\u00e9dio", None))
        self.cb_level.setItemText(2, QCoreApplication.translate("MainWindow", u"Dif\u00edcil", None))

        self.label_9.setText(QCoreApplication.translate("MainWindow", u"1:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"2:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"3:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"4:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Resposta Certa:", None))
        self.cb_right_answer.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.cb_right_answer.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.cb_right_answer.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.cb_right_answer.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))

        self.btn_register.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Cadastrar Perguntas", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Importar Perguntas", None))
        self.imglogo.setText("")
        self.btninicio.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
    # retranslateUi

