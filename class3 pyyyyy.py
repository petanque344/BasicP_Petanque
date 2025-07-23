# haverice = True
# havespoon = False
# havehand = True

# if haverice:
#     if havespoon:
#         print("กินข้าว")
#     elif havehand:
#         print("กินข้าวเหนียว")

# p=int(input("enter your score"))
# if p >= 0:
#     if p <= 100:
#         if p >= 80:#80-100
#             print("A")
#         if p >= 70:
#             if p < 80:#70-79
#                 print("B")
#         if p >= 60:
#             if p < 70: #60-69
#                 print("C")
#         if p >= 50:
#             if p <60 : #50-59
#                 print("D")
#         if p < 50: #<50
#             print("F")

# for i in range(1,1000000,2):
#     print(i)

# i=0
# while i < 8 :
#     print(i)
#     i = i+1

# while True:
#     choice = int(input("กรอก1เพื่อบวกเลข,กรอก2เพื่อออก:"))

#     if choice ==1:
#         num = int(input("จำนวนเลขที่ต้องการจะบวก:"))
#         sumation = 0

#         for i in range(num):
#             num1=int(input("กรอกเลข:"))
#             sumation = sumation+num1

#         print("ผลลัพท์",sumation) 

#     if choice==2:
#         print("bye")
#         break


while True:
    

    de = int(input("1forfight,2forleave"))

    monster_hp = 50
    weapon1 = 10
    weapon2 = 20
    weapon3 = 30 

    if de ==1:
        num = int(input("rounds for attack"))

        for i in range(num):
            we=int(input("weapons???"))
            if we==(1):
             monster_hp = monster_hp -weapon1
            elif we==(2):
             monster_hp = monster_hp -weapon2
            elif we==(3):
             monster_hp = monster_hp -weapon3

            if monster_hp == (0):
                print("You win")
                break
            elif monster_hp < (0):
                monster_hp = 20
                
            print("result",monster_hp)

        j=i+1
        if j==num and monster_hp > 0:
            print("You lose")
            break
        else:
            break

    if de==2:
        print("bye")
        break



            
                   
              

         

       