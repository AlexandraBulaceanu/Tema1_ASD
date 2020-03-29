import math
import time
import random


def validitatesortare(initial, final):
    if len(initial) != len(final):
        return False
    else:
        for i in range(1,len(initial)):
            if(final[i-1]>final[i]):

                return False
    return True


def bublesort(a, maxx):
    if(len(a)>10000):
        return
    for i in range(len(a) - 1, 0, -1):
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


def countsort(a, maxx):
    if(len(a)>20000000) or maxx > 20000000:
        return
    t = [0] * (maxx + 2)
    for i in a:
        t[i] += 1
    j = 0
    while (t[j] == 0):
        j += 1
    for i in range(len(a)):
        a[i] = j
        t[j] -= 1
        while (t[j] == 0 and j<=maxx):
            j += 1


def mergesort(a, maxx):
    if (len(a) > 10000000):
        return
    if len(a) == 2:
        a[0], a[1] == min(a[0], a[1]), max(a[0], a[1])
        return
    if len(a) == 1:
        return

    b = a[:len(a) // 2]
    c = a[len(a) // 2:]
    mergesort(b, maxx)
    mergesort(c, maxx)
    i = 0
    j = 0
    z = 0
    while i < len(b) and j < len(c):
        if b[i] > c[j]:
            a[z] = c[j]
            j += 1
        else:
            a[z] = b[i]
            i += 1
        z += 1
    while i < len(b):
        a[z] = b[i]
        i += 1
        z += 1
    while j < len(c):
        a[z] = c[j]
        j += 1
        z += 1

def medianamedianelor_aka_BFPRT(a):
    lung=len(a)
    if lung <= 5:
        return sorted(a)[lung//2]
    sublista = [sorted(a[i:i+5]) for i in range(0, lung, 5)]
    mediana = [el[len(el)//2] for el in sublista]
    return medianamedianelor_aka_BFPRT(mediana)


def quicksort(a, maxx):
    if (len(a) > 10000000):
        return
    lung = len(a)
    if lung == 0:
        return []
    if lung == 1:
        return a
    pivot = medianamedianelor_aka_BFPRT(a)
    less = []
    equal = []
    more = []
    for el in a:
        if el < pivot:
            less.append(el)
        elif el == pivot:
            equal.append(el)
        else:
            more.append(el)
    less = quicksort(less, maxx)
    more = quicksort(more, maxx)
    less.extend(equal)
    less.extend(more)
    a = []
    a.extend(less)
    return less

def nrcifreMaxi(n):
    digits = 0
    while(n>0):
        n=n//10
        digits=digits+1
    return digits

#iterativ
def radixsort_baza10(a, maxx):
    maxi = max(a)
    digits = nrcifreMaxi(maxi)
    p = 1
    listsor = [el for el in a]
    for i in range(digits):
        list = [[] for i in range(10)]
        for el in listsor:
            list[el//p%10].append(el)
        listsor = []
        for el in list:
            listsor.extend(el)
        p = p*10
    return listsor


#cu counting_sort ca baza
def counting_sort(a, digit):

    listsor = [0]*len(a)
    list = [0]*int(2)
    lung = len(a)
    for i in range(lung):
        digita = (a[i]//2**digit)%2
        list[digita] = list[digita] +1

    for j in range(1,2):
        list[j] = list[j] + list[j-1]
    for el in range(len(a)-1, -1, -1):
        digita = (el//2**digit)%2
        list[digita] = list[digita] -1
        listsor[list[digita]] = el

    return listsor

def radixsort_baza2(a, maxx):
    maxi = max(a)
    listsor = a
    digits = int(math.floor(math.log(maxi, 2)+1))
    for i in range(digits):
        listsort = counting_sort(listsor,i)

    return listsort


f = open("input.txt",'r')
tests = int(f.readline())



sorts = [bublesort, countsort, mergesort, quicksort, radixsort_baza2, radixsort_baza10]
sortsname = ["bublesort", "countsort", "mergesort", "quicksort", "radixsort_baza2", "radixsort_baza10"]

for el in range(tests):
    line = f.readline()
    i=int(line.split()[0])
    maxx=int(line.split()[1])
    a = [random.randint(0, maxx) for s in range(i)]
    index=0
    for sortare in sorts:
        start_time = time.time()
        cop = a.copy()
        sortare(cop, maxx)
        print("sortarea ", sortsname[index], " a durat " "--- %s seconds ---" % (time.time() - start_time))
        print("sortarea a fost corecta: ",validitatesortare(a,cop))
        index=index+1
        a = cop.copy()


