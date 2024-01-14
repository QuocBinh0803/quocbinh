def USCLN(a, b):
    if b == 0:
        return a
    else:
        return USCLN(b, a % b)
a = int(input("Nhập a = "))
b = int(input("Nhập b = "))
print(f"USCLN của {a} và {b} là: {USCLN(a,b)}")