print("\nPROGRAM KONVERSI SUHU\n")

celcius = float(input("masukkan suhu dalam celcius = "))
print("\nsuhu adalah",celcius,"celcius")

# celcius > reamur

reamur = (4/5) * celcius
print("\nsuhu dalam reamur adalah = ",reamur,"reamur")

# celcius > fahrenheit

fahrenheit = ((9/5) * celcius) + 32
print("\nsuhu dalam fahrenheit adalah = ",fahrenheit,"fahrenheit")

# celcius > kelvin

kelvin = celcius + 273
print("\nsuhu dalam kelvin adalah : ",kelvin,"kelvin")


reamur1 = float(input("\n\nmasukkan suhu dalam reamur = "))
print("\nsuhu adalah",reamur1,"reamur")


# reamur > celcius

celcius1 = (5/4) * reamur1 
print("\nsuhu dalam celcius adalah : ",celcius1,"celcius")

# reamur > fahrenheit

celcius1 = ((9/4) * reamur1) + 32
print("\nsuhu dalam fahrenheit adalah : ",celcius1,"fahrenheit")

# reamur > kelvin

celcius1 = ((5/4) * reamur1 * 273) 
print("\nsuhu dalam kelvin adalah : ",celcius1,"kelvin")