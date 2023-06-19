import numpy as np
#Unos matrice A i slobodnih članova b
A = np.array([[4, -1, 0, 1, 0], [-1, 4, -1, 0 ,1], [0,-1, 4, -1, 0], [1,0,-1,4,-1], [0,1,0,-1,4]])
b = np.array([100,100,100,100,100])

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

#Funkcija zeros vraća novi niz zadanog oblika i tipa ispunjen nulama
x = np.zeros(kolona)
print("\nRješenje jednačine za prvih 10 iteracija: ")
for i in range(brIter):
    #Funkcijom dot množi se matrica
    x = np.dot(B,x)+g
    #Ispis zadanog broja iteracija s dobivenim vrijednostima
    print(i, x)


