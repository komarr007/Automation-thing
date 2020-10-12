import random

nomor_pilih=[' ' for x in range(10)]

tampungan=[]

def player():
    a = int(input("masukan angka: "))
    nomor_pilih[a]='X'
    tampungan.append(a)
    papan(a)

def komputer():
    kosong =[1,2,3,4,5,6,7,8,9]
    acak=random.choice(kosong)
    while acak in tampungan:
        acak=random.choice(kosong)
    if acak not in tampungan:
        acak
    nomor_pilih[acak]='O'
    papan(acak)

def papan(nomor):
    print('    |   |    ')
    print('  ' + nomor_pilih[1] + ' | ' + nomor_pilih[2] + ' | ' + nomor_pilih[3])
    print('    |   |    ')
    print('-------------')
    print('    |   |    ')
    print('  ' + nomor_pilih[4] + ' | ' + nomor_pilih[5] + ' | ' + nomor_pilih[6])
    print('    |   |    ')
    print('-------------')
    print('    |   |    ')
    print('  ' + nomor_pilih[7] + ' | ' + nomor_pilih[8] + ' | ' + nomor_pilih[9])
    print('    |   |    ')

player() #jalan pertama
print("komputer jalan")
komputer() #jalan pertama
print("player jalan")
player() #jalan kedua
print("komputer jalan")
komputer() #jalan kedua
print("player jalan")
player() #jalan ketiga
print("komputer jalan")
komputer() #jalan ketiga

if ((nomor_pilih[1] and nomor_pilih[2] and nomor_pilih[3]) or (nomor_pilih[4] and nomor_pilih[5] and nomor_pilih[6]) or (nomor_pilih[7] and nomor_pilih[8] and nomor_pilih[9]) or (nomor_pilih[1] and nomor_pilih[4] and nomor_pilih[7]) or (nomor_pilih[2] and nomor_pilih[5] and nomor_pilih[8]) or (nomor_pilih[3] and nomor_pilih[6] and nomor_pilih[9]) or (nomor_pilih[1] and nomor_pilih[5] and nomor_pilih[9]) or (nomor_pilih[3] and nomor_pilih[5] and nomor_pilih[7])) == 'X':
    print("menang bos")
elif ((nomor_pilih[1] and nomor_pilih[2] and nomor_pilih[3]) or (nomor_pilih[4] and nomor_pilih[5] and nomor_pilih[6]) or (nomor_pilih[7] and nomor_pilih[8] and nomor_pilih[9]) or (nomor_pilih[1] and nomor_pilih[4] and nomor_pilih[7]) or (nomor_pilih[2] and nomor_pilih[5] and nomor_pilih[8]) or (nomor_pilih[3] and nomor_pilih[6] and nomor_pilih[9]) or (nomor_pilih[1] and nomor_pilih[5] and nomor_pilih[9]) or (nomor_pilih[3] and nomor_pilih[5] and nomor_pilih[7])) == 'O':
    print("kalah bos")
else:
    print("seri bos")
