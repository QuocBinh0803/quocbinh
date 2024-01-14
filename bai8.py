def tinh_luy_thua(x, n):
    if n == 0:
        return 1
    else:
        return x * tinh_luy_thua(x, n-1)

# Thử nghiệm đoạn mã
coso = int(input("Nhập cơ số: "))
luythua = int(input("Nhập lũy thùa của cơ số: "))
ketqua = tinh_luy_thua(coso, luythua)
print(f"{coso}^{luythua} = {ketqua}")
