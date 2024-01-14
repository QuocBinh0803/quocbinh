def recursiveMethod(n):# tạo hàm recursiveMethod với tham số n
    if n<1:#điều kiện kiểm tra xem 'n' có nhỏ hơn 1 không
        print("n is less than 1")#nếu nhỏ hơn 1 hàm sẽ in ra "n is less than 1".Còn không thì sẽ chuyển sang eles và thực hiện câu lệnh trong đó
    else:
        recursiveMethod(n-1)# nếu 'n' không nhỏ hơn 1 hàm sẽ trừ đi 1 Quá trình đệ quy này sẽ tiếp tục cho đến khi 'n' trở thành 0 hoặc âm.
        print(n)#in ra kết quả