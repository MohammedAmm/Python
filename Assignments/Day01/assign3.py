def multiplication(n):
    outerList=[]
    for a in range(1,n+1):
        innerList=[]
        for b in range(1,(a+1)):
            innerList.append((a)*(b))
        outerList.append(innerList)
    return(outerList)
if __name__ == '__main__':
    number=input("Enter a number \n")
    try:
        multiplication(3)
    except:
        print("Can't get integer value of string")

