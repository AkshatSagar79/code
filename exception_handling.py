try:
    op1 = int(input("Enter first operand: "))
    op2 = int(input("Enter second operand: "))
    result = op1 / op2
    print('The result is', result)
    
except ValueError:
    print('Invalid numeric value')
except ZeroDivisionError:
    print('Invalid division by 0')
