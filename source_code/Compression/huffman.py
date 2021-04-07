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


import codecs 
import json

def nb_occurence(text) :
    dico = {}
    for char in text:
        if char in dico.keys() :
            dico[char] = dico[char] + 1
        else :
            dico[char] = 1
    return dico


def sort_dico(dico):
    sort = sorted(dico.items(), key=lambda x: x[1], reverse=False)
    return sort

print(sort_dico(nb_occurence("test")))


"""def construc_arbre(dico):
    sort = sort_dico
    arb = []
    def construction(sort,somme):
        if len(sort) == 1:
            return somme
        else:
            key1,value1 = sort.pop(0)
            key2,value2 = sort.pop(1)
            return (construction(sort, value1+value2)) + []
"""
"""def construc_arbre(dico):
    dico_sorted = sort_dico(dico)
    arb = []
    arb_temp = {}
    while len(dico_sorted) > 2:
        #sort = sort_dico(dico)
        key1,value1 = dico_sorted.pop(0)
        key2,value2 = dico_sorted.pop(1)
        if value1 in arb_temp.keys():
            arb_temp[value1] += [(key1, value1)]
        else:
            arb_temp[value1] = [(key1, value1)]
        if value2 in arb_temp.keys():
            arb_temp[value2] += [(key2, value2)]
        else:
            arb_temp[value2] = [(key2, value2)]
    print(arb_temp)
    while len(arb_temp.keys()) != 1:
        current_key = min(arb_temp.keys())
        temp = arb_temp.pop(current_key)
        for i in range(0,len(temp),2):
            #print(current_key)
            print(temp[i])
            key1, value1 = temp[i]
            key2, value2 = temp[i+1]
            if value1+value2 in arb_temp.keys():
                arb_temp[value1+value2] += [[(value1+value2,None), [(key1, value1), (key2, value2)]]]
            else:
                arb_temp[value1+value2] = [[(value1+value2,None), [(key1, value1), (key2, value2)]]]
            
        print(arb_temp)"""


def initialisation(arbre): # Convertion du tableau en un tableau de feuille
    final_arbre = []
    for i in range(len(arbre)):
        final_arbre.append(['F',arbre[i]]) # F -> Feuille, N -> Noeud
    return final_arbre

#
"""
        COnstruction de l'abre : 
            Noeud : ['N', etiquette, fils gauche, fils droit]
            Feuille : ['F', (lettre, occurence)]

    """
def get_weight(arbre,i):
    poids = 0
    if i>=len(arbre):
        return -1
    if arbre[i][0] == 'F':
        _,poids = arbre[i][1]
    else : # On a un noeuf
        poids = arbre[i][1]
    return poids

def construc_arbre(arbre):
    if len(arbre)==1:
        return arbre
    else:
        current_occurence = get_weight(arbre,0) # On regarde le plus bas poids
        poids = current_occurence
        current = 0 # Indice du noeuf/feuille à traier. Celui associé sera le suivant
        while poids == current_occurence and current + 1 <len(arbre):
            fg = arbre[current] # Va être remplacé
            fd = arbre.pop(current + 1) # Supprimé
            poids_fg = 0
            if fg[0] == 'F':
                _,poids_fg = fg[1]
            else :
                poids_fg = fg[1]
            poids_fd = 0
            if fd[0] == 'F':
                _,poids_fd = fd[1]
            else :
                poids_fd = fd[1]
            poids = poids_fd + poids_fg
            arbre[current] = ['N', poids, fg,fd]
            current += 1
            poids = get_weight(arbre,current) #On actualise le poids
            #print(arbre)
        return construc_arbre(arbre)

def list_to_dico(liste):
    #print("liste to encode " , liste)
    dico = {}
    for li in liste:
        dico[li[0]] =  li[1]
    return dico


def codage_feuille(arbre, chemin= ""):
    #print("arbre transmis", arbre, " ", len(arbre))
    
    if len(arbre)>=1 and arbre[0] == 'F':
        #print("fin recursion ", arbre[0])
        letter,_ = arbre[1]
        return [[letter,chemin]]
    else:
        #print(arbre)
        fg = arbre.pop(2)
        fd = arbre.pop(2)
        #print(fg)
        return codage_feuille(fg, chemin=chemin+"0") + codage_feuille(fd,chemin=chemin+"1")

def compression(encoded, mot):
    string = ""
    for e in mot:
        string+=encoded[e] + " "
    return string


def tree_reading(tree, letter):
    #print("tree = ",tree, " letter = ",letter)
    if letter == "":
        if len(tree)==2:
            if tree[0] == 'F' :
                letter,_ = tree[1]
                return letter
            else:
                raise Exception("Wrong tree format. That is not a leaf")
        else:
            #print("*****ERROR******", tree)
            raise Exception("Wrong tree format")
    else:
        if letter[0] == '0':
            #print("tree[2] = ", tree[2])
            return tree_reading(tree[2], letter[1:])
        elif letter[0] == '1':
            #print("tree[3] = ", tree[3])
            return tree_reading(tree[3], letter[1:])
        else:
            raise Exception("Unreadable char")


            

def decompression(tree,mot):
    letters = mot.split(" ")
    string = ""
    for letter in letters:
        if letter != "":
            string += tree_reading(tree,letter)
    return string





#print(construc_arbre(sort_dico(nb_occurence("AABCDCCEF"))))





def hoffman():
    print("Encode (1) | Decode (2)")
    user = input()
    #user = "1"
    if user == "1":
        print("\n\n[*] Extraction ...", end=' ')
        file = open("text.txt", mode = "r")
        text=file.readlines()[0]
        file.close()
        print("Ok")
        print("[*] Recherche d'occurence ...", end=' ')
        occurrence = nb_occurence(text)
        print("Ok")
        print("[*] Tris par occurence ...", end=' ')
        sort_arbre = sort_dico(occurrence)
        print("Ok")
        print("[*] Initialisation de l'arbre ...", end=' ')
        formatting = initialisation(sort_arbre)
        print("Ok")
        print("[*] Construction de l'arbre ...", end=' ')
        arbre = construc_arbre(formatting)
        print("Ok")
        print("[*] Enregistrement de l'abre ...", end=' ')
        file = open("tree.txt", mode="w")
        file.write(json.dumps(arbre))
        file.close()
        print("Ok")
        print("[*] Encodage des feuilles ...", end=' ')
        #print(codage_feuille(arbre[0]))
        #print("Ok2")
        encoded = list_to_dico(codage_feuille(arbre[0]))
        print("Ok")
        print("[*] Compression ...", end=' ')
        compressed = compression(encoded,text)
        print("Ok\n\n")
        file = open("compressed.txt", mode="w")
        file.write(compressed)
        file.close()
        print("*** SUCCESSFULLY COMPRESSED ***")
    elif user == "2":
        print("\n\n[*] Extraction ...", end=' ')
        file = open("compressed.txt", mode = "r")
        compressed=file.readlines()[0]
        file.close()
        file = open("tree.txt", mode='r')
        tree = file.readlines()[0]
        tree = json.loads(tree)
        file.close()
        print("Ok")
        print("[*] Decompression ...", end=' ')
        file = open("decompressed.txt", mode='w')
        clear = decompression(tree[0],compressed)
        file.write(clear)
        file.close()
        print("Ok\n\n")
        print("*** SUCCESSFULLY COMPRESSED ***")
hoffman()