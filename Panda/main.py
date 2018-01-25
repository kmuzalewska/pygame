#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from run import Game

def help():
    print "\nGra autorstwa Klary Muzalewskiej.\n\n" \
          "Gra została napisana przy pomocy biblioteki pygame, numpy w jezyku python.  Aby gra działała należy doinstalować podane biblioteki jeśli nie są dotychczas zaintalowane. komenda: \n sudo apt-get install python-pygame \n"
    print "Projekt składa się z kilku części:"
    print "main.py - skrypt zarządzający opcjami z terminala"
    print "run.py - główny zarządzca gry"
    print "Obiekty które pojawiają się w grze:"
    print "panda.py"
    print "bambus.py"
    print "szustak.py"
    print "Jest również folder ze zdjęciami, które są używane w czasie działania programu"

    print "Aby uruchomić grę należy nadać wykonywalność wszystkim plikom z końcówką .py i uruchomić main.py.\n" \
          "Gra włącza się w wyskakującym okienku."
    print "\n"
    print "Opis gry:"
    print "Gra polega na poruszaniu pandą tak by ją nakarmić bambusem i uniknąć przytulania człowieka (wykorzystane tu zdjęcie o.Adama Szustaka). Nie chcemy zagłodzić pandy bo umrze." \
          "Stan wyrzywienia podany jest w 'score' a czas pozostały do zebrania aktualnie widocznego bambusa w \'seconds\'. Po tym czasie odejmuje się nam punkt i pojawia się nowy bambus. Człowiek przytula przez pewien czas. Jest on wyświetlony na jego postaci w momencie zetknięcia się z pandą. Po tym czasie człowiek pojawia sie w nowym miejscu. W międzyczasie panda może umrzeć z głodu. Należy uważać."
    print "\n"
    print "Po planszy poruszamy się strzałkami (góra, dół, prawo, lewo) lub klawiszami (a,s,d,w). Gra się kończy jeśli zagłodzimy pande. Możemy zastopować grę spacją."
    print "\n"


arg = sys.argv[1:]

for i in arg:
    if i=="-h" or i=="--help":
        help()
        sys.exit(0)
try:
    Game()
except Exception as e:
    print e.message
    help()
    sys.exit(0)