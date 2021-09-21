class BangunDatar :
    SegitigaSamaKakiTerbalik = None
    JajarGenjang = None

BD = BangunDatar()
SegitigaSamaKakiTerbalik = None
JajarGenjang = None

rows = 5

for i in range(rows + 1, 0, -1):
    #nested reverse loop
    for j in range(0, i - 1):
        #display star
        print("*", end= "")
    print ()

print ("JAJAR GENJANG")
n = int (input("Masukkan n: "))
i = 1
a = n
while (i<=n):
    print (" "*(n-1), "*" * a)
    n = n-1