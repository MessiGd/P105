import csv
import math
with open ('data.csv', newline="") as f:
    read = csv.reader(f)
    a = list(read)
data = a[0]
n = len(data) 
def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total += int(x)
    mean = total/n
    return mean
squared_list=[]
for i in data:
    a = int(i) - mean(data)
    a = a**2
    squared_list.append(a)
sum = 0 
for c in squared_list:
    sum = sum+c
result = sum/(n-1)
answer = math.sqrt(result)
print("The answer is:"+str(answer))

