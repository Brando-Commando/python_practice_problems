if __name__ == '__main__':
    year = int(input())

def is_leap(year):
    leap = False
    
    # This was an attempt to combine tree if statements into a single line statement, it was unsuccessful and would 
    # result in 2/3 tests pass 
    '''
    if ((year % 4) == 0) or ((year % 400) == 0) and not ((year % 100) == 0):
        leap = True
        
    else:
        leap = False
    
    return leap
    '''
    
    if ((year % 4) == 0):
        leap = True
        if ((year % 100) == 0):
            leap = False
            if ((year % 400) == 0):
                leap = True 
    else:
        leap = False
        
    return leap
