N, M = [int(x) for x in input().split()]

A = [int(x) for x in input().split()]
A.insert(0, 0)

B = [int(x) for x in input().split()]
B.insert(0, 0)

C = [int(x) for x in input().split()]
C.insert(0, 0)

values_occurred = {}
p = (10**9) + 7


for i in range(1, M+1):
    if B[i] in values_occurred:
        values_occurred[B[i]] = (values_occurred[B[i]] * C[i]) % p
    else:
        values_occurred[B[i]] = C[i]

for i in range(1, N+1):
    for j in range(1, int(N/i) + 1):
        if i in values_occurred:
            A[i*j] = A[i*j] * values_occurred.get(i) % p
for i in range(1, len(A)):
    print(A[i], end=" ")

