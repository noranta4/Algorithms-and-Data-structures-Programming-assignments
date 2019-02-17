__author__ = 'Antonio Norelli'

#CORSO DI ALGORITMI E STRUTTURE DATI 2016
#esPROG1
#STABLE MARRIAGE

###############################################################################

import sys
orig_stdout = sys.stdout #servira' per stampare su file

#acquisizione dati in due dizionari

men_pref = {}
wmen_pref = {}
men_status = {}
wmen_status = {}

with open('men.txt') as f:
    n_men = int(f.readline())
    for man in range(n_men):
        rank_man = map(int, f.readline().split())
        id_m = rank_man.pop(0)
        men_pref[id_m] = rank_man
        men_status[id_m] = 0 #libero

with open('women.txt') as f:
    n_wmen = int(f.readline())
    for wman in range(n_wmen):
        rank_wman = map(int, f.readline().split())
        id_w = rank_wman.pop(0)
        wmen_pref[id_w] = rank_wman
        wmen_status[id_w] = 0

#algoritmo


def matching(men_pref, men_status, wmen_pref, wmen_status):
    while 0 in men_status.values(): #finche' ci sono uomini liberi
        for m in men_pref: #scansione uomini
            if men_status[m] == 0: #se libero
                for w in men_pref[m]: #scansione della sua lista di preferenze
                    if wmen_status[w] == 0: #se la donna e' libera
                        men_status[m] = w #match
                        wmen_status[w] = m
                        break #smetti di scorrere la lista di preferenze
                    else: #se la donna non e' libera
                        if wmen_pref[w].index(wmen_status[w]) > wmen_pref[w].index(m): #se preferisce questo uomo a quello con cui sta
                            men_status[wmen_status[w]] = 0 #l'uomo con cui sta torna libero
                            wmen_status[w] = m #match
                            men_status[m] = w
                            break #smetti di scorrere la lista di preferenze
    return men_status

def output(dict_couples):
    f = file('marriage.txt', 'w')
    sys.stdout = f
    for i in dict_couples:
        print i, '\t', dict_couples[i]


#esecuzione


output(matching(men_pref, men_status, wmen_pref, wmen_status))







