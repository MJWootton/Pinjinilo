# -*- coding: UTF-8 -*-
"""
================================================================================
  _____    _____   _   _        _   _____   _   _   _____   _         ____
 |  __ \  |_   _| | \ | |      | | |_   _| | \ | | |_   _| | |       / __ \
 | |__) |   | |   |  \| |      | |   | |   |  \| |   | |   | |      | |  | |
 |  ___/    | |   | . ` |  _   | |   | |   | . ` |   | |   | |      | |  | |
 | |       _| |_  | |\  | | |__| |  _| |_  | |\  |  _| |_  | |____  | |__| |
 |_|      |_____| |_| \_|  \____/  |_____| |_| \_| |_____| |______|  \____/

Pinjinilo: Konverti Ĉinan Pinjinan (汉语拼音) Tekston
           kaj Ĉinsignojn (汉字) al Esperanto-Literumsistemo
================================================================================
Pinjino estas sistemo por priskribi la sonojn de ĉinsignoj per latinaj literoj.
La literoj uzataj malsamas al tiuj en la alfabeto de Esperanto, do la celo de ĉi
tiu programo estas konverti de norma Pinjino aŭ ĉinsignoj al proksimumo laŭ la
literumsistemo de Esperanto. Defaŭlte, ĝi uzas la sistemon kreitan de la revuo
El Popola Ĉinio [1], sed la uzanto povas uzi iun ajn sistemon, se oni kreas sian
propran dosieron priskribantan ĝin. Python 3 estas bezonata por roli Pinjinon
[2]. Modulo "xpinyin" [3] necesas por konverti ĉinsignojn.

Ĉi tiu dosiero provizas la funkciojn por legi la konvertsistemon laŭ nomo aŭ
dosierindiko kaj konverti tekston de la komandlinio aŭ dosiero. Krom kiel la
interna funkciaro uzata de la grafika fasado, oni povas uzi ĝin kiel memstaran
terminalprogramon aŭ kiel alvokitan modulon en alia Python-skripto.

Citaĵoj
----------
[1] https://eo.wikipedia.org/wiki/Esperantigo_de_vortoj_el_%C4%89ina_fonto
[2] https://www.python.org
[3] https://pypi.org/project/xpinyin
[4] ASCII-arto kreita per http://www.patorjk.com/software/taag

Bezonaĵoj
----------
* Python 3
* xpinyin
* Konvertsistemoj (modulo de Pinjinilo)

Aŭtorrajto
----------
(c) Mark Woottton 2020
================================================================================
"""

# Alvoki modulojn
import os
import sys
import string
import textwrap
import shutil

try:
    import xpinyin
except:
    if __name__ != '__main__':
        import xpinyin

import Konvertsistemoj

# Trovi la larĝon de terminalfenestro
try:
    largxoDefauxlta, _ = shutil.get_terminal_size()
except:
    largxoDefauxlta = 80

def pjv():
    """
    Liveri la nuntempan version
    """
    return "1-0"

def plprint(montroto, largxo=largxoDefauxlta):
    """
    Funkcio por montri plurajn lineojn sen saltoj en vortoj ĉe la linefino

    Enigoj
    ----------
    montroto : string
        Teksto montrota
    largxo : integer
        Maksimuma larĝo de lineo
        Defaŭlta valoro: 'largxoDefauxlta', kiel videbla supren

    """
    print(textwrap.fill(montroto, largxo))

def legiTekston(teksto):
    """
    Funkcio por havigi la tekston konverotan

    Enigoj
    ----------
    teksto : string
        Teksto konverota mem aŭ indiko al dosiero enhavanta ĝin

    Eligoj
    ----------
    teksto : string
        La teksto konverota

    """
    # Legi la dosiero, se 'teksto' estas la dosierindiko kaj ne la teksto mem
    dosierindiko = os.path.join(os.getcwd(), teksto)
    if os.path.isfile(dosierindiko) is True:
        dosiero = open(dosierindiko, 'r', encoding='utf-8')
        teksto = ''
        # Igi, ke 'teksto' estu la enhavo de la dosiero
        for linio in dosiero:
            teksto += linio
        dosiero.close()
    # Liveri tekston
    return teksto

def konserviTekston(teksto, dosierindiko):
    """
    Funcio por konservi konvertitan tekston en dosiero

    Enigoj
    ----------
    teksto : string
        Teksto konservota
    dosierindiko : string
        Indiko al la dosiero, kie 'teksto' estos konservita

    """
    konservataDosiero = open(dosierindiko, 'w', encoding='utf-8')
    konservataDosiero.write(teksto)
    konservataDosiero.close()

def legiKonvertsistemon(ks=None):
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
    # Krei datumujojn
    konvertsistemo = {}
    sxlosiloj = []
    ordo = []
    dosiero = None

    # Serĉi la konvertsistemon en la modulo 'Konvertsistemoj'
    konvertsistemo, sxlosiloj = Konvertsistemoj.doniSistemon(nomo=ks)
    if konvertsistemo is None:
        konvertsistemo = {}
        if ks is None:
            # Uzi la defaŭlta konvertsistemon
            dosierindiko = os.path.join(os.path.split(os.path.dirname(sys.argv[0]))[0], 'konvertsistemoj', 'defaŭlto.csv')
        else:
            if os.path.isfile(ks):
                # Uzi la dosieron de konvertsistemo, se 'ks' estas tia
                dosierindiko = ks
            else:
                # Serĉi konvertsistemon kun la donita nomo, se 'ks' ne estas dosierindiko
                dosierujo = os.path.join(os.path.split(os.path.dirname(sys.argv[0]))[0], 'konvertsistemoj')
                for dosiernomo in os.listdir(dosierujo):
                    dosierindiko = os.path.join(dosierujo, dosiernomo)
                    dosiero = open(dosierindiko, 'r', encoding='utf-8')
                    if ks == dosiero.readline().strip('\n,'):
                        break
                    dosiero.close()
                dosiero.close()
        # Malfermi la dosieron de la konvertsistemo
        dosiero = open(dosierindiko, 'r', encoding='utf-8')
        # Meti la konvertsistemon en vortar-objekton
        for linio in dosiero:
            aparte = linio.split(',')
            # Trovi nomon de la konvertsistemo
            if len(aparte) == 1 and 'NOMO' not in konvertsistemo:
                konvertsistemo['NOMO'] = aparte[0].strip('\n,')
            else:
                konvertsistemo[aparte[0].lower()] = aparte[1].strip('\n,').lower()
                sxlosiloj.append(aparte[0].lower())
        # Fermi la dosieron de la konvertsistemo
        dosiero.close()
    # Nomi ne konatan konvertsistemon
    if 'NOMO' not in konvertsistemo:
        konvertsistemo['NOMO'] = 'Ne konata konvertsistemo'
    # Ordigi la ŝlosilojn de plej longa mallongen
    while len(sxlosiloj) > 0:
        aldono = ''
        indekso = None
        for sxn in range(len(sxlosiloj)):
            sx = sxlosiloj[sxn]
            if sx not in ordo and len(aldono) < len(sx):
                aldono = sx
                indekso = sxn
        ordo.append(sxlosiloj.pop(indekso))
    # Liveri konvertsistemon kaj ordigitajn ŝlosilojn
    return konvertsistemo, ordo

def konverti(teksto, konvertsistemo, ordo):
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
    # Krei listojn de literojn
    literoj = string.ascii_uppercase + 'ĈĜĤĴŜŬ'
    kromsignoj = [['a', 'āáǎà'], ['e', 'ēéěè'], ['i','īíǐì'], ['o', 'ōóǒò'], ['u', 'ūúǔù'], ['ü', 'ǖǘǚǜ']]
    # Krei datumujojn
    neripetoj = ''
    rezulto = ''
    # Konverti ĉinsignojn pinjinen kaj meti streketon inter nur apudajn ĉinsignojn
    teksto = xpinyin.Pinyin().get_pinyin(teksto, '¬').replace('¬ ¬', ' ').replace('¬ ', ' ').replace(' ¬', ' ')
    for t in range(len(teksto)-1):
        if teksto[t] == '¬' and teksto[t+1].upper() in literoj:
            teksto = teksto[:t] + '-' + teksto[t+1:]
    teksto = teksto.replace('¬', '')
    # Krei minuskligitan version de la teksto
    anstatauxigita = teksto.lower()
    # Forigi tonajn kromsignojn
    for k in kromsignoj:
        literoj += k[1].upper()
        for kk in k[1]:
            anstatauxigita = anstatauxigita.replace(kk, k[0])
            anstatauxigita = anstatauxigita.replace(kk.upper(), k[0].upper())
    # Meti spaceton post la linefinajn signojn
    anstatauxigita = anstatauxigita.replace('\n' , '\n ')
    # Fari la anstatauxigadon laŭ la konvertsistemo
    for sx in ordo:
        anstatauxigita = anstatauxigita.replace(sx, konvertsistemo[sx].upper())
    # Forigi ripetitajn literojn
    for m in range(len(anstatauxigita)-1):
        if anstatauxigita[m] != anstatauxigita[m+1] and anstatauxigita[m] in literoj:
            neripetoj += anstatauxigita[m]
        elif anstatauxigita[m] not in literoj:
            neripetoj += anstatauxigita[m]
    neripetoj += anstatauxigita[-1]
    # Krei listojn de la individuaj vortoj de la originala kaj konvertita tekstoj
    aparte = teksto.replace('\n' , '\n ').split(' ')
    neripetoj = neripetoj.split(' ')
    # Restaŭri la usklecon de la literoj de la originala teksto en la konvertita
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
        if '\n' not in neripetoj[tn]:
            rezulto += ' '
    # Liveri la tekston rezultintan de la konvertado
    return rezulto

def main(enigo, ks=None):
    """
    La ĉefa funkcio

    Enigoj
    ----------
    enigo : string
        Teksto konverota mem aŭ indiko al dosiero enhavanta ĝin
    chuDosiero : boolean
        Ĉu 'enigo' estas la teksto mem aŭ ĝia dosierindiko
    ks : string
        Nomo de la konvertsistemo uzota aŭ indiko al dosiero enhavanta ĝin

    Eligoj
    ----------
    rezulto : string
        La teksto konvertita

    """
    teksto = legiTekston(enigo)
    konvertsistemo, ordo = legiKonvertsistemon(ks)
    rezulto = konverti(teksto, konvertsistemo, ordo)

    print('')
    p = 'Originala pinjina teksto:'
    if '\n' in teksto:
        plprint(p)
        p = teksto.split('\n')
        for l in p:
            plprint(l)
    else:
        plprint(p + ' ' + teksto)
    print('')
    p = 'Konvertita esperantigita teksto:'
    if '\n' in rezulto:
        plprint(p)
        p = rezulto.split('\n')
        for l in p:
            plprint(l)
    else:
        plprint(p + ' ' + rezulto)
    print('')

    return rezulto

def helpmesagxo(versio=None):
    """
    Funcio por montri la helpmesaĝon, kiu priskribas:
    * la celon de la programaro
    * la aŭtorrajton
    * la neprajn kaj nedevigajn enigojn laŭ ordo
    kaj avertas la uzanton, se ties versio de Python ne estas sufiĉe freŝa.

    Enigoj
    ----------
    La versio de Python uzata ruli la programon
    """
    tab = ' '*4
    print('='*80)
    print('  _____    _____   _   _        _   _____   _   _   _____   _         ____')
    print(' |  __ \\  |_   _| | \\ | |      | | |_   _| | \\ | | |_   _| | |       / __ \\')
    print(' | |__) |   | |   |  \\| |      | |   | |   |  \\| |   | |   | |      | |  | |')
    print(' |  ___/    | |   | . ` |  _   | |   | |   | . ` |   | |   | |      | |  | |')
    print(' | |       _| |_  | |\\  | | |__| |  _| |_  | |\\  |  _| |_  | |____  | |__| |')
    print(' |_|      |_____| |_| \\_|  \\____/  |_____| |_| \\_| |_____| |______|  \\____/')
    #print('\nVersio %s\n' % pjv())
    print('')
    plprint('Konverti Ĉinan Pinjinan (汉语拼音) Tekston kaj Ĉinsignojn (汉字) al Esperanto-Literumsistemo')
    plprint('(c) Mark Wootton 2020 [Versio %s]' % pjv())
    print('='*80)
    print('Enigoj:')
    plprint(tab + '[teksto] (unua, nepra)  :  la teksto konverota mem (uzu citmarkojn) aŭ indiko al tekstdosiero')
    plprint(tab + '-k [konvertsistemo] (nedeviga)  :  dosierindiko al alternativa sistemo por konverti la tekston')
    plprint(tab + '-h (nedeviga)  :   peti helpon - meti ĉi tiun mesaĝon kaj ĉesi')
    atentoj = []
    if versio[0] < 3:
        atentoj.append('- Python 3 estas bezonata. Versio %d.%d rekoniĝis.' % (versio[0], versio[1]))
    if "xpinyin" not in sys.modules:
        atentoj.append('- Modulo "xpinyin" ne povis esti alvokita.')
    if len(atentoj):
        print('\nATENTU:')
        for a in atentoj:
            plprint(a)

    print('='*80)

if __name__ == '__main__':
    """
    Ruli la ĉefan funkcion, se ĉi tiu estas la ĉefa modulo (t.e. ne alvokita)

    """
    # Trovi la version de Python
    versio = sys.version_info
    # Krei datumujojn
    helpo = False # Ĉu la helpmesaĝo montriĝos
    enigo = None # La teksto por konverti
    ks = None # Kiu konvertsistemo uziĝos
    # Legi la komandliniajn enigojn
    argv = sys.argv[1:]
    for a in range(len(argv)):
        aa = argv[a]
        if aa.lower() in ['-h', '--helpo', '-helpo', '--help', '-help']:
            helpo = True
        elif aa == '-k':
            ks = a+1
    try:
        enigo = argv[0]
    except IndexError:
        helpo = True
    if ks is not None:
        try:
            ks = argv[ks]
        except IndexError:
            helpo = True
    # Montri helpmesaĝon, se:
    #       * neniu enigo estas donita
    #       * la uzanto petis helpon (per '-h' ktp.)
    #       * la enigoj ne legablas
    #       * la versio de Python estas nesufiĉe freŝa
    if helpo or versio[0] < 3:
        helpmesagxo(versio)
    # Ruli la ĉefan funkcion, se neniu problemo troviĝis
    else:
        main(enigo, ks)
