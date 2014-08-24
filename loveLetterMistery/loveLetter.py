def apply_changes(string):
    number_of_changes = 0
    length = len(string)
    low = 0
    high = length-1
    for index in range(int(length/2)):
        number_of_changes += abs(ord(string[low]) - ord(string[high]))
        high -= 1
        low += 1
    print(number_of_changes)


def calculate_answers():
    for i in range(number_of_tests):
        string = str(input())
        apply_changes(string)


number_of_tests = int(input())
calculate_answers()