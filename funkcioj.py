"""
================================================================================
  _____    _____   _   _        _   _____   _   _   _____   _         ____
 |  __ \  |_   _| | \ | |      | | |_   _| | \ | | |_   _| | |       / __ \
 | |__) |   | |   |  \| |      | |   | |   |  \| |   | |   | |      | |  | |
 |  ___/    | |   | . ` |  _   | |   | |   | . ` |   | |   | |      | |  | |
 | |       _| |_  | |\  | | |__| |  _| |_  | |\  |  _| |_  | |____  | |__| |
 |_|      |_____| |_| \_|  \____/  |_____| |_| \_| |_____| |______|  \____/

Pinjinilo: Konverti Ĉinan Pinjinan (汉语拼音) Tekson al Esperanto-Literumsistemo.
================================================================================
Pinjino estas sistemo por priskribi la sonojn de ĉinsignoj per latinaj literoj.
La literoj uzataj malsamas al tiuj en la alfabeto de Esperanto, do la celo de ĉi
tiu skripto estas konverti de norma Pinjino al proksimumo laŭ la literumsistemo
de Esperanto. Defaŭlte, ĝi uzas la sistemon kreitan de la revuo El Popola
Ĉinio [1], sed la uzanto povas uzi iun ajn sistemon, se ri kreas sian propran
dosieron priskribantan ĝin. Oni rekomendas roli Pinjinon per Python 3 [2].

Citaĵoj
----------
[1] https://eo.wikipedia.org/wiki/Esperantigo_de_vortoj_el_%C4%89ina_fonto
[2] https://www.python.org

Bezonaĵoj
----------
Python 3

Aŭtorrajto
----------
(c) Mark Woottton 2020
================================================================================
"""

# Alvoki modulojn
import os
import sys
import string

def legiTekston(teksto, chuDosiero=False):
    """
    Funkcio por havigi la tekston konverotan

    Enigoj
    ----------
    teksto : string
        Teksto konverota mem aŭ indiko al dosiero enhavanta ĝin
    chuDosiero : boolean
        Ĉu "teksto" estas la teksto mem aŭ ĝia dosieroindiko

    Eligoj
    ----------
    teksto : string
        La teksto konverota

    """
    # if enigo is None:
    #     return "REN Jiang nü qian QIAN" + "\n" + "āáǎà ēéěè īíǐì ōóǒò ūúǔù ǖǘǚǜ" + " " + "āáǎà ēéěè īíǐì ōóǒò ūúǔù ǖǘǚǜ".upper() + " " + "A a" + "\n"
    # Legi tekston konverotan, se ĝi estas en dosiero,
    if chuDosiero is True:
        dosiero = open(os.path.join(os.getcwd(), enigo), "r")
        teksto = ""
        for linio in dosiero:
            teksto += linio
        dosiero.close()
    return teksto

def legiKonvertsistemoon(ks=None):
    """
    Funkcio por havigi la deziratan sistemon por konverti la tekston

    Enigoj
    ----------
    ks : string
        Nomo de la konvertsistemo uzota aŭ indiko al dosiero enhavanta ĝin

    Eligoj
    ----------
    konvertsistemo : dictionary
        Vortar-objekto enhavanta la konvertsistemon
    ordo : list
        Ordigita listo de ŝlosiloj de la vortar-objekto

    """
    konvertsistemo = {}
    shlosiloj = []
    dosiero = None
    if ks is None:
        dosierindiko = os.path.join(os.path.split(os.path.dirname(sys.argv[0]))[0], "konvertsistemoj", "defaŭlto.csv")
    else:
        if os.path.isfile(ks):
            dosierindiko = ks
        else:
            dosierujo = os.path.join(os.path.split(os.path.dirname(sys.argv[0]))[0], "konvertsistemoj")
            for dosiernomo in os.listdir(dosierujo):
                dosierindiko = os.path.join(dosierujo, dosiernomo)
                dosiero = open(dosierindiko, "r")
                if ks == dosiero.readline().strip("\n,"):
                    break
                dosiero.close()
            dosiero.close()
    dosiero = open(dosierindiko, "r")
    for linio in dosiero:
        aparte = linio.split(",")
        if len(aparte) == 1 and "NOMO" not in konvertsistemo:
            konvertsistemo["NOMO"] = aparte[0][:-1]
        else:
            konvertsistemo[aparte[0]] = aparte[1][:-1]
            shlosiloj.append(aparte[0])
    ordo = []
    while len(shlosiloj) > 0:
        aldono = ""
        indekso = None
        for shn in range(len(shlosiloj)):
            sh = shlosiloj[shn]
            if sh not in ordo and len(aldono) < len(sh):
                aldono = sh
                indekso = shn
        ordo.append(shlosiloj.pop(indekso))
    # print("\n", ordo, "\n")
    dosiero.close()
    return konvertsistemo, ordo

def ruli(teksto, konvertsistemo, ordo):
    """
    Funkcio por konverti la tekston laŭ la donita konvertsistemo

    Enigoj
    ----------
    teksto : string
        La teksto konverota
    konvertsistemo : Dictionary
        Vortar-objekto enhavanta la konvertsistemon
    ordo : list
        Ordigita listo de ŝlosiloj de la vortar-objekto

    Eligoj
    ----------
    rezulto : string
        La teksto konvertita

    """
    literoj = string.ascii_uppercase + "ĈĜĤĴŜŬ"
    kromsignoj = [["a", "āáǎà"], ["e", "ēéěè"], ["i","īíǐì"], ["o", "ōóǒò"], ["u", "ūúǔù"], ["ü", "ǖǘǚǜ"]]
    neripetoj = ""
    rezulto = ""
    anstatauxigita = teksto.lower()
    for k in kromsignoj:
        literoj += k[1].upper()
        for kk in k[1]:
            anstatauxigita = anstatauxigita.replace(kk, k[0])
            anstatauxigita = anstatauxigita.replace(kk.upper(), k[0].upper())
    anstatauxigita = anstatauxigita.replace("\n" , "\n ")
    for sh in ordo:
        anstatauxigita = anstatauxigita.replace(sh, konvertsistemo[sh].upper())
    for m in range(len(anstatauxigita)-1):
        if anstatauxigita[m] != anstatauxigita[m+1] and anstatauxigita[m] in literoj:
            neripetoj += anstatauxigita[m]
        elif anstatauxigita[m] not in literoj:
            neripetoj += anstatauxigita[m]
    neripetoj += anstatauxigita[-1]
    # print("*"*80)
    # print(teksto)
    # print("*"*80)
    # print(anstatauxigita)
    # print("*"*80)
    # print(neripetoj)
    # print("*"*80)
    aparte = teksto.replace("\n" , "\n ").split(" ")
    neripetoj = neripetoj.split(" ")
    for tn in range(len(aparte)):
        if not len(aparte[tn]):
            continue
        if aparte[tn][0] in literoj:
            rezulto += neripetoj[tn][0]
            if len(aparte[tn]) > 1:
                if aparte[tn][1] in literoj:
                    rezulto += neripetoj[tn][1:]
                else:
                    rezulto += neripetoj[tn][1:].lower()
        else:
            rezulto += neripetoj[tn].lower()
        if "\n" not in neripetoj[tn]:
            rezulto += " "
    # print(rezulto)
    return rezulto

def main(enigo, chuDosiero, ks):
    """
    La ĉefa funkcio

    Enigoj
    ----------
    enigo : string
        Teksto konverota mem aŭ indiko al dosiero enhavanta ĝin
    chuDosiero : boolean
        Ĉu "enigo" estas la teksto mem aŭ ĝia dosieroindiko
    ks : string
        Nomo de la konvertsistemo uzota aŭ indiko al dosiero enhavanta ĝin

    Eligoj
    ----------
    rezulto : string
        La teksto konvertita

    """
    teksto = legiTekston(enigo, chuDosiero=chuDosiero)
    konvertsistemo, ordo = legiKonvertsistemoon(ks)
    rezulto = ruli(teksto, konvertsistemo, ordo)
    p = "\nOriginala pinjina teksto:"
    if "\n" in teksto:
        p += "\n" + teksto + "\n"
    else:
        p += " \"%s\"\n" % teksto
    p += "Konvertita esperantigita teksto:"
    if "\n" in rezulto:
        p += "\n" + rezulto + "\n"
    else:
        p += " \"%s\"\n" % rezulto
    print(p)
    return rezulto

if __name__ == '__main__':
    """
    Ruli la ĉefan funkcion, se ĉi tiu estas la ĉefa modulo (t.e. ne alvokita)

    """
    enigo = None
    helpo = False
    teksto = None
    dosiero = None
    ks = None
    argv = sys.argv[1:]
    for a in range(len(argv)):
        aa = argv[a]
        if aa == "-h":
            helpo = True
        elif aa == "-d":
            dosiero = a+1
        elif aa == "-t":
            teksto = a+1
        elif aa == "-k":
            ks = a+1
    if (dosiero is not None and teksto is not None) or (dosiero is None and teksto is None):
        helpo = True
        dosiero = None
        teksto = None
    if dosiero is not None:
        try:
            enigo = argv[dosiero]
            dosiero = True
        except IndexError:
            helpo = True
    if teksto is not None:
        try:
            enigo = argv[teksto]
            dosiero = False
        except IndexError:
            helpo = True
    if ks is not None:
        try:
            ks = argv[ks]
        except IndexError:
            helpo = True
    if helpo:
        print("...")
    else:
        # print(enigo, dosiero, ks)
        main(enigo, dosiero, ks)
