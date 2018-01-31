#v1
def vowelsRemove(d):
    b=''
    for a in d:
        if a.lower() not in ('a', 'e', 'i', 'o', 'u') :
            b+=a
    return b
if __name__ == '__main__':
    d=input("Enter word\n")
    print(vowelsRemove(d))
#v2
# def multiRemove(*args):
#     for a in args:
#         b=''
#         for ae in a:
#             if ae.lower() not in ('a', 'e', 'i', 'o', 'u') :
#                 b+=ae
#         print(b)
# if __name__ == '__main__':
#     multiRemove('ahmooooed','mohamed')
#v3
def multiRemoveList(myList):
    newList=[]
    for a in myList:
        b=''
        for ae in a:
            if ae.lower() not in ('a', 'e', 'i', 'o', 'u') :
                b+=ae
        newList.append(b)
    return newList    
if __name__ == '__main__':    
    strList=['ahmooooed','mohamed']
    list=multiRemoveList(strList)
    print(list)
