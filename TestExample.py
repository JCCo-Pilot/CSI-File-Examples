import sys
intake = input()
print (int(intake))
total = 0
counter = 0
while counter<=int(intake):
    total = counter+total
    counter = counter+1
print (total)
#intake = input()
#intake2 = input()
#print(intake)
#print(intake2)
#for line in sys.stdin:
    #print(line)