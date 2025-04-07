def check_string(string):
    
    temp = ''
    for i in string:
        temp = i+temp
    if  temp==string:
        return True
    return False

    
string='palilap'
if check_string(string):
    print("string is palindrome")
else:
    print('string is not palindrome')