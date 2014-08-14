
def calculate_largest_vehicle():
    [x, y] = [int(x) for x in input().split()]
    return min(freeway[x:y+1])



[length_of_freeway, number_of_tests] = input().split()
freeway = [int(x) for x in input().split()]

for test in range(int(number_of_tests)):
    print(str(calculate_largest_vehicle()))
