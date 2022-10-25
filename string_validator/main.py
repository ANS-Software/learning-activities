
def string_validator(s: str) ->list:    
    
    list_of_methods = [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]

    # str.isupper(s)

    # list_of_booleans = []
    
    for method in list_of_methods:
        print(any(method(char) for char in s))

        # for char in s:
        #     if method(char):       #alnum(q)
        #         list_of_booleans.append('True')
    


    # return list_of_booleans

# print(string_validator('tatiana'))
string_validator('qA2')


#notes--
#typing-- what is the type of 
#the argument  = is assigment : tells the object type 
# that you are parsing


# str.isalnum()
# str.isalpha()
# str.isdigit()
# str.islower()
# str.isupper()