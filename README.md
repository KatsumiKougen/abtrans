For those who do not know, the Al Bhed language is a "constructed" language, spoken by the Al Bhed - a sub-group of humans in the 2001 JRPG **Final Fantasy Ⅹ** and its spin-off sequel, **Final Fantasy Ⅹ-２**.

Despite sounding and feeling like an actual constructed language, the Al Bhed language is not a language - at least not in a conventional way. It is actually just a substitution cipher.

In the game, there are items scattered across the world called *Al Bhed Primers*. Each *Al Bhed Primer*, when collected, can translate an Al Bhed letter. In order to learn the Al Bhed language, you need to collect 26 Primers.

You can find more information about the Al Bhed language [here](https://finalfantasy.fandom.com/wiki/Al_Bhed#Language).

This is the Al Bhed language translator that I wrote in Python 3.

The translator basically translates anything that the user writes (in English) into Al Bhed.<br>
```Do you not speak?``` --> ```Tu oui hud cbayg?```

Furthermore, it has a special feature that detects special vocabulary *(loanwords in Al Bhed language)* and ignores them when translating. The special vocabulary includes "aeon", "fayth", "sin", etc.<br>
```A lady summoner! We must report.``` --> ```Y myto summoner! Fa sicd nabund.```

~~However, the translator only care about special vocabulary, and not the non-letter symbols or digits next to it. When using the translator, make sure to add white space in between the special word and the non-letter symbol right next to it, like this: ```* fayth```. Otherwise, the translator outputs this instead:~~<br>
* ~~```Fill me with *fayth``` --> ```Vemm sa fedr *vyodr``` :x:~~
* ~~```Fill me with * fayth``` --> ```Vemm sa fedr * fayth``` :heavy_check_mark:~~
~~Don't worry, I'll fix it later.~~

**26 Feb. 2022 update:** fixed it.

The source code is free for all to download. You can get it by just downloading from the website. If you're using Linux, you can open the terminal and type ```git clone https://github.com/KatsumiKougen/abtrans```.

Example:
```python
import abtrans as abt

print(abt.trans("Bnacahdat po Katsumi - pa cyva yht ryja y hela tyo! :3",False))
```

Credit to [DudeBro249](https://github.com/DudeBro249) for contribution.

> Final Fantasy X, Final Fantasy X-2 - ©2001-2022 Square Enix. All rights reserved.