#danh sách điện thoại = [Tên điện thoại,giá tiền]
dsdt = [["Iphone Mini",25000000], ["Iphone 13",40000000], ["Iphone 13 Pro",50000000], ["Iphone 13 Pro Max",30000000]]
DT = 0
dstongtien =[]


#tính doanh thu: = giá tiền loại điện thoại * số lượng
def doanhthu(dsdt,loaidt,sl,DT):
    DT = dsdt[loaidt-1][1]*sl
    return DT


while True:
    print("-"*160)
    print("Cap nhat doanh thu hom nay? Co/Khong")
    capnhat = str(input())
    if capnhat == "Khong":
        print("-"*160)
        break
    print("Chon loai hang: \n1. Iphone Mini\n2. Iphone 13\n3. Iphone 13 Pro\n4. Iphone 13 Pro Max: ")
    chon = int(input("Loai hang ma so: "))
    print("Nhap so luong: ", end="")
    sl = int(input())
    tongDT = doanhthu(dsdt,chon,sl,DT)
    dstongtien.append(tongDT)
    print("Tong tien:",format(tongDT,",d"), str("VNĐ"))
print("Tong doanh thu hom nay: ", format(sum(dstongtien),",d"), str("VNĐ"))

#Tổng tiền khi bán được 1 loại hàng
#Tổng doanh thu là tổng bán được tất cả loại hàng




