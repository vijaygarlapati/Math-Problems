def spy_game(list):
    '''Spy game: write a function that takes a list of integers and returns True if
    it contains 007 in order'''

    for num in range(0,len(list)-2):
        if list[num]==0 and list[num+1]==0 and list[num+2]==7:
            return True
        else:
            pass
    return False
