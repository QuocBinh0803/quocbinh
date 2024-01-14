def tinh_tong_chu_so(n):#định nghĩa và tham số n
    if n == 0:#điều kiện dừng của đệ quy
        return 0
    else:
        return n % 10 + tinh_tong_chu_so(n // 10)#hàm thực hiện phép chia lấy dư n % 10 để lấy chữ số cuối cùng của n,sau đó cộng với kết quả của việc gọi đệ quy với n đã bỏ đi chữ số cuối

a = int(input("Nhập só nguyên dương: "))#nhập 1 số nguyên dương từ bàn phím
tong_chu_so = tinh_tong_chu_so(a)#tính tổng các chữ số của số nguyên dương này, và kết quả được gán cho biến tong_chu_so
print(f"Tổng các chữ số của {a} là {tong_chu_so}")#in ra kết quả
