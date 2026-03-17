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




w = "2 + 3*(765 + 8/3) + 3*(9 - 3)# aa"
scan = Scanner()
tokens = scan.get_tokens(w)
for t in tokens:
    print(t)


