# 1. feladat
n = int(input("Hetek száma: "))
cel = float(input("Elérni kívánt testtömeg (kg-ban): "))

# 2. feladat
tomeg = []
for i in range(n):
    tomeg.append(float(input(f"{i+1}. héten: ")))

# 3. feladat
cel_elerte = False
for i in range(n):
    if tomeg[i] <= cel:
        print(f"Mari néni a(z) {i+1}. héten érte el a célt")
        cel_elerte = True
        break

if not cel_elerte:
    print("Sajnos Mari néni nem érte el a célját.")

# 4. feladat
novekvo_hetek_szama = 0
for i in range(1, n):
    if tomeg[i] > tomeg[i-1]:
        novekvo_hetek_szama += 1

print(f"A tömege {novekvo_hetek_szama} esetben nőtt egyik hétről a másikra.")
