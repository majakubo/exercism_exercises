def verify(isbn):
    isbn = isbn.replace('-', '')
    if len(isbn) != 10:
        return False

    isbn_list = list(isbn)
    
    #change last position x or X for 10
    if isbn_list[-1] == 'X' or isbn_list[-1] == 'x':
        isbn_list[-1] = '10'

    #check is there any letters in isbn
    for element in isbn_list:
        if not element.isdigit():
            return False

    
    isbn_list = [int(x) for x in isbn_list]        

    result = 0
    for i in range(len(isbn_list)):
        result = result + ((10-i) * isbn_list[i])

    if result % 11 == 0: 
        return True
    else:
        return False
