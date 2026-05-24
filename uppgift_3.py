print("Matchen är över, nu ska vi räkna ut resultatet!")
lag_1 = "Tottenham"
lag_2 = "Liverpool"
lag_1_mål = int(input("Hur många mål gjorde " + lag_1 + "? "))
lag_2_mål = int(input("Hur många mål gjorde " + lag_2 + "? "))
skillnad = abs(lag_1_mål - lag_2_mål)
if lag_1_mål < 0 or lag_2_mål < 0:
    print("Ange ett giltigt värde!")
elif lag_1_mål > lag_2_mål:
    print(lag_1 + " vann med " + str(skillnad) + " mål!")
elif lag_1_mål < lag_2_mål:
    print(lag_2 + " vann med " + str(skillnad) + " mål!")
else:
    print("Det blev oavgjort!")
