#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Nivo.py: Traitement de données brutes nivologiques diffusées par Météo France"""

__author__ = "Sylvain Duclos"
__copyright__ = "Copyright 2017, ./LeCairn"
__version__ = "1.0.1"
__status__ = "Development"

import urllib
import csv
from inc import jour_prec



from datetime import datetime






# Classe permettant le débug couleur #
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def TelechargerFichier(cheminDistant, cheminLocal):
    print "* Téléchargement depuis : " + urlNivoCsv
    urllib.urlretrieve(urlNivoCsv, pathCsv)
    print bcolors.OKGREEN + " => Téléchargement complet" + bcolors.ENDC


# On détermine le jour précédent #
date = datetime.now()
myList = []
#jour_precedent = format(int(date.strftime('%Y%m%d'))
date_precedante = jour_prec.un_jour_avant(int(date.strftime('%d')),int(date.strftime('%m')),int(date.strftime('%Y')))

print "* Previous date : " + date_precedante
# Construction de l'URL #
urlNivoCsv = "https://donneespubliques.meteofrance.fr/donnees_libres/Txt/Nivo/nivo." + date_precedante + ".csv"
pathCsv = "dl/" + date_precedante + ".csv"
TelechargerFichier(urlNivoCsv, pathCsv)

# Lecture du CSV #
myReader = csv.reader(open(pathCsv), delimiter=';')
for row in myReader:
    myList.append(list(row))

print myList[1][15]


