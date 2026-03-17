Omborxona = {
    "Kompyuter":{"soni":357,"narxi":7500000},
    "Mouse":{"soni":300,"narxi":4000000},
    "Monitor":{"soni":250,"narxi":2500000},
    "Klaviatura":{"soni":570,"narxi":500000},
    "Laptop":{"soni":204,"narxi":6700000},
    "Iphone":{"soni":409,"narxi":15000000}
}

def mahsulot_topish(mahsulot_nomi):
    qidiruv = mahsulot_nomi.lower().strip()
    for mahsulot in Omborxona:
        if mahsulot.lower() == qidiruv:
            return mahsulot
    return None

def mahsulotlar_royxati():
    if not Omborxona:
        return "Omobrxona bo'sh"
    for mahsulot in Omborxona:
        print(f"{mahsulot}: {Omborxona[mahsulot]['soni']} dona qolgan (Narx: {Omborxona[mahsulot]['narxi']} so'm)")

def yangi_mahsulot_qoshish(mahsulot_nomi, soni, narx):
    mahsulot_nomi = mahsulot_nomi.strip().title()
    topilgan = mahsulot_topish(mahsulot_nomi)

    if topilgan:
        return f"{topilgan} - allaqachon mavjud"
    else:
        Omborxona[mahsulot_nomi] = {"soni":soni,"narxi":narx}
        return f"{mahsulot_nomi} - Omborga qo'shildi"

def mahsulot_chiqarish(mahsulot_nomi, miqdori):
    topilgan = mahsulot_topish(mahsulot_nomi)

    if topilgan:
        if Omborxona[topilgan]["soni"] >= miqdori:
            Omborxona[topilgan]["soni"] -= miqdori
            return f"{miqdori} dona {topilgan} sotildi. Qoldi: {Omborxona[topilgan]['soni']} dona"
        else:
            return f"Omborda faqat {Omborxona[topilgan]['soni']} dona bor"
    else:
        return "Bunday mahsulot mavjud emas"

def mahsulot_kiritish(mahsulot_nomi, miqdori):
    topilgan = mahsulot_topish(mahsulot_nomi)

    if topilgan:
        Omborxona[topilgan]["soni"] += miqdori
        return f"{miqdori} dona {topilgan} kiritildi. Jami: {Omborxona[topilgan]['soni']} dona"
    else:
        return "Bunday mahsulot mavjud emas"

def mahsulot_ochirish(mahsulot_nomi):
    topilgan = mahsulot_topish(mahsulot_nomi)

    if topilgan:
        del Omborxona[topilgan]
        return f"{topilgan} Ombordan o'chirildi"
    else:
        return "Bunday mahsulot mavjud emas"

def mahsulot_qidirish(mahsulot_nomi):
    topilgan = mahsulot_topish(mahsulot_nomi)

    if topilgan:
        return f"{topilgan}: {Omborxona[topilgan]['soni']} dona qolgan, Narxi: {Omborxona[topilgan]['narxi']:,} so'm"
    else:
        return "Bunday mahsulot mavjud emas"

def umumiy_qiymat():
    jami = 0
    for mahsulot in Omborxona:
        jami += Omborxona[mahsulot]['soni'] * Omborxona[mahsulot]['narxi']
    return f"Ombordagi mahsulotlarning umumiy qiymati {jami:,} so'm"

def menu():
    while True:
        print("""\n====== Omborxona boshqaruv tizimi ======
        
        1. Mahsulotlar ro'yxati
        2. Yangi mahsulot qo'shish
        3. Mahsulotni sotish
        4. Mahsulot kiritish
        5. Mahsulot o'chirish
        6. Mahsulot qidirish
        7. Ombordagi mahsulotlarning umumiy qiymati
        0. Chiqish
        """)

        tanlov = input("Tanlang:  ")

        if tanlov == "1":
            mahsulotlar_royxati()

        elif tanlov == "2":
            nomi = input("Mahsulot nomini kiriting :  ")
            soni = input("Miqdorini kiriting : ")
            narx = input("Mahsulot narxini kiriting :  ")

            if soni.isdigit() and narx.replace('.','',1).isdigit():
                soni = int(soni)
                narx = float(narx)
                print(yangi_mahsulot_qoshish(nomi, soni, narx))
            else:
                print("❌ Xato: Miqdor va narx son bo'lishi kerak!")

        elif tanlov == "3":
            nomi = input("Mahsulot nomini kiriting :  ")
            miqdori = input("Miqdorini kiriting : ")

            if miqdori.isdigit():
                miqdori = int(miqdori)
                print(mahsulot_chiqarish(nomi, miqdori))
            else:
                print("❌ Xato: Miqdor son bo'lishi kerak!")

        elif tanlov == "4":
            nomi = input("Mahsulot nomini kiriting :  ")
            miqdori = input("Miqdorini kiriting : ")

            if miqdori.isdigit():
                miqdori = int(miqdori)
                print(mahsulot_kiritish(nomi, miqdori))
            else:
                print("❌ Xato: Miqdor son bo'lishi kerak!")

        elif tanlov == "5":
            nomi = input("Mahsulot nomini kiriting :  ")
            print(mahsulot_ochirish(nomi))

        elif tanlov == "6":
            nomi = input("Mahsulot nomini kiriting :  ")
            print(mahsulot_qidirish(nomi))

        elif tanlov == "7":
            print(umumiy_qiymat())

        elif tanlov == "0":
            print("Dastur yakunlandi !!!")
            break

        else:
             print("Noto'g'ri tanlov")

if __name__ == "__main__":
    menu()


