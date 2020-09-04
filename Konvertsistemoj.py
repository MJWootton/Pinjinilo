# -*- coding: UTF-8 -*-
'''
================================================================================
  _____    _____   _   _        _   _____   _   _   _____   _         ____
 |  __ \  |_   _| | \ | |      | | |_   _| | \ | | |_   _| | |       / __ \
 | |__) |   | |   |  \| |      | |   | |   |  \| |   | |   | |      | |  | |
 |  ___/    | |   | . ` |  _   | |   | |   | . ` |   | |   | |      | |  | |
 | |       _| |_  | |\  | | |__| |  _| |_  | |\  |  _| |_  | |____  | |__| |
 |_|      |_____| |_| \_|  \____/  |_____| |_| \_| |_____| |______|  \____/

Pinjinilo: Konverti Ĉinan Pinjinan (汉语拼音) Tekston al Esperanto-Literumsistemo
================================================================================
Pinjino estas sistemo por priskribi la sonojn de ĉinsignoj per latinaj literoj.
La literoj uzataj malsamas al tiuj en la alfabeto de Esperanto, do la celo de ĉi
tiu skripto estas konverti de norma Pinjino al proksimumo laŭ la literumsistemo
de Esperanto. Defaŭlte, ĝi uzas la sistemon kreitan de la revuo El Popola
Ĉinio [1], sed la uzanto povas uzi iun ajn sistemon, se oni kreas sian propran
dosieron priskribantan ĝin. Python 3 aŭ pli freŝa versio estas bezonata por roli
Pinjinon [2].

Ĉi tiu dosiero enhavas la antaŭinstalitajn konvertsistemojn.

Citaĵoj
----------
[1] https://eo.wikipedia.org/wiki/Esperantigo_de_vortoj_el_%C4%89ina_fonto
[2] https://www.python.org

Bezonaĵoj
----------
* Python 3

Aŭtorrajto
----------
(c) Mark Woottton 2020
================================================================================
'''

def doniSistemon(nomo=None):
    """
    Funkcio por trovi konvertsistemon de iu nomo

    Enigoj
    ----------
    nomo : string
        La nomo de la konvertsistemo serĉota.
        Defaŭlte 'nomo' estas 'None', kion la funkcio anstataŭigos al 'Defaŭlto'

    Eligoj
    ----------
    konvertsistemo : dictionary
        Vortar-objekto enhavanta la konvertsistemon

    """
    if nomo is None:
        nomo = 'Defaŭlto'
    defauxlto = {'NOMO' : 'Defaŭlto',
            'b':'b',
            'd':'d',
            'g':'g',
            'j':'ĝj',
            'zh':'ĝ',
            'z':'z',
            'p':'p',
            't':'t',
            'k':'k',
            'q':'ĉj',
            'ch':'ĉ',
            'c':'c',
            'm':'m',
            'n':'n',
            'h':'h',
            'x':'ŝj',
            'sh':'ŝ',
            's':'s',
            'f':'f',
            'l':'l',
            'y':'j',
            'r':'ĵ',
            'w':'ŭ',
            'a':'a',
            'ai':'aj',
            'an':'an',
            'ü':'u',
            'o':'o',
            'ei':'ej',
            'en':'en',
            'i':'i',
            'e':'e',
            'ao':'aŭ',
            'ang':'ang',
            'u':'u',
            'ou':'oŭ',
            'eng':'eng',
            'er':'er',
            'ie':'je',
            'ia':'ja',
            'üa':'ŭa',
            'uo':'ŭo',
            'üe':'ŭe',
            'iao':'jaŭ',
            'iou':'juŭ',
            'uei':'ŭej',
            'uai':'ŭaj',
            'ian':'jan',
            'uen':'ŭen',
            'üan':'ŭan',
            'iang':'jang',
            'iong':'jong',
            'ueng':'ŭeng',
            'uang':'ŭang'
        }

    ss = []
    for s in [defauxlto]:
        if s['NOMO'] == nomo:
            for sx in s.keys():
                if sx != 'NOMO':
                    ss.append(sx.lower())
            print("Found")
            return s, ss
    return None, ss
