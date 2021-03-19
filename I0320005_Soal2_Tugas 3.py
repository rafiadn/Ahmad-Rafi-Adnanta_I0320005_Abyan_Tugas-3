#Data diri awal
dict = {
    'Nama': 'Ahmad Rafi Adnanta',
    'Hobi': {
        1: 'Bermain game',
        2: 'Sepakbola',
        3: 'Renang'
    },
    'Sosial media': {
        1: 'WA: 085156376753',
        2: 'IG: @rafi_adn',
        3: 'FB: Ahmad Rafi Adnanta'
    },
    'Lagu kesukaan': {
        1: 'December',
        2: 'Mean it',
        3: 'Dive'
    },
    'Makanan favorit': {
        1: 'Lasagna',
        2: 'Sate kambing',
        3: 'Fastfood'
    }
}
print("Data diri awal: ", dict)

#Mengubah salah satu hobi
dict['Hobi'] = {
        1: 'Bermain game',
        2: 'Sepakbola',
        3: 'Mendengarkan musik'
    }

# Mengubah salah satu sosmed
dict['Sosial media'] = {
        1: 'WA: 085156376753',
        2: 'IG: @rafi_adn',
        3: 'Tiktok: @.adnn'
    }

#Menghapus 2 makanan favorit
dict['Makanan favorit'] = {1: 'Lasagna'}

#Menambahkan 1 hobi
dict['Hobi'] = {
        1: 'Bermain game',
        2: 'Sepakbola',
        3: 'Mendengarkan musik',
        4: 'Nongkrong'
    }

# Data diri akhir
print('Data diri akhir: ', dict)