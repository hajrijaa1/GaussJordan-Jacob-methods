import numpy as np
#Unos matrice A i slobodnih članova b
A = np.array([[8, -2, -3, 0], [-2, 4, -2, 0], [-3, -2, 8, -3], [0,0,-3,8]])
b = np.array([3,2,3,6])

#Funkcija shape se koristi za dobijanje oblika niza
red, kolona = A.shape
B = np.zeros((red, kolona))
g = np.zeros(kolona)

#U numpy modulu B[i,:] koristi se za dodjeljivanje vektora isječku 2D polja
for i in range(0, red):
    B[i,:] = A[i,:]/A[i,i]
    g[i] = b[i]/A[i,i]
    B[i,i] = 0

#B mijenjamo negativnom vrijednošću zbog matrice
B = -B
print(B)

#Broj iteracija postavljen je na 10, može se mijenjati
brIter = 10

#Funkcija zeros vraća novi niz zadanog oblika i tipa, ispunjen nulama
x = np.zeros(kolona)
print("\nRješenje jednačine za prvih 10 iteracija: ")
for i in range(brIter):
    #Funkcijom dot množi se matrica
    x = np.dot(B,x)+g
    #Ispis zadanog broja iteracija s dobivenim vrijednostima
    print(i, x)
