

# zadanie 4.1
import math
def czyPierwsza(n):

    for i in range(2, n):
        if n % i == 0:
            return False
        return True

liczby=[]

plik=open('przyklad.txt','r')
wiersze = plik.readlines()
for wiersz in wiersze:
    wiersz.strip()
    if wiersz[1]!="":
        liczby.append(str(wiersz[0]+wiersz[1]))
    else:
        liczby.append(str(wiersz[0]))

for liczba in liczby:
    if int(liczba)%2==0:

        for i in range(3,len(liczby)):
            cos=int(liczba) - i
            if  cos %2 == 0 or i % 2 == 0:
                continue
            if czyPierwsza (cos)and czyPierwsza(i):
                # print( str(liczba)+" "+str(cos)+" "+str(i))
                cos=int(0)
                break

#zadanie 4.2

wyrazy=[]
pom=""
licznik=0
liczniki=[]
for wiersz in wiersze:
    wiersz=wiersz.strip()
    for i in  range(2,len(wiersz)):
        if wiersz[i]==" ":
            continue
        else:
            pom+=wiersz[i]
        if i==(len(wiersz)-1):
            wyrazy.append(pom)
            pom=""

for wyraz in wyrazy:
    for i in  range(len(wyraz)-1):
        if wyraz[i]==wyraz[i+1]:
            licznik+=1
        if i == (len(wyraz) - 2):
            liczniki.append(licznik+1)
            licznik=0

for wiersz in wiersze:
    wiersz = wiersz.strip()
    # for i in range(len(liczniki)):
    #     print(str(liczniki[i])+" "+ wiersz)

#zadanie 4.3
minLenght=len(wyrazy[0])
index=0
for i in  range(len(liczby)):
    if len(wyrazy[i])==int(liczby[i]):
        if(minLenght>len(wyraz[i])):
            minLenght=len(wyraz[i])
            index=i

    if (i==(len(liczby)-1)):
        print(str(wyrazy[index])+" "+str(liczby[index]))

