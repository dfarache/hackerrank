number_of_sticks = int(input())
sticks_and_length = [int(x) for x in input().split()]
while number_of_sticks > 0:
    print(number_of_sticks)
    minimum_size = min(sticks_and_length)
    sticks_and_length = [x-minimum_size for x in sticks_and_length]
    number_of_sticks -= sticks_and_length.count(0)
    sticks_and_length = [x for x in sticks_and_length if x != 0]



