def thap_phan_sang_nhi_phan(n):
    assert n >= 0, "Đầu vào phải là một số nguyên không âm."
    if n == 0:
        return '0'
    else:
        return thap_phan_sang_nhi_phan(n // 2) + str(n % 2)

# Thử nghiệm đoạn mã
ket_qua = thap_phan_sang_nhi_phan(14)
print(ket_qua)

