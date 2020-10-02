# *<img src='bildsimbolo/bildsimbolo.png' width='45' title='Pinjinilo'> Pinjinilo*
## Konverti Ĉinan Pinjinan (汉语拼音) Tekston kaj Ĉinsignojn (汉字) al Esperanto-Literumsistemo

Pinjino estas sistemo por priskribi la sonojn de ĉinsignoj per latinaj literoj. La literoj uzataj malsamas al tiuj en la alfabeto de Esperanto, do la celo de ĉi tiu programo estas konverti de norma Pinjino aŭ ĉinsignoj al proksimumo laŭ la literumsistemo de Esperanto. Defaŭlte, ĝi uzas la [sistemon kreitan](https://eo.wikipedia.org/wiki/Esperantigo_de_vortoj_el_%C4%89ina_fonto) de la revuo [*El Popola Ĉinio*](https://eo.wikipedia.org/wiki/El_Popola_%C4%88inio) (vidu suben), sed la uzanto povas uzi iun ajn sistemon, se oni kreas sian propran dosieron priskribantan ĝin.

<p align="center">
  <img src='ekrankopioj/GrafikaFasado.png' width='500' title='La grafika fasado de Pinjinilo'><img src='ekrankopioj/Komandlineo.png' width='400' title='La komandlinea fasado de Pinjinilo'>
</p>
### Aŭtorrajto

© Mark Woottton 2020

### Bezonaĵoj

* [*Python 3*](https://www.python.org) kaj la jenaj moduloj de ekstera liveranto:
  * [*PySimpleGUI*](https://pysimplegui.readthedocs.io)
  * [*xpinyin*](https://pypi.org/project/xpinyin)
  * [*tkinter*](https://wiki.python.org/moin/TkInter) (Oni eble trovos, ke tiu jam estis instalita samtempe de Python mem)
* [*PyInstaller*](https://www.pyinstaller.org) (nur por krei memstaran ruleblan dosieron)

### Uzado
Oni havas tri opciojn por uzi *Pinjinilon*:
* Per la komanda linio. Rulu la *Python3*-skripton *Funkcioj.py* kun la jenaj enigoj:
  1. `[teskto]` - La teksto, kiun oni volus konverti, aŭ indiko al tekstdosiero enhavanta ĝin
  2. `-k [konvertsistemo]`  - Iu alternativa sistemo por konverti la tekson (nedeviga)
  3. `-h`  - Montri helpmesaĝon (nedeviga)
* Per la grafika fasado. Rulu la *Python3*-skripton *Pinjinilo.py*
* Kiel memstaran programon. En la dosierujo *memstaraĵoj* troviĝas iom da ruleblaj dosieroj por diversaj operaciumoj. Se estas iu taŭga por onia komputilo, oni povas uzi ĝin por ruli *Pinjinilon* sen la bezono esti instalinta *Python*-interpretilon aŭ la modulojn de ekstera liveranto. Se neniu estas uzebla, oni povas krei sian propran per [*PyInstaller*](https://www.pyinstaller.org), uzante komandon el la la jenaj, kiu taŭgas por onia operaciumo:

*Linux*:
```
pyinstaller --onefile --noconsol --icon bildsimbolo/bildsimbolo.png Pinjinilo.py
```

*Windows*:
```
pyinstaller --onefile --noconsol --icon bildsimbolo/bildsimbolo.ico Pinjinilo.py
```

*MacOS*:
*Se oni ekscias, kiel funkciigi la memstaraĵon en MacOs, bonvole sciigu ankaŭ min*

### Krei Konvertsistemon
Por krei alian konvertsistemon, skribu ĝin en `*.csv` dosiero kun la jenan strukturon (ne inkluzivu la krampojn):
```
{nomo de konvertsistemo}
{pinjino 1},{esperantigo 1}
{pinjino 2},{esperantigo 2}
{pinjino 3},{esperantigo 3}
k.t.p......
```
Oni povas alvoki ĝin per alklako de la butono *Ŝanĝi konvertsistemon* en la grafika fasado aŭ per la `-k` opcio en la komandlinea versio de `Funkcioj.py`.

### Defaŭlta Konvertsistemo

La [defaŭlta konvertsistemo](https://eo.wikipedia.org/wiki/Esperantigo_de_vortoj_el_%C4%89ina_fonto) estis kreita de la ĉina Esperanto-revuo [*El Popola Ĉinio*](https://eo.wikipedia.org/wiki/El_Popola_%C4%88inio) kaj troviĝas en la jena tabelo.

| Pinjino | Esperantigo |
| ------- | ----------- |
| b       | b           |
| d       | d           |
| g       | g           |
| j       | ĝj          |
| zh      | ĝ           |
| z       | z           |
| p       | p           |
| t       | t           |
| k       | k           |
| q       | ĉj          |
| ch      | ĉ           |
| c       | c           |
| m       | m           |
| n       | n           |
| h       | h           |
| x       | ŝj          |
| sh      | ŝ           |
| s       | s           |
| f       | f           |
| l       | l           |
| y       | j           |
| r       | ĵ           |
| w       | ŭ           |
| a       | a           |
| ai      | aj          |
| an      | an          |
| ü       | u           |
| o       | o           |
| ei      | ej          |
| en      | en          |
| i       | i           |
| e       | e           |
| ao      | aŭ          |
| ang     | ang         |
| u       | u           |
| ou      | oŭ          |
| eng     | eng         |
| er      | er          |
| ie      | je          |
| ia      | ja          |
| üa      | ŭa          |
| uo      | ŭo          |
| üe      | ŭe          |
| iao     | jaŭ         |
| iou     | juŭ         |
| uei     | ŭej         |
| uai     | ŭaj         |
| ian     | jan         |
| uen     | ŭen         |
| üan     | ŭan         |
| iang    | jang        |
| iong    | jong        |
| ueng    | ŭeng        |
| uang    | ŭang        |