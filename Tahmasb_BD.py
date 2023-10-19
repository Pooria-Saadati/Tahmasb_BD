n = int(input())
degree = (input().split(" "))

for i in range(0,n):
    degree[i] = float(degree[i])
degree.sort()
degree.insert(0, 0)
print(degree)
resault = dict()
for i in range(0,n):
    resault[degree[i+1] - degree[i]]=degree[i+1]
    print(i)
    print(resault)
print(resault[max(resault)])
# print(resault[max(resault.values())])
# print(100*(max(resault)/360))