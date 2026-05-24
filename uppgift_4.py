fråga = input("Vill du ange temperatur i Celsius eller Fahrenheit? (C/F): ").upper()
if fråga == "C":
    input_celsius = float(input("Skriv in en temperatur i grader Celsius:"))
    fahrenheit = (input_celsius * 1.8) + 32
    print("Det blir " + str(fahrenheit) + " grader Fahrenheit.")

    if input_celsius < 10:
        print("Ta på dig vinterkläder!")

    elif input_celsius >= 20:
        print("Packa badkläder :)")

elif fråga == "F":
    input_fahrenheit = float(input("Skriv in en temperatur i grader Fahrenheit:"))
    celsius = (input_fahrenheit - 32) / 1.8
    print("Det blir " + str(celsius) + " grader Celsius.")
    if celsius < 10:
        print("Ta på dig vinterkläder!")
    elif celsius >= 20:
        print("Packa badkläder :)")
else:
    print("Ange \"F\" eller \"C\"")
