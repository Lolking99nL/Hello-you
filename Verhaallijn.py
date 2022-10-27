print("Je zit op een bank en je hoort iets. Je loopt er naar toe en ziet een man hij heeft een mes bij zich\n")


print("A. Je rent naar buiten en belt de politie.")
print("B. Je gaat met hem vechten.")
print("C. Je rent in je kamer en verstop je.")

while True:
    vraag1 = input("Wat ga je doen?\n")

    if vraag1== "A":
     print("Je rent naar buiten en belt de politie.Je wacht drie minuten en gekomen en vertelt dat er iemand met een mes in je huis is. Ze gaan naar binnen en ge hebben hem gevonden en gearresteerd goede einde")
    elif vraag1== "B":
        print("Je gaat met hem vechten. Je geeft hem een paar klappen en je schopt hem maar ja hij heeft een mes en steek je een paar keer en je bent dood")
    elif vraag1=='C':
        print("Je gaat onder je bed vandaan en Je gaat met hem vechten.")
        break
    else:
        continue



    print("Je rent in je kamer en verstopt je onder je bed en hoort voet stappen. Je hoort het steeds dichterbij komen\n")


print("A. Je gaat onder je bed vandaan en Je gaat met hem vechten.")
print("B. Je gaat onder je bed vandaan en pakt iets en gooit iets naar hem.")
print("C. Je gaat onder je bed vandaan en rent naar buiten.")

while True:
    vraag1 = input("Wat ga je doen?\n")

    if vraag1== "A":
        print("Je rent naar buiten en belt de politie.")
    elif vraag1== "B":
        print("Je gaat met hem vechten.")
        break
    elif vraag1=='C':
        print("Je gaat onder je bed vandaan en Je gaat met hem vechten. Je geeft hem een paar klappen en je schopt hem maar ja hij heeft een mes en steek je een paar keer en je bent dood")
    else:
        continue


