# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/hda5/develop/radj/new/main.ui'
#
# Created: Thu Jul 17 22:24:26 2008
#      by: PyQt4 UI code generator 4.0.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,755,705).size()).expandedTo(MainWindow.minimumSizeHint()))

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)

        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        self.gridlayout = QtGui.QGridLayout(self.centralWidget)
        self.gridlayout.setMargin(9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.label_current_music = QtGui.QLabel(self.centralWidget)

        font = QtGui.QFont(self.label_current_music.font())
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_current_music.setFont(font)
        self.label_current_music.setObjectName("label_current_music")
        self.vboxlayout.addWidget(self.label_current_music)

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setSpacing(2)
        self.hboxlayout.setObjectName("hboxlayout")

        self.text_music_current = QtGui.QTextBrowser(self.centralWidget)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_music_current.sizePolicy().hasHeightForWidth())
        self.text_music_current.setSizePolicy(sizePolicy)
        self.text_music_current.setMaximumSize(QtCore.QSize(321,111))
        self.text_music_current.setObjectName("text_music_current")
        self.hboxlayout.addWidget(self.text_music_current)

        self.volume_current = QtGui.QSlider(self.centralWidget)
        self.volume_current.setMaximumSize(QtCore.QSize(16,101))
        self.volume_current.setOrientation(QtCore.Qt.Vertical)
        self.volume_current.setObjectName("volume_current")
        self.hboxlayout.addWidget(self.volume_current)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.gridlayout.addLayout(self.vboxlayout,1,0,1,1)

        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.label_next_music = QtGui.QLabel(self.centralWidget)

        font = QtGui.QFont(self.label_next_music.font())
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_next_music.setFont(font)
        self.label_next_music.setObjectName("label_next_music")
        self.vboxlayout1.addWidget(self.label_next_music)

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setMargin(0)
        self.hboxlayout1.setSpacing(2)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.text_music_next = QtGui.QTextBrowser(self.centralWidget)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_music_next.sizePolicy().hasHeightForWidth())
        self.text_music_next.setSizePolicy(sizePolicy)
        self.text_music_next.setMaximumSize(QtCore.QSize(256,111))
        self.text_music_next.setObjectName("text_music_next")
        self.hboxlayout1.addWidget(self.text_music_next)

        self.volume_next = QtGui.QSlider(self.centralWidget)
        self.volume_next.setMaximumSize(QtCore.QSize(15,101))
        self.volume_next.setOrientation(QtCore.Qt.Vertical)
        self.volume_next.setObjectName("volume_next")
        self.hboxlayout1.addWidget(self.volume_next)
        self.vboxlayout1.addLayout(self.hboxlayout1)
        self.gridlayout.addLayout(self.vboxlayout1,3,0,1,1)

        self.vboxlayout2 = QtGui.QVBoxLayout()
        self.vboxlayout2.setMargin(0)
        self.vboxlayout2.setSpacing(6)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.label_previous_music = QtGui.QLabel(self.centralWidget)

        font = QtGui.QFont(self.label_previous_music.font())
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_previous_music.setFont(font)
        self.label_previous_music.setTextFormat(QtCore.Qt.RichText)
        self.label_previous_music.setObjectName("label_previous_music")
        self.vboxlayout2.addWidget(self.label_previous_music)

        self.text_music_previous = QtGui.QTextBrowser(self.centralWidget)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_music_previous.sizePolicy().hasHeightForWidth())
        self.text_music_previous.setSizePolicy(sizePolicy)
        self.text_music_previous.setMaximumSize(QtCore.QSize(16777215,111))
        self.text_music_previous.setObjectName("text_music_previous")
        self.vboxlayout2.addWidget(self.text_music_previous)
        self.gridlayout.addLayout(self.vboxlayout2,0,0,1,1)

        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setMargin(0)
        self.hboxlayout2.setSpacing(6)
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.label_remaining_music_time = QtGui.QLabel(self.centralWidget)
        self.label_remaining_music_time.setObjectName("label_remaining_music_time")
        self.hboxlayout2.addWidget(self.label_remaining_music_time)

        self.timeEdit = QtGui.QTimeEdit(self.centralWidget)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeEdit.sizePolicy().hasHeightForWidth())
        self.timeEdit.setSizePolicy(sizePolicy)
        self.timeEdit.setMaximumSize(QtCore.QSize(80,21))
        self.timeEdit.setWrapping(False)
        self.timeEdit.setFrame(True)
        self.timeEdit.setReadOnly(True)
        self.timeEdit.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        #self.timeEdit.setAccelerated(False)
        self.timeEdit.setObjectName("timeEdit")
        self.hboxlayout2.addWidget(self.timeEdit)
        self.gridlayout.addLayout(self.hboxlayout2,2,0,1,1)

        self.vboxlayout3 = QtGui.QVBoxLayout()
        self.vboxlayout3.setMargin(0)
        self.vboxlayout3.setSpacing(2)
        self.vboxlayout3.setObjectName("vboxlayout3")

        self.list_music = QtGui.QListWidget(self.centralWidget)
        self.list_music.setObjectName("list_music")
        self.vboxlayout3.addWidget(self.list_music)
        self.gridlayout.addLayout(self.vboxlayout3,0,1,4,1)

        self.hboxlayout3 = QtGui.QHBoxLayout()
        self.hboxlayout3.setMargin(0)
        self.hboxlayout3.setSpacing(2)
        self.hboxlayout3.setObjectName("hboxlayout3")

        self.music_trackbar = QtGui.QSlider(self.centralWidget)
        self.music_trackbar.setOrientation(QtCore.Qt.Horizontal)
        self.music_trackbar.setObjectName("music_trackbar")
        self.hboxlayout3.addWidget(self.music_trackbar)
        self.gridlayout.addLayout(self.hboxlayout3,4,0,1,2)
        MainWindow.setCentralWidget(self.centralWidget)

        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0,0,755,28))
        self.menuBar.setObjectName("menuBar")

        self.menuArquivo = QtGui.QMenu(self.menuBar)
        self.menuArquivo.setObjectName("menuArquivo")

        self.menuA_es = QtGui.QMenu(self.menuBar)
        self.menuA_es.setObjectName("menuA_es")

        self.menuEditar = QtGui.QMenu(self.menuBar)
        self.menuEditar.setObjectName("menuEditar")
        MainWindow.setMenuBar(self.menuBar)

        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setOrientation(QtCore.Qt.Horizontal)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(self.toolBar)

        self.toolBar_2 = QtGui.QToolBar(MainWindow)
        self.toolBar_2.setOrientation(QtCore.Qt.Horizontal)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(self.toolBar_2)

        self.action_Abrir = QtGui.QAction(MainWindow)
        self.action_Abrir.setIcon(QtGui.QIcon("images/fileopen.png"))
        self.action_Abrir.setObjectName("action_Abrir")

        self.action_Sair = QtGui.QAction(MainWindow)
        self.action_Sair.setIcon(QtGui.QIcon("images/exit.png"))
        self.action_Sair.setObjectName("action_Sair")

        self.action_Parar = QtGui.QAction(MainWindow)
        self.action_Parar.setIcon(QtGui.QIcon("images/player_stop.png"))
        self.action_Parar.setObjectName("action_Parar")

        self.action_Proximo = QtGui.QAction(MainWindow)
        self.action_Proximo.setIcon(QtGui.QIcon("images/player_fwd.png"))
        self.action_Proximo.setObjectName("action_Proximo")

        self.action_Anterior = QtGui.QAction(MainWindow)
        self.action_Anterior.setIcon(QtGui.QIcon("images/player_rew.png"))
        self.action_Anterior.setObjectName("action_Anterior")

        self.action_Primeiro_da_Lista = QtGui.QAction(MainWindow)
        self.action_Primeiro_da_Lista.setIcon(QtGui.QIcon("images/player_start.png"))
        self.action_Primeiro_da_Lista.setObjectName("action_Primeiro_da_Lista")

        self.action_Ultimo_da_Lista = QtGui.QAction(MainWindow)
        self.action_Ultimo_da_Lista.setIcon(QtGui.QIcon("images/player_end.png"))
        self.action_Ultimo_da_Lista.setObjectName("action_Ultimo_da_Lista")

        self.action_Pausa_apos_proximo = QtGui.QAction(MainWindow)
        self.action_Pausa_apos_proximo.setIcon(QtGui.QIcon("images/player_time.png"))
        self.action_Pausa_apos_proximo.setObjectName("action_Pausa_apos_proximo")

        self.action_Tocar_Pausar = QtGui.QAction(MainWindow)
        self.action_Tocar_Pausar.setIcon(QtGui.QIcon("images/player_play.png"))
        self.action_Tocar_Pausar.setObjectName("action_Tocar_Pausar")
        self.menuArquivo.addAction(self.action_Abrir)
        self.menuArquivo.addSeparator()
        self.menuArquivo.addAction(self.action_Sair)
        self.menuA_es.addAction(self.action_Tocar_Pausar)
        self.menuA_es.addAction(self.action_Parar)
        self.menuA_es.addAction(self.action_Proximo)
        self.menuA_es.addAction(self.action_Anterior)
        self.menuA_es.addSeparator()
        self.menuA_es.addAction(self.action_Primeiro_da_Lista)
        self.menuA_es.addAction(self.action_Ultimo_da_Lista)
        self.menuA_es.addSeparator()
        self.menuA_es.addAction(self.action_Pausa_apos_proximo)
        self.menuBar.addAction(self.menuArquivo.menuAction())
        self.menuBar.addAction(self.menuEditar.menuAction())
        self.menuBar.addAction(self.menuA_es.menuAction())
        self.toolBar.addAction(self.action_Tocar_Pausar)
        self.toolBar.addAction(self.action_Pausa_apos_proximo)
        self.toolBar.addAction(self.action_Parar)
        self.toolBar.addAction(self.action_Primeiro_da_Lista)
        self.toolBar.addAction(self.action_Anterior)
        self.toolBar.addAction(self.action_Proximo)
        self.toolBar.addAction(self.action_Ultimo_da_Lista)
        self.toolBar_2.addAction(self.action_Abrir)
        self.toolBar_2.addAction(self.action_Sair)
        self.toolBar_2.addSeparator()

        self.retranslateUi(MainWindow)
        self.set_all_connections(MainWindow)
        self.call_init()

    def set_all_connections(self,MainWindow):
        print "to-do"

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label_current_music.setText(QtGui.QApplication.translate("MainWindow", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; color:#ff0000;\">Música Atual</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_next_music.setText(QtGui.QApplication.translate("MainWindow", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Próxima Música</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_previous_music.setText(QtGui.QApplication.translate("MainWindow", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:600; font-style:normal; text-decoration:none;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#a9a9a9;\">Música Anterior</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_remaining_music_time.setText(QtGui.QApplication.translate("MainWindow", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ff0000;\">Tempo Remanescente</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.menuArquivo.setTitle(QtGui.QApplication.translate("MainWindow", "Arquivo", None, QtGui.QApplication.UnicodeUTF8))
        self.menuA_es.setTitle(QtGui.QApplication.translate("MainWindow", "Ações", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEditar.setTitle(QtGui.QApplication.translate("MainWindow", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Abrir.setText(QtGui.QApplication.translate("MainWindow", "Abrir", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Sair.setText(QtGui.QApplication.translate("MainWindow", "Sair", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Parar.setText(QtGui.QApplication.translate("MainWindow", "Parar", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Proximo.setText(QtGui.QApplication.translate("MainWindow", "Próximo", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Anterior.setText(QtGui.QApplication.translate("MainWindow", "Anterior", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Primeiro_da_Lista.setText(QtGui.QApplication.translate("MainWindow", "Primeiro da Lista", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Ultimo_da_Lista.setText(QtGui.QApplication.translate("MainWindow", "Último da Lista", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Pausa_apos_proximo.setText(QtGui.QApplication.translate("MainWindow", "Pausa após o próximo", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Tocar_Pausar.setText(QtGui.QApplication.translate("MainWindow", "Tocar/Pausar", None, QtGui.QApplication.UnicodeUTF8))

    def Tocar_Pausar(self):
        print "to-do"

    def Pausa_apos_Proximo(self):
        print "to-do"

    def Parar(self):
        print "to-do"

    def Primeiro_da_Lista(self):
        print "to-do"

    def Anterior(self):
        print "to-do"

    def Proximo(self):
        print "to-do"

    def Ultimo_da_Lista(self):
        print "to-do"
