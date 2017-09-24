import sys
MAX = sys.maxsize

print ("This is a Fibonacci generator.")
numTerms = input ("Number of terms: ")

if int(numTerms) == 0:
    numTerms = MAX

a = 0
b = 1

init = 0
while init < int(numTerms):
    print ("Term ", str(init), " - ", b)
    temp = b
    b = b + a
    a = temp
    init += 1