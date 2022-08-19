
'''
if __name__ == '__main__':
    
    # Taking inputs for all values
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # assigns i,j,k values 
    # i is for all values up to the max and then stops once it is reached
    
    # the last if statement will filter out any responses that sum up to n
    print(list([i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)  if i+j+k !=n))

'''


if __name__ == '__main__':

    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

def comprehension(x,y,z,n):

        print(list([i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)  if i+j+k !=n))