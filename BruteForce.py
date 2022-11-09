def createList():

    liczba_elementow = 21 # Ogranicznik, który blokuje wprowadzenie więcej niż 20 elementów
    while not  (liczba_elementow <= 20 and liczba_elementow >= 1): # Ograniczenie tablicy od 1 do 20 elementów
        liczba_elementow = int(input("Wprowadz liczbe elementow z przedzialu 1-20: "))

    elementy_zbioru = [] # Pusta tablica, która w dalszej części będzie przechowywać 
                         # elementy wprowadzone przez użytkownika

    for i in range(liczba_elementow): # Wprowadzenie kolejnych liczb do tablicy 'elementy_zbioru'
        element = int(input("Podaj liczbe: "))
        elementy_zbioru.append(element) # Dodawanie elementów do tablicy

    print(f'Zbior liczb: {elementy_zbioru}') # Wypisanie zawartości tablicy
    return elementy_zbioru # Zwrócenie wartości tablicy z funkcji


def exhaustiveSearch(elementy_zbioru):
    element = int(input("Ktory element chcesz szukac? "))
    licznik_przejsc = 0
    for i in range(len(elementy_zbioru)):
        if elementy_zbioru[i] == element:
            return print(f'Znaleziono element {element} pod indeksem {elementy_zbioru.index(element)}')
    return print(f'Brak wskazanego elementu')
        
def binarySearch(elementy_zbioru):
    element = int(input("Ktory element chcesz szukac? "))
    low = 0 # Indeks 0 pierwszego elementu listy
    high = len(elementy_zbioru) -1 # Indeks ostatniego elementu listy
    while low <= high:
        mid = (high + low) // 2 # Znalezienie środkowego elementu
        print(f'Indeks z lewej strony {low}, indeks z prawej strony {high}, środek {mid}')
        if elementy_zbioru[mid] < element:
            low = mid + 1
        elif elementy_zbioru[mid] > element:
            high = mid -1
        else: 
            return mid
    return -1


def listIndex(elementy_zbioru):
    index = 0
    for i in elementy_zbioru:
        print(f'[Index:{index} Wartosc:{i} ]') # Iteracja wypisująca wartość wraz z indexem tablicy
        index += 1


def implementacja():
    elementy_zbioru = createList()
    listIndex(elementy_zbioru)
    exhaustiveSearch(elementy_zbioru)
    elementy_zbioru.sort()
    print(f'Posortowana tablica: {elementy_zbioru}')
    listIndex(elementy_zbioru)
    wynik_binarySearch = binarySearch(elementy_zbioru)
    if wynik_binarySearch != -1:
        print(f'Element znajduje się na indeksie {wynik_binarySearch}')
    else:
        print(f'Brak wskazanego elementu')
implementacja()

