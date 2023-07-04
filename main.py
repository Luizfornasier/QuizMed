import random
from PySide6.QtWidgets import *
from PySide6.QtCore import QCoreApplication,QSize,Qt
from PySide6.QtGui import QIcon
from ui_main import Ui_MainWindow
import sys
from database import Data_base
from ui_pacientes import Ui_Pacientes
from ui_doutores import Ui_Doutores

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Quiz MedShow")
        appIcons= QIcon(u":/icons/Icons/estetoscopio2.png")
        self.setWindowIcon(appIcons)
        self.num_perguntas = 0

        ##############################################
        #Pontuação
        self.errar = 0
        self.acertar = 0
        self.parar = 0


        ##############################################
        #PÁGINAS DO SISTEMA
        self.btninicio.clicked.connect(lambda: self.Pages.setCurrentWidget(self.inicio_pg))
        self.btnjogar.clicked.connect(lambda: self.Pages.setCurrentWidget(self.game_pg))
        self.btncadastrar.clicked.connect(lambda: self.Pages.setCurrentWidget(self.page_cadastrar))
        self.btn_backmenu.clicked.connect(lambda: self.Pages.setCurrentWidget(self.inicio_pg))
        self.btn_back.clicked.connect(lambda: self.Pages.setCurrentWidget(self.home_pg))
        ##############################################

        ##############################################
        #PULAR
        self.btn_pular.clicked.connect(lambda: self.pular(1))
        self.btn_pular1.clicked.connect(lambda: self.pular(2))
        self.btn_pular2.clicked.connect(lambda: self.pular(3))
        
        #######Cadastra Pergunta
        self.btn_register.clicked.connect(self.cadastrar_nova_pergunta)
        
        ##############################################
        #Pacientes
        self.btn_convidados.clicked.connect(self.pacientes)

        ##############################################
        #Doutores
        self.btn_cartas.clicked.connect(self.odoutor)

        #############################################
        #Parar
        self.btnparar.clicked.connect(self.parargame)
            
        
        #######Confirma Resposta
        self.btn_resp1.clicked.connect(lambda: self.confirmar_resposta('1'))
        self.btn_resp2.clicked.connect(lambda: self.confirmar_resposta('2'))
        self.btn_resp3.clicked.connect(lambda: self.confirmar_resposta('3'))
        self.btn_resp4.clicked.connect(lambda: self.confirmar_resposta('4'))


        self.btn_novojogo.clicked.connect(self.jogar)
        

    def cadastrar_nova_pergunta(self):
        db= Data_base()
        db.connect()
        db.criare_tabela_perguntas()

        if (self.txt_answer1.text() == "" or self.txt_answer2.text() =='' 
        or self.txt_answer3.text() =='' or self.txt_answer4.text() ==''):
            msg=QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Favor preencher todos os campos!")
            msg.exec()
            return
        pergunta = [self.txt_question.text(), self.cb_level.currentText(), self.txt_answer1.text(),
                    self.txt_answer2.text(),self.txt_answer3.text(),self.txt_answer4.text(),
                    self.cb_right_answer.currentText()]
        
        resp = db.cadastrar_pergunta(pergunta)

        if resp.lower() == 'ok':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText('Pergunta cadastrada com sucesso!')
            msg.exec()

            self.txt_question.setText('')
            self.txt_answer1.setText('')
            self.txt_answer2.setText('')
            self.txt_answer3.setText('')
            self.txt_answer4.setText('')
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Falha ao cadastrar a pergunta.')
            msg.exec()

    def jogar(self):

        msg = QMessageBox()
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setText("Deseja começar um novo jogo?")
        msg.setIcon(QMessageBox.Question)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            db = Data_base()
            self.num_perguntas = 0

            self.perguntas_faceis = db.selecionar_pergunta("Fácil")
            self.perguntas_medias = db.selecionar_pergunta('Médio')
            self.perguntas_dificeis = db.selecionar_pergunta('Difícil')

            self.selecionar_perguntas()

    def parargame(self):
        msg = QMessageBox()
        msg.setWindowTitle("Fim de jogo!")
        msg.setText(f"Sua pontuação foi de:{str(self.parar)} pontos")
        msg.setIcon(QMessageBox.Information)
        msg.exec()
        self.selecionar_perguntas()

        self.lbl_errar.setText(QCoreApplication.translate("MainWindow", f"<html><head/><body><p align=\"center\">0</p><p align=\"center\">PARAR</p></body></html>", None))
        self.lbl_parar.setText(QCoreApplication.translate("MainWindow", f"<html><head/><body><p align=\"center\">0</p><p align=\"center\">PARAR</p></body></html>", None))
        self.lbl_acertar.setText(QCoreApplication.translate("MainWindow", f"<html><head/><body><p align=\"center\">0</p><p align=\"center\">PARAR</p></body></html>", None))
        self.num_perguntas = 0


    def selecionar_perguntas(self):
        
        if self.num_perguntas <= 5:
            pergunta = self.perguntas_faceis[random.randint(0,len(self.perguntas_faceis)-1)]
            self.perguntas_faceis.remove(pergunta)

        elif self.num_perguntas >5 and self.num_perguntas <=10:
            pergunta = self.perguntas_medias[random.randint(0,len(self.perguntas_medias)-1)]
            self.perguntas_medias.remove(pergunta)
        
        elif self.num_perguntas >10 and self.num_perguntas <=15:
            pergunta = self.perguntas_dificeis[random.randint(0,len(self.perguntas_dificeis)-1)]
            self.perguntas_dificeis.remove(pergunta)
            
        else:
            print("Win")

        self.label_2.setText(pergunta[1])
        self.label_2.setStyleSheet(u"background-color: rgb(105, 186, 252);\n"
        "border-radius: 15px;\n"
        'font: bold 14pt;\n'
        "border: 2px solid white;\n"
        "color: rgb(255, 255, 255);")
        self.label_2.setWordWrap(True)
        
        self.btn_resp1.setText(pergunta[3])
        self.btn_resp2.setText(pergunta[4])
        self.btn_resp3.setText(pergunta[5])
        self.btn_resp4.setText(pergunta[6])

        self.resp_certa = pergunta[7]

        self.num_perguntas +=1

    def confirmar_resposta(self, s):

        msg = QMessageBox()
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setText("Confirma sua resposta?")
        msg.setIcon(QMessageBox.Question)
        resp = msg.exec()

        resposta_certa = False

        if resp == QMessageBox.Yes:
            
            if s == '1' and self.resp_certa == '1':
                resposta_certa = True
                self.btn_resp1.setStyleSheet(u"""
                                QCommandLinkButton{
                                    background-color: rgb(79, 238, 0);
                                    border-radius: 15px;
                                    border: 2px solid white;
                                    color: rgb(255, 255, 255);}
                                QCommandLinkButton:hover{
                                    background-color: rgb(0, 170, 255);
                                }""")
                msg = QMessageBox()
                msg.setWindowTitle("Resposta")
                msg.setText("Resposta Certa!")
                msg.setIcon(QMessageBox.Information)
                msg.exec()
            elif s == '2' and self.resp_certa == '2':
                resposta_certa = True
                self.btn_resp2.setStyleSheet(u"""
                                QCommandLinkButton{
                                    background-color: rgb(79, 238, 0);
                                    border-radius: 15px;
                                    border: 2px solid white;
                                    color: rgb(255, 255, 255);}
                                QCommandLinkButton:hover{
                                    background-color: rgb(0, 170, 255);
                                }""")
                msg = QMessageBox()
                msg.setWindowTitle("Resposta")
                msg.setText("Resposta Certa!")
                msg.setIcon(QMessageBox.Information)
                msg.exec()
            elif s == '3' and self.resp_certa == '3':
                resposta_certa = True
                self.btn_resp3.setStyleSheet(u"""
                                QCommandLinkButton{
                                    background-color: rgb(79, 238, 0);
                                    border-radius: 15px;
                                    border: 2px solid white;
                                    color: rgb(255, 255, 255);}
                                QCommandLinkButton:hover{
                                    background-color: rgb(0, 170, 255);
                                }""")
                msg = QMessageBox()
                msg.setWindowTitle("Resposta")
                msg.setText("Resposta Certa!")
                msg.setIcon(QMessageBox.Information)
                msg.exec()
            elif s == '4' and self.resp_certa == '4':
                resposta_certa = True
                self.btn_resp4.setStyleSheet(u"""
                                QCommandLinkButton{
                                    background-color: rgb(79, 238, 0);
                                    border-radius: 15px;
                                    border: 2px solid white;
                                    color: rgb(255, 255, 255);}
                                QCommandLinkButton:hover{
                                    background-color: rgb(0, 170, 255);
                                }""")
                msg = QMessageBox()
                msg.setWindowTitle("Resposta")
                msg.setText("Resposta Certa!")
                msg.setIcon(QMessageBox.Information)
                msg.exec()
        
            else:
                
                self.num_perguntas = 0

                if self.resp_certa == '1':
                    self.btn_resp1.setStyleSheet(u"""
                                        QCommandLinkButton{
                                            background-color: rgb(79, 238, 0);
                                            border-radius: 15px;
                                            border: 2px solid white;
                                            color: rgb(255, 255, 255);}
                                        QCommandLinkButton:hover{
                                            background-color: rgb(0, 170, 255);
                                        }""")        
                if self.resp_certa == '2':
                    self.btn_resp2.setStyleSheet(u"""
                                        QCommandLinkButton{
                                            background-color: rgb(79, 238, 0);
                                            border-radius: 15px;
                                            border: 2px solid white;
                                            color: rgb(255, 255, 255);}
                                        QCommandLinkButton:hover{
                                            background-color: rgb(0, 170, 255);
                                        }""")
                if self.resp_certa == '3':
                    self.btn_resp3.setStyleSheet(u"""
                                        QCommandLinkButton{
                                            background-color: rgb(79, 238, 0);
                                            border-radius: 15px;
                                            border: 2px solid white;
                                            color: rgb(255, 255, 255);}
                                        QCommandLinkButton:hover{
                                            background-color: rgb(0, 170, 255);
                                        }""")
                if self.resp_certa == '4':
                    self.btn_resp4.setStyleSheet(u"""
                                        QCommandLinkButton{
                                            background-color: rgb(79, 238, 0);
                                            border-radius: 15px;
                                            border: 2px solid white;
                                            color: rgb(255, 255, 255);}
                                        QCommandLinkButton:hover{
                                            background-color: rgb(0, 170, 255);
                                        }""")
                    
                msg = QMessageBox()
                msg.setWindowTitle("Resposta")
                msg.setText("Resposta Errada!")
                msg.setIcon(QMessageBox.Critical)
                msg.exec()

        #####zerar pontuação

                self.formatar_resposta()
                self.calcular_pontuacao()

        if resposta_certa:
            self.selecionar_perguntas()
            self.formatar_resposta()
            self.calcular_pontuacao()

        else:
            msg = QMessageBox()
            msg.setWindowTitle("Resposta")
            msg.setText(f"Resposta Errada! \n sua pontuação foi de: {self.errar} pontos" )
            msg.setIcon(QMessageBox.Critical)
            msg.exec()

    def pacientes(self):
        self.x = Pacientes_window(self.resp_certa)
        self.x.show()
        self.btn_convidados.setEnabled(False)
        self.btn_convidados.setStyleSheet("QPushButton{background-color: rgb(148,148,148)}")

    def odoutor(self, c):
                doutoresx = random.randint(1,4)
                self.w = Doutores_window(doutoresx)
                self.w.setFocusPolicy(Qt.StrongFocus)
                self.w.show()

                self.btn_cartas.setEnabled(False)
                self.btn_cartas.setStyleSheet("QPushButton{background-color: rgb(148,148,148)}")

                if doutoresx == 4:
                    return
                
                resp = [1,2,3,4]
                resp.remove(int(self.resp_certa))

                if doutoresx == 1:
                    resp.remove(random.choice(resp))
                elif doutoresx == 2:
                    resp.remove(random.choice(resp))
                    resp.remove(random.choice(resp))
                elif doutoresx == 3:
                    resp.remove(random.choice(resp))
                    resp.remove(random.choice(resp))
                    resp.remove(random.choice(resp))
                
                resp.append(int(self.resp_certa))

                if 1 not in resp:
                    self.btn_resp1.setText("")
                if 2 not in resp:
                    self.btn_resp2.setText("")
                if 3 not in resp:
                    self.btn_resp3.setText("")
                if 4 not in resp:
                    self.btn_resp4.setText("")
                    
    def pular(self, n_pulo):
        if n_pulo == 1:
            self.btn_pular.setEnabled(False)
            self.btn_pular.setStyleSheet("QPushButton{background-color: rgb(148,148,148)}")
        elif n_pulo == 2:
            self.btn_pular1.setEnabled(False)
            self.btn_pular1.setStyleSheet("QPushButton{background-color: rgb(148,148,148)}")
        elif n_pulo == 3:
            self.btn_pular2.setEnabled(False)
            self.btn_pular2.setStyleSheet("QPushButton{background-color: rgb(148,148,148)}")
        self.selecionar_perguntas()
        
    def formatar_resposta(self):
        lista = [self.btn_resp1,self.btn_resp2,self.btn_resp3,self.btn_resp4]

        for btn in lista:
            btn.setStyleSheet(u"""
        
                                        QCommandLinkButton{

                                            background-color: rgb(0,17,35); 
                                            color:rgb(255,255,255);
                                            border-color: rgb(255,255,255);
                                            border-radius:15px;
                                            border: 1px solid white



                                    }

                                        QCommandLinkButton:hover{

                                            background-color: rgb(0,71,149);
                                                        }
            """)

    def calcular_pontuacao(self):
        self.errar = (self.num_perguntas * 10) /2
        self.acertar = (self.num_perguntas * 10 + 10)
        self.parar = self.num_perguntas * 10

        self.lbl_errar.setText(QCoreApplication.translate("MainWindow", f"<html><head/><body><p align=\"center\">{self.errar}</p><p align=\"center\">PARAR</p></body></html>", None))
        self.lbl_parar.setText(QCoreApplication.translate("MainWindow", f"<html><head/><body><p align=\"center\">{self.parar}</p><p align=\"center\">PARAR</p></body></html>", None))
        self.lbl_acertar.setText(QCoreApplication.translate("MainWindow", f"<html><head/><body><p align=\"center\">{self.acertar}</p><p align=\"center\">PARAR</p></body></html>", None))

class Doutores_window(QWidget, Ui_Doutores):
    def __init__(self, doutoresx) -> None:
        super(Doutores_window, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Doutores")

        self.selecionados_doutores = ''
        self.btndr1.clicked.connect(lambda: self.selecionar_cartas(1))
        self.btndr2.clicked.connect(lambda: self.selecionar_cartas(2))
        self.btdr3.clicked.connect(lambda: self.selecionar_cartas(3))
        self.btndr4.clicked.connect(lambda: self.selecionar_cartas(4))
        self.doutoresx = doutoresx

    def selecionar_cartas(self, c):
        icon = QIcon()
 
        if c == 1:
            icon.addFile(f":/icons/Icons/carta_{self.doutoresx}.png", QSize(), QIcon.Normal, QIcon.Off)
            self.btndr1.setIcon(icon)
            self.btndr2.setDisabled(True)
            self.btdr3.setDisabled(True)
            self.btndr4.setDisabled(True)
            self.selecionados_doutores = self.doutoresx

        elif c == 2:
            icon.addFile(f":/icons/Icons/carta_{self.doutoresx}.png", QSize(), QIcon.Normal, QIcon.Off)
            self.btndr2.setIcon(icon)
            self.btndr1.setDisabled(True)
            self.btdr3.setDisabled(True)
            self.btndr4.setDisabled(True)
            self.selecionados_doutores = self.doutoresx

        elif c == 3:
            icon.addFile(f":/icons/Icons/carta_{self.doutoresx}.png", QSize(), QIcon.Normal, QIcon.Off)
            self.btdr3.setIcon(icon)
            self.btndr1.setDisabled(True)
            self.btndr2.setDisabled(True)
            self.btndr4.setDisabled(True)
            self.selecionados_doutores = self.doutoresx

        elif c == 4:
            icon.addFile(f":/icons/Icons/carta_{self.doutoresx}.png", QSize(), QIcon.Normal, QIcon.Off)
            self.btndr4.setIcon(icon)
            self.btndr1.setDisabled(True)
            self.btndr2.setDisabled(True)
            self.btdr3.setDisabled(True)
            self.selecionados_doutores = self.doutoresx

class Pacientes_window(QWidget, Ui_Pacientes):
    def __init__(self, resposta_certa):
        super(Pacientes_window, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Pacientes")
        
        lista = [resposta_certa,resposta_certa,resposta_certa,resposta_certa,resposta_certa,resposta_certa,1,2,3,4,4]

        self.lblalt1.setText(QCoreApplication.translate("Pacientes", f"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Alternativa: {lista[random.randint(0,9)]}</span></p></body></html>", None))
        self.lblalt2.setText(QCoreApplication.translate("Pacientes", f"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Alternativa: {lista[random.randint(0,9)]}</span></p></body></html>", None))
        self.lblalt3.setText(QCoreApplication.translate("Pacientes", f"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Alternativa: {lista[random.randint(0,9)]}</span></p></body></html>", None))

if __name__ == '__main__':
    app = QApplication()
    window =MainWindow()
    window.show()
    app.exec()
