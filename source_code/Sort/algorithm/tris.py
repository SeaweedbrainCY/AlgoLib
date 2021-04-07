# 
# Copyright (c) 2021 STCHEPINSKY Nathan
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



########################################################
############# TRI PAR INSERTION ########################
########################################################


"""

            Compléxité : Theta(n^2)
"""


def insertion(liste):
    for i in range(1,len(liste)):
        counter = i
        while liste[counter-1]>liste[counter] and counter>0 :
            liste[counter],liste[counter-1]=liste[counter-1],liste[counter]
            counter-=1
    return liste


########################################################
############# TRI PAR SELECTION ########################
########################################################


"""

            Compléxité : Theta(n^2)
"""

def minLi(liste):
    if liste == []:
        return None
    else :
        min_e = liste[0]
        min_i = 0
        for i in range(len(liste)):
            if liste[i] < min_e:
                min_i = i
                min_e = liste[i]
        return min_i

def selection(liste):
    new_li = []
    while liste != []:
        min_i = minLi(liste)
        #print(min_i)
        min_e = liste.pop(min_i)
        #print(min_e)
        new_li.append(min_e)
        #print(liste)
    return new_li

########################################################
############# TRI BULLE ################################
########################################################

"""

            Compléxité : Theta(n^2)
"""

def tri_bulle(liste):
    length = len(liste)-1
    for i in range(length):
        for j in range(length - i):
            if liste[j]>liste[j+1]:
                liste[j],liste[j+1]=liste[j+1],liste[j]
    return liste

########################################################
############# TRI FUSION ###############################
########################################################


def fusion(l1,l2):
    if l1 ==[]:
        return l2
    elif l2 == []:
        return l1
    else:
        if l1[0]<=l2[0]:
            return [l1[0]] + fusion(l1[1:],l2)
        else:
            return [l2[0]] + fusion(l1,l2[1:])

def tri_fusion(liste):
    if len(liste)<=1:
        return liste
    else: 
        n = len(liste)
        return fusion(tri_fusion(liste[:n//2]), tri_fusion(liste[n//2:]))
#print(tri_fusion([18, 27, 16, 20, 39, 28, 18, 5, 42, 25, 38, 24, 41, 30, 12, 34, 15, 19, 6, 23, 36, 10, 7, 29, 8, 37, 11, 22, 26, 31, 13, 14]))

########################################################
############# TRI RAPIDE ###############################
########################################################


def partition(liste, pivot):
    if liste == []:
        return []
    liste[-1],liste[pivot]=liste[pivot],liste[-1]
    j = 0
    last = liste[-1]
    for i in range(len(liste)-1):
        if liste[i]<=last :
            liste[i],liste[j] = liste[j],liste[i]
            j += 1
    liste[j],liste[-1] = liste[-1],liste[j]
    return j

def tri_rapide(liste):
    if liste == []:
        return []
    pivot = len(liste)//2
    pivot = partition(liste, pivot)
    return tri_rapide(liste[:pivot]) + [liste[pivot]] + tri_rapide(liste[pivot+1:])
    


#print(tri_rapide([8,5,2,9,1,0,4]))

#print(tri_rapide([18, 27, 16, 20, 39, 28, 18, 5, 42, 25, 38, 24, 41, 30, 12, 34, 15, 19, 6, 23, 36, 10, 7, 29, 8, 37, 11, 22, 26, 31, 13, 14]))