#!/usr/bin/env python3

def happy_new_year():
    i = 10
    for i in range (10, 0, -1):
        print(i)
    print("Happy New Year!")
    pass

def square_integers(int_list):
    # code goes here!
    int_list = [1,2,3,4,5]
    return [i**2 for i in int_list]
    pass

def fizzbuzz():
    # code goes here!
    for i in range (1, 101, 1):
        if i%15 == 0:
            print("FizzBuzz")
        elif i%5 == 0:
            print ("Buzz")
        elif i%3 == 0:
            print ("Fizz")
        else :
            print(i)
print(fizzbuzz)
