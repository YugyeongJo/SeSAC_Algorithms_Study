def find_1st(lsts, algorithms_type):
    if algorithms_type == 'in_method':
        if 1 in lsts:
            return True
        else:
            return False
    elif algorithms_type == 'exhaustive_search':
        for lst in lsts:
            if lst == 1:
                return True
            else: 
                return False     

if __name__ == '__main__':
    gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1]
    algorithms_type = ['in_method', 'exhaustive_search']
    for algorithm in algorithms_type:
        print(find_1st(gems, algorithm))