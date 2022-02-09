def unique_list(lst):
    '''To get the unique list out of given list having repeated objects'''
    seen_numbers = []

    for num in lst:
        if num not in seen_numbers:
            seen_numbers.append(num)
    return seen_numbers
