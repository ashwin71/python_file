
'''number = int(input("enter the number: "))
# If i enter number it run but if it is a text it shows error
print(number)'''


'''try:
    number = int(input("enter the number: "))
    print(number)
except:
    print("invalid number")'''

#We can catch special type of error.

'''try:
    n = 10/0
    #this is a zero division error.
    number = int(input("enter the number: "))
    print(number)
except ZeroDivisionError:
    print("number is divided by zero")
except ValueError:
    print("type of value is not same")'''

'''try:
    n = 10/0
    #this is a zero division error.
    number = int(input("enter the number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
    #it will print error
except ValueError:
    print("type of value is not same")
except:
    print("errorr")'''