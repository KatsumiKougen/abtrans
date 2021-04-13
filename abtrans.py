#!/usr/bin/env python3

# Al Bhed Translator - Python 3.8+
# Written by Katsumi Kougen - All rights reserved.
# Final Fantasy X - (C) 2001-2021 Square Enix.

def trans(text,toAlBhed=True):
    alb="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    eng="epstiwknuvgclrybxhmdofzqajEPSTIWKNUVGCLRYBXHMDOFZQAJ"
    specialvocab=(
        "fiend","magic","aeon","airship","yevon","sin","summoner","machina","fayth","blitz","blitzball", # In-game terminology
        "maester","guardian","spiran","summoners","maesters","fiends","airships","machinas","fayths",
        "guardians","gullwings",
        "spira","besaid","kilika","luca","gagazet","bikanel","zanarkand",                                # Location names
        "al-bhed","hypello","cactuar","ronso","guado","moogle","chocobo","chocobos",                     # Race names
        "tidus","yuna","auron","kimahri","wakka","lulu","rikku","paine",                                 # Player characters
        "seymour","braska","dona","belgemine","gandof","ginnem","isaaru","ohalland","yocun","zuke",      # Non-player characters
        "yunalesca","barthello","jecht","maroda","pacce","zaon","chappu","clasko","elma","lucil",
        "luzzu","gatta","mi'ihen","jyscal","kelk","mika","wen-kinoc","cid","rin","keyakku","biran",
        "yenke","calli","maechen","omega","shelinda","shinra",
        "python","bisqwit","katsumi","shulk","reyn","fiora","dunban","melia","sharla","riki","github",   # Miscellaneous
        "minecraft","c++","cloud","tifa","barret","aerith","jessie","biggs","wedge","yuffie","noctis",
        "noct","gladiolus","gladio","gladdy","gladi","ignis","iggy","prompto",
    )
    out=[]
    if toAlBhed:
        wordlist=text.split(" ")
        return " ".join([word if word.lower() in specialvocab else "".join([alb[eng.index(char)] if char in eng else char for char in word]) for word in wordlist])
    else:
        wordlist=text.split(" ")
        return " ".join([word if word.lower() in specialvocab else "".join([eng[alb.index(char)] if char in alb else char for char in word]) for word in wordlist])
