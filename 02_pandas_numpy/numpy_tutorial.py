"""
This script is dedicated to the NumPy library for Python.
"""

import numpy as np

# NumPy (Numerical Python) is an OpSr-Python library created in 2005 by Travis Oliphant and used for working with arrays
# NumPy aims to provide an array object that is up to 50x faster than traditional and are slow to process Python lists.
#
# Basic functions of NumPy include # creating, indexing, slicing, reshaping, iterating, joining, splitting of arrays
# as well as searching, sorting and filtering them.
#
# Extended functionality includes plotting (Beschriftung) of random data sets: Data Distribution (normal / binomial /
# poisson / uniform / logistic / multinomial / exponential / Chi Square / Rayleigh / Pareto / Zipf) and Random Permutation
#
# as well as UFUNC (Universal Functions) - functions for working in domain of linear algebra, fourier transform
# and matrices. UFuncs operate on the ndarray object through implementing the vectorization in NumPy (way faster than
# iterating over elements) and provide broadcasting and additional methods like reduce, accumulate etc. (very helpful
# for computation)

# Erstellen eines ndarray objetks mit der .array() funktion

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

# check version

print(np.__version__)

# Man kann aus beliebigem Array-ähnlichen Objekt ein ndarray machen BSP am tuple:

arr1 = np.array((1, 2, 3, 4, 5))
print(arr1)

"""
Array Dimensionen:
    Eine Array Dimension ist die tiefe eines Array (nested arrays = arrays die arrays als element enthalten) 
    0-D Arrays - Die elemnte eines Arrays. Jeder Value in einem Array ist ein 0-D Array
    BSP:    0D = np.array(42)
    1-D Arrays - Ein Array, welches 0-D Arrays als Element hat
    BSP:    siehe oben bei Erstellen eines ndarray objekts
    2-D Arrays - Ein Array das 1-D Arrays als Elemente hat. Diese werden oft benutzt um eine Matrix darzustellen
    BSP:    np.array([[1,2,3], [4,5,6]])
    3-D Arrays - Ein Array aus 2-D Arrays...
    BSP:    arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
"""

# Numpy hat einen Attribut der mit einem Integer ausgibt wie viele Dimensionen ein Array hat. .ndim

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# Ein Aray kann unbegrenzt viele Dimensionen haben
# Man kann beim erstellen eines Arrays schon festlegen wie viele Dimensionen das Array haben soll
# Das geht mit dem Argument .ndmin

mehrdimensionen = np.array([1, 2, 3, 4], ndmin=5)
print(mehrdimensionen)
print("Wie viele Dim?: ", mehrdimensionen.ndim)

# In this array the innermost dimension (5th dim) has 4 elements,
# the 4th dim has 1 element that is the vector, the 3rd dim has 1 element that is the matrix with the vector,
# the 2nd dim has 1 element that is 3D array and 1st dim has 1 element that is a 4D array.


# Array indexing
# man kann auf Array Elemente zugreifen indem man Indexe nutzt
# NumPy Arrays starten mit dem Index 0. Das heißt das erste Lement hat Index 0, das zweite 1 usw.

arr2 = np.array([1, 2, 3, 4])
print(arr2[2])

# Hier wird nun das 3. Element ausgegeben

# Man kann 2 Elemente auch sofot miteinander verrechnen

print(arr2[2] + arr2[3])

# Aber wie greift man auf 2-D oder 3-D Arrays zu?
# Man nutzt mit einem Komma getrente Integer

arr3 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("3. Element von in der 2. Dimension: ", arr3[1, 2])

# Das gleiche gilt für 3-D Arrays, nur dann mit 3 Integern

arr4 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr4[0, 1, 2])

# Das Ergebniss hier lautet 6
# Warum? Hier die Erklärung:

"""
    arr[0, 1, 2] prints the value 6.
    And this is why:
    The first number represents the first dimension, which contains two arrays:
    [[1, 2, 3], [4, 5, 6]]
    and:
    [[7, 8, 9], [10, 11, 12]]
    Since we selected 0, we are left with the first array:
    [[1, 2, 3], [4, 5, 6]]
    The second number represents the second dimension, which also contains two arrays:
    [1, 2, 3]
    and:
    [4, 5, 6]
    Since we selected 1, we are left with the second array:
    [4, 5, 6]
    The third number represents the third dimension, which contains three values:
    4
    5
    6
    Since we selected 2, we end up with the third value:
    6
 """

# Man kann negative Indexe nutzen um auf das Ende des Arrays zu zu greifen

arr5 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("Vorletztes Element in der 2 Dim:  ", arr5[1, -2])

# Array Slicing

# Slicing in python means taking elements from one given index to another given index.

# We pass slice instead of index like this: [start:end].
# We can also define the step, like this: [start:end:step].
# If we don't pass start its considered 0
# If we don't pass end its considered length of array in that dimension
# If we don't pass step its considered 1

arr = np.array(
    [1, 2, 3, 4, 5, 6, 7]
)  # Hier wird das Array von Index bis 5 (nicht enthalten) ausgegebn
print(arr[1:5])

arr = np.array([1, 2, 3, 4, 5, 6, 7])  # Hier werden Index 4 bis Ende ausgegeben
print(arr[4:])

arr = np.array(
    [1, 2, 3, 4, 5, 6, 7]
)  # Hier wwerden der Anfang des Arrays bis Index 4 (nicht enthalten) ausgegeben
print(arr[:4])

arr = np.array(
    [1, 2, 3, 4, 5, 6, 7]
)  # Vom vor vor letzten bis zum letzten (nicht enthalten) Index
print(arr[-3:-1])

arr = np.array(
    [1, 2, 3, 4, 5, 6, 7]
)  # Vom ersten bis zum fünften Index, wird jeder 2. Index ausgegeben
print(arr[1:5:2])

arr = np.array(
    [1, 2, 3, 4, 5, 6, 7]
)  # Jeder 2. Index aus dem ganzen Array wird ausgegeben
print(arr[::2])

# Slicing 2-D Arrays

arr = np.array(
    [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
)  # Vom 2. Element werden Index 1 bis 4 (nicht enthalten) ausgegeben
print(arr[1, 1:4])

arr = np.array(
    [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
)  # Von beiden Elementen wird der 2. Index ausgegeben
print(arr[0:2, 2])

arr = np.array(
    [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
)  # Von beiden Elementen Index 1 bis 4 (nicht enthalten)
print(arr[0:2, 1:4])

# Was ist Reshape und wie funktioniert es?

"""
Die Form eines Arrays, also dessen shape kann abgefragt werden:
print(arr.shape)    
returned wird hier (2, 5). Das heißt das Array hat 2 Dimensionen mit jeweils 5 Elementen.
"""

# Man kann ein Array umformen, es also reshapen.
# Die Form eines Arrays ist festgelegt durch die Anzahl an Elementen in jeder Dimension.
# Mit einem reshape können Dimensionen hinzugefügt oder entfernt werden,
# und auch die Anzahl an Elementen in jeder Dimension geändert werden.

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)

# Hier wird ein 1-D Array mit 12 Elementen in ein 2-D Array, welches 4 Elemnte hat dir selbst Arrys sind und
# jeweils 3 Elementen haben gereshaped.


# Man kann auch von 1-D in 3-D reshapen

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr1 = arr.reshape(2, 3, 2)
print(newarr1)

# Man kann nicht in beliebige Dimensionen reshapen, es muss Mathematisch Sinn ergeben
# Zum Beispiel ist es nicht möglich ein 1 Dimensionales Array mit 8 Elementen in ein Array reshapen,
# welches 3 Elemente in 3 Reihen hat. Dazu bräuchte es nämlich 9 Elemente


# NumPy erlaubt es eine Dimension als ubekannt einzutragen.
# Man kann also in der reshape Methode, eine Zahl als unbekannt eintragen in dem man "-1" dort eingibt.
# NumPy berechnet den Wert dann für dich.

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)

# Flattening Arrays

# Man kann multi-dimensionale Arrays in ein 1-D array reshapen.7
# Das heißt dann Flattening
# Man macht dies mit "reshape(-1)"

arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)
