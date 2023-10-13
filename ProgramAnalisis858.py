ListAutoTP = []
sumKupon = 0

def transferPulsa():
    # Meminta nomor tujuan yang valid
    nomorValid = False
    while not nomorValid:
        print("Silakan Masukkan Nomor Tujuan Transfer Pulsa (Contoh: 081234567890):")
        nomorTujuan = input()
        if len(nomorTujuan) >= 10 and len(nomorTujuan) <= 13 and nomorTujuan[0:2] == "08": 
            nomorValid = True
        else:
            print("Nomor yang Anda Masukkan Salah.")

    # Meminta nominal pulsa yang valid
    nominalValid = False
    while not nominalValid:
        print("Silakan Masukkan Nominal Pulsa yang Akan Ditransfer (Min : Rp. 5000, Max : Rp. 1000000):")
        nominalPulsa = int(input())
        if nominalPulsa >= 5000 and nominalPulsa <= 1000000:
            nominalValid = True
        else:
            print("Nominal yang Anda Masukkan Salah.")

    print(f"Hati Hati Penipuan, Anda Akan Transfer Pulsa {nominalPulsa} Ke Nomor {nomorTujuan}")
    print("1. Ya")
    print("2. Back")
    print("3. Home")
    print("Silakan Masukkan Pilihan Anda:")
    pilihan = int(input())
    if pilihan == 1:
        print("Pulsa Berhasil Ditransfer")
        sumKupon += 1
        exit()
    elif pilihan == 2:
        transferPulsa()
    elif pilihan == 3:
        menu()
    else:
        print("Pilihan yang Anda Masukkan Salah.")

def mintaPulsa():
    # Meminta nomor tujuan yang valid
    nomorValid = False
    while not nomorValid:
        print("Silakan Masukkan Nomor Minta Pulsa (Contoh: 081234567890):")
        nomorTujuan = input()
        if len(nomorTujuan) >= 10 and len(nomorTujuan) <= 13 and nomorTujuan[0:2] == "08":
            nomorValid = True
        else:
            print("Nomor yang Anda Masukkan Salah.")

    # Meminta nominal pulsa yang valid
    nominalValid = False
    while not nominalValid:
        print("Silakan Masukkan Nominal Pulsa yang Akan Diminta (Min : Rp. 5000, Max : Rp. 1000000):")
        nominalPulsa = int(input())
        if nominalPulsa >= 5000 and nominalPulsa <= 1000000:
            nominalValid = True
        else:
            print("Nominal yang Anda Masukkan Salah.")

    print(f"Anda akan meminta pulsa sebesar {nominalPulsa} ke nomor {nomorTujuan}")
    print("1. Ya")
    print("2. Back")
    print("3. Home")
    print("Silakan Masukkan Pilihan Anda:")
    pilihan = int(input())
    if pilihan == 1:
        print("Pulsa Berhasil Diminta")
        sumKupon += 1
        exit()
    elif pilihan == 2:
        mintaPulsa()
    elif pilihan == 3:
        menu();
    else:
        print("Pilihan yang Anda Masukkan Salah.")    

def insertAutoTP():
    # Meminta nomor tujuan yang valid
    nomorValid = False
    while not nomorValid:
        print("Silakan Masukkan Nomor Tujuan Auto Transfer Pulsa (Contoh: 081234567890):")
        nomorTujuan = input()
        if len(nomorTujuan) >= 10 and len(nomorTujuan) <= 13 and nomorTujuan[0:2] == "08":
            nomorValid = True
        else:
            print("Nomor yang Anda Masukkan Salah.")

    # Meminta nominal pulsa yang valid
    nominalValid = False
    while not nominalValid:
        print("Silakan Masukkan Nominal Pulsa yang Akan Diminta (Min : Rp. 5000, Max : Rp. 1000000):")
        nominalPulsa = int(input())
        if nominalPulsa >= 5000 and nominalPulsa <= 1000000:
            nominalValid = True
            ListAutoTP.append(nomorTujuan)
        else:
            print("Nominal yang Anda Masukkan Salah.")

    tanggalValid = False
    while not tanggalValid:
        print("Silakan Masukkan Tanggal Auto Transfer Pulsa (Contoh: 1-31):")
        tanggal = int(input())
        if tanggal >= 1 and tanggal <= 31:
            tanggalValid = True
        else:
            print("Tanggal yang Anda Masukkan Salah.")

    print(f"Hati Hati Penipuan, Anda Akan Transfer Pulsa {nominalPulsa} Ke Nomor {nomorTujuan} Setiap Tanggal {tanggal}")
    print("1. Ya")
    print("2. Back")
    print("3. Home")
    print("Silakan Masukkan Pilihan Anda:")
    pilihan = int(input())
    if pilihan == 1:
        print("Auto Transfer Pulsa Berhasil Ditambahkan")
        sumKupon += 1
        exit()
    elif pilihan == 2:
        insertAutoTP()
    elif pilihan == 3:
        menu();
    else:
        print("Pilihan yang Anda Masukkan Salah.")

def deleteAutoTP():
    # Meminta nomor tujuan yang valid
    nomorValid = False
    while not nomorValid:
        print("Silakan Masukkan Nomor yang akan dihapus dari List Auto Transfer Pulsa (Contoh: 081234567890):")
        nomorTujuan = input()
        if len(nomorTujuan) >= 10 and len(nomorTujuan) <= 13 and nomorTujuan[0:2] == "08":
            for element in ListAutoTP:
                if element == nomorTujuan:
                    ListAutoTP.remove(nomorTujuan)
                    nomorValid = True
                else:
                    print("Nomor yang Anda Masukkan Tidak Ada di List Auto Transfer Pulsa.")
        if not nomorValid:
            print("Nomor yang Anda Masukkan Salah.")

    print(f"Anda akan menghapus nomor {nomorTujuan} dari List Auto Transfer Pulsa")
    print("1. Ya")
    print("2. Back")
    print("3. Home")
    print("Silakan Masukkan Pilihan Anda:")
    pilihan = int(input())
    if pilihan == 1:
        print("Nomor Berhasil Dihapus dari List Auto Transfer Pulsa")
        exit()
    elif pilihan == 2:
        deleteAutoTP()
    elif pilihan == 3:
        menu();
    else:
        print("Pilihan yang Anda Masukkan Salah.")   

def displayListAutoTP():
    print("List Auto Transfer Pulsa")
    for i, nomor in enumerate(ListAutoTP, start=1):
        print(f"{i}. {nomor}")
    print("====================================")

    print("1. Back")
    print("2. Home")
    print("Silakan Masukkan Pilihan Anda:")
    pilihan = int(input())
    if pilihan == 1:
        menu()
    elif pilihan == 2:
        menu();
    else:
        print("Pilihan yang Anda Masukkan Salah.")    

def cekKupon():
    print("Anda Memiliki", sumKupon, "Kupon")
    exit()

def displayMenu():
    print("Menu:")
    print("1. Transfer Pulsa")
    print("2. Minta Pulsa")
    print("3. Insert Auto Transfer Pulsa")
    print("4. Delete Auto Transfer Pulsa")
    print("5. Display List Auto Transfer Pulsa")
    print("6. Cek Kupon")
    print("7. Exit")


def menu():
    exit = False
    while not exit:
        displayMenu()
        print("Silakan Masukkan Pilihan Anda:")
        pilihan = int(input())
        if pilihan == 1:
            transferPulsa()
        elif pilihan == 2:
            mintaPulsa()
        elif pilihan == 3:
            insertAutoTP()
        elif pilihan == 4:
            deleteAutoTP()
        elif pilihan == 5:
            displayListAutoTP()
        elif pilihan == 6:
            cekKupon()
        elif pilihan == 7:
            exit = True
        else:
            print("Pilihan yang Anda Masukkan Salah")

if __name__ == "__main__":
    menu()
