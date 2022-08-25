#!/usr/bin/env python3

import random

def pw_gen():
    lower_list = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
    
    upper_list = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
    
    num_list = [ '1', '2', '3', '4', '5', '6', '7', '8', '9', '0' ]
    
    specials_list = [ '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '[', ']', '{', '}', '\\', '|', ';', ':', '"', "'", ',', '<', '>', '.', '/', '?' ]
    
    char_list = [ ]
    
    char_list_selection = input("Enter each list you want to use or type help for options: ").lower().strip()
    while True:
        if char_list_selection == 'help':
            print("Options:")
            print("lower:    " + str(lower_list))
            print("upper:    " + str(upper_list))
            print("num:      " + str(num_list))
            print("specials: " + str(specials_list))
        options = char_list_selection.split()
        if 'all' in options:
            char_list = lower_list + upper_list + num_list + specials_list
            break
        for i in options: 
            if i == 'lower' or i == 'l':
                char_list = char_list + lower_list
            elif i == "upper" or i == 'u':
                char_list = char_list + upper_list
            elif i == 'num' or i == 'n':
                char_list = char_list + num_list
            elif i == 'specials' or i == 's':
                char_list = char_list + specials_list
            else:    
                print("Invalid Option:", i)
        break
    
    #print(char_list)
    #print(len(char_list))
    
    char_list_len = len(char_list)
    
    pw_fin = ""
    pw_len = input("How long should the password be? ")
    
    print(50*"=")
    print("Password Generator")
    print(50*"=")
    
    for i in range(int(pw_len)):
        r = random.randint(1, char_list_len-1)
        rand_char =  char_list[r]
        pw_fin = pw_fin + rand_char
   
    return pw_fin
