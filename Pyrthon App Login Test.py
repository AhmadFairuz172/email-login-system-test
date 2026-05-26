def app_login():

    from email_validation import email_valid  #mengurangkan ruang func
    import time
    percubaan = 0
    max_percubaan = 3

    print('Selamat datang ke aplikasi ini.Sila masukkan akaun emel dan kata laluan')
    
    while True:
        
        emel = input('\nEmel: ')
        kata_laluan = input('Kata Laluan: ')

        if email_valid(emel):
            print('Telah mendaftar masuk')
            return                                  #tutup semua command

        else:
            percubaan = percubaan + 1
            tinggal = max_percubaan - percubaan
            print(f'Salah!Anda ada {tinggal} percubaan lagi')#f tu bagi python baca fungsi tertentu dan tk baca macamtu je
                
            if percubaan == max_percubaan:
                print('\nMaaf.Ada tidsk boleh melog masuk.Sila cuba lagi selepas 60 saat')
                time.sleep(60)
                return

app_login()
        
                
     
