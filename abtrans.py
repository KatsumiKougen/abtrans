#!/usr/bin/env python3

# Al Bhed Translator - Python 3.8+
# Written by Katsumi Kougen - All rights reserved.
# Final Fantasy X - (C) 2001-2021 Square Enix.

alb="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
eng="epstiwknuvgclrybxhmdofzqajEPSTIWKNUVGCLRYBXHMDOFZQAJ"
specialvocab=(
    "fiend","magic","aeon","airship","yevon","sin","summoner","machina","fayth","blitz","blitzball", # In-game terminology
    "maester","guardian","spiran","summoners","maesters","fiends","airships","machinas","fayths",
    "guardians",
    "spira","besaid","kilika","luca","gagazet","bikanel","zanarkand",                                # Location names
    "al-bhed","hypello","cactuar","ronso","guado","moogle","chocobo","chocobos",                     # Race names
    "tidus","yuna","auron","kimahri","wakka","lulu","rikku","paine",                                 # Player characters
    "seymour","braska","dona","belgemine","gandof","ginnem","isaaru","ohalland","yocun","zuke",      # Non-player characters
    "yunalesca","barthello","jecht","maroda","pacce","zaon","chappu","clasko","elma","lucil",
    "luzzu","gatta","mi'ihen","jyscal","kelk","mika","wen-kinoc","cid","rin","keyakku","biran",
    "yenke","calli","maechen","omega","shelinda",
    "python","bisqwit","katsumi","shulk","reyn","fiora","dunban","melia","sharla","riki","github",   # Miscellaneous
)

def trans(text,toAlBhed=True):
    out=[]
    if toAlBhed:
        wordlist=text.split(" ")
        for word in wordlist:
            if word.lower() in specialvocab:out.append(word)
            else:out.append("".join([alb[eng.index(char)] if char in eng else char for char in word]))
        return " ".join(out)
    else:
        wordlist=text.split(" ")
        for word in wordlist:
            if word.lower() in specialvocab:out.append(word)
            else:out.append("".join([eng[alb.index(char)] if char in alb else char for char in word]))
        return " ".join(out)

while True:print(trans(input()))
