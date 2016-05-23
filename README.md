"# ProgramDoNauki" 
Program do nauki j. angielskiego

1. Wstęp
    Program będzie posiadał prostą szatę graficzną, słówka będa pobierane z bazy danych, która będzie dostępna dla użytkownika.
  Użytkownik będzie miał możliwość modyfikowania tej bazy poprzez aktualizowanie oraz edytowanie jej zawartości. Użytkownik
  po włączeniu programu wybiera ilość słów do przyswojenia, po czym zostają one wylosowane z bazy danych i wyświetlone na
  ekranie. Celem użytkownika jest wpisanie poprawnej definicji w języku polskim, co skutkuje zmianą stanu słowa na zaliczone,
  w przeciwnym wypadku użytkownik musi poprawić swoją odpowiedź.
  
2. Opis ogólny

  a. Interfejs systemowy
    - połączenie z bazą danych
    - połączenie z modułem odpowiedzialnym za GUI - tkinter
    
  b. Interfejs użytkownika
    - Widget graficzny z 3 przyciskami (rozpocznij naukę, edytuj bazę danych, wyjście) oraz rozwijane menu
    z dostępnymi tematami słówek.
    - Główne okno zawierające pole, do którego wprowadzamy słowo, widget wyświetlający zadane słowo oraz
    przycisk wysyłający wprowadzone słowo do przetworzennia przez program i wyświetlenia rezultatu po zakończeniu
    sesji (czyli po wprowadzeniu zadanej ilości słów).
    - Widget edycji bazy słówek, dostępny po kliknięciu przycisku "Edytuj". Widget posiada 2 zakładki,
    pierwsza, w której znajduje się input field do wprowadzania słowa, drugi do jego tłumacznia oraz
    button zatwierdzający decyzję. Druga zakładka będzie posiadała rozwijane menu, z którego użytkownik może wybrać
    daną kategorię, button zatwierdzający decyzję oraz widget wyświetlający słówka w wybranej kategorii.
    
  c. Funkcje
    - połączenie z bazą danych w celu pobrania słówek
    - edycja bazy danych
    - generowanie GUI
    - sortowanie zawartości bazy danych
    
  d. Ogranicznia
    - brak kontroli poprawności słów wprowadzanych do bazy przez użytkowinka
    - szybkość działania programu na rozległych bazach danych
    
3. Wymagania szczegółowe
    - Python 3.5.1
    - baza danych sqlite3
    - moduł łączący się z bazą danych sqlite3
    - tkinter
    - podejście obiektowe
  
    a) Wydajność programu w głównej mierze zależna od zastosowanego algorytmu sortującego bazę danych. W związku z wysokim
obciażeniem procesora przez proces sortujący, szata graficzna programu nie może być skomplikowana, co powinno wpłynąć
pozytywnie na działanie całości programu.

    b) Obsługa wyjątków:
    - W przypadku wpisania niedozwolonego znaku (np. cyfy lub znaku interpunkcyjnego) program pozwala użytkownikowi
        na ponowne wprowadzenie danych.
    - W przypadku braku wymaganej ilości słów z danej kategorii w bazie danych, program wyświetli tyle słów ile
        obecnie znajduje się w bazie danych.

5. Cel i zakres systemu
    Celem programu jest ułatwienie i zautomatyzowanie procesu nauki i powtarzania nowych słów w języku angielskim.
    Program jest przeznaczony do działania na komputerze użytkownika bez konieczności łączenia się z internetem.
    Program zapisuje postęp dla jednego użytkownika.

6. Wymagania funkcjonalne
  - Przetwarzanie zawartosci bazy danych i wyswietlanie jej na ekranie.
  - Sprawdzanie poprawnosci wprowadzonej odpowiedzi.
  - Zapisywanie postepu uzytkownika.

7. Wymagania pozafunkcjonalne
  - Przejrzysty interfejs użytkownika.
  - Szybkość działania programu.

8. Harmonogram prac
  - Utworzenie prostej bazy danych, zawierającej kilkanaście słow wraz z ich tłumaczeniem.
  - Storzenie klas odpowiedzialnych za połączenie z baza danych i przetwarzanie jej zawartości do programu.
  - Stworzenie wstepnej wersji interfejsu żzytkownika.
  - Opisanie systemu w jezyku UML.
  - Utworzenie prototypu.
  - Usuniecie wiekszych błędów.
  - Ewentualna optymalizacja działania programu.
  - Utworzenie dokumentacji technicznej i podręcznika użytkownika.
