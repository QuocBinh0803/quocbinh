def tinh_luy_thua(x, n):#x là cơ số và n là số mũ
    if n == 0:#điều kiện dừng của đệ quy
        return 1
    else:
        return x * tinh_luy_thua(x, n-1)#hàm thực hiện phép nhân x * tinh_luy_thua(x, n-1) để tính lũy thừa
coso = int(input("Nhập cơ số: "))#nhập cơ số (coso) và số mũ (luythua) từ bàn phím
luythua = int(input("Nhập lũy thùa của cơ số: "))#nhận giá trị lũy thừa từ bàn phím
ketqua = tinh_luy_thua(coso, luythua)#Hàm tinh_luy_thua được gọi với đối số là coso và luythua để tính lũy thừa, và kết quả được gán cho biến ketqua
print(f"{coso}^{luythua} = {ketqua}")#in ra kết quả
