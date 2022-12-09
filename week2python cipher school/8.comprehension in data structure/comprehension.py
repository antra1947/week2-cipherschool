a = []
for i in range(5):
    temp = []
    for j in range(5):
        temp.append(j)
        a.append(temp)
        print(a)


        n = 5
        [[max (i+1, j+1,n-i, n-j) for j in range(n)] for i in range(n)]

        [ j for i in range(2) for j in range (2)]

        #dict comprehension
a={
   2:4,
   5:7,
   6:8,
}
print(a)

#set comprehennsiion

a = { i for i in range(5)}
print(type(a))

a = (i for i in range(5))
print(type(a))

it = iter(a)
print(next(it))


 













