# -*- coding: UTF-8 -*-
'''
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

Ĉi tiu dosiero provizas la grafikan fasadon uzante la modulon PySimpleGUI [4].

Citaĵoj
----------
[1] https://eo.wikipedia.org/wiki/Esperantigo_de_vortoj_el_%C4%89ina_fonto
[2] https://www.python.org
[3] https://pypi.org/project/xpinyin
[4] https://pysimplegui.readthedocs.io
[5] ASCII-arto kreita per http://www.patorjk.com/software/taag

Bezonaĵoj
----------
* Python 3
* PySimpleGUI
* Funkcioj (modulo de Pinjinilo)

Aŭtorrajto
----------
(c) Mark Woottton 2020

================================================================================
'''

import os
import sys
import platform
import PySimpleGUI as sg
import pyperclip

import Funkcioj as fk

def helpoFenestro():
    """
    Funkcio por montri la helpfenestron

    """
    # Trovi operaciumon por agordi larĝon de teksta areo
    operaciumo = platform.system()
    if operaciumo == 'Linux':
        largxo = 105
    elif operaciumo == 'Windows':
        largxo = 95
    elif operaciumo == 'Dawin': # MacOs ktp.
        largxo = 88
    else:
        largxo = 105
    # Krei mesaĝon
    titolo  = '  _____    _____   _   _        _   _____   _   _   _____   _         ____\n'
    titolo += ' |  __ \\  |_   _| | \\ | |      | | |_   _| | \\ | | |_   _| | |       / __ \\\n'
    titolo += ' | |__) |   | |   |  \\| |      | |   | |   |  \\| |   | |   | |      | |  | |\n'
    titolo += ' |  ___/    | |   | . ` |  _   | |   | |   | . ` |   | |   | |      | |  | |\n'
    titolo += ' | |       _| |_  | |\\  | | |__| |  _| |_  | |\\  |  _| |_  | |____  | |__| |\n'
    titolo += ' |_|      |_____| |_| \\_|  \\____/  |_____| |_| \\_| |_____| |______|  \\____/\n'
    titolo += 'Versio %s' % fk.pjv()
    priskribo  = 'Pinjino estas sistemo por priskribi la sonojn de ĉinsignoj per latinaj literoj. '
    priskribo += 'La literoj uzataj malsamas al tiuj en la alfabeto de Esperanto, do la celo de '
    priskribo += 'Pinjinilo estas konverti de norma Pinjino kaj ĉinsignoj* al proksimumo laŭ la literumsistemo '
    priskribo += 'de Esperanto. Defaŭlte, ĝi uzas la sistemon kreitan de la revuo El Popola '
    priskribo += 'Ĉinio, sed la uzanto povas uzi iun ajn sistemon, se oni kreas sian propran '
    priskribo += 'dosieron priskribantan ĝin.'
    priskribo += '\n\nKonsciu, ke Pinjinilo ne estas tradukilo, sed transliterumilo.'
    helpo  = 'Helpo:\n\n'
    helpo += 'Oni povas doni tekston al Pinjinilo por konverti aŭ rekte aŭ de dosiero. Por '
    helpo += 'konverti tekston, aŭ tajpu en la tekstujon apud "Tajpu pinjinan tekston aŭ ĉinsignojn" kaj alklaku la '
    helpo += 'butonon "Konverti tekston", aŭ alklaku la butonon "Konverti dosieron" por elekti '
    helpo += 'tekstdosieron. Via originala teksto aperos maldekstre kaj la konvertita dekstre. '
    helpo += '\n\n'
    helpo += 'Por uzi nedefaŭltan konvertsistemon, alklaku la butonon "Ŝanĝi konvertsistemon" '
    helpo += 'kaj elektu la dosieron enhavantan vian deziratan sistemon. Tiaj dosieroj devas '
    helpo += 'havi la dosiertipon "csv" kaj jenan strukturon:'
    intrukcioj  = '{nomo de konvertsistemo}\n'
    intrukcioj += '{pinjino 1},{esperantigo 1}\n'
    intrukcioj += '{pinjino 2},{esperantigo 2}\n'
    intrukcioj += '{pinjino 3},{esperantigo 3}\n'
    intrukcioj += 'k.t.p......'
    # Krei aranĝon
    arangxo = [   [sg.Text(titolo, font='Courier 12', size=(80,7), background_color="white")],
                  [sg.Text('Konverti Ĉinan Pinjinan (汉语拼音) Tekston kaj Ĉinsignojn (汉字) al Esperanto-Literumsistemo', background_color="white")],
                  [sg.Text('© Mark Wootton 2020', background_color="white")],
                  [sg.Text('_'*76, font='Courier 12', background_color="white")],
                  [sg.Text(priskribo, size=[largxo,6], background_color="white")],
                  # [sg.Text('='*76, font='Courier 12', background_color="white")],
                  [sg.Text('_'*76, font='Courier 12', background_color="white")],
                  [sg.Text(helpo, size=[largxo,8], background_color="white")],
                  [sg.Text(intrukcioj, font='Courier 12', background_color="white")],
                  [sg.Text('Ne inkluzivu la krampojn kaj ne metu spaceton inter pinjinon kaj esperantigon.', background_color="white")],
                  [sg.Text('_'*76, font='Courier 12', background_color="white")],
                  [sg.Text('*Iomete da ĉinsignoj havas plurajn elparolojn, do tiukaze, oni eble ricevos malĝustan rezulton por tiuj ĉinsignoj.', background_color="white")],
                  [sg.Button('Reen')]
              ]
    # Krei fenestron
    fenestro = sg.Window('Pinjinilo: Helpo kaj Priskribo', arangxo, background_color='white')#, keep_on_top=True)
    while True:
        eventoH, _ = fenestro.read()
        if eventoH == sg.WIN_CLOSED or eventoH == 'Reen':
            break
    # Fermi fenestron
    fenestro.close()

def main():
    """
    La ĉefa funkcio, kiu kreias la ĉeffenestron kaj petas konvertojn de la
    modulo 'Funkcioj'.

    """
    # Agordi kolorojn
    sg.theme('DarkGreen')
    # Krei datumujojn
    enTeksto = ''
    elTeksto = ''
    ks = None
    ordo = None
    konvertsistemo = None
    # Trovi bildsimbolon laǔ operaciumo kaj agordi la larĝon de la tekstskatolo
    operaciumo = platform.system()
    if operaciumo == 'Linux':
        dosiertipo = 'png'
        largxo = 28
    elif operaciumo == 'Windows':
        dosiertipo = 'ico'
        largxo = 37
    elif operaciumo in ['Dawin', 'MacOs']: # MacOs ktp.
        dosiertipo = 'png'
        largxo = 44
    else:
        dosiertipo = 'png'
        largxo = 28
    # bildsimbolo = os.path.join(os.path.split(os.path.dirname(sys.argv[0]))[0], 'bildsimbolo', 'bildsimbolo.%s' % dosiertipo)
    # Agordi bildsimbolon
    sg.SetGlobalIcon(os.path.join(os.path.split(os.path.dirname(sys.argv[0]))[0], 'bildsimbolo', 'bildsimbolo.%s' % dosiertipo))
    # Krei maldekstran aranĝon
    enigo = [   [sg.Text('Elektu tekston aŭ dosieron por konverti', size=(50,1))],
                [sg.Text('Tajpu pinjinan tekston aŭ ĉinsignojn:'), sg.InputText(background_color='white', size=(largxo,1), do_not_clear=True)],
                # [sg.Text('Dosiero:'), ],
                [sg.Button('Konverti tekston', bind_return_key=True), sg.Input(key='_LEGIDOSIERON_', enable_events=True, visible=False), sg.FileBrowse('Konverti dosieron', target='_LEGIDOSIERON_', file_types=(('TXT', '.txt'), ('All files', '*'))), sg.Input(key='_SXANGXIKONVERTSISTEMON_', enable_events=True, visible=False), sg.FileBrowse('Ŝanĝi konvertsistemon', target='_SXANGXIKONVERTSISTEMON_', file_types=(('csv', '.csv'), ('TXT', '.txt'), ('All files', '*')), initial_folder=os.path.join(os.path.split(os.path.dirname(sys.argv[0]))[0], 'konvertsistemoj') )],#, sg.Button('Forigi enigojn')],
                [sg.Text('', key='dosiero', size=(60, 2))],
                [sg.Text('Originala teksto:')],
                [sg.Text(enTeksto, background_color='white', size=(60,10), key='enTeksto')],
                [sg.Button('Helpo kaj Priskribo')]
            ]
    # Krei dekstran aranĝon
    eligo = [   [sg.Text('Pinjinilo v%s' % fk.pjv(), size=(60,1), justification='right')],
                [sg.Text('Konverti Ĉinan Pinjinan (汉语拼音) Tekston al Esperanto-Literumsistemo', size=(60,1), justification='right')],
                [sg.Text('© Mark Wootton 2020', size=(60,1), justification='right')],
                # [sg.Text('', size=(50,1))],
                [sg.Text('', size=(50,1))],
                [sg.Text('', size=(50,1))],
                [sg.Text('Jen la konvertita teksto:', size=(60,1), key='jen')],
                [sg.Text(elTeksto, background_color='white', size=(60,10), key='elTeksto')],
                [sg.Button('Kopii al tondujo'), sg.Input(key='_KONSERVIDOSIERON_', enable_events=True, visible=False), sg.FileSaveAs('Konservi konvertitan tekston', file_types=(('TXT', '.txt'), ('All files', '*')), target='_KONSERVIDOSIERON_')]#, sg.Button('Ĉesi')] # , sg.Text(' '*72)
            ]
    # Kunmeti la du kolumnojn
    cxefarangxo = [[sg.Column(enigo), sg.VSeperator(), sg.Column(eligo)]]
    # Krei la ĉeffenestron
    cxeffenestro = sg.Window('Pinjinilo', cxefarangxo)
    # Iteracii ĝis ĉeffenestro estos fermita
    while True:
        # Legi eventojn kaj enmetitan datumon
        evento, datumujo = cxeffenestro.read()
        # Fenestro fermita
        if evento == sg.WIN_CLOSED or evento == 'Ĉesi':
            break
        # Konverti tekston rekte enmetitan
        elif evento == 'Konverti tekston':
            enTeksto = datumujo[0]
            cxeffenestro['dosiero'].update('')
            if not len(enTeksto):
                sg.popup('Mankas teksto por konverti', title='Mankas teksto', custom_text=('Bone'), background_color='white', keep_on_top=True)
        # Konverti tekston de dosiero
        elif evento == '_LEGIDOSIERON_':
            novaDosiero = datumujo['Konverti dosieron']
            enTeksto = fk.legiTekston(novaDosiero)
            cxeffenestro['dosiero'].update('Legante dosieron:\n%s' % novaDosiero)
        # Ŝanĝi konvertsistemon uzatan
        elif evento == '_SXANGXIKONVERTSISTEMON_':
            konvertsistemo = datumujo['Ŝanĝi konvertsistemon']
        # Montri fenestron de Helpo kaj Priskribo
        elif evento == 'Helpo kaj Priskribo':
            cxeffenestro.hide()
            helpoFenestro()
            cxeffenestro.un_hide()
        # Kopii eligon al tondujo
        elif evento == 'Kopii al tondujo' and len(elTeksto):
            pyperclip.copy(elTeksto)
        # Konservi eligon
        elif evento == '_KONSERVIDOSIERON_' and len(elTeksto):
            konservindiko = datumujo['Konservi konvertitan tekston']
            try:
                fk.konserviTekston(elTeksto, konservindiko)
            except:
                if len(konservindiko):
                    sg.popup('Vi ne povas konservi dosieron ĉe \'%s\'.\nReprovu aliloke.' % konservindiko, title='Konservada Eraro', custom_text=('Bone'), background_color='white', keep_on_top=True)
            else:
                sg.popup('Troviĝas ankoraŭ nenio por konservi', title='Nenio konservebla', custom_text=('Bone'), background_color='white', keep_on_top=True)

        # Ĝisdatigi etikedon ĉu nedefaŭlta konvertsistemo estas uzata
        if ks is None or ks['NOMO'] == 'Defaŭlto':
            cxeffenestro['jen'].update('Jen la konvertita teksto:')
        else:
            cxeffenestro['jen'].update('Jen la konvertita teksto (laŭ sistemo \'%s\'):' % ks['NOMO'])

        # Konverti tekston
        if len(enTeksto):
            ks, ordo = fk.legiKonvertsistemon(ks=konvertsistemo)
            elTeksto = fk.konverti(enTeksto, ks, ordo)
        # Montri originalan kaj konvertitan tekston
        cxeffenestro['enTeksto'].update(enTeksto)
        cxeffenestro['elTeksto'].update(elTeksto)
    # Fermi fenestro-objekton
    cxeffenestro.close()

if __name__ == '__main__':
    main()
