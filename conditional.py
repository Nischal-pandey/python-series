#wap to check year is leap year or not
year=int(input("enter year"))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print(year,"is leap  year")
        else:
            print(year,"not leap year")
    else:
        print(year,"is leap year")
else:
    print(year,"not leap year")
    
    
    
    num=int(input("enter any num"))
#////////////////////////////////////////////////////////////////////////////*/
if num%2==0:
    if num%3==0:
        if num%6==0:
            if num%12==0:
                print("divisible by 2 ,3 and 6 and 12")
            else:
                print('not divisible by 12 only 2 ,3 and 6')
        else:
            print("not such condition")
    else:
        print('divisible by 2')
elif num%3==0:
    print(" divisible by 3")
else:
    print("not divisible by 2,3 and 6 and 12")