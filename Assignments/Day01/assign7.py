def pyramid(n):
    for i in range(n):
        print(" "*(n-i-1)+"*"*(i+1))
number=input("Enter numbe of lines :\n")
try:
    pyramid(int(number))
except ValueError :
    print("Enter an integer value")