# list = []

# 1 - misol

# banan_narxi = 30000
# new_banan = 0
# for i in range(1,11):
#     new_banan += banan_narxi

# print(banan_narxi)

# 2 - misol

# yog_narxi = 15000
# new_yog = 0
# for i in range(1, 6):
#     new_yog += yog_narxi

# print(new_yog)

# 3 misol
# toglar = 0
# for i in range(1, 50):
#     if i % 2 == 1:
#         print(i)
#         toglar += i

# print(toglar)

# 4 - misol
# juft = 0
# for i in range(1, 100):
#     if i % 2 == 0:
#         juft += i

# print(juft)

# 5 - misol

# n = int(input("N soni: "))
# k = int(input("K soni: "))

# yigindi = 0
# nlist = []

# for i in range(1, n):
#     nlist.append(i)
#     yigindi += i

# if yigindi > k:
#     print(nlist[0])
# else:
#     print("K soni N soni yig'indisidan katta")


# 6 - misol

# n = int(input("N soni: "))
# k = int(input("K soni: "))
# yigindi = 0
# list = []
# for i in range(1, n + 1):
#     yigindi += i
#     list.append(i)

# if yigindi < k:
#     print(list[-1])
# else:
#     print("else")

# 7 - misol

# n = int(input("n ga teng: "))
# yigindi = 0
# for i in range(1, n):
#     yigindi += i * i

# print(yigindi)


# 8 - misol

# a = int(input("a: "))
# b = int(input("b: "))
# kopaytma = 1

# for i in range(a, b):
#     kopaytma = kopaytma * i


# print(kopaytma)


# 9 - misol

# n = int(input("n soni: "))
# m = int(input("m soni: "))

# for i in range(m - 1):
#     print(i * (f" {n}"))

# 10 - misol

# YO'Q

# 11 - misol

# a = int(input("a: "))
# b = int(input("b: "))
# butun = 0
# 23 - 7 = 16 (1) 16 - 7 = 9 (2) 9 - 7 = 2 (3)
# for i in range(100):
#     if a - b >= 0:
#         a -= b
#         butun += 1
#     else:
#         break

# print(butun)

# 12 - misol

# a = int(input("a: "))
# b = int(input("b: "))
# 23 - 7 = 16 (1) 16 - 7 = 9 (2) 9 - 7 = 2 (3)
# for i in range(100):
#     if a - b >= 0:
#         a -= b
#     else:
#         break

# print(a)

# 13 - misol

# listt = ["osh", "mastava", "chuchvara", "sho'rva", "kabob", "dimlama", "shashlik"]
# tanlangan = []
# enter = 3
# for i in range(enter):
#     a = input("Taom: ")
#     if a in listt:
#         tanlangan.append(a)
#     else:
#         print("bunday taom menyuda yoq")

# for index in range(enter):
#     print(f"{index + 1}.tanlangan taom {tanlangan[index]}")

# 14 - misol
# ism = input("ism: ")
# indexlar = []

# for i in range(len(ism)):
#     if i % 2 == 0:
#         indexlar.append("0")
#     else:
#         indexlar.append("1")

# result = " ".join(indexlar)
# print(result)

# 15 - misol

# matn = input("matn: ")
# length = 0
# for i in matn:
#     length += 1

# print(length)
