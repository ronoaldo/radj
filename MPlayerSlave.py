#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys, os, time, threading

class ReadPlayerMessage(threading.Thread):
    def __init__(self, extern_player):
        threading.Thread.__init__(self)
        self.ep = extern_player

    def reading(self, playout):
        if playout != None:
            return playout.readline()
        else:
            return ""

    def run(self):
        def get_split(msg,spl=": "):
            return msg.split(spl)[1]
        message = ""
        Loop = True
        # verifica o inicio da musica
        # pegando suas informacoes
        while Loop:
            message=self.reading(self.ep.playout)
            # verificando o final do cabecalho de inicio da musica
            if message.find("Starting playback") != -1:
                #DEBUG: print "Player playing"
                Loop = False
            # verificando Exiting para casos de erro de abrir a musica
            elif message.find("Exiting") != -1: Loop = False
            elif message.find("Title:") != -1: self.ep.musica.set_title(get_split(message))
            elif message.find("Artist:") != -1: self.ep.musica.set_artist(get_split(message))
            elif message.find("Album:") != -1: self.ep.musica.set_album(get_split(message))
            elif message.find("Year:") != -1: self.ep.musica.set_year(get_split(message))
            elif message.find("Comment:") != -1: self.ep.musica.set_comment(get_split(message))
            elif message.find("Track:") != -1: self.ep.musica.set_track(get_split(message))
            elif message.find("Genre:") != -1: self.ep.musica.set_genre(get_split(message))
        self.ep.head_readed = True
        
        Loop = True
        while Loop:
            # o teste da mensagem eh primeiro, pq se tiver ocorrido
            # um erro no laço de cima e tiver saído do programa mplayer
            # ele verá e terminará a thread
            if message != "":
                #se for Exiting, libera a thread
                if message.find("Exiting") != -1:
                    self.ep.quit()
                    Loop = False
                else:
                    self.ep.add_play_messages(message)
                    message=self.reading(self.ep.playout)
        #DEBUG: print "Player FREE"

class MusicDefinitions:
    __path = ""
    __title = ""
    __artist = ""
    __album = ""
    __year = ""
    __comment = ""
    __track = ""
    __genre = ""

    def __init__(self, path):
        self.__path = path

    def get_path(self):
        return self.__path

    def set_title(self, msg):
        self.__title = msg.replace("\n"," ")

    def get_title(self):
        return self.__title

    def set_artist(self, msg):
        self.__artist = msg.replace("\n"," ")

    def get_artist(self):
        return self.__artist

    def set_album(self, msg):
        self.__album = msg.replace("\n"," ")

    def get_album(self):
        return self.__album

    def set_year(self, msg):
        self.__year = msg.replace("\n"," ")

    def get_year(self):
        return self.__year

    def set_comment(self, msg):
        self.__comment = msg.replace("\n"," ")

    def get_comment(self):
        return self.__comment

    def set_track(self, msg):
        self.__track = msg.replace("\n"," ")

    def get_track(self):
        return self.__track

    def set_genre(self, msg):
        self.__genre = msg.replace("\n"," ")

    def get_genre(self):
        return self.__genre


class MPlayerSlave:
    """ Mplayer frontend for Python. """
    __default_volume = "90"
    __volume = 0
    __defaultargs__ = ("mplayer","-quiet","-slave","-softvol")
    __old_pos = 0
    __play_messages = []
    __play_messages_pos = 0
    __nomessage = "NOMESSAGEFII"

    def __init__(self, extraargs = tuple() ):
        """ Constructor.
            Creates a new MPlayerSlave instance. """
        self.mplayer_command = self.__defaultargs__ + extraargs
        self.playin, self.playout, self.playerr = None, None, None

    def add_play_messages(self,message):
        self.__play_messages.append(message)

    def read_play_messages(self):
        #print "READING"
        try:
            retorno=self.__play_messages[self.__play_messages_pos]
            self.__play_messages_pos += 1
            return retorno
        except:
            return self.__nomessage

    def play(self, path):
        """ Play a file, ou URL.
            path must be a format recognized by Mplayer.
            See mplayer(1) for details. """
        if self.playin == None:
            self.playin, self.playout, self.playerr = os.popen3(self.mplayer_command + (path,))
            self.musica = MusicDefinitions(path)
            self.head_readed = False
            self.player = ReadPlayerMessage(self)
            self.player.start()
            self.set_volume(self.__default_volume)
            #self.send("loadfile %s" % path)

    def about_music(self):
        return self.musica

    def pause(self):
        """ Pause the current track. """
        self.send("pause")

    def quit(self):
        #Envia o sinal de parada
        self.send("quit")
        #espera o thread parar, a execucao da linha abaixo
        # eh muito rapida e nao costuma dar tempo de parar
        # assim, ele obriga a esperar o thread
        try:
            self.player.join()
        except:
            pass
        #limpa os dados
        self.playin, self.playout, self.playerr = None,None,None
        self.__play_messages = []
        self.__play_messages_pos = 0
        #self.head_readed = False

    def stop(self):
        self.quit()

    def increase_volume (self):
        #FIXME
        #self.set_volume(1,0)
        self.set_volume(self.get_volume()+7)
   
    def decrease_volume (self):
        #FIXME
        #self.set_volume(-1,0)
        less = 7
        volume=self.get_volume()
        if volume < less:
            if volume == less/2: volume = 0
            else: volume = less/2
        else: volume = self.get_volume()-less
        self.set_volume(volume)
    """
        Define o volume
        com parametro value1 somente setado, defin este valor
        velue2 utilizado para increase e decrease
    """
    def set_volume (self, value1, value2=1):
        # garantindo valores inteiros
        value1 , value2 = int(value1) , int(value2)
        if value2 == 0:
            print "TODO"
        else:
            if value1 < 0:   value1=0
            if value1 > 100: value1=100
            self.send( "volume %d %d" % ( value1, value2 ) )
            self.__volume = value1
            #DEBUG: print "VOLUME: ", self.__volume

    def get_volume (self):
        return self.__volume

    def get_percent_pos(self):
        self.send("get_percent_pos")
        tmp = self.read_play_messages().strip()
        while tmp <> self.__nomessage and tmp.find("ANS_PERCENT_POSITION") == -1:
            tmp = self.read_play_messages().strip()
        if tmp <> self.__nomessage:
            pos = tmp.split("=")[1]
            #DEBUG: print "POS=",pos
            return int(pos)
        else:
            return 0

    def is_playing(self):
        if self.playin == None: return False
        else: return True

    def send(self,command):
        """ Send a command to the mplayer process. """
        try:
            self.playin.write(command + "\n")
            self.playin.flush()
        except:
            pass
