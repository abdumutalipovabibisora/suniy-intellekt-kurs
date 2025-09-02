narx = input("daftar qalam chizgich - narxlari = ").split()
soni = input("daftar qalam chizgich - soni = ").split()

daftar = float(narx[0]) * float(soni[0])
qalam = float(narx[1]) * float(soni[1])
chizgich = float(narx[2]) * float(soni[2])
umumiy = daftar + qalam + chizgich

print(f"Kanstovarni umumiy narxi: {umumiy} som")