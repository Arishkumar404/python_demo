a = [25,10,5,20,35,30,34]

for i in range(len(a)):
    for j in range(len(a)):
        if a[i]<a[j]:
            a[i] = a[i]^a[j]
            a[j] = a[i]^a[j]
            a[i] = a[i]^a[j]
print(a)
div = a[1]-a[0]
for i in range(len(a)-1):
    if a[i+1]-a[i]!=div:
        print (a[i]+div)
        break



