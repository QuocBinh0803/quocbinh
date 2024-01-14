def openRussianDoll(doll): #hàm này có doll là tham số đại diện cho số lượng búp bê 
    if doll == 1: #hàm này là điều kiện nếu chỉ có 1 con búp bê thì sẽ ra dòng "All dolls are opened "
        print("All dolls are opened")
    else:
        print(doll)
        openRussianDoll(doll-1) #nếu có nhiều hơn 1 búp bê thì điều kiện này nó sẽ trừ đi 1 cho đến khi 
        #nào hiện chữ "All dolls are opened " quá trình này được lặp lại cho đến khi chỉ còn 1 búp bê  
       
doll = int(input("Nhập số lượng búp bê: "))
openRussianDoll(doll)