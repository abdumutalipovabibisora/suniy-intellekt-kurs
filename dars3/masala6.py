import math

silindr = input("radius balandlik = ").split()

pi = math.pi
yuza = 2*pi*float(silindr[0])*(float(silindr[0])+float(silindr[1]))
hajm = pi*float(silindr[0])**2*float(silindr[1])

print(f"silindrning yuzi: {yuza}, hajmi: {hajm} ga teng")

