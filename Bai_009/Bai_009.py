import math
n = int(input("Nhap so canh cua da giac deu: "))
r = float(input("Nhap ban kinh duong tron: "))
square = 1/2*n*r*r*math.sin(2*3.14/n)
print("Dien tich cua da giac deu n canh noi tiep duong tron ban kinh r: ", square)