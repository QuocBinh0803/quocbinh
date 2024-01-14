def USCLN(a, b):#nhận hai đối số là a và b
    if b == 0:#điều kiện dừng của đệ quy
        return a
    else:
        return USCLN(b, a % b)#thực hiện thuật toán Euclid để tìm USCLN
a = int(input("Nhập a = "))#nhập hai số nguyên dương a và b từ bàn phím
b = int(input("Nhập b = "))
print(f"USCLN của {a} và {b} là: {USCLN(a,b)}")#in ra kết quả