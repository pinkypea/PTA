class CaSi:
    TenThat = ""
    NickName = ""
    Hits = ""
HuongTram = CaSi()
HuongTram.TenThat = "Phạm Thị Hương Tràm"
HuongTram.NickName = "Hương Tràm"
HuongTram.Hits = "Em gái mưa"
print(HuongTram.TenThat)
print(HuongTram.NickName)
print(HuongTram.Hits)
print("------------------------------")
SonTung = CaSi()
SonTung.TenThat = "Nguyễn Thanh Tùng"
SonTung.NickName = "Sơn Tùng M-TP"
SonTung.Hits = "Em của ngày hôm qua"
print(SonTung.TenThat)
print(SonTung.NickName)
print(SonTung.Hits)

class ThongTinXe:
    loai_xe = ""
    hang_xe = ""
    mau_xe = ""
    so_cho_ngoi = ""
    so_banh_xe = ""
    gia_tien = ""
    def ThongTin(self):
        print(self.loai_xe)
        print(self.hang_xe)
        print(self.mau_xe)
        print(self.so_cho_ngoi)
        print(self.so_banh_xe)
        print(self.gia_tien)

o_to = ThongTinXe()
o_to.loai_xe = "C300 AMG​"
o_to.hang_xe = "Mercedes"
o_to.mau_xe = "Trắng"
o_to.so_cho_ngoi = 4
o_to.so_banh_xe = 4
o_to.gia_tien = 2353277000
o_to.ThongTin()

# Viết chương trình tạo ra lớp TamGiac, có 3 thuộc tính là 3 cạnh của tam giác, có 1 phương thức tính chu vi.

class TamGiac:
    canh1 = 0
    canh2 = 0
    canh3 = 0
    def chuVi(self):
        print("Chu vi:", self.canh1 + self.canh2 + self.canh3)
alpha = TamGiac()
alpha.canh1 = 6
alpha.canh2 = 8
alpha.canh3 = 10
alpha.chuVi()