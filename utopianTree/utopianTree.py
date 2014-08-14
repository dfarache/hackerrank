def calculate_tree_size(growth_cycles):
    size_of_tree = 1
    for cycle in range(growth_cycles):
        if cycle%2 == 0:
            size_of_tree *= 2
        else:
            size_of_tree += 1
    return size_of_tree


def calculate_answers():
    for i in range(number_of_tests):
        growth_cycles = int(input())
        print(calculate_tree_size(growth_cycles))


number_of_tests = int(input())
calculate_answers()

