l = input("data: ")
lst = l.split(",")
new = []
for i in lst:
    if i not in new:
        new.append(i)
print(new)
# new version 5