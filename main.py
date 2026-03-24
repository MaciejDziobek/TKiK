class Token:
    def __init__(self, typ , wartosc, pos):
        self.typ = typ
        self.wartosc = wartosc
        self.pos = pos

    def __str__(self):
        if self.typ == "ERROR":
            return f"ERROR: nie rozpoznano tokena: '{self.wartosc}' na pozycji {self.pos}"

        return f"({self.typ}, '{self.wartosc}') pos = {self.pos}"

class Scanner:
    def __init__(self):
        self.types = {"+": "PLUS", "-": "MINUS", "*": "ILOCZYN", "/": "ILORAZ", "(": "LNAWIAS", ")": "PNAWIAS"}

    def get_tokens(self, wyrazenie):
        tokens = []
        pos = 0

        while pos < len(wyrazenie):
            if wyrazenie[pos] == " ":
                pos += 1
                continue

            if wyrazenie[pos].isdigit():
                num = wyrazenie[pos]
                start_pos = pos
                pos += 1
                while pos < len(wyrazenie) and wyrazenie[pos].isdigit():
                    num += wyrazenie[pos]
                    pos += 1
                tokens.append(Token("INT", num, start_pos))
            elif wyrazenie[pos].isalpha():
                ciag = wyrazenie[pos]
                start_pos = pos
                pos += 1
                while pos < len(wyrazenie) and wyrazenie[pos].isalpha():
                    ciag += wyrazenie[pos]
                    pos += 1
                tokens.append(Token("STR", ciag, start_pos))
            else:
                try:
                    tokens.append(Token(self.types[wyrazenie[pos]], wyrazenie[pos], pos))
                except KeyError:
                    tokens.append(Token("ERROR", wyrazenie[pos], pos))
                pos+=1
        return tokens




def tokens_to_html(tokens):
    html = '<!DOCTYPE html>\n<html lang="en">\n'
    html += '<head>\n<meta charset="UTF-8">\n<title>Skaner</title>\n<style>\n'
    html += ".INT { color: cyan; }\n"
    html += ".STR { color: green; }\n"
    html += ".PLUS, .MINUS, .ILOCZYN, .ILORAZ { color: lightgoldenrodyellow; }\n"
    html += ".LNAWIAS, .PNAWIAS { color: orange; }\n"
    html += ".ERROR { color: white; background-color: red; }\n"
    html += "</style>\n</head>\n<body style='background-color: #2b2b2b;'>\n<pre>\n"

    for t in tokens:
        html += f"{' ' if t.wartosc in "+-" else ''}<span class='{t.typ}'>{t.wartosc}</span>{' ' if t.wartosc in "+-" else ''}"

    html += "\n</pre>\n</body>\n</html>"
    return html



w = "2 + 3*(765 + 8/3) + 3*(9 - 3) #ab + 2 - 7()"
scan = Scanner()
tokens = scan.get_tokens(w)
for t in tokens:
    print(t)
html = tokens_to_html(tokens)

with open("output.html", "w", encoding="utf-8") as f:
    f.write(html)


