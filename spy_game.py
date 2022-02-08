def spy_game(list):
    '''Spy game: write a function that takes a list of integers and returns True if
    it contains 007 in order'''
    code = [0,0,7,'x']
    for num in list:
        if num == code[0]:
            code.pop(0)
    return len(code)==1
