import datetime
filename = 'Dane.txt'
with open(filename) as plik:
    zawartosc = plik.read()

print(zawartosc)

filename = 'Dane.txt'
with open(filename) as plik:
    for wiersz in plik:
        print(wiersz.rstrip())

filename = 'Dane.txt'
with open(filename) as plik:
    wiersze = plik.readlines()
    
for wiersz in wiersze:
    print(wiersz)
    
filename_2 = 'kwadraty.txt'

with open(filename_2, 'w') as f:
    for i in range(1,101):
        f.write(str(i**2) + '\n')
        i += 1
        
with open(filename_2, 'a') as f_a:
    for i in range(101,201):
        f_a.write(str(i**2) + '\n')
        i += 1

f_path = 'Eksporty/eksport1.txt'
with open(f_path, 'w') as f:
    for i in range(1,31):
        f.write(str(datetime.date.today() + datetime.timedelta(days=i)) + '\n')
        i += 1
        
windows_path = 'C:/Users/Marek/Desktop/Python/Eksporty/eksport2.txt' ### tutaj normalne slashe
with open(windows_path, 'w') as f:
    for i in range(1,31):
        f.write(str(i**i) + '\n')
        i += 1
        
        try:
            result = 10/0
        except ZeroDivisionError: ## Obsluga bledu dzielenia przez 0, musi byc dokladnie ta nazwa przy Except
            print('Nie podzielisz Pan przez 0, nie ma bata')
        else:
            print(result)
f_name = 'brakpliku.txt'

        try:
            f3 = open(f_name)
        except FileNotFoundError:
            print('Nie ma takiego pliku!')

x = input('Podaj pierwsza liczbe:\n')
y = input('Podaj druga liczbe - wykladnik potegi:\n')

while isinstance(x, str):
    x = input('Podaj pierwsza liczbe:\n')
    if x == 'q':
        break

while isinstance(y, int):
    y = input('Podaj druga liczbe - wykladnik potegi:\n')
    if y == 'q':
        break
  
    #################

f_names = ['kwadraty.txt', 'konto.txt', 'brakpliku.txt']

try: 
    for file in f_names:
        with open(file) as plik:
            dane = plik.readlines()
            print(file + ': ' + str(len(dane)))
except FileNotFoundError:
    print(file + ' was not found!')

    #################
    
    try:
        5/abcd
    except Exception as blad:
        print(blad)
    
   #####################
   
import json

wartosci = ['Bogdan', 1000, 'Andre', 3000, 'Jeremiasz', 500]

nazwa_pliku = 'liczby.json'

with open(nazwa_pliku, 'w') as plik:
    json.dump(wartosci,plik)


   ####---- ####

with open(nazwa_pliku) as plik:
    wartosci = json.load(plik)
    
print(wartosci)

try:
    with open(nazwa_pliku) as plik:
        wartosci = json.load(plik)
        print(wartosci)
except FileNotFoundError:
    print('File ' + nazwa_pliku + ' was not found!')
    
    ### Strona 15
    
    import unittest

f_n = 'cos'
l_n = 'ktos'

def get_full_name(first,last):

        f_n = first[0].upper() + first[1:].lower()
        l_n = last[0].upper() + last[1:].lower()
 
        full_name = f_n + ' ' + l_n
        return full_name

class NamesTestCase(unittest.TestCase):
    def test_first_last(self):
        full_name = get_full_name ('janusz', 'januszewski')
        self.assertEqual (full_name, 'Janusz Januszewski')

unittest.main() ### test dziala OK jezeli zgadza sie wielkosc znakow
### po zmianie musialem uporzadkowac wciecia + przypisac cos do f_n oraz l_n

### Strona 16 - ciag dalszy sprwadzania klas.

import pygame