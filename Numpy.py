import webbrowser
webbrowser.open_new_tab("https://docs.scipy.org/doc/numpy/user/quickstart.html")

import numpy as np
from numpy import pi
a = np.arange(20).reshape(4,5)
a.shape
a.ndim
a.dtype.name
a.itemsize
a.size

b = np.array([10,20,30]) ## mozna konwertowac liste lub krotke na array
b.dtype ## int
c = np.array([1.2,3.5,5.1]) 
c.dtype ## float
d = np.array([(10,20,30), (50,60,70)])
e = np.array( [ [1,2], [3,4] ], dtype = complex)


f = np.zeros( (10,2) )
g = np.ones( (5,5), dtype = np.int16)
g

h = np.empty( (2,3) )     
i = np.arange (10,50,5)
j = np.arange (10,50,0.5) ## arange akceptuje float
k = np.linspace(0,10,21) ## 21 liczb co 0.5 (samo sie wylicza od 0 do 10)
k 

np.set_printoptions(threshold=0) ## zmiana sposobu wyswietlania tablic w numpy

l = np.array( [10,30,50,70])
k = np.linspace(2,20,4)
m = l - k
m ** 2
m < 25

A = np.array ( [[1,2], [3,4]])

A * A
A @ A

n = np.ones((2,3), dtype=int)
o = np.random.random((2,3))

o += n
o *= n

o 

p = np.ones(3, dtype = np.int32) ## upcasting - konwertujemy do bardziej ogolnego typu danych
r = np.linspace(0,pi,3)

s= p+r
s.dtype.name ## przekonwertowalo na floata

s = np.exp(r*1j)
s.dtype.name

t = np.random.random((2,3))
t.sum()
t.min()
t.max()

u = np.arange(12).reshape(3,4)
u.sum(axis=0) ## suma wszystkich kolumn
u.sum(axis=1) ## suma wszystkich wierszy
u.cumsum(axis=1) ## suma skumulowana dla kazdego wiersza

w = np.arange(4)
np.exp(w)
np.sqrt(w)
y = np.array([2,4,8,68])
np.add(w,y)

## Sekcja See also: z all, any, apply, along_axis, corrcoef itd.