__author__ = 'Antonio Norelli'

#Take the total, you have at least one solution with:
#0 coin of the largest size... i coins of the largest size... q coins of the largest size where q=int(total/(largest size))
#now for every combination from 0 to q coins of the largest size, remaining are total-i*(largest size)=total'
#and you have at least one solution with:
#0 coin of the second largest size... i coins of the  second largest size... q' coins of the second largest size
# where q'=int(total'/(second largest size))
#and so on
#when your total' is 0 or you are working with the smallest size there is only one solution
#and you add it to the global variable result

#COST there are at least k calls of the recursive function where k=result
#An upperbound for the result is n*(n/5)*(n/10)*(n/25)
#It's impossible to have a solution with more than n pennies, n/5 nikels, n/10 dimes, n/25 quarters...
#So the cost is O(n^4)

#................................................................................................................

#SAMPLE INPUT

cents = 100

#PROGRAM

#cicli = 0 #use the commented lines if you want the number of calls of combination function

sizes = [1, 5, 10, 25]
result = 0

def combinations(remaining, j): #j is the index of the actual coin size
    global sizes
    global result

    #global cicli
    #cicli += 1

    current_value = sizes[j]
    if remaining == 0 or j == 0: #if remaining is 0 or you are working with the smallest size there is only one solution
        result += 1
        return
    for i in range(int(remaining/current_value)+1): #at least one solution with i coins of the current value
        combinations(remaining-i*current_value, j-1) #recall the function with remaining and next smaller coin value

combinations(cents, len(sizes)-1)
print 'number of ways of representing', cents, 'cents:', result

#print cicli
