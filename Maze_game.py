"BIKIN APP MAZE MEME SEA"

#step 1: import module

from pygame import*
init() #core

#step 2: define parameter
#screen:
width = 780
height = 780

#ukuran karakter
Player_width = 50
Player_height = 50

Fruit_width = 50
Fruit_height = 50

Meme_width = 50
Meme_height = 50

#kecepatan karakter
Player_speed = 7
Meme_speed = 6

warna_tembok = (255, 0, 0)
warna_merah = (255, 0, 0)

#step 3: buat class karakter
class karakter(sprite.Sprite): #sprite.sprite artinya install semua fungsi2 sprite di pygame. kyk: collision, klik char/tidak, dll

    #karakteristik dari char yg kita buat
    def __init__(self, player_image, x, y, width, height, speed):
        #install dari parent class
        super().__init__()
        
        #upload image karakter
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = speed

        #buat frame buat karakter
        self.rect = self.image.get_rect()

        #lokasiin frame char ke dalam x dan y
        self.rect.x = x
        self.rect.y = y

    #fungsi untuk tampilin char ke layar
    def show(self):
        #window adalah nama variabel screen.jadi
        screen.blit(self.image  , (self.rect.x, self.rect.y))

#step 4: bikin class buat main char 
class player(karakter): #kelas player adalah anak class dari katakter

    #control player
    def control(self):

        #untuk tau key apa yg kita tekan
        keys = key.get_pressed()

        if keys[K_a] and self.rect.x > 5: #kalo keyboard a
            self.rect.x -= self.speed

        if keys[K_d] and self.rect.x < width: #kalo keyboard d
            self.rect.x += self.speed

        if keys[K_w] and self.rect.y > 5: #kalo keyboard w (kalo di pygame yang ke atas Y nya -)
            self.rect.y -= self.speed

        if keys[K_s] and self.rect.y < height: #kalo keyboard s  (kalo di pygame yang ke bawah Y nya +)
            self.rect.y += self.speed

#step 5: buat class enemy gerak otomatis
class enemy(karakter):
    def automatic_move(self):
        #cek apakah enemy di batasan atas

        if self.rect.y > 5:
            #jika enemy di atas nanti kebawah
            self.gerak = "down"

        if self.rect.y < height:
            #jika enemy di bawah nanti keatas
            self.gerak = "up"

        #cek jika betul gerakan = atas/bawah
        if self.gerak == 'down':
            self.rect.y += self.speed
        else: 
            self.rect.y -= self.speed

def move_towards_player(self, Player, speed):
        dx, dy = self.rect.x - Player.rect.x, self.rect.y - Player.rect.y
        dist = m.hypot(dx, dy)
        dx, dy = dx/dist, dy/dist
        self.rect.x -= dx * speed
        self.rect.y-= dy*speed
#step 6: buat dinding
class dinding():
    #karakteristik dinding
    def __init__(self, x, y, width, height, warna):
        #cara bikin persegi
        self.rect = Rect(x,y,width,height)
        self.warna = warna

    #method dinding
    def show(self):
        draw.rect(screen, self.warna, self.rect)

    #method dinding untuk kena dinding/ngga
    def nabrak(self, karakter_lain):
        return self.rect.colliderect(karakter_lain)

#step 7: bikin screennya
screen = display.set_mode((width, height))

#step 8: karna bg nya foto, di upload dulu

bg_image = transform.scale(image.load('Background.jpeg'), (width, height))

#step 9: taruh bg image ke screen
screen.blit(bg_image,(0,0))
Mc_width = 50
Mc_height = 50
Mc_speed = 8

Npc_width = 50
Npc_height = 50
Npc_speed = 6

Item_width = 50
Item_height = 50
Item_speed = 0
#step 10: upload karakter2
Mc = player('Player.png', 100, 200, Mc_width, Mc_height, Mc_speed)
Npc = enemy('Meme.png', 100, 100, Npc_width, Npc_height, Npc_speed)
Item = karakter('Fruit.png', 680, 660, Item_width, Item_height, 0)

#karakter dinding
dinding1 = dinding(0, 0, 20, 780, warna_tembok)
dinding2 = dinding(180, 0, 600, 20, warna_tembok)
dinding3 = dinding(760, 0, 20, 600, warna_tembok)
dinding4 = dinding(0, 760, 780, 20, warna_tembok)
dinding5 = dinding(180, 0, 20, 380, warna_tembok)
dinding6 = dinding(180, 380, 300, 20, warna_tembok)
dinding7 = dinding(180, 600, 450, 20, warna_tembok)
dinding8 = dinding(610, 210, 20, 400, warna_tembok)
dinding9 = dinding(320, 190, 310, 20, warna_tembok)
dinding_hilang1 = dinding(630, 600, 200, 20, warna_merah)
dinding_hilang2 = dinding(630,610, 20, 200, warna_merah)

#step 11: buat flag
game_start = True

#step 12: buat fps
fps = time.Clock()

#step 13: buat loop gamenya
while game_start:
    screen.blit(bg_image,(0,0))
    Mc.show()
    Npc.show()
    Item.show()
    dinding1.show()
    dinding2.show()
    dinding3.show()
    dinding4.show()
    dinding5.show()
    dinding6.show()
    dinding7.show()
    dinding8.show()
    dinding9.show()

    #deteksi event = apa aja yg terjadi pas kita mainin gamenya. contoh pas kita pencet x, nanti keluar
    for e in event.get():
        #jika event = pencet tombol x
        if e.type == QUIT:
            game_start = False
    if dinding1.nabrak(Mc) or dinding2.nabrak(Mc) or dinding3.nabrak(Mc) or dinding4.nabrak(Mc) or dinding5.nabrak(Mc) or dinding6.nabrak(Mc) or dinding7.nabrak(Mc) or dinding8.nabrak(Mc) or dinding9.nabrak(Mc):
        Mc.rect.x = 100
        Mc.rect.y = 100
    Mc.control()
    display.update()

    #set fps
    fps.tick(60)