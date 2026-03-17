# Teoria Kompilacji i Kompilatory AGH


### Program wypisuje tokeny w postaci: (typ, wartość)

| typ       | wartość     |
|-----------|-------------|
| STR       | ciąg znaków |
| INT       | liczba      |
| PLUS      | +           |
| MINUS     | -           |
| ILOCZYN   | *           |
| ILORAZ    | /           |
| LNAWIAS   | (           |
| PNAWIAS   | )           |
| ERROR     | inny typ    |

- Skaner zwraca listę Tokenów - .get_tokens() przyjmujac ciąg znaków
- pomija spacje
- informuje na której pozycji znajduje się Token
- gdy nie rozpoznał danego znaku Token posiada typ ERROR

#### Maciej Dziobek
