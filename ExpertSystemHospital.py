que = ["do you have cough ?",
       "do you have fever ?",
       "do you have swor-Throat ?",
       "do you have cold ?",
       "do you have headache ?"]

print("Welcome to the expert System of Hospital Management : ")

sc = 0
for i in que:
    print(i,end = " ")
    ans = input("y/s : ")
    if ans=='y':
        print("please scale the symptoms in the range of 1 to 10",end=" ")
        score = int(input("Enter Scale"))
        print()
        sc = sc + score
    
    
print("\n")
print("your score is : ",sc)
if sc >=30 :
    print("You have serious condition , please meet doctor immedialtely")
if sc >=20 and sc<30:
    print("Your in in intermediate state ,Please take advise of medicians")
if sc < 20 :
    print("your are normal , you take rest, you will be fine")