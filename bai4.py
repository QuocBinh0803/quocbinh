def powerOfTwo(n):#tạo hàm'powerOfTwo' với tham số n
    if n == 0:#đặt điều kiện dừng
         return 1#Nếu n bằng 0, hàm trả về giá trị 1, là kết quả của lũy thừa 2^0
    else:
        power = powerOfTwo(n-1)#lũy thừa của 2 với giảm giá trị của n
        return power * 2#hàm trả về lũy thừa của 2 với giá trị n.
n = int(input("Nhập n = "))
print(powerOfTwo(n))
