#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""jour_prec.py: Retour du jour précédant pour une date donnée"""

__author__ = "Sylvain Duclos"
__copyright__ = "Copyright 2017, ./LeCairn"
__version__ = "1.0.1"
__status__ = "Development"

def bissextile(annee):  # On définit une fonction pour savoir si l'année est bissextile
    if (annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0)):
        return True
    return False


def un_jour_avant(jour, mois, annee):
    if (jour == 1):  # Si le jour est 1, on change de mois, voire d'année
        if (mois == 1):  # Si le mois est 1, on change d'année
            nouveau_mois = 12
            nouvelle_annee = annee - 1
        else:  # Autrement on se trouve simplement au mois précédent
            nouveau_mois = mois - 1
            nouvelle_annee = annee

        if (nouveau_mois == 2):  # Si on se trouve en février
            if bissextile(nouvelle_annee):
                nouveau_jour = 29
            else:
                nouveau_jour = 28

        else:
            jours_par_mois = (31, None, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
            nouveau_jour = jours_par_mois[nouveau_mois - 1]

    else:
        nouveau_jour = jour - 1
        nouveau_mois = mois
        nouvelle_annee = annee

    return (format(nouvelle_annee)+format(nouveau_mois).zfill(2)+format(nouveau_jour).zfill(2))
