import re # For re.replace() and re.match()
#!/usr/bin/env python3

# Al Bhed Translator - Python 3.8+
# Written by Katsumi Kougen - All rights reserved.
# Final Fantasy X - (C) 2001-2022 Square Enix.

def trans(text: str, toAlBhed: bool = True) -> str:
    """
    Translates a piece of text into Al Bhed.
    def trans(text, toAlBhed)
        text: A string
        toAlBhed: A boolean flag for indicating if the text is to be translated from Al Bhed to English (Spiran) and vice versa
            True: Alb -> Eng
            False: Eng -> Alb
    """
    alb = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" # Al Bhed alphabet
    eng = "epstiwknuvgclrybxhmdofzqajEPSTIWKNUVGCLRYBXHMDOFZQAJ" # English (Spiran) alphabet
    specialvocab = ( # Special vocabulary
        "fiend","magic","aeon","airship","yevon","sin","summoner","machina","fayth","blitz","blitzball", # In-game terminology
        "maester","guardian","spiran","summoners","maesters","fiends","airships","machinas","fayths",
        "guardians","gullwings",
        "spira","besaid","kilika","luca","gagazet","bikanel","zanarkand","bevelle",                      # Location names
        "al-bhed","hypello","cactuar","ronso","guado","moogle","chocobo","chocobos",                     # Race names
        "tidus","yuna","auron","kimahri","wakka","lulu","rikku","paine",                                 # Player characters
        "seymour","braska","dona","belgemine","gandof","ginnem","isaaru","ohalland","yocun","zuke",      # Non-player characters
        "yunalesca","barthello","jecht","maroda","pacce","zaon","chappu","clasko","elma","lucil",
        "luzzu","gatta","mi'ihen","jyscal","kelk","mika","wen-kinoc","cid","rin","keyakku","biran",
        "yenke","calli","maechen","omega","shelinda","shinra",
        "python","bisqwit","katsumi","shulk","reyn","fiora","dunban","melia","sharla","riki","github",   # Miscellaneous
        "minecraft","c++","cloud","tifa","barret","aerith","jessie","biggs","wedge","yuffie","noctis",
        "noct","gladiolus","gladio","gladdy","gladi","ignis","iggy","prompto","lunafreya","ardyn"
    )
    out = [] # Create an output list
    wordlist = text.split(" ") # Create a list of words
    while "" in wordlist:
        wordlist.remove("") # Remove all empty strings
    for pos, word in enumerate(wordlist):
        cword = re.sub("[`\"\\|'\\<\\^\\>\\!\\?\\,\\.:;\\-\\(\\)\\[\\]\\{\\}\\=\\+&%@#\\$~/\\*\\\\\\d]*", "", word) # Remove all non-ASCII characters
        if cword.lower() in specialvocab: # Is the word in the special vocabulary?
            out.append(word) # Add that word to the output list
        elif re.match("[`\"\\|'\\<\\^\\>\\!\\?\\,\\.:;\\-\\(\\)\\[\\]\\{\\}\\=\\+&%@#\\$~/\\*\\\\\\d]*[A-Za-z]+", word) != None: # Is the word contains nothing but letters, and just letters?
            if toAlBhed: # English to Al Bhed
                out.append("".join([alb[eng.index(char)] if char in eng else char for char in word])) # Add the translated word to the output list
            else: # Vice versa
                out.append("".join([eng[alb.index(char)] if char in alb else char for char in word])) # Same above
        else:
            out.append(word) # Add that word to the output list
    return " ".join(out) # Join the words with spaces and return the string