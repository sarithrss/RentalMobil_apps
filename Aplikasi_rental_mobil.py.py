initial_menu_admin = """
    Selamat datang di Aplikasi Rental Mobil
         
    ======= MENU ADMIN =======
    1. Lihat Mobil
    2. Tambah Mobil
    3. Update Mobil
    4. Hapus Mobil 
    5. Lihat Mobil Nonaktif
    6. Aktifkan Mobil
    7. Exit
    """

initial_menu_cust = """
    Selamat datang di Aplikasi Rental Mobil

    ======= MENU CUSTOMER =======
    1. Lihat Mobil
    2. Sewa Mobil
    3. Update Rental
    4. Batalkan Rental
    5. Exit
    """

customers = []

data_transaksi = []

def cek_tanggal(tgl):
    if len(tgl) != 10:
        return False

    if tgl[2] != "-" or tgl[5] != "-":
        return False

    return True

initialData = [
   {
        'id_mobil': 1,
        'plat_nomor': 'B1234VRX',
        'merek': 'Brio',
        'tahun': 2020,
        'warna': 'kuning',
        'transmisi': 'matic',
        'kapasitas_penumpang': 4,
        'harga_sewa': 250000,
        'status': 'tersedia'
    },
    {
        'id_mobil': 2,
        'plat_nomor': 'B2780VRZ',
        'merek': 'Avanza',
        'tahun': 2025,
        'warna': 'hitam',
        'transmisi': 'manual',
        'kapasitas_penumpang': 6,
        'harga_sewa': 300000,
        'status': 'tersedia'
    },
    {
        'id_mobil': 3,
        'plat_nomor': 'B5372VBC',
        'merek': 'Baleno',
        'tahun': 2025,
        'warna': 'biru',
        'transmisi': 'matic',
        'kapasitas_penumpang': 4,
        'harga_sewa': 350000,
        'status': 'tersedia'
    },
    {
        'id_mobil': 4,
        'plat_nomor': 'B7810VFH',
        'merek': 'Raize',
        'tahun': 2025,
        'warna': 'putih',
        'transmisi': 'matic',
        'kapasitas_penumpang': 4,
        'harga_sewa': 350000,
        'status': 'nonaktif'
    },
    {
        'id_mobil': 5,
        'plat_nomor': 'B9123ABC',
        'merek': 'Innova',
        'tahun': 2024,
        'warna': 'silver',
        'transmisi': 'manual',
        'kapasitas_penumpang': 7,
        'harga_sewa': 450000,
        'status': 'tersedia'
    },
    {
        'id_mobil': 6,
        'plat_nomor': 'B4567DEF',
        'merek': 'Xpander',
        'tahun': 2023,
        'warna': 'abu-abu',
        'transmisi': 'matic',
        'kapasitas_penumpang': 7,
        'harga_sewa': 425000,
        'status': 'nonaktif'
    },
    {
        'id_mobil': 7,
        'plat_nomor': 'B8901GHI',
        'merek': 'Rush',
        'tahun': 2022,
        'warna': 'merah',
        'transmisi': 'manual',
        'kapasitas_penumpang': 7,
        'harga_sewa': 400000,
        'status': 'tersedia'
    },
    {
        'id_mobil': 8,
        'plat_nomor': 'B2345JKL',
        'merek': 'Agya',
        'tahun': 2024,
        'warna': 'oranye',
        'transmisi': 'matic',
        'kapasitas_penumpang': 4,
        'harga_sewa': 225000,
        'status': 'tersedia'
    },
    {
        'id_mobil': 9,
        'plat_nomor': 'B6789MNO',
        'merek': 'Fortuner',
        'tahun': 2025,
        'warna': 'hitam',
        'transmisi': 'matic',
        'kapasitas_penumpang': 7,
        'harga_sewa': 750000,
        'status': 'nonaktif'
    },
    {
        'id_mobil': 10,
        'plat_nomor': 'B3456PQR',
        'merek': 'Jazz',
        'tahun': 2021,
        'warna': 'putih',
        'transmisi': 'manual',
        'kapasitas_penumpang': 5,
        'harga_sewa': 275000,
        'status': 'tersedia'
    }
]

# MENU ADMIN

def tampilkan_mobil(data):

    print(
        f"{'ID':<3} | "
        f"{'Plat Nomor':<12} | "
        f"{'Merek':<10} | "
        f"{'Tahun':<5} | "
        f"{'Warna':<8} | "
        f"{'Transmisi':<10} | "
        f"{'Kapasitas':<9} | "
        f"{'Harga Sewa':<8} | "
        f"{'Status'}"
    )

    print("-" * 100)

    for car in data:
        print(
            f"{car['id_mobil']:<3} | "
            f"{car['plat_nomor']:<12} | "
            f"{car['merek']:<10} | "
            f"{car['tahun']:<5} | "
            f"{car['warna']:<8} | "
            f"{car['transmisi']:<10} | "
            f"{car['kapasitas_penumpang']:<9} | "
            f"Rp{car['harga_sewa']:,} | "
            f"{car['status']}"
        )
        

def admin_create():

    while True:
        merek = input('Masukkan merek mobil: ')
        plat = input('Masukkan plat nomor (contoh: B3790VRG): ')
        plat_input = plat.upper()
        sudah_ada = False

        for car in initialData:
            if car['plat_nomor'] == plat_input:
                print('Data Mobil sudah tersedia!')
                sudah_ada = True
                break
            else:
                sudah_ada = False

        if sudah_ada:
            print('Silakan input ulang Plat Mobil!')
        else:
            while True:
                tahun = input('Masukkan tahun mobil: ')
                if tahun.isdigit():
                    break  
                else:
                    print('Masukkan Tahun dengan value number!')

            while True:
                warna = input('Masukkan warna mobil: ')  
                if warna.isdigit():
                    print('Input tidak valid! Warna tidak boleh berupa angka.')
                if not warna.isdigit():
                    break

            while True:
                transmisi = input('Masukkan transmisi mobil (manual/matic): ')
                if transmisi.lower().strip() == 'manual':
                    break
                elif transmisi.lower().strip() == 'matic':
                    break
                else:
                    print('Tidak valid!')   

            while True:
                kapasitas_penumpang = input('Masukkan kapasitas penumpang: ')
                if kapasitas_penumpang.isdigit():
                    break
                else:
                    print('Masukkan kapasitas dengan value number!')

            while True:
                harga_sewa = input('Masukkan harga sewa: ')
                if harga_sewa.isdigit():        
                    break
                else:
                    print('Masukan harga sewa dengan value number!') 
                

            while True:
                submit = input('Apakah data ingin disimpan? (Y/N): ')

                 # ID Baru
                new_id = max(car['id_mobil'] for car in initialData) + 1

                if submit.lower() == 'y':
                    new_car = {
                    'id_mobil': new_id,
                    'plat_nomor': plat_input,
                    'merek': merek.capitalize(),
                    'tahun': int(tahun),
                    'warna': warna.lower(),
                    'transmisi': transmisi.lower(),
                    'kapasitas_penumpang': int(kapasitas_penumpang),
                    'harga_sewa': int(harga_sewa),
                    'status': 'tersedia'
                }
            
                    initialData.append(new_car)
                    print('Data Mobil Baru sudah di simpan\n')
                    tampilkan_mobil(initialData)
                    return True
                
                elif submit.lower() == 'n':
                    print('Penyimpanan dibatalkan.')
                    return True
                else:
                    print('Input tidak valid. Silakan masukkan Y atau N.')   


def admin_update():

    while True:

        tampilkan_mobil(initialData)
        id_update = int(input('Masukkan ID Mobil: '))
        mobil = None

        for car in initialData:
            if car['id_mobil'] == id_update:
                mobil = car
                break

        if mobil is None:
            print('Mobil tidak ditemukan!')
            continue
        break
    

    while True:

        print("""
                Pilih menu yang ingin diupdate:
                1. Plat Nomor
                2. Merek
                3. Tahun
                4. Warna
                5. Transmisi
                6. Kapasitas Penumpang
                7. Harga Sewa
                """)

        update_menu = input('Pilih menu: ')

        if update_menu == '1':

            while True:
                plat_baru = input('Masukkan plat nomor baru: ').strip().upper()
                if not plat_baru:
                    print('Data tidak boleh kosong!')
                    continue
                
                plat_ada = False
                for car in initialData:
                    if car['plat_nomor'].lower() == plat_baru.lower():
                        plat_ada = True
                        break
                if plat_ada:
                    print('Data sudah tersedia!')
                else:
                    while True: 
                        submit = input('Apakah data ingin disimpan? (Y/N): ').strip().lower()

                        if submit.lower() == 'y':
                            mobil['plat_nomor'] = plat_baru
                            print('Data berhasil diupdate.')
                            tampilkan_mobil([mobil])
                            return 
                        elif submit.lower() == 'n':
                            print('Penyimpanan dibatalkan.')
                            return 
                        else:
                            print('Input tidak valid. Silakan masukkan Y atau N.') 

        elif update_menu == '2':

            while True:
                merek_baru = input('Masukkan merek baru: ').strip().lower()
                if not merek_baru:
                    print('Data tidak boleh kosong!')
                    continue
                if merek_baru.isdigit():
                    print('Merek tidak boleh berupa angka!')
                    continue
                if merek_baru == mobil['merek'].lower():
                    print('Tidak ada perubahan data.')
                    return
                
                while True: 
                    submit = input('Apakah data ingin disimpan? (Y/N): ').strip().lower()

                    if submit.lower() == 'y':
                        mobil['merek'] = merek_baru.capitalize()
                        print('Data berhasil diupdate.')
                        tampilkan_mobil([mobil])
                        return True
                    elif submit.lower() == 'n':
                        print('Penyimpanan dibatalkan.')
                        return True
                    else:
                        print('Input tidak valid. Silakkan masukkan Y atau N.')

        elif update_menu == '3':

            while True:
                tahun_baru = input('Masukkan tahun baru: ').strip()

                if not tahun_baru:
                    print('Tahun tidak boleh kosong!')
                    continue
                if not tahun_baru.isdigit():
                    print('Tahun harus dengan value number!')
                    continue

                tahun_baru = int(tahun_baru)

                if tahun_baru < 2015:
                    print('Tahun tidak boleh dibawah tahun 2015!')
                    continue
                elif tahun_baru > 2026:
                    print('Tahun tidak boleh melebihi tahun saat ini!')
                    continue

                while True:
                    submit = input('Apakah data ingin disimpan? (Y/N): ').strip().lower()

                    if submit.lower() == 'y':
                        mobil['tahun'] = tahun_baru
                        print('Merek berhasil diupdate.')
                        tampilkan_mobil([mobil])
                        return
                    elif submit.lower() == 'n':
                        print('Penyimpanan dibatalkan.')
                        return
                    else:
                        print('Input tidak valid. Silakan masukkan Y atau N.') 
    
        elif update_menu == '4':
            
            while True:
                warna_baru = input('Masukkan warna baru: ').lower()
                if not warna_baru:
                    print('Warna tidak boleh kosong!')
                    continue
                if warna_baru.isdigit():
                    print('Warna tidak boleh berupa angka!')
                    continue
                if warna_baru == mobil['warna'].lower():
                    print('Tidak ada perubahan data.')
                    return
            
                while True:
                    submit = input('Apakah data ingin disimpan? (Y/N): ').strip().lower()
                    
                    if submit.lower() == 'y':
                        mobil['warna'] = warna_baru
                        print('Data berhasil diupdate.')
                        tampilkan_mobil([mobil])
                        return 
                    elif submit.lower() == 'n':
                        print('Penyimpanan dibatalkan.')
                        return 
                    else:
                        print('Input tidak valid. Silakan masukkan Y atau N.') 

        elif update_menu == '5':
            
            while True:
                transmisi_baru = input('Masukkan transmisi baru: ').strip().lower()

                if not transmisi_baru:
                    print('Transmisi tidak boleh kosong!')
                    continue
                if transmisi_baru not in ['manual', 'matic']:
                    print('Tidak valid. Masukan transmisi kembali!')
                    continue

                if mobil['transmisi'].lower() == transmisi_baru:
                    print('Tidak ada perubahan data.')
                    return
    
                while True:
                    submit = input('Apakah data ingin disimpan? (Y/N): ').strip().lower()
                    
                    if submit.lower() == 'y':
                        mobil['transmisi'] = transmisi_baru
                        print('Transmisi berhasil diupdate.')
                        tampilkan_mobil([mobil])
                        return 
                    elif submit.lower() == 'n':
                        print('Penyimpanan dibatalkan.')
                        return 
                    else:
                        print('Input tidak valid. Silakan masukkan Y atau N.') 

        elif update_menu == '6':

            while True:
                kapasitas_baru = input('Masukkan kapasitas baru: ').strip()

                if not kapasitas_baru:
                    print('Kapasitas tidak boleh kosong!')
                    continue
                if not kapasitas_baru.isdigit():
                    print('Kapasitas harus dengan value number!')
                    continue

                kapasitas_baru = int(kapasitas_baru)

                if kapasitas_baru <= 0:
                    print('Kapasitas tidak boleh 0!')
                    continue
                
                while True:
                    submit = input('Apakah data ingin disimpan? (Y/N): ').strip().lower()

                    if submit.lower() == 'y':
                        mobil['kapasitas_penumpang'] = kapasitas_baru
                        print('Kapasitas berhasil diupdate.')
                        tampilkan_mobil([mobil])
                        return
                    elif submit.lower() == 'n':
                        print('Penyimpanan dibatalkan.')
                        return
                    else:
                        print('Input tidak valid. Silakan masukkan Y atau N.') 

        elif update_menu == '7':

            while True:
                harga_baru = input('Masukkan harga sewa baru: ').strip()

                if not harga_baru:
                    print('Harga tidak boleh kosong!')
                    continue
                if not harga_baru.isdigit():
                    print('Harga harus dengan value number!')
                    continue

                harga_baru = int(harga_baru)

                if harga_baru <= 0:
                    print('Tidak valid! Silakan input kembali harga sewa.')
                    continue

                while True:
                    submit = input('Apakah data ingin disimpan? (Y/N): ').strip().lower()

                    if submit.lower() == 'y':
                        mobil['harga_sewa'] = harga_baru
                        print('Harga sewa berhasil diupdate.')
                        tampilkan_mobil([mobil])
                        return 
                    elif submit.lower() == 'n':
                        print('Penyimpanan dibatalkan.')
                        return
                    else:
                        print('Input tidak valid. Silakan masukkan Y atau N.') 
        else:
            print('Menu tidak valid!')
        
                 
def admin_delete():

    tampilkan_mobil(initialData)

    while True:
        id_delete = int(input('Masukkan ID Mobil: '))
        mobil = None


        for car in initialData:
            if car['id_mobil'] == id_delete:
                mobil = car
                break

        if mobil is None:
            print('Data mobil tidak ditemukan.')
            continue

        status = mobil.get('status', '').lower()

        if status == 'booked':
            print('Mobil sedang disewa dan tidak dapat dinonaktifkan.')
            return False

        elif status == 'nonaktif':
            print("Mobil sudah dinonaktifkan.")
            return False

        elif status == 'tersedia':

            print("Data mobil ditemukan")
            tampilkan_mobil([mobil])

            while True:
                submit = input('Apakah data ingin dinonaktifkan? (Y/N): ').strip().lower()

                if submit == 'y':
                    mobil['status'] = 'nonaktif'
                    aktif_mobil = [
                        car for car in initialData
                        if car['status'].lower() != 'nonaktif'
                    ]
                    print('\nMobil berhasil dinonaktifkan')
                    print('Daftar mobil aktif:')

                    tampilkan_mobil(aktif_mobil)

                    return True

                elif submit == 'n':
                    print('Penghapusan dibatalkan.')
                    return False

                else:
                    print('Input tidak valid. Silakan masukkan Y atau N.')


def admin_mobil_nonaktif():

    data_nonaktif = [
        car for car in initialData
        if car['status'].lower() == 'nonaktif'
    ]

    if not data_nonaktif:
        print('Tidak ada mobil nonaktif.')
        return

    tampilkan_mobil(data_nonaktif)
    return data_nonaktif


def admin_aktifkan_mobil():

    nonaktif_mobil = admin_mobil_nonaktif()

    if not nonaktif_mobil:
        print('Tidak ada mobil nonaktif.')
        return

    id_mobil =  int(input('Masukkan ID Mobil: '))

    mobil = None

    for car in initialData:
        if car['id_mobil'] == id_mobil:
            mobil = car
            break

    if mobil is None:
        print('Data mobil tidak ditemukan.')
        return

    while True:
        
        submit = input('Aktifkan kembali mobil? (Y/N): ').strip()

        if submit.lower() == 'y':
            mobil['status'] = 'Tersedia'
            print('Mobil berhasil di aktifkan kembali.')
            tampilkan_mobil([mobil])
            return
        elif submit.lower() == 'n':
            print('Pengaktifan mobil dibatalkan.')
            return
        else:
            print('Input tidak valid. Silakan masukkan Y atau N.')



# MENU CUSTOMER

def register_customer():
    print('\n=== REGISTER CUSTOMER ===')

    # NAMA
    while True:
        nama = input('Input nama: ')
        if nama == '':
            print("Nama tidak boleh kosong!")
        else:
            break

    # JENIS KELAMIN
    while True:
        jk = input('Input jenis kelamin (P/L): ').upper()
        if jk == 'P' or jk == 'L':
            break
        else:
            print('Tidak valid. Silakan masukkan P atau L!')

    # TANGGAL LAHIR
    while True:
        tgl = input('Input tanggal lahir (DD-MM-YYYY): ')

        if tgl == '':
            print('Tanggal lahir tidak boleh kosong!')
        elif cek_tanggal(tgl) == False:
            print('Format harus DD-MM-YYYY!')
        else:
            break

    # USERNAME
    while True:
        username = input('Input username: ')

        if username == '':
            print('Username tidak boleh kosong!')
            continue

        sudah_ada = False

        for c in customers:
            if c['username'] == username:
                sudah_ada = True

        if sudah_ada:
            print('Username sudah dipakai!')
        else:
            break

    # BUAT ID
    customer_id = len(customers) + 1

    # SIMPAN DATA
    customer = {
        'customer_id': customer_id,
        'nama': nama,
        'jenis_kelamin': jk,
        'tanggal_lahir': tgl,
        'username': username
    }

    customers.append(customer)

    print("\nRegistrasi berhasil!")
    print("Customer ID kamu:", customer_id)

    return customer_id


def customer_read():

    print('\nDaftar Mobil Tersedia')

    print(
        f"{'ID':<3} | "
        f"{'Plat Nomor':<12} | "
        f"{'Merek':<10} | "
        f"{'Tahun':<5} | "
        f"{'Warna':<8} | "
        f"{'Transmisi':<10} | "
        f"{'Kapasitas':<9} | "
        f"{'Harga Sewa':<10} | "
        f"{'Status'}"
    )

    print("-" * 100)

    for car in initialData:
        if car['status'] == 'tersedia':
            print(
                f"{car['id_mobil']:<3} | "
                f"{car['plat_nomor']:<12} | "
                f"{car['merek']:<10} | "
                f"{car['tahun']:<5} | "
                f"{car['warna']:<8} | "
                f"{car['transmisi']:<10} | "
                f"{car['kapasitas_penumpang']:<9} | "
                f"Rp{car['harga_sewa']:,} | "
                f"{car['status']}"
            )

def customer_create():

    while True:
        merek = input('Masukkan merek mobil: ').strip()
        mobil_ada = None

        for car in initialData:
            if car['merek'].lower() == merek.lower():
                print('Mobil tersedia.')
                mobil_ada = car
                mobil_ada['merek'] = merek.capitalize()
                tampilkan_mobil([mobil_ada])
        if mobil_ada is None:
            print('Mobil tidak ditemukan.')
            continue
        break
    
    while True:

        submit = input('Apakah Anda ingin menyewa mobil tersebut? (Y/N): ')

        if submit.lower() == 'y':
            transmisi = input('Masukkan transmisi (manual/matic): ')

            if not transmisi:
                print('Input tidak boleh kosong!')
                continue

            mobil_transmisi = []
                
            for car in initialData:
                if(car['merek'].lower() == merek.lower()
                   and car['transmisi'].lower() == transmisi):
                    mobil_transmisi.append(car)

            if len(mobil_transmisi) == 0:
                print('Mobil tidak tersedia dengan transmisi tersebut!')
                continue


            warna_tersedia = []

            for car in mobil_transmisi:
                if car['warna'] not in warna_tersedia:
                    warna_tersedia.append(car['warna'])

            print("Warna tersedia:")
            for warna in warna_tersedia:
                print("-", warna)

            while True:
                warna = input('Masukkan warna: ').strip().lower()

                if not warna:
                    print('Input warna tidak boleh kosong!')
                    continue

                mobil = None

                for car in mobil_transmisi:
                    if car['warna'].lower() == warna:
                        mobil = car
                        break

                if mobil is None:
                    print('Warna tidak tersedia.')
                    continue

                break


            status = input('Apakah semua sudah sesuai? (Y/N): ')

            if submit.lower() == 'y':

                    while True:
                        lama_sewa = input('Masukan berapa hari lama sewa: ').strip()
                        if not lama_sewa:
                            print('Data tidak boleh kosong! Silakan input kembali.')
                            continue
                        if not lama_sewa.isdigit():
                            print('Data harus dengan value number!')
                            continue
                        if len(data_transaksi) == 0:
                            id_transaksi = 1
                        else:
                            id_transaksi = data_transaksi[-1][id_transaksi] + 1

                        transaksi_baru = {
                            'id_transaksi' : id_transaksi,
                            'id_mobil' : mobil['id_mobil'],
                            'lama_sewa' : int(lama_sewa)
                        }

                        data_transaksi.append(transaksi_baru)
                        mobil['status'] = 'Booked'
                        print('Mobil berhasil dibooked.')
                        tampilkan_mobil([mobil])
                        print(f'ID Transaksi Anda adalah: {id_transaksi}')
                        return
        
            elif submit.lower() == 'n':
                print('Batal melakukan booking.')
                return
            else:
                print('Input tidak valid. Silakan masukkan Y atau N.')

        elif submit.lower() == 'n':
            print('Dibatalkan.')
            return
        else:
            print('Input tidak valid. Silakan masukkan Y atau N.')


def customer_update():

    while True:

        customer_id = input('Masukan customer ID: ')

        if not customer_id:
            print('ID customer tidak boleh kosong! Silakan input kembali.')
            continue

        if not customer_id.isdigit():
            print('ID harus dengan value number!')
            continue
        
        break

    customer_id = int(customer_id)

    customer = None

    for c in customers:
        if c['customer_id'] == customer_id:
            customer = c
            break
    if customer is None:
        print('Data tidak ditemukan!')
        return
    else:
        print('customer')
        print(customer)


    while True:

        id_transaksi = input('Masukan transaksi ID: ')

        if not id_transaksi:
            print('ID transaksi tidak boleh kosong! Silakan input kembali.')
            continue

        if not id_transaksi.isdigit():
            print('ID harus dengan value number!')
            continue
        
        id_transaksi = int(id_transaksi)

        ada = False

        for t in data_transaksi:
            if t['id_transaksi'] == id_transaksi:
                ada = True
                transaksi = t
                print(transaksi)
                break
        
        if ada == False:
            print('ID transaksi tidak ditemukan!')
            return
    
        while True:
            
            update_sewa = input('Apakah ingin update sewa? (Y/N): ')

            if update_sewa.lower() == 'y':
                
                while True:
                    sewa_hari = input('Masukkan lama hari sewa: ')
                    if not sewa_hari:
                        print('Data tidak boleh kosong!')
                        continue
                    if not sewa_hari.isdigit():
                        print('Data harus dengan value number!')
                        continue

                    sewa_hari = int(sewa_hari)

                    if t['lama_sewa'] == sewa_hari:
                        print('Tidak ada perubahan data!')
                        return

                    break
                
                while True:
                    submit = input('Apakah data ingin disimpan? (Y/N): ').strip().lower()

                    if submit == 'y':

                        transaksi['lama_sewa'] = sewa_hari

                        print('Data berhasil disimpan.')
                        print(transaksi)
                        return
                    elif submit == 'n':
                        print('Update dibatalkan.')
                        return
                    else:
                        print('Input tidak valid. Silakan masukkan Y atau N.')

            elif update_sewa.lower() == 'n':
                print('Update dibatalkan.')
                return
            else:
                print('Input tidak valid. Silakan masukkan Y atau N.')


def customer_cancel():

    while True:

        customer_id = input('Masukkan customer ID: ').strip()

        if not customer_id:
            print('ID customer tidak boleh kosong! Silakan input kembali.')
            continue

        if not customer_id.isdigit():
            print('ID customer harus dengan value number!')
            continue

        customer_id = int(customer_id)
        break


    customer = None

    for c in customers:
        if c['customer_id'] == customer_id:
            customer = c
            break

    if customer is None:
        print('Data customer tidak ditemukan!')
        return

    print('Customer ditemukan:', customer)


    while True:

        id_transaksi = input('Masukkan transaksi ID: ').strip()

        if not id_transaksi:
            print('ID transaksi tidak boleh kosong! Silakan input kembali.')
            continue

        if not id_transaksi.isdigit():
            print('ID transaksi harus dengan value number!')
            continue

        id_transaksi = int(id_transaksi)

        transaksi = None

        for t in data_transaksi:
            if t['id_transaksi'] == id_transaksi:
                transaksi = t
                break

        if transaksi is None:
            print("Transaksi tidak ditemukan!")
            return

        break


    while True:

        batal = input('Apakah ingin membatalkan transaksi? (Y/N): ').strip().lower()

        if batal == 'y':
            for car in initialData:
                if car['id_mobil'] == transaksi['id_mobil']:
                    car['status'] = 'tersedia'
                    break

            data_transaksi.remove(transaksi)

            print('Transaksi berhasil dibatalkan.')
            return

        elif batal == 'n':
            print('Pembatalan dibatalkan.')
            return

        else:
            print('Input tidak valid. Silakan masukkan Y atau N.')



def admin():
    pick_menu = ""
    print(initial_menu_admin)  
    pick_menu = input("Pilih menu: ")

    if pick_menu == '1':
        print('Data Mobil Saat ini :\n')
        tampilkan_mobil(initialData)
    elif pick_menu == '2':
        admin_create()
    elif pick_menu == '3':
        admin_update()
    elif pick_menu == '4':
        admin_delete()
    elif pick_menu == '5':
        admin_mobil_nonaktif()
    elif pick_menu == '6':
        admin_aktifkan_mobil()
    elif pick_menu == '7':
        print('Terima kasih telah menggunakan aplikasi rental mobil.')
        exit()
    else:
        print('Menu tidak tersedia, silakan input kembali.')

def customer():

    customer_login = None

    if customer_login is None:
        print('Silakan register:')
        customer_login = register_customer()


    while True: 

        pick_menu = ""
        print(initial_menu_cust)
        pick_menu = input('Pilih menu: ')

        if pick_menu == '1':    
            customer_read()
        elif pick_menu == '2':
            customer_create()
        elif pick_menu == '3':
            customer_update()
        elif pick_menu == '4':
            customer_cancel()
        elif pick_menu == '5':
            print('Terima kasih telah menggunakan aplikasi rental mobil.')
            exit()
        else:
            print('Menu tidak tersedia, silakan input kembali.')


def run_application():
    
    while True: 
        user = ''
        user = input('Masukkan username (admin/customer): ')

        if user.lower() == 'admin':
            while True:
                admin()
        elif user.lower() == 'customer':
            while True:
                customer()

run_application()