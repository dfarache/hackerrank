L = int(input())
R = int(input())

maximum = 0
for A in range(L, R+1):
    for B in range(L,R+1):
        if A^B > maximum:
            maximum = A^B
print(maximum)