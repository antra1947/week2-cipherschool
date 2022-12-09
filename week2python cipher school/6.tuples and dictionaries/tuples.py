a = 7
b = 6
a,b = b,a
c = a, b
print(type(c))

def sum_diff(a,b):
    a = a+b
    d = a-b
    return a,d
c = sum_diff(1,6)
print((c))

a = [9,7,6,5]
print(list(range(5)))

a={
    "name": "antra",
    "company": "google",
    "college":"LPU",
}
print(a)


for x in a:
    print(x)
    
    list (a)