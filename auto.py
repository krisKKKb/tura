name = str(input("Mis on sinu nimi?: "))
x = name.capitalize()
print("Tere " + x)

location = str(input("Mis on sinu elukoht?: "))
y = location.capitalize()
if location == "Saaremaa" or location == "saaremaa":
    print(y + " on lahe koht")

age = int(input("Kui vana sa oled: "))
if age>18:
    print("Sa võid autoga sõita")
elif age == 18:
    print("Palju õnne täisealiseks saamise puhul")
else:
    print("Sa oled liiga noor et juhtida autot")

    
