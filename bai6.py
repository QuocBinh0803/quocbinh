def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Nhập số lượng số Fibonacci muốn in: "))
ket_qua = [fibonacci(i) for i in range(n)] #Lưu n số Fibonacci đầu tieeb vào danh sách ket_qua
print(f"Dãy Fibonacci đầu tiên {n} số là: {ket_qua}")
