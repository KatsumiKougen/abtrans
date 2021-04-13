For those who do not know, the Al Bhed language is a verbal language, spoken by the Al Bhed - a sub-group of human in the 2001 JRPG **Final Fantasy Ⅹ** and its standalone sequel, **Final Fantasy Ⅹ-２**.</br>
Despite sounding and feeling like an actual constructed language, the Al Bhed language is not a language - at least not in a conventional way. It is actually just a substitution cipher.</br>
In the game, there are items scattered across the world called *Al Bhed Primers*. Each *Al Bhed Primer*, when collected, can translate an Al Bhed letter. In order to learn the Al Bhed language, you need to collect 26 Primers.

You can find more information about the Al Bhed language [here](https://finalfantasy.fandom.com/wiki/Al_Bhed#Language).

This is the Al Bhed language translator that I wrote in Python 3.</br>
The translator basically translates anything that the user writes (in English) into Al Bhed.</br>
```Do you not speak?``` --> ```Tu oui hud cbayg?```</br>
Furthermore, it has a special function that detects special vocabulary *(loanwords in Al Bhed language)* and ignore them when translating.</br>
The special vocabulary includes "aeon", "fayth", "sin", etc.</br>
```A lady summoner ! We must report.``` --> ```Y myto summoner ! Fa sicd nabund.```</br>
However, the translator only care about special vocabulary, and not the non-letter symbols or digits next to it. When using the translator, make sure to add white space in between the special word and the non-letter symbol right next to it, like this: ```* fayth```. Otherwise, the translator outputs this instead:</br>
```Fill me with *fayth``` --> ```Vemm sa fedr *vyodr``` :x:</br>
```Fill me with * fayth``` --> ```Vemm sa fedr * fayth``` :heavy_check_mark:</br>
Don't worry, I'll fix it later.

The source code is free to download. You can get it by just downloading from the website, or if you're using Linux, you can open the terminal and type ```git clone https://github.com/KatsumiKougen/abtrans```.

The translator is a Python module. To use it, you must import it to your program.</br>
```python
import abtrans as abt

print(abt.trans("Bnacahdat po Katsumi - pa cyva yht ryja y hela tyo! :3",False))
```

Credit to [DudeBro249](https://github.com/DudeBro249) for some refactoring here and there.

> Final Fantasy X, Final Fantasy X-2 - ©2001-2021 Square Enix. All rights reserved.
