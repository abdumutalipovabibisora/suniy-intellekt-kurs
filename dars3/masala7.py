narx = input("daftar qalam ruchka - narxlari = ").split()
soni = input("daftar qalam ruchka - soni = ").split()

daftar = float(narx[0]) * float(soni[0])
qalam = float(narx[1]) * float(soni[1])
ruchka = float(narx[2]) * float(soni[2])
umumiy = daftar + qalam + ruchka

print(f"Kanstovarni umumiy narxi: {umumiy} som")


