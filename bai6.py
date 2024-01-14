def fibonacci(n):#Định nghĩa hàm fibonacci nhận một tham số n
    if n <= 1:#điều kiện trong hàm Fibonacci để xác định điều kiện dừng của việc sử dụng đệ quy
        return n#
    else:
        return fibonacci(n-1) + fibonacci(n-2)#Cộng hai kết quả trên lại và trả về kết quả cuối cùng cho số Fibonacci ở vị trí n
n = int(input("Nhập số lượng số Fibonacci muốn in: "))#nhập vào một số nguyên n để xác định số lượng số Fibonacci cần in
ket_qua = [fibonacci(i) for i in range(n)] #Lưu n số Fibonacci đầu tieeb vào danh sách ket_qua
print(f"Dãy Fibonacci đầu tiên {n} số là: {ket_qua}")#in kết quả ra màn hình
