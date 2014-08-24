
number_of_tests = int(input())
for test in range(number_of_tests):
    cuts = int(input())
    middle = int(cuts/2)
    rest = cuts % 2
    print(middle * (middle + rest))