print('hello world')

def main():
    pass

#łańcuchy znaków
imie = "Marian"
print(imie)
print(type(imie))
print(type(5))
print(type(5.7))
print(type(True))
print(type(None))
#<class 'str'>
#<class 'int'>
#<class 'float'>
#<class 'bool'>
#<class 'NoneType'>
print(imie[2])
#imie[0] = "D"
imie = "Darian"
imie = imie.lower()
print (imie)
wiek = 30
#print imie(imie + " ma " + wiek + "lat.")
#print imie(imie + " ma " + wiek.__str__() + "lat.")
print imie(imie + " ma " + str(wiek) + "lat.")
print imie("{}  ma  {} lat.".format(imie,wiek))
print imie("{0}  ma  {1} lat.".format(imie,wiek))
# f-string
print imie(f"{imie}  ma  {wiek} lat.")
# pyformat.info
liczba = 6.7574623823846
print(f"{liczba:.2f}")

# typ liczby
liczba = 5
ficzbaf = 5.5
printf(1+2)
printf(1-2)
printf(1*2)
printf(1/2)
printf(1//2) # dzielenie bez reszty
printf(1**2) # potęgowanie
printf(1%2) # modulo

tekst = "A100"
liczba_z_tekstu = int(tekst)
print(liczba_z_tekstu)
import math
pi = 3.15
from math import *
from math import sqrt
import math as m
m.pow()
print(m.pi)

# listy

lista = [] 
lista2 = list()
lista3 = [1, 2, 3]
lista3 = [1, "Ala", True, None, [i, 2]]
lista3[1] = "zosia"
#lista3[1][0] = "0"
macierz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(macierz[1][1])
print(0.1 + 0.2 == 0.3)
# Decimal
lista += lista3

slownik = {}
slownik = dict{}
slownik3 = {"klucz":"wartość"}
slownik3['klucz']
