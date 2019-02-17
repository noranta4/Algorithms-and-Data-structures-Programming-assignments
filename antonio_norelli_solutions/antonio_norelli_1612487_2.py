__author__ = 'Antonio Norelli'

#CORSO DI ALGORITMI E STRUTTURE DATI 2016
#esPROG2
#STRONGLY CONNECTED COMPONENTS

###############################################################################


#acquisizione dati e costruzione del grafo inverso


import sys
orig_stdout = sys.stdout #servira' per stampare su file

graph = {}
node_v = {} #valore nodo: 0 se non visitato 1 se visitato n<0 postnumber
inv_graph = {} #grafo inverso
inv_node_v = {}

with open('graph.txt') as f: #acquisizione grafo su dizionario
    n_nodes = int(f.readline())
    for node in range(n_nodes):
        reachable_nodes = map(int, f.readline().split())
        id_n = reachable_nodes.pop(0)
        graph[id_n] = set(reachable_nodes)
        inv_graph[id_n] = set() #inizializzazione grafo inverso, valore nodi grafo e grafo inverso
        node_v[id_n] = 0
        inv_node_v[id_n] = 0

for node in graph: #costruzione grafo inverso
    for reachable in graph[node]:
        inv_graph[reachable].add(node)


#funzione depth first search


def dfs(graph, start, node_v):
    global clock #variabile globale per il postnumber
    global stack #variabile globale con l'insieme dei nodi visitati in una dfs
    node_v[start] = 1 #marcato come visitato
    for node in graph[start]: #per ogni nodo raggiungibile
        if node_v[node] == 0: #se non visitato
            dfs(graph, node, node_v) #esegui una dfs
    node_v[start] = clock #postnumber quando si blocca la dfs
    stack.append(start)
    clock -= 1
    return node_v


#dfs sul grafo inverso per ottenere la lista ordinata rev_rank su cui eseguire la seconda dfs


clock = -1
rev_rank = []
for node in graph:
    if inv_node_v[node] == 0:
        stack = [] #inizializzazione stack
        inv_node_v = dfs(inv_graph, node, inv_node_v)
        rev_rank.extend(stack) #costruzione del rank (inverso)

clock = -1
group = {} #componenti fortemente connesse
rank_comp = 0 #rank componente = max of postnumbers = postnumber of start in the dfs
component = [] #inizializzazione rank e componente

for node in reversed(rev_rank): #seconda dfs
    if node_v[node] == 0: #se non visitato
        stack = [] #inizializzazione variabile
        node_v = dfs(graph, node, node_v)
        rank_comp = node_v[node]
        group[-rank_comp] = stack #memorizzazione delle scc


#output


f = file('scc.txt', 'w')
sys.stdout = f
print len(group)
for component in sorted(group, reverse=True):
    print str(group[component])[1:-1]