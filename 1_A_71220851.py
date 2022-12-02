print ("======= Program Manipulasi String =======")
print ("Pilihan Menu:")
print ("1. Hitung Kata")
print ("2. Ubah Kata")
pilih = int(input("Pilihan Anda :"))
def ubahkata():
    a = input("Masukan sebuah kalimta/kata :")
    b = input("Masukan kata yang ingin di ubah :")
    c = input("Masukan kata pengganti :")
    ubah = a.replace(b,c)
    print ("String berhasil diubah menjadi :", ubah)
def hitungkata():
    d = input("Masukan sebuah kalimat/kata :")
    e = input("Masukan kata yang ingin dihitung :")
    hitung = d.count(e)
def bukansemua():
    f = input("Masukan sebuah kalimat/kata :")
    print ("Pilihan yang anda input tidak terdaftar di daftar pilihan")
if pilih == 1:
    (hitungkata())
elif pilih == 2:
    (ubahkata())
else:
    (bukansemua())
