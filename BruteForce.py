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
    element = int(input("Ktory element chcesz szukac?"))
    pos = elementy_zbioru.index(element) 
    print("Indeks twojego elementu to",pos)


createList()
exhaustiveSearch(elementy_zbioru)
