def GetMin(values):
    if len(values) == 0:
        raise ValueError('List is empty')


    #Assume that the minimum value is first element
    result = values[0]

    # Otherwise Traverse the rest
    for i in range(1, len(values)):
        if values[i] < result:
            result = values[i]

    # Return minimum value
    return result


# Main program

my_list = [4,2,6,8,3,5,9,1]
my_list_min = GetMin(my_list)

print('Minimum value:', my_list_min)    
w