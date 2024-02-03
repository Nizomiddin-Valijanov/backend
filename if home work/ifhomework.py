# 1 - misol
# car = input("Mashinani kiriting: ")

# if car.lower() == "spark":
#     print("Brat spark urniga Jentra oling chunki u kotta bollani moshinasi")

# else:
#     print("Siz olmoqchi bulgan mashina", car)

# a = "SALOM"
# print(a.lower())

# 2 - misol
# a = input("A ga teng:")
# b = input("B ga teng:")

# if a > b:
#     print("A soni katta")
# elif a == b:
#     print("Sonlar teng")
# else:
#     print("B soni katta")


# 3 - misol
# list = [2, 12, 3, 34, 6]
# yig = int(input("Son: "))

# if sum(list) < yig:
#     print("men listdan kattaman")
# elif sum(list) == yig:
#     print("list menga teng")
# else:
#     print("list mendan katta")

# 4 - misol
# son = int(input("son kiriting: "))
# if son % 2 == 0:
#     son += 3
# else:
#     son -= 50
# print(son)

# 5 - misol
# a = int(input("a: "))
# b = int(input("b: "))
# musbat = 0
# if a > 0:
#     musbat += 1
# if b > 0:
#     musbat += 1
# print(musbat)

# 6 - misol
# son = input("son kiriting:")

# if son[0] == 8:
#     son = int(son) / 2
# else:
#     son = int(son) - 10
#     print("salom")
# print(son)

# 7 - misol
# a = int(input("A ga teng:"))
# b = int(input("B ga teng:"))

# if a < b:
#     print("A soni kichkina")
# elif a == b:
#     print("sonlar teng")
# else:
#     print("B soni kichkina")


# 8 - misol

# a = int(input("A ga teng:"))
# b = int(input("B ga teng:"))
# c = int(input("C ga teng:"))

# if a < b and a < c:
#     print("A soni kichik")
# elif b < a and b < c:
#     print("B soni kichik")
# elif c < a and c < b:
#     print("C soni kichik")

# else:
#     print("Sonlar har hil bulishi kerak")

# 9 misol
# a = int(input("A ga teng:"))
# b = int(input("B ga teng:"))
# c = int(input("C ga teng:"))
# if a > b and a > c:
#     print("A soni katta")
# elif b > a and b > c:
#     print("B soni katta")
# elif c > a and c > b:
#     print("C soni katta")
# else:
#     print("Sonlar har hil bulishi kerak emas")

# 10 - misol
# a = int(input("A ga teng:"))
# b = int(input("B ga teng:"))
# c = int(input("C ga teng:"))

# if a > b and a < c or a < b and a > c:
#     print("urta son a")
# elif b > a and b < c or b < a and b > c:
#     print("urta son b")
# elif c > a and c < b or c < a and c > b:
#     print("urta son c")
# else:
#     print("Togri son kiriting")


# 11 - misol
# uzunlik = int(input("Uzunlikni kiriting: "))
# Efel = 375

# if uzunlik > Efel:
#     print("efeldan kattaman")
# else:
#     print("efel mendan katta")

# 12 - misol

# avtobus = int(input("Abtobus: "))
# bilet = int(input("bilet: "))

# if avtobus > bilet:
#     print("Avtobus kuchligida")
# else:
#     print("shu raqamli avtobus Namanganga qatnaydi")

# 13 misol
# a = int(input("A ga teng:"))
# b = int(input("B ga teng:"))
# c = int(input("C ga teng:"))

# array = [a, b, c]
# print(array.sort(), array)
# if array == array.sort():
# print("Ushish tartibida")
# else:
# print("Ushish tartibida emas")
# if a < b < c:
#     print("Ushish tartibida")
# else:
#     print("Ushish tartibida emas")

# 14 - misol
# a = int(input("A ga teng:"))
# b = int(input("B ga teng:"))
# c = int(input("C ga teng:"))

# if a == b and b == c:
#     print(a, b, c)
# else:
#     print(a + b + c)

# 15 - misol
# ism1 = input("1 ism: ")
# ism2 = input("2 ism: ")


# if len(ism1) == len(ism2):
#     print("Biz tengmiz")
# elif len(ism1) > len(ism2):
#     print(f"{ism1} dan {ism2} uzunlikda katta")
# elif len(ism1) < len(ism2):
#     print(f"{ism2} dan {ism1} uzunlikda katta")


# 16 - misol
# a = int(input("A ga teng:"))

# if a // 2 == 0:
#     print("Juft son")
# else:
#     print("toq son")

# 17 - misol

# rang = input("rang: ")
# text = "qizil va katta sharlar ushlagan bir nechta kursdoshlarim bitiruv kechasida ularni yorishdi "

# if text.split()[0] != rang:
#     text.split()[0] = rang

# print(text)


# 18 - misol

# yil = int(input("yil kiriting: "))

# if yil % 4 != 0:
#     print("Kabisa")
# else:
#     print("kabisa emas")

# 19 - misol
# son = int(input("son kiriting: "))

# if son == 0:
#     print("Nolga teng")

# if son > 0 and son % 2 == 0:

# bobur chiqadigan avtobus nomeri 4 ga karrali bo'lsa, u uchun har dushanba yo'lkira tekin
# qolgan kunlari esa 2 barobar arzon. Qolgan nomerdagi avtobuslar faqat Juma kuni tekinga,
# qolgan kunlari 1.5 barobar qimmatga masofaga eltadi. Sizga avtobus nomeri va hafta kuni kiritilganda,
# yo'l kirani aniqlovchi dastur tuzing. kod tuzishdan oldin yo'l kirani 2000 deb oling.
# Avtobus misoli
# nomer = int(input("Abtobus nomeri: "))
# kun = input("Kun: ")
# kira = 2000
# if nomer % 4 == 0 and kun.lower() == "dushanba":
#     kira = kira // 2
# elif kun.lower() == "juma":
#     kira = 0
# else:
#     kira = kira * 1.5

# print(kira)n

# ismlar = ["Nizomiddin", "asdfasdf", "ASdfasdfasdf", "tolinjon",]
# array = []
# enterNum = 3
# for num in range(enterNum):
#     car = input("tachka:")
#     array.append(car)

# for index in range(enterNum):
#     print(f"{index + 1}.My car: {array[index]}")
