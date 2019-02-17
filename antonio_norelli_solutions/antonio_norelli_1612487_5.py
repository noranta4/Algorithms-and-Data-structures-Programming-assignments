__author__ = 'Antonio Norelli'

#Assuming binary tree stored in an array where the father of array[i] is array[int((array[i]-1)/2))]:
#EXAMPLE:   array = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
#indexes of array = [ 0 ,  1 ,  2 ,  3 ,  4 ,  5 ,  6 ,  7 ,  8 ,  9 ,  10]
#A father of B, C; B father of D, E; C father of F, G...

#COST O(log(n)) where n is the lenght of the array

#................................................................................................................

#SAMPLE INPUT

input_alb_bin = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
input_node_a = 'H'
input_node_b = 'D'

#PROGRAM

def find_index(alb_bin, node_a, node_b): #find indexes of two nodes in input
    index_a = alb_bin.index(node_a)
    index_b = alb_bin.index(node_b)
    return [index_a, index_b]

def find_ancestor(indexes): #indexes = [index_a, index_b]
    while True:
        if indexes[0] < indexes[1]: #change deeper node with his father
            indexes[1] = int((indexes[1]-1)/2)
        elif indexes[1] < indexes[0]:
            indexes[0] = int((indexes[0]-1)/2)
        else: #if the two nodes are the same, return one of them
            return indexes[0]

print 'common ancestor is:', input_alb_bin[find_ancestor(find_index(input_alb_bin, input_node_a, input_node_b))]




