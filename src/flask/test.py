lit = [1,2,3,4,5,6,7,8,9,10]
sum = [0]*2
for index, i in enumerate(lit): 
    if index < 5:
        sum[0] = int(sum[0])+i
    else:
        sum[1] = int(sum[1])+i
x = sum.index(max(sum))
print(x)