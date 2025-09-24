def header():
    print(f"{"="*40 :^50}")
    print(f"{"INI ADALAH PROGRAM KALKULATOR" :^50}")
    print(f"{"="*40 :^50}")

def input_user(messange):
    num = int(input(f"masukkan angka {messange} : "))
    return num

def operator():
    oper = input("masukkan pilihan operator (+,-,*,/): ")
    return oper

def tambah(num1,num2):
    return num1+num2

def kurang(num1,num2):
    return num1-num2

def kali(num1,num2):
    return num1*num2

def bagi(num1,num2):
    return num1 / num2

while True:
    header()
    num1 = input_user("pertama")
    oper = operator()
    num2 = input_user("kedua")
    if oper == "+":
        hasil = tambah(num1,num2)
        print(f"hasil dari {num1} + {num2} = {hasil}")
    elif oper == "-":
        hasil = kurang(num1,num2)
        print(f"hasil dari {num1} - {num2} = {hasil}")
    elif oper == "*":
        hasil = kali(num1,num2)
        print(f"hasil dari {num1} * {num2} = {hasil}")
    elif oper == "/":
        if num2 == 0:
            print("cannot division by zero!!")
        else:
            hasil = bagi(num1,num2)
            print(f"hasil dari {num1} / {num2} = {hasil}")

    else:
        print('input tidak valid')
    
    lanjut = input("apakah ingin lanjut? (y/t): ")
    if lanjut == "t":
        break
    
print("program selesai, terima kasih")