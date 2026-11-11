def divide(a,b):
    return a/b
while True:
    try:
        number1=int(input("please enter the first number:"))
        number2=int(input("please enter the second number:"))
        result=divide(number1,number2)
    except ValueError:
        print("you should enter a number")
    except ZeroDivisionError:
        print("the number 'b' shouldn't be zero")
    else:
        print("the program has ran successfully")
        print("result:",result)
        break                