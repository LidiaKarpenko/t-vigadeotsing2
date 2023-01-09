print("*** Arvude mäng ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = abs(int(input("Sisestage täisarv => "))) #lõppus on lisanud sulg
    except ValueError:
         print("see ei ole paaris arv")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("nulliga pole mõnet midagi teha")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("määrame paaris ja paaritu numbruide arv")
    print()
    c=b=a
    paaris=0
    paaritu=0
    while b > 0:
         if b % 2 == 0:
             paaris += 1
         else:
             paaritu += 1
         b = b // 10
    print("paaris arvude kogus:",paaris)
    print("paaritu on:",paaritu)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("pöörame ümber sisestanud numbrit")
    print()
    b=0
    while a > 0:
        number = a % 10
        a = a // 10
        b = b * 10
        b += number
    print("ümberpööranud arv", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("kontrollime Sürakuse hüpotenuus") #lisasulgud eemaldatud
    if c % 2 == 0:
        print("с - ´paaris arv. Jagame 2.")
    else:
        print("с - paaritu arv. Korrutame 3, liidame 1 ja jagame 2.")
    while c != 1:
            if c % 2 == 0:
                    c = c / 2
            else:
                    c = (3*c + 1) / 2
            print(round(c), end=" ") #algudes lisanud jutumärkid
    print()
    print("Hüpotees om õige") #parandatud jutumärkidega
