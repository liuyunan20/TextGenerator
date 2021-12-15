def divide_by(number):
    try:
        n = 100 / number
    except ZeroDivisionError:
        print("Please enter a number that is not equal to zero")
    else:
        if number > 0:
            print(100 / number)
        else:
            print(100 / (number / 2))
