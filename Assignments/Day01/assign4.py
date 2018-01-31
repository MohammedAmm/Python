def calcArea(*args):
    if len(args) in (2,3) :
        if args[0].lower() == 't':
            area=0.5*int(args[1])*int(args[2])
        elif args[0].lower() == 'r':
            if len(args) == 2:
                area=args[1] ** 2
            elif len(args) == 3:
                area=args[1] * args[2]
            else:
                print("Error in parameters")
                return
        elif args[0].lower() == 'c':
                if len(args) == 2 :
                    area=3.14*(args[1]**2)
                else:
                    print("Error in parameters")
                    return                    
        else:
            print("Unsupported shape!")
            return
        return area
    else:
        print("Error in parameters")
        return
if __name__ == '__main__':
    myArea=calcArea("r",3)
    if myArea is not None:
        print("The area of shape is : ",myArea)