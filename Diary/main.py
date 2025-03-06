from diary import Diary

def main():
    diary = Diary()
    while True:
        komut = input("Not girin (komut: goruntule, sil, çıkış): ").strip().lower()
        if komut == "çıkış":
            break
        elif komut == "goruntule":
            notlar = diary.view_notes()
            print("Kayıtlı notlar:\n" + notlar)
        elif komut == "sil":
            sonuc = diary.delete_notes()
            print(sonuc)
        else:
            diary.add_note(komut)
            print("Not eklendi.")

if __name__ == "__main__":
    main()