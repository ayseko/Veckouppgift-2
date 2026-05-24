print("Ange tre tal")
tal_1 = int(input("Tal 1 : "))
tal_2 = int(input("Tal 2 : "))
tal_3 = int(input("Tal 3 : "))

summa = tal_1 + tal_2 + tal_3
print("Summa : " + str(summa))

if tal_1 == tal_2 == tal_3:
    print("Alla tre tal är lika")
    print("Det finns inget mellersta tal.")
else:
# Största talet
    if tal_1 >= tal_2 and tal_1 >= tal_3:
        print("Största talet : " + str(tal_1))
    elif tal_2 >= tal_1 and tal_2 >= tal_3:
        print("Största talet : " + str(tal_2))
    else:
        print("Största talet : " + str(tal_3))

# Minta talet
    if tal_1 <= tal_2 and tal_1 <= tal_3:
        print("Minsta talet : " + str(tal_1))
    elif tal_2 <= tal_1 and tal_2 <= tal_3:
        print("Minsta talet : " + str(tal_2))
    else:
        print("Minsta talet : " + str(tal_3))


    if tal_1 == tal_2 or tal_1 == tal_3 or tal_2 == tal_3:
        print("Två av talen är lika")
        print("Det finns inget mellersta tal.")
    elif (tal_2 < tal_1 < tal_3) or (tal_3 < tal_1 < tal_2):
        print("Mellerta talet : " +str(tal_1))
    elif (tal_1 < tal_2 < tal_3) or (tal_3 < tal_2 < tal_1):
        print("Mellerta talet : " +str(tal_2))
    else:
        print("Mellerta talet : " +str(tal_3))
