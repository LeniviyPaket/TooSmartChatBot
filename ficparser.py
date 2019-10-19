with open("ficnums.txt", "r") as fin:
    for line in fin:
        txt = open("./texts/fic" + line + ".txt").read()
        beg = txt.find("jsPartText")
        en = beg + txt[beg:].find("</div>")
