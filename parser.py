from html.parser import HTMLParser

with open("dial_test.html", "r") as fin:
    line = fin.read()
    line = line[line.find("</head>") + 7:]

f = open("dial_test.txt", "w")

message_packs = []
msg_pack = []
prev_id = ""
prev = ""

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        pass
        #print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        pass
        #print("Encountered an end tag :", tag)

    def handle_data(self, data):
        global msg_pack, prev_id, prev
        data = data.strip()

        if ("Даты сообщений:" in data or "Всего сообщений:" in data):
            pass
        elif len(data) == 0:
            pass
        #elif data[0] == "[" or data == "Материалы:" or data == "Ссылка" or data == "Пересланные сообщения:":
            #prev = data
        elif data[0] == "@":
            if len(msg_pack):
                msg_pack.pop(-1)
            if prev_id != data and len(prev_id) and len(msg_pack):
                message_packs.append((prev_id, msg_pack))
                msg_pack = []
            prev_id = data
            prev = data
        elif len(data) >= 17 and (data[4] == "." and data[7] == "." and data[10] == " " and data[13] == ":" and data[16] == ":"):
            print("time", file = f)
        elif "https" in data:
            pass
        else:
            if prev != "Ссылка":
                msg_pack.append(data)
            #print(data, file = f)
            prev = data

parser = MyHTMLParser()
parser.feed(line)

f.close()

with open("dial_tst.txt", "w") as fout:
    for line in message_packs:
        print(line[0], line[1], file = fout)
