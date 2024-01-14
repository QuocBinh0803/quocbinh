def giaithua(n):#tạo hàm giai thừa với biến n
    if n == 0 or n ==1:#đặt điều kiện dừng
        return 1#trả về 1 nếu n bằng 1 hoặc 0
    else:
        return n*giaithua(n-1)#điều kiện chưa thõa trả vè giá trị: n*n-1 
a = int(input("Nhập n = "))#nhập n từ bàn phím
ketqua = giaithua(a)#khai báo biến n đồng thời gán hàm giaithua cho biến a 
print(f"{a}! = {ketqua}")#in kết quả ra màn hình