# Teoria Kompilacji i Kompilatory AGH


### Program wypisuje tokeny w postaci: (typ, wartosc)

| typ       | wartosc      |
|-----------|--------------|
| STR       | ciąg znaków  |
| INT       | liczba       |
| PLUS      | +            |
| MINUS     | -            |
| ILOCZYN   | *            |
| ILORAZ    | /            |
| LNAWIAS   | (            |
| PNAWIAS   | )            |
| ERROR     | inny typ     |

- skaner pomija spacje
- informuje na ktorej pozycji znajduje się token
- gdy nie rozpoznał danego znaku token posiada typ ERROR

#### Maciej Dziobek
