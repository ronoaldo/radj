#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
from PyQt4 import QtCore, QtGui
import Ui_main
from MPlayerSlave import MPlayerSlave
import threading, time

class Radj(Ui_main.Ui_MainWindow):
    def call_init(self):
        self.player = MPlayerSlave(), MPlayerSlave()

    def set_all_connections(self,MainWindow):
        QtCore.QObject.connect(self.action_Sair,
                               QtCore.SIGNAL("activated()"),self.Fechar)
        QtCore.QObject.connect(self.action_Abrir,
                               QtCore.SIGNAL("activated()"),self.Abrir)
        QtCore.QObject.connect(self.action_Tocar_Pausar,
                               QtCore.SIGNAL("activated()"),self.Tocar_Pausar)
        QtCore.QObject.connect(self.action_Pausa_apos_proximo,
                               QtCore.SIGNAL("activated()"),self.Pausa_apos_Proximo)
        QtCore.QObject.connect(self.action_Parar,
                               QtCore.SIGNAL("activated()"),self.Parar)
        QtCore.QObject.connect(self.action_Primeiro_da_Lista,
                               QtCore.SIGNAL("activated()"),self.Primeiro_da_Lista)
        QtCore.QObject.connect(self.action_Anterior,
                               QtCore.SIGNAL("activated()"),self.Anterior)
        QtCore.QObject.connect(self.action_Proximo,
                               QtCore.SIGNAL("activated()"),self.Proximo)
        QtCore.QObject.connect(self.action_Ultimo_da_Lista,
                               QtCore.SIGNAL("activated()"),self.Ultimo_da_Lista)
        QtCore.QObject.connect(self.list_music,
                               QtCore.SIGNAL("itemActivated(QListWidgetItem*)"),self.Lista_Ativado)
        QtCore.QObject.connect(self.list_music,
                               QtCore.SIGNAL("currentRowChanged(int)"), self.Lista_Mudou_Item)
        QtCore.QObject.connect(MainWindow,
                               QtCore.SIGNAL("close()"), self.Fechar)

        MainWindow.showMaximized()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    """
        Retorna qual o Player que está tocando
        -1: nenhum dos dois
         0: player 0
         1: player 1
         2: os dois //acontece na transição de faixas
    """
    def __Qual_Player_Toca(self):
        tmp_0 = self.player[0].is_playing()
        tmp_1 = self.player[1].is_playing()
        if   tmp_0 + tmp_1 == 0: return -1
        elif tmp_0 + tmp_1 == 2: return 2
        elif tmp_0 == 1: return 0
        else: return 1

    def __Tocar_Musica_Posicao(self,pos,tocar=True):
        self.list_music.setCurrentRow(pos)
        self.Tocar_Pausar()

    def Fechar(self):
        resp = QtGui.QMessageBox.question(None,"Sair do Programa", "Deseja realmente Sair?",
                                          QtCore.QString.fromUtf8("Não"), "Sim")
        if resp == 1:
            tmp = self.__Qual_Player_Toca()
            # se nenhum toca, nao tenta parar
            if tmp <> -1:
                try:
                    # se os dois tocam, para os dois
                    if tmp == 2:
                        self.__Crossfade(None,"wait")
                        self.__Posicao_Barra(None,"wait")
                        self.player[0].stop()
                        self.player[1].stop()
                    # senao para o que esta tocando
                    else:
                        self.player[tmp].stop()
                except:
                    pass
            sys.exit()

    def Abrir(self):
        filename=QtGui.QFileDialog.getOpenFileNames(None, "Abrir Arquivos", "", "*.mp3")
        self.list_music.addItems(filename)
        if self.list_music.currentRow() == -1:
            self.list_music.setCurrentRow(0)
            self.list_music.setFocus()

    def Tocar_Pausar(self):
        ##########################################
        #codigo original: sem pausar
        #tmp = self.__Qual_Player_Toca()
        #if tmp <> 2:
            #musica=self.list_music.currentItem().text()
            #if   tmp == -1:
                #self.player[0].play(musica)
            #else:
                #self.efeito=Crossfade(self.player[tmp])
                #self.efeito.start()
                #self.player[ (tmp+1)%2 ].play(musica)
            #self.Music_Info( (tmp+1)%2 )
        ##########################################
        tmp = self.__Qual_Player_Toca()
        #se os dois tocam, o kra espera parar a transicao
        if tmp <> 2:
            musica=self.list_music.currentItem().text()
            #se nenhum toca, nao tem pausa
            if tmp == -1:
                self.player[0].play(musica)
                self.Music_Info(0)
                self.__Posicao_Barra(self.player[0])
            else:
                # tmp -> está tocando, (tmp+1)%2 -> vai tocar
                # se é a mesma música que está tocando, deve pausar
                if self.player[tmp].about_music().get_path() == musica:
                    self.player[tmp].pause()
                else:
                    self.__Crossfade(self.player[tmp])
                    self.player[ (tmp+1)%2 ].play(musica)
                    self.Music_Info( (tmp+1)%2 )
                    self.__Posicao_Barra(self.player[ (tmp+1)%2 ])
            self.list_music.setCurrentRow(self.list_music.currentRow()+1)

    def __Crossfade(self, player, o_que_fazer="run"):
        try: self.efeito.join()
        except: pass
        if o_que_fazer == "run":
            self.efeito = Crossfade(player)
            self.efeito.start()

    def __Posicao_Barra(self, player, o_que_fazer="run"):
        try: self.pos.join()
        except: pass
        if o_que_fazer == "run":
            self.pos_barra = Posicao_Barra(self, player, self.music_trackbar, self.Tocar_Pausar)
            self.pos_barra.start()

    def Pausa_apos_Proximo(self):
        print "to-do"

    def Parar(self):
        tmp=self.__Qual_Player_Toca()
        self.player[tmp].stop()

    def Primeiro_da_Lista(self):
        self.__Tocar_Musica_Posicao(0)

    def Anterior(self):
        if self.list_music.currentRow() == 0:
            self.Ultimo_da_Lista()
        else:
            self.__Tocar_Musica_Posicao(self.list_music.currentRow()-1)

    def Proximo(self):
        if self.list_music.currentRow() == self.list_music.count()-1:
            self.Primeiro_da_Lista()
        else:
            self.__Tocar_Musica_Posicao(self.list_music.currentRow()+1)

    def Ultimo_da_Lista(self):
        self.__Tocar_Musica_Posicao(self.list_music.count()-1)

    def Lista_Ativado(self,item):
        self.Tocar_Pausar()

    def Lista_Mudou_Item(self, item):
        try:
            musica=self.list_music.item(item).text().split("/")[-1].split(".")[0]
        except:
            musica=""
        self.Inserir_Texto(self.text_music_next,musica)

    def Inserir_Texto(self, onde, texto):
        font_size = 8
        t = "<font size=%d>%s</font>" % (font_size, texto)
        onde.setHtml(t)
        #onde.insertPlainText(texto)

    def Music_Info(self, qual):
        while not self.player[qual].head_readed:
            time.sleep(0.01)
        atual = self.text_music_current.toPlainText()
        self.Inserir_Texto(self.text_music_previous, atual)
        aux = self.player[qual].about_music()
        self.Inserir_Texto(self.text_music_current,
                           "[%s]<br> %s" % (aux.get_artist(), aux.get_title()) )

class Crossfade(threading.Thread):
    def __init__(self, player):
        threading.Thread.__init__(self)
        self.player = player

    def run(self):
        while (self.player.get_volume() <> 0):
            self.player.decrease_volume()
            time.sleep(0.3)
        self.player.stop()

class Posicao_Barra(threading.Thread):
    def __init__(self, other, player, barra, tocar):
        threading.Thread.__init__(self)
        self.other, self.player , self.barra, self.tocar = other, player, barra, tocar

    def run(self):
        self.barra.setMaximum = 100
        while self.player.is_playing():
            pos = self.player.get_percent_pos()
            self.barra.setValue(pos)
            time.sleep(0.0001)
        self.tocar(self.other)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Radj()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
