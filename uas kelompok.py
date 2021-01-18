from tkinter import *
from tkinter.ttk import Combobox
import time
from math import cos,sin,pi
import pygame

class MyClock():
    def __init__(self, main_window):
        self.size=300
        self.parent=main_window

        self.frameAlarm=Frame(main_window)
        self.frameJam = Frame(main_window)

        self.alarmHidup = False
        self.teksJam = StringVar()
        self.hidupMati = BooleanVar(False)
        self.fileMusik = 'balebale.mpeg'

        self.teksTombol = StringVar(value='set')

        self.buatFrameJam()
        self.buatJarum()
        self.buatTeksAngka()
        self.teks()
        self.buatTombol()
        self.buatComboBox()
        self.update_clock()

    def teks(self):
        self.teks = Label(text="Kelompok GG Gaming Gaes.py", font="Helvetica 12 bold")
        self.teks.pack()

    def buatFrameJam(self):
        main_window.title("Clock")
        self.w = Canvas(self.frameJam,width=320, height=320, relief= "sunken", border=10)
        self.w.pack()
        self.frameJam.pack()


    def buatJarum(self):
        self.w.create_line(0, 0, 0, 0, fill="red", tags="hour", width=3)
        self.w.create_line(0, 0, 0, 0, fill="black", tags="minute", width=6)
        self.w.create_line(0, 0, 0, 0, fill="black", tags="second", width=6)

    def buatTeksAngka(self):
        Label(self.frameJam, text="12").place(x=160, y=13)
        Label(self.frameJam, text="11").place(x=80, y=28)
        Label(self.frameJam, text="10").place(x=31, y=90)
        Label(self.frameJam, text="9").place(x=11, y=157)
        Label(self.frameJam, text="8").place(x=31, y=230)
        Label(self.frameJam, text="7").place(x=80, y=285)
        Label(self.frameJam, text="6").place(x=160, y=303)
        Label(self.frameJam, text="5").place(x=240, y=285)
        Label(self.frameJam, text="4").place(x=291, y=230)
        Label(self.frameJam, text="3").place(x=310, y=157)
        Label(self.frameJam, text="2").place(x=291, y=90)
        Label(self.frameJam, text="1").place(x=240, y=28)

    def update_clock(self):
        s=time.localtime()[5]
        m=time.localtime()[4]
        h=time.localtime()[3]

        jam = time.strftime("%H", time.localtime())
        menit = time.strftime("%M", time.localtime())
        detik = time.strftime("%S", time.localtime())

        if jam==self.comboJam.get() and menit==self.comboMenit.get() and (detik=='00') and self.hidupMati :
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load(self.fileMusik)
            pygame.mixer.music.play()
            self.alarmHidup=True

        if self.alarmHidup and pygame.mixer.music.get_busy()==False :
            self.perintahSetAlarm()

        degrees = 6*s
        angle = degrees*pi*2/360
        ox = 165
        oy = 165
        x = ox + self.size*sin(angle)*0.45
        y = oy - self.size*cos(angle)*0.45
        self.w.coords("hour", (ox,oy,x,y))

        degrees1 = 6*m
        angle1 = degrees1*pi*2/360
        ox1 = 165
        oy1 = 165
        x1 = ox1 + self.size*sin(angle1)*0.4
        y1 = oy1 - self.size*cos(angle1)*0.4
        self.w.coords("minute", (ox1,oy1,x1,y1))

        degrees2 = 30*h
        angle2 = degrees2*pi*2/360
        ox2 = 165
        oy2 = 165
        x2 = ox2 + self.size*sin(angle2)*0.2
        y2 = oy2 - self.size*cos(angle2)*0.2
        self.w.coords("second",(ox2,oy2,x2,y2))

        self.parent.after(1000, self.update_clock)

    def buatComboBox(self):
        Label(self.frameAlarm, text='Jam : ').grid(row=0, column=0)
        self.alarmJam = StringVar()
        self.comboJam = Combobox(self.frameAlarm, textvariable=self.alarmJam,
                                 state='readonly', width=2)
        self.comboJam['values'] = (
            '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15',
            '16', '17', '18', '19', '20', '21', '21', '22', '23', '24')
        self.comboJam.current(0)
        self.comboJam.grid(row=0, column=1)

        Label(self.frameAlarm, text='  Menit : ').grid(row=0, column=2)
        self.alarmMenit = StringVar()
        self.comboMenit = Combobox(self.frameAlarm, textvariable=self.alarmMenit,
                                   state='readonly', width=2)
        self.comboMenit['values'] = (
            '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15',
            '16', '17', '18', '19', '20', '21', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
            '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46',
            '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59')
        self.comboMenit.current(0)
        self.comboMenit.grid(row=0, column=3)

        self.frameAlarm.pack(pady=6)

    def buatTombol(self):
        self.tombolSet = Button(self.frameAlarm, textvariable=self.teksTombol, command=self.perintahSetAlarm).grid(
            row=0, column=4)

    def perintahSetAlarm(self):
        if self.teksTombol.get() == 'set':
            self.teksTombol.set('stop')
            self.hidupMati.set(True)
            self.teks.config(
                text='Alarm ready untuk getarkan telinga anda -> ' + self.comboJam.get() + ' : ' + self.comboMenit.get())
        else:
            self.hidupMati.set(False)
            self.teksTombol.set('set')
            self.alarmHidup=False
            try:
                pygame.mixer.music.stop()
            except:
                pass
            self.teks.config(text="Kelompok GG Gaming Gaes.py")

main_window = Tk()  
app = MyClock(main_window) 

mainloop() 
