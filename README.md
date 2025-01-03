The Al Bhed language, introduced in the 2001 game "Final Fantasy X" and its follow-up "Final Fantasy X-2", is a "constructed" language spoken by the Al Bhed, a distinct human group.

Although it might seem like a legitimate constructed language, Al Bhed is, in fact, [a simple cipher](https://tvtropes.org/pmwiki/pmwiki.php/Main/CypherLanguage) where one letter is substituted for another.

Throughout the game, there are collectible items known as Al Bhed Primers, each of which reveals the translation for one Al Bhed letter. Collecting all 26 Primers will allow you to understand the entire language.

You can find more information about the Al Bhed language [here](https://finalfantasy.fandom.com/wiki/Al_Bhed#Language).

I developed this Al Bhed language translator in Python 3.

The tool translates any text written in English to Al Bhed.

`Do you not speak?` --> `Tu oui hud cbayg?`

It also features a special function that identifies certain words (like "aeon", "fayth", "sin") and leaves them untranslated, as they are part of Al Bhed's unique lexicon.

`A lady summoner! We must report.` --> `Y myto summoner! Fa sicd nabund.`

~~However, the translator only care about special vocabulary, and not the non-letter symbols or digits next to it. When using the translator, make sure to add white space in between the special word and the non-letter symbol right next to it, like this: ```* fayth```. Otherwise, the translator outputs this instead:~~<br>
* ~~```Fill me with *fayth``` --> ```Vemm sa fedr *vyodr``` :x:~~
* ~~```Fill me with * fayth``` --> ```Vemm sa fedr * fayth``` :heavy_check_mark:~~
~~Don't worry, I'll fix it later.~~

**26 Feb. 2022 update:** I finally fixed it.

You can download the source code for free. Simply navigate to the website to get it.

On Linux, you can also clone the repository by opening the terminal and running: ```git clone https://github.com/KatsumiKougen/abtrans```.

Example:

```python
import abtrans as abt

print(abt.trans("Bnacahdat po Katsumi - pa cyva yht ryja y hela tyo! :3",False))
```

Credit to [DudeBro249](https://github.com/DudeBro249) for contribution.

> Final Fantasy X, Final Fantasy X-2 - ©2001-2025 Square Enix. All rights reserved.
