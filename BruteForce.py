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
    if element in elementy_zbioru:
        return print(f'Znaleziono element {element} pod indeksem {elementy_zbioru.index(element)}')
    else:
        return print("Brak wskazanego elementu")


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

#MASZALAH
implementacja()

#https://www.programiz.com/dsa/binary-search