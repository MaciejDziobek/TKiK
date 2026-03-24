# Teoria Kompilacji i Kompilatory AGH


### Program wypisuje tokeny w postaci: (typ, wartość), następnie koloruje składnie w html


| typ       | wartość     | Kolor                 |
|-----------|-------------|-----------------------|
| STR       | ciąg znaków | zielony               |
| INT       | liczba      | cyan                  |
| PLUS      | +           | jasny pozłacany żółty |
| MINUS     | -           | jasny pozłacany żółty |
| ILOCZYN   | *           | jasny pozłacany żółty |
| ILORAZ    | /           | jasny pozłacany żółty |
| LNAWIAS   | (           | pomarańczowy          |
| PNAWIAS   | )           | pomarańczowy          |
| ERROR     | inny typ    | czerwone tło          |

- Skaner zwraca listę Tokenów - .get_tokens() przyjmujac ciąg znaków
- pomija spacje
- informuje na której pozycji znajduje się Token
- gdy nie rozpoznał danego znaku Token posiada typ ERROR
- funkcja tokens_to_html zwraca string w formacie html który potem jest zapisywany do pliku .html

#### Maciej Dziobek
