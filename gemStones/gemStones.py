def build_list():
    occurrences_list = []
    for i in range(ord('z')-ord('a')+1):
        occurrences_list.append(0)
    return occurrences_list


number_of_stones = int(input())
list_of_occurrences = build_list()

for stone in range(number_of_stones):
    element = str(input())
    occurrences = []
    for character in element:
        if character not in occurrences:
            list_of_occurrences[ord(character)-97] += 1
            occurrences.append(character)

gem_elements = [i for i, x in enumerate(list_of_occurrences) if x==number_of_stones]
print(len(gem_elements))
