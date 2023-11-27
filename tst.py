c = int(input("candy: "))
ch = int(input("children: "))
count = c
while c % ch != 0:
    c += 1 
print("EXCESS:",c-count)


n = int(input())
k =True
while n % 10 != 0:
    n+= 1
print(n)
# new version 7