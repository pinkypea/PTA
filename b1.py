# So sánh chiều cao 3 người
a = int(input("Chiều cao bạn a là (cm): "))
b = int(input("Chiều cao bạn b là (cm): "))
c = int(input("Chiều cao bạn c là (cm): "))
if a > b and a > c:
    print("a là người cao nhất")
elif b > a and b > c:
    print("b là người cao nhất")
elif c > a and c > b:
    print("c là người cao nhất")

n = int(input("Nhập n: "))
arr = []
for i in range (n):
    index = float(input("Nhập phần tử của mảng: "))
    arr.append(index)
total = 0
for i in range(len(arr)):
    total += arr[i]
print(arr)
print(total)

name = input("Nhập tên của bạn: ")
for i in range (len(name)):
    print(name[i])

import math
def rutgon(tu, mau):
    UCLN = math.gcd(tu, mau)
    tu_moi = int(tu / UCLN)
    mau_moi = int(mau / UCLN)
    print(tu_moi, "/", mau_moi)
tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))
rutgon(tu,mau)
