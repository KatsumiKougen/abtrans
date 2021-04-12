#!/usr/bin/env python3

# Al Bhed Translator - Python 3.8+
# Written by Katsumi Kougen - All rights reserved.
# Final Fantasy X - (C) 2001-2021 Square Enix.

from typing import Optional


def trans(text: str, toAlBhed: Optional[bool] = True) -> str:
    alb = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    eng = "epstiwknuvgclrybxhmdofzqajEPSTIWKNUVGCLRYBXHMDOFZQAJ"
    specialvocab = (
        # In-game terminology
        "fiend", "magic", "aeon", "airship", "yevon", "sin", "summoner", "machina", "fayth", "blitz", "blitzball",
        "maester", "guardian", "spiran", "summoners", "maesters", "fiends", "airships", "machinas", "fayths",
        "guardians",
        # Location names
        "spira", "besaid", "kilika", "luca", "gagazet", "bikanel", "zanarkand",
        # Race names
        "al-bhed", "hypello", "cactuar", "ronso", "guado", "moogle", "chocobo", "chocobos",
        # Player characters
        "tidus", "yuna", "auron", "kimahri", "wakka", "lulu", "rikku", "paine",
        # Non-player characters
        "seymour", "braska", "dona", "belgemine", "gandof", "ginnem", "isaaru", "ohalland", "yocun", "zuke",
        "yunalesca", "barthello", "jecht", "maroda", "pacce", "zaon", "chappu", "clasko", "elma", "lucil",
        "luzzu", "gatta", "mi'ihen", "jyscal", "kelk", "mika", "wen-kinoc", "cid", "rin", "keyakku", "biran",
        "yenke", "calli", "maechen", "omega", "shelinda",
        "python", "bisqwit", "katsumi", "shulk", "reyn", "fiora", "dunban", "melia", "sharla", "riki", "github",   # Miscellaneous
    )
    out = []
    if toAlBhed:
        wordlist = text.split(" ")
        out = [word if word.lower() in specialvocab else "".join(
            [alb[eng.index(char)] if char in eng else char for char in word]) for word in wordlist]
        return " ".join(out)
    else:
        wordlist = text.split(" ")
        out = [word if word.lower() in specialvocab else "".join([eng[alb.index(
            char)] if char in alb else char for char in word]) for word in wordlist]
        return " ".join(out)
