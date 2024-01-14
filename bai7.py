def tinh_tong_chu_so(n):
    if n == 0:
        return 0
    else:
        return n % 10 + tinh_tong_chu_so(n // 10)

a = int(input("Nhập só nguyên dương: "))
tong_chu_so = tinh_tong_chu_so(a)
print(f"Tổng các chữ số của {a} là {tong_chu_so}")
