
import tkinter as tk
import random
import time

rastgele_sayi = random.randint(1, 100)
hak = 5
skor = 100
en_yuksek_skor = 0
tahmin_gecmisi = []
baslangic = time.time()


def tahmin_et():
    global hak, skor, en_yuksek_skor

    tahmin = entry_tahmin.get().strip()

    if tahmin == "":
        label_sonuc.config(text="Lütfen bir sayı giriniz.")
        return

    if not tahmin.isdigit():
        label_sonuc.config(text="Lütfen sadece sayı giriniz.")
        entry_tahmin.delete(0, tk.END)
        return

    tahmin = int(tahmin)

    if tahmin < 1 or tahmin > 100:
        label_sonuc.config(text="1 ile 100 arasında sayı giriniz.")
        entry_tahmin.delete(0, tk.END)
        return

    tahmin_gecmisi.append(tahmin)
    label_gecmis.config(
    text=f"Tahmin Geçmişi:\n{tahmin_gecmisi}"
)

    if tahmin == rastgele_sayi:
        gecen_sure = round(time.time() - baslangic, 2)

        if skor > en_yuksek_skor:
            en_yuksek_skor = skor
            label_rekor.config(text=f"🏆 Rekor : {en_yuksek_skor}")

        label_sonuc.config(
                    text=f"🎉 Tebrikler!\n"
                         f"Skor: {skor}\n"
                         f"Süre: {gecen_sure} sn"
                )
        
        btn_tahmin.config(state="disabled")
        entry_tahmin.config(state="disabled")

    else:
        hak -= 1
        skor = max(0, skor - 20)

        if tahmin < rastgele_sayi:
            label_sonuc.config(
    text="⬆️ Daha büyük bir sayı giriniz.",
    fg="blue"
)
        else:
            label_sonuc.config(
    text="⬇️ Daha küçük bir sayı giriniz.",
    fg="purple"
)

        label_hak.config(text=f"Kalan Hak : {hak}")
        label_skor.config(text=f"Skor : {skor}")

        if hak == 0:
            label_sonuc.config(
    text=f"❌ Oyun Bitti!\nDoğru Sayı: {rastgele_sayi}",
    fg="red"
)
            btn_tahmin.config(state="disabled")
            entry_tahmin.config(state="disabled")

    entry_tahmin.delete(0, tk.END)
    entry_tahmin.focus()
def sure_guncelle():

    gecen = int(time.time() - baslangic)

    label_sure.config(text=f"⏱ Süre : {gecen} sn")

    if btn_tahmin["state"] == "normal":
        root.after(1000, sure_guncelle)
def yeni_oyun():
    global rastgele_sayi, hak, skor, tahmin_gecmisi, baslangic

    rastgele_sayi = random.randint(1, 100)
    hak = 5
    skor = 100
    tahmin_gecmisi = []
    label_gecmis.config(text="Tahmin Geçmişi:\n[]")
    baslangic = time.time()
    sure_guncelle()

    label_hak.config(text=f"Kalan Hak : {hak}")
    label_skor.config(text=f"Skor : {skor}")
    label_sonuc.config(
    text="🎮 Yeni oyun başladı!",
    fg="black"
)

    entry_tahmin.config(state="normal")
    entry_tahmin.delete(0, tk.END)
    entry_tahmin.focus()

    btn_tahmin.config(state="normal")

root = tk.Tk()
root.configure(bg="#1E3A5F")
root.title("🎯 Sayı Tahmin Oyunu")
root.geometry("700x700")
genislik = 700
yukseklik = 700

ekran_genislik = root.winfo_screenwidth()
ekran_yukseklik = root.winfo_screenheight()

x = (ekran_genislik // 2) - (genislik // 2)
y = (ekran_yukseklik // 2) - (yukseklik // 2)

root.geometry(f"{genislik}x{yukseklik}+{x}+{y}")
root.resizable(False, False)

baslik = tk.Label(
    root,
    text="🎯 SAYI TAHMİN OYUNU",
    font=("Arial", 20, "bold")
)
baslik.pack(pady=20)

aciklama = tk.Label(
    root,
    text="1 ile 100 arasında tuttuğum sayıyı tahmin et.",
    font=("Segoe UI",20,"bold")
)
aciklama.pack()

entry_tahmin = tk.Entry(
    root,
    font=("Arial", 16),
    justify="center",
    width=15
)
entry_tahmin.pack(pady=20)
entry_tahmin.bind("<Return>", lambda event: tahmin_et())

label_hak = tk.Label(
    root,
    text=f"Kalan Hak : {hak}",
    font=("Segoe UI",11),
    bg="#1E3A5F",
    fg="white"
)
label_hak.pack()

label_skor = tk.Label(
    root,
    text=f"Skor : {skor}",
    font=("Segoe UI",11,"bold"),
    bg="#1E3A5F",
    fg="white"
)
label_skor.pack()

label_rekor = tk.Label(
    root,
    text=f"🏆 Rekor : {en_yuksek_skor}",
    font=("Arial", 12, "bold"),
    bg="#1E3A5F",
    fg="white"
)
label_rekor.pack()
label_sure = tk.Label(
    root,
    text="⏱ Süre : 0 sn",
    font=("Arial", 12),
    bg="#1E3A5F",
    fg="white"
)
label_sure.pack()
frame_sonuc = tk.Frame(
    root,
    bg="white",
    bd=2,
    relief="solid"
)
frame_sonuc.pack(
    pady=15,
    padx=20,
    fill="x",
    ipady=10
)

label_sonuc = tk.Label(
    frame_sonuc,
    text="Tahmininizi bekliyorum...",
    font=("Segoe UI", 11, "bold"),
    bg="white",
    fg="black",
    pady=10
)
label_sonuc.pack(fill="x")

label_gecmis = tk.Label(
    root,
    text="Tahmin Geçmişi:\n[]",
    font=("Arial", 11),
    justify="left",
    bg="#1E3A5F",
    fg="white"
)
label_gecmis.pack(pady=10)

btn_tahmin = tk.Button(
    root,
    text="Tahmin Et",
    font=("Arial", 12),
    width=18,
    command=tahmin_et
)
btn_tahmin.pack(pady=15)
btn_yeni = tk.Button(
    root,
    text="🔄 Yeni Oyun",
    font=("Arial", 12),
    width=18,
    command=yeni_oyun
)
btn_yeni.pack(pady=5)
sure_guncelle()
footer = tk.Label(
    root,
    text="Python • Tkinter • v2.3",
    font=("Segoe UI", 8),
    bg="#1E3A5F",
    fg="white"
)
footer.pack(side="bottom", pady=8)
root.mainloop()
