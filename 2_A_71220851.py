def cetakHuruf(str):
    strkalimat = len(str)
    if strkalimat % 2 == 0 :
        return str [0] + str [1] + str[2] + "dan" + str [-3] + str [-2] + str [-1]
    else:
        tengah = int(strkalimat/2) 
        return str[tengah - 1] + str[tengah] + str[tengah+1]

awal = input("Masukan kata : ")
out = cetakHuruf(awal)
print("Huruf yang diambil pada kata", awal, "adalah", out)


