
# Bu fonksiyon öğrenci eklemeyi sağlar program çalıştığında.
def add_student():
    print("Öğrenci isimlerini girin (Bitirmek için 'bitti' yazın):")

    while True:
        name = input("Öğrenci adı ya da bitti yazarak programı sonlandırabilirsiniz: ")
        if name.lower() == "bitti":
            break
        if name.isalpha():
            with open("student.txt", "a") as file:
                file.write(name + "\n")
                print(f"{name} isimli öğrenci eklendi.")
        else:
            print("Lütfen sadece harfler kullanarak isim girin.")

    print("Öğrenci kayıt işlemi tamamlandı.")

# Bu fonksiyon öğrenci listesini gösterir.
def show_student():
    try:
        # Dosyayı aç ve r ile oku.
        with open("student.txt", "r") as file:
            print("\nKayıtlı Öğrenciler:")
            print("-" * 20)

            # Dosyada öğrenci var mı kontrol eder. False ise yoktur. True ise vardır. True ise öğrencileri görürüz. False ise kayıt yok der.
            has_students = False
            for index, line in enumerate(file, 1):
                print(f"{index}. {line.strip()}")
                has_students = True

            if not has_students:
                print("Dosyada kayıtlı öğrenci bulunmamaktadır.")

    except FileNotFoundError:
        print("Henüz öğrenci kaydı yapılmamış.")


# Programı çalıştırdığımızda sırayla fonksiyonlar çalışır.
if __name__ == "__main__":
    add_student()
    show_student()
