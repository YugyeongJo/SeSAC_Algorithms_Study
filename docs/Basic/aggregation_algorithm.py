from collections import defaultdict

def count_elements(elements):
    count_dict = defaultdict(int)
    for element in elements:
        count_dict[element] += 1
    return count_dict

gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1]
result = count_elements(gems)
print(result)
