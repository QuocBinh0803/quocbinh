def firstMethod():#àm này thực hiện các câu lệnh bên trong nó
    secondMethod()#Gọi hàm secondMethod() từ firstMethod(). Chương trình chuyển sang thực hiện câu lệnh trong secondMethod()
    print("I am the first Method") # in ra một thông báo từ "firstMethod()"
def secondMethod():#định nghĩa hàm
    thirdMethod()# Gọi hàm thirdMethod() từ secondMethod(). Chương trình chuyển sang thực hiện câu lệnh trong thirdMethod()
    print("I am the second Method") #in ra một thông báo từ "secondMethod()"
def thirdMethod():#định nghĩa hàm
    fourthMethod()#Gọi hàm fourthMethod() từ thirdMethod(). Chương trình chuyển sang thực hiện câu lệnh trong fourthMethod()
    print("I am the third Method")#in ra một thông báo từ "thirdMethod()"
def fourthMethod():#định nghĩa hàm
    print("I am the fourth Method")#in ra một thông báo từ "fourthMethod()"
firstMethod() #Gọi hàm firstMethod() để hiển thị tất cả thông tin