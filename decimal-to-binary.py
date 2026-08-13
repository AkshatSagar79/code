def DecimalToBinary(x):

    #Check if 0
     if x == 0:
        return '0'
    
     #Initialize result 
     result = ''

     #Iterate until x is 0
     while x>0:
     
        #Get remainder and append it on the left
        remainder = x % 2
        result = str(remainder) + result
     
    #Divide x by 2
     x = x // 2

     #End
     return result

# Main program
x = int(input("Enter number to convert: "))
y =  DecimalToBinary(x)
print(x, 'is', y, 'in binary')
