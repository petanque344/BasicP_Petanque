# def grade(score):
#     if score >= 80:
#         print("Grade A")
#     elif score>=





# def my_sum(a,b):
#     return a+b

# print(my_sum(5,5))

# def my_sum(a,b):
#     return a+b

# result = my_sum(5,5)
# print(result)

# def choose(a,b):
#     if a == 1:
#         num = int(input("how many?"))
#         for i in range(num):
#             price=int(input("how much?"))


# de = int(input("1for,2leave"))
# if de == 1:
#         num = int(input("how many?"))
#         for i in range(num):
#             price=int(input("how much?"))

# def my_sum(a,b):
#     de = int(input("1for,2leave"))
#     if de == a :
#      print("ggg")

    

# my_sum(1,2)


# def sumation(quan,per):#Bussiness logic ###me
#    result=quan*per
#    vat=result*0.07
#    total=result+vat
#    return result


# def menu():#user Interface
#    while True:
#       choice=int(input("1.go,2.leave"))
#       if choice == 1:
#          quan=int(input("how many?"))
#          per = int(input("how much?"))
#          print(sumation(quan,per))

#       if choice == 2:
#          print("bye")
#          break
         
# menu()   

# def sumation(quan, per): #p gab
#     result = quan * per
#     total_vat = result * 0.07
#     total = result + total_vat
#     return total
 
# def menu():
#     while True:
#         choice = int(input("1.) เพื่อคำนวณราคาสินค้า, 2.) เพื่อออกโปรแกรม"))
#         if choice == 1:
#             quan = int(input("จำนวนสินค้าทั้งหมด: "))
#             per = int(input("ราคาต่อชิ้น: "))
#             print(sumation(quan, per))
 
#         if choice == 2:
#             print("Bye")
#             break
 
# menu()

# my_list = [1,2,"GGG"]
# # print("Before",my_list[0])

# # my_list[0] = 3
# # print("After",my_list)

# print("Before",my_list)

# # my_list.append("GGG")
# my_list.pop(1)

# print("After",my_list)

# my_list = [1,2,"GGG"]

# for i in my_list:
#     print(i)

# my_dict = {"name": "P","age": 20}
# print("Before",my_dict)

# my_dict["name"] = False
# print("After",my_dict)

students = [
    {"name":"P","age":20},
    {"name":"G","age":30}
]

for i in students:
    print(i["name"])