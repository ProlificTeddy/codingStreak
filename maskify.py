"""Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four characters into '#'."""

def maskify(cc):
    length = len(cc)
    char_list = list(cc)  
    if length == 4:
        return cc  
    elif length > 4:

        for i in range(length - 4):
            char_list[i] = "#"  
        
        new_string = "".join(char_list)  
        return new_string
    else:
        return cc 


print(maskify("Skippy"))
print(maskify("Nananananananananananananananana Batman!"))
