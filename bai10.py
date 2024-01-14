def thap_phan_sang_nhi_phan(n):#nhận một số nguyên không âm n và trả về biểu diễn nhị phân của n 
    assert n >= 0, "Đầu vào phải là một số nguyên không âm."#kiểm tra xem n có phải là số nguyên không âm hay không
    if n == 0:#điều kiện dừng của đệ quy
        return '0'
    else:
        return thap_phan_sang_nhi_phan(n // 2) + str(n % 2)#để chuyển đổi phần nguyên của n sang hệ nhị phân. Kết quả được cộng với chuỗi chứa phần dư của n khi chia cho 2 

x = int(input("Nhập số cần chuyển đổi: "))#nhập một số nguyên từ bàn phím và giá trị này được chuyển đổi
ket_qua = thap_phan_sang_nhi_phan(x)#với đối số là x để chuyển đổi số này sang hệ nhị phân

