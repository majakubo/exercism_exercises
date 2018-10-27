def is_armstrong(number):
    len_of_num = len(str(number))

    numbers = [int(num)**len_of_num for num in str(number)]
    
    armstrong = sum(numbers)

    if armstrong == number:
        return True
    else:
        return False

    

   

