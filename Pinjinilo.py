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

(c) Mark Woottton 2020

================================================================================

Por krei memstaran aplikaĵon per PyInstaller (https://www.pyinstaller.org), uzu
unu el la jenaj komandoj, taŭgan por via operaciumo.

[Linux & MacOs]
pyinstaller --onefile --noconsol --icon bildsimbolo/bildsimbolo.png Pinjinilo.py

[Windows]
pyinstaller --onefile --noconsol --icon bildsimbolo/bildsimbolo.ico Pinjinilo.py

"""
import GrafikaFasado
GrafikaFasado.main()
