from tkinter import *
from tkinter import messagebox

pencere = Tk()
pencere.title("Hesap Makinesi")
pencere.configure(background="cyan")
pencere.resizable(width="False", height="False")
pencere.geometry(f"500x180")

def temizle():
    birinci_sayi.delete(0, END)
    ikinci_sayi.delete(0, END)
    sonuç_etk.config(text="Sonuç :")

def topla():
   veri1 = birinci_sayi.get()
   veri2 = ikinci_sayi.get()
   sayı1 = int(veri1)
   sayı2 = int(veri2)

   sonuç = sayı1 + sayı2
   sonuç_etk["text"] = "Sonuç : " + str(sonuç)

def çıkar():
   veri1 = birinci_sayi.get()
   veri2 = ikinci_sayi.get()
   sayı1 = int(veri1)
   sayı2 = int(veri2)

   sonuç = sayı1 - sayı2
   sonuç_etk["text"] = "Sonuç : " + str(sonuç)

def çarp():
   veri1 = birinci_sayi.get()
   veri2 = ikinci_sayi.get()
   sayı1 = int(veri1)
   sayı2 = int(veri2)

   sonuç = sayı1 * sayı2
   sonuç_etk["text"] = "Sonuç : " + str(sonuç)

def böl():
   veri1 = birinci_sayi.get()
   veri2 = ikinci_sayi.get()
   sayı1 = int(veri1)
   sayı2 = int(veri2)

   sonuç = sayı1 / sayı2
   sonuç_etk["text"] = "Sonuç : " + str(sonuç)

l1 = Label(text="Birinci Sayı :")
l1.place(x=10, y=30)
l2 = Label(text="İkinci Sayı :")
l2.place(x=12, y=56)
birinci_sayi = Entry(text="Birinci sayı")
birinci_sayi.place(x=100, y=30)
ikinci_sayi = Entry(text="İkinci sayı")
ikinci_sayi.place(x=100, y=56)
topla_butonu = Button(text="Topla", fg="red", command=topla)
topla_butonu.place(x=12, y=90)
çıkar_butonu = Button(text="Çıkar ", fg="green", command=çıkar)
çıkar_butonu.place(x=60, y=90)
böl_butonu = Button(text="Böl", fg="blue", command=böl)
böl_butonu.place(x=110, y=90)
çarp_butonu = Button(text="Çarp", fg="purple", command=çarp)
çarp_butonu.place(x=145, y=90)
temizle_butonu = Button(text="Temizle", fg="gray", command=temizle)
temizle_butonu.place(x=189, y=90)
sonuç_etk = Label(text="Sonuç :")
sonuç_etk.place(x=280, y=45)
yapımcı_yazı = Label(text="Yapımcı : İlker Sezer")
yapımcı_yazı.place(x=380, y=150)


pencere.mainloop()
