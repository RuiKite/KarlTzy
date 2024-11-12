#step 1: import modules
#pyqt5 -> buat app
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

#PIL -> python image library
from PIL import ImageFilter
from PIL.ImageFilter import *
from PIL import Image
from PIL.Image import *

#upload folder
import os #operation system

#step 2: bikin app
#screen
width = 500
height = 500
app = QApplication([])
screen = QWidget()
screen.resize(width,height) #ganti ukuran
screen.setWindowTitle("Photo Editor Panda") #ganti sesuaiin kalian

#label image -> nampung imagenya
lb_image = QLabel("Image")
#list files photo
list_files = QListWidget()
#btn
#upload
btn_upload = QPushButton("upload a folder")
#filter
#bnw, puter kanan, puter kiri, flip, mirror, sharp, blur
#minimal 5
btn_bnw = QPushButton("Black n White")
btn_kanan = QPushButton("Putar Kanan")
btn_kiri = QPushButton("Putar Kiri")
btn_flip = QPushButton("Flip")
btn_mirror = QPushButton("Mirror")
btn_sharp = QPushButton("Sharp")
btn_blur = QPushButton("Blur")

#step 3: pembuatan layout -> penempatan
main_layout = QHBoxLayout()
#kolom 1
kolom1 = QVBoxLayout()
'''#kalau mau btn folder dibawah
kolom1.addWidget(list_files)
kolom1.addWidget(btn_upload)

#kalau mau btn folder diatas
kolom1.addWidget(btn_upload)
kolom1.addWidget(list_files)'''
kolom1.addWidget(list_files)
kolom1.addWidget(btn_upload)
#kolom 2
#terdapat btn2 filter
#harus buat layout khusus btn filter
layout_btn = QHBoxLayout()
layout_btn.addWidget(btn_kiri)
layout_btn.addWidget(btn_kanan)
layout_btn.addWidget(btn_bnw)
layout_btn.addWidget(btn_flip)
layout_btn.addWidget(btn_blur)
layout_btn.addWidget(btn_mirror)
layout_btn.addWidget(btn_sharp)

kolom2 = QVBoxLayout()

#btn filter diatas
kolom2.addWidget(layout_btn)
kolom2.addWidget(lb_image, 95) #95% layar dari kolom 2

'''
#btn filter dibawah
kolom2.addWidget(lb_image, 95) #95% layar dari kolom 2
kolom2.addWidget(layout_btn)'''

#set kolom 1 & 2 kedalam main layout
main_layout.addLayout(kolom1, 25) #kolom 1 akan memenuhi 25% dari 1 keseluruhan layar
main_layout.addLayout(kolom2, 75) #kolom 2 akan memenuhi 75% dari 1 keseluruhan layar

#set ke dalam screen
screen.setLayout(main_layout)
#tampilin
screen.show()

workdir = ''
#fungsi upload folder
def chooseworkdir():
    global workdir
    #ambil path dari folder yg mau di upload
    workdir = QFileDialog.getExistingDirectory()
#fungsi untuk filter format file
def filter(files, ekstension):
    #semua file di dalam folder harus ditaruh ke dalam 1 list
    result = list()
    #untuk setiap filename yang ada di dalam folder files
    for filename in files:
        #cek dulu ekstension format nya apa aja
        for ext in ekstension:
            if filename.endswith(ext): #filename nya bagian akhir sesuai dgn format
                result.append(filename)
    return result
#fungsi untuk tampilin hasil file filter ke dalam tampilan app
def showfilenamelist():
    #list ekstension format
    ekstension = ['.jpg','.png','.pdf','.jpeg','.pnp']
    #upload folder
    chooseworkdir()
    #filter mana aja file2 yg sesuai dgn format ekstension
    files = os.listdir(workdir) #kita ambil path folder yg diupload
    filenames = filter(files, ekstension)
    #di app, list file nya harus di kosong
    list_files.clear()
    #untuk setiap filename, harus di tampilin
    for filename in filenames:
        list_files.addItem(filename)

#step 5: pembuatan kelas / mesin image editor
class imageprocessor():
    #karakteristik
    def __init__(self):
        self.filename = None #karena filenamenya belum ada
        self.dir = None #karena folder yg diupload belom ada
        self.image = None #karena image (gambar) nya belum ada
        self.save_dir = 'Modified/' #kita akan buat folder modified u/ simpen photo edit
    #method
    def loadImage(self, filename, dir):
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir,filename) #cari tau path dari photo tsb
        #upload image
        self.image = Image.open(image_path)

        def showimage(self):
        lb_image.hide() #hide dulu gambar sebelumnya
        pixmapimage = QPixmap(path) #gunanya untuk samain width, height, ratio, dll
                                    #dari photo aslinya
        w, h = lb_image.width(), lb_image.height() #photo akan di sesuaikan dgn
                                                    #ukuran tempat tampilan
        pixmapimage = pixmapimage.scaled(w,h,Qt.KeepAspectRatio)
        #set ke dalam lb image -> untuk ditampilin
        lb_image.setPixmap(pixmapimage)
        #tampilin
        lb_image.show()