def locator(myStr,key):
    i=0
    myList=[]
    for a in myStr:
        if a == key:
            myList.append(i)
        i+=1
    return myList
# list=locator("This is javaScript","i")
# print(list)
if __name__ == '__main__':
    newStr=input("Enter a sentence \n")
    newKey=input("Enter a char to search\n")
    list=locator(newStr,newKey)
    if len(list) != 0 :
        print("Exists at :",list)
    else :
        print("Not Exists")
