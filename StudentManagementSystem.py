print("******  Student Management System  ******")

name = "Oguzhan"
surname ="Dogan"
tries = 3
courselist = []
choosencourse = []
exam = []

while tries>0:
    name1 = input("Lütfen adınızı giriniz")
    surname1 = input("Lütfen soyadınızı giriniz.")

    if (name != name1 and surname == surname1):
        print("Adınız hatalı! Kontrol edip tekrar giriniz")
        tries -= 1
        print(f'You have {tries} tries left')
    elif (name ==name1 and surname != surname1):
        print("Soyadınız hatalı! Kontrol edip tekrar giriniz")
        tries -= 1
        print(f'You have {tries} tries left')
    elif (name != name1 and surname!= surname1):
        print("Kullanıcı adınız ve parolanız hatalıdır.")
        tries -= 1
        print(f'You have {tries} tries left')
    else:
        print("Welcome",name1,surname1)
        tries = 0
for i in range(0,5):       
    course = input("Alınması gereken dersleri giriniz")
    courselist.append(course)
print(courselist)

while len(choosencourse) >= 0:
    chosen = input("Almak istediğiniz dersleri giriniz:")
    choosencourse.append(chosen)
    cont = input("Başka ders almak istiyor musunuz? Y/N:")
    if cont.upper() == "Y":
        continue
    elif cont.upper() == "N":  
        break      

if len(choosencourse) < 3:
    print("En az 3 adet ders almalısınız!!")
elif len(choosencourse) >= 3:
    print("Dersleriniz başarı ile eklendi.")

examcourse = input("Sınav notlarını gireceğiniz dersi seçiniz:")
midterm = int(input(f'{examcourse} dersine ait Midterm notunu giriniz:'))
final = int(input(f'{examcourse} dersine ait Final notunu giriniz:'))
project = int(input(f'{examcourse} dersine ait Proje notunu giriniz:'))
grade = midterm*30/100 + final*50/100 + project*20/100
if grade <= 30:
    print(f'{examcourse} dersine ait harf notunuz FF geçme notunuz ise {grade}')
elif 30 < grade <= 50:
    print(f'{examcourse} dersine ait harf notunuz DD geçme notunuz ise {grade}')
elif 50 < grade <= 70:
    print(f'{examcourse} dersine ait harf notunuz CC geçme notunuz ise {grade}')
elif 70 < grade <= 90:
    print(f'{examcourse} dersine ait harf notunuz BB geçme notunuz ise {grade}')
elif grade >= 90:
    print(f'{examcourse} dersine ait harf notunuz AA geçme notunuz ise {grade}')
