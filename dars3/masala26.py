narxi = input("pomidor bodring olma - narxlari = ").split()
vazni = input("pomidor bodring olma - vazni = ").split()

pomidor = float(narxi[0]) * float(vazni[0])
bodring = float(narxi[1]) * float(vazni[1])
olma = float(narxi[2]) * float(vazni[2])
umumiy = pomidor + bodring + olma

print(f"Umumiy narxi: {umumiy} som")