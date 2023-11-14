class ThongTinXe:
    LoaiXe = ""
    HangXe = ""
    MauXe = ""
    SoChoNgoi = ""
    SoBanhXe = ""
    GiaTien = ""
    def __init__(self, loai_xe, hang_xe, mau_xe, so_cho_ngoi, so_banh_xe, gia_tien):
        self.LoaiXe = loai_xe
        self.HangXe = hang_xe
        self.MauXe = mau_xe
        self.SoChoNgoi = so_cho_ngoi
        self.SoBanhXe = so_banh_xe
        self.GiaTien = gia_tien
    def ThongTin(self):
        print("Loại:", self.LoaiXe)
        print("Hãng", self.HangXe)
        print("Màu", self.MauXe)
        print("Số chỗ:", self.SoChoNgoi)
        print("Số bánh:", self.SoBanhXe)
        print("Gía:", self.GiaTien)

o_to = ThongTinXe("C300 AMG", "Mercedes", "Trắng", 4, 4, 2353277000)
o_to.ThongTin()

class SoHoc:
    number1 = 0
    number2 = 0
    def __init__(self, n1, n2):
        self.number1 = n1
        self.number2 = n2
    def printInfo(self):
        print(self.number1, self.number2)
    def addition(self):
        print(self.number1 + self.number2)
    def subtract(self):
        print(self.number1 - self.number2)
    def multi(self):
        print(self.number1 * self.number2)
    def division(self):
        print(self.number1 / self.number2)
soHoc = SoHoc(3, 4)
soHoc.division()
import math
class Triagle:
    a = 0
    b = 0
    c = 0
    def __init__(self, canh1, canh2, canh3):
        self.a = canh1
        self.b = canh2
        self.c = canh3
    def checkTriagle(self):
        if self.a + self.b > self.c or self.a + self.c > self.b or self.b + self.c > self.a:
            return True
        else: 
            return False
    def Area(self):
        p = (self.a + self.b + self.c)/2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
    
tam_giac = Triagle(6, 8, 10)
if tam_giac.checkTriagle() == True:
    print(tam_giac.Area())
else:
    print("Đây không phải tam giác")

class soThapPhan:
    PhanNguyen = 0
    PhanThapPhan = 0
    def __init__(self, nguyen, thapPhan):
        self.PhanNguyen = nguyen
        self.PhanThapPhan = thapPhan
    def print(self):
        print(str(self.PhanNguyen) + "." + str(self.PhanThapPhan))
a = soThapPhan(4, 5)
a.new = 10 # thêm thuộc tính vào object
a.print()
print(a.PhanNguyen, a.PhanThapPhan, a.new)

del a.new # xóa thuộc tính của object
print(a.PhanNguyen, a.PhanThapPhan, a.new)

class ThuCung:
    ten = ""
    giong = ""
    mau = ""
    tuoi = 0
    can = 0
    def __init__(self, TEN, GIONG, MAU, TUOI, CAN):
        self.ten = TEN
        self.giong = GIONG
        self.mau = MAU
        self.tuoi = TUOI
        self.can = CAN
    def print(self):
        print(self.ten, self.giong, self.mau, self.tuoi, self.can)
cho = ThuCung('HEO', "CHIBA", "VANG", 4, 10)
cho.print()