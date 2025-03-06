import os

class Diary:
    def __init__(self, filename="diary.txt"):

        # Dosya adını ve yolunu belirler. Yoksa ekler.
        diary_dir = os.path.dirname(os.path.abspath(__file__))
        if not os.path.exists(diary_dir):
            os.makedirs(diary_dir)
        self.filename = os.path.join(diary_dir, filename)

    def add_note(self, note):
        # Girilen notu dosyaya ekler.
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(note + "\n")

    def view_notes(self):
        # Dosyadaki tüm notları okur ve döndürür.
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            return "Kayıt dosyası bulunamadı."

    def delete_notes(self):
        # Dosyayı siler.
        try:
            os.remove(self.filename)
            return "Dosya silindi."
        except FileNotFoundError:
            return "Dosya zaten mevcut değil."
