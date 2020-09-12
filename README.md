![Pinjinilo](bildsimbolo/bildsimbolo.png?raw=true)
# *Pinjinilo*
## Konverti Ĉinan Pinjinan (汉语拼音) Tekston kaj Ĉinsignojn (汉字) al Esperanto-Literumsistemo

Pinjino estas sistemo por priskribi la sonojn de ĉinsignoj per latinaj literoj. La literoj uzataj malsamas al tiuj en la alfabeto de Esperanto, do la celo de ĉi tiu programo estas konverti de norma Pinjino aŭ ĉinsignoj al proksimumo laŭ la literumsistemo de Esperanto. Defaŭlte, ĝi uzas la sistemon kreitan de la revuo [*El Popola Ĉinio*](https://eo.wikipedia.org/wiki/Esperantigo_de_vortoj_el_%C4%89ina_fonto), sed la uzanto povas uzi iun ajn sistemon, se oni kreas sian propran dosieron priskribantan ĝin. [Python 3](https://www.python.org) aŭ pli freŝa versio estas bezonata por roli *Pinjinilon*. Modulo [*xpinyin*](https://pypi.org/project/xpinyin) necesas por konverti ĉinsignojn.

### Bezonaĵoj
* *Python 3*
* *xpinyin*
* *Konvertsistemoj* (modulo de *Pinjinilo*)
* Oni eble bezonos instali ankaŭ la modulon *tkinter*

### Uzado
Oni havas tri opciojn por uzi *Pinjinilon*:
* Per la komanda linio. Rulu la Python3-skripton *Funkcioj.py* kun la jenaj enigoj:
  1. `[teskto]` - La teksto, kiun oni volus konverti, aŭ indiko al tekstdosiero enhavanta ĝin
  2. `-k [konvertsistemo]`  - Iu alternativa sistemo por konverti la tekson (nedeviga)
  3. `-h`  - Montri helpmesaĝon (nedeviga)
* Per la grafika fasado. Rulu la Python3-skripton *Pinjinilo.py*
* Kiel memstaran programon. En la dosierujo *memstaraĵoj* troviĝas iom da ruleblaj dosieroj por diversaj operaciumoj. Se estas iu taŭga por onia komputilo, oni povas uzi ĝin por ruli *Pinjinilon* sen la bezono esti instalinta Python-interpretilon aŭ la modulojn de ekstera liveranto. Se neniu estas uzebla, oni povas krei sian propran per [*PyInstaller*](https://www.pyinstaller.org), uzante komandon el la la jenaj, kiu taŭgas por onia operaciumo:

Linux:
```
pyinstaller --onefile --noconsol --icon bildsimbolo/bildsimbolo.png Pinjinilo.py
```

Windows:
```
pyinstaller --onefile --noconsol --icon bildsimbolo/bildsimbolo.ico Pinjinilo.py
```

MacOS:
*Se oni ekscias, kiel funkciigi la memstaraĵon en MacOs, bonvole sciigu ankaŭ min*

### Aŭtorrajto
© Mark Woottton 2020
