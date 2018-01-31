#v1
def dictionary(myList):
    newDict={}
    for a in myList :
        if a[0] not in newDict:
            nList=[]
        else:
            nList=newDict[a[0]]
        nList.append(a)
        newDict[a[0]]=nList
    return newDict
#v2
def dictionary2(myList):
    newDict={}
    for a in myList :
        try :
            nList=newDict[a[0]]
        except KeyError:
            nList=[]
        finally:
            nList.append(a)
            newDict[a[0]]=nList
    return newDict
if __name__ == '__main__':
    newList=["ahmed","fatma","Ibrahim","ammar","Islam"]
    dict=dictionary(newList)
    print(dict)