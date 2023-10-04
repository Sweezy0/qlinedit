import sys
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
verdana_font=QFont("verdana",15)
class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLine Edit Kullanımı")
        self.setGeometry(400,100,600,400)
        self.arayuz()
    def arayuz(self):
        self.yazi=QLabel("Merhaba Python",self)
        self.yazi.setFont(verdana_font)
        self.yazi.move(200,50)
        self.yazi.resize(300,200)

        self.isim_kutusu=QLineEdit(self)
        self.isim_kutusu.move(200,100)
        self.isim_kutusu.setPlaceholderText("Lütfen İsminizi girin:")

        self.sifre_kutusu=QLineEdit(self)
        self.sifre_kutusu.move(200,150)
        self.sifre_kutusu.setPlaceholderText("Lütfen şifreenizi girin:")
        self.sifre_kutusu.setEchoMode(QLineEdit.Password)

        self.buton_kaydet=QPushButton("Kaydet",self)
        self.buton_kaydet.setFont(verdana_font)
        self.buton_kaydet.move(200,300)
        self.buton_kaydet.clicked.connect(self.fonksiyon_kaydet)

        self.show()
    def fonksiyon_kaydet(self):
        isim=self.isim_kutusu.text()
        sifre=self.sifre_kutusu.text()
        self.yazi.setText(f"Hoşgeldiniz {isim}")
    
uygulama=QApplication(sys.argv)
pencere=Pencere()
sys.exit(uygulama.exec())