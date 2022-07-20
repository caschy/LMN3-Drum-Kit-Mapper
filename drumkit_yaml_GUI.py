#from Tkinter import *  #for python2.7
from tkinter import * # for python > 3.4
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askstring
from tkinter.messagebox import askquestion
import os

user_in = ""
F3_filename = ""
FF3_filename = ""
G3_filename = ""
GG3_filename = ""
A3_filename = ""
AA3_filename = ""
B3_filename = ""
C4_filename = ""
CC4_filename = ""
D4_filename = ""
DD4_filename = ""
E4_filename = ""
F4_filename = ""
FF4_filename = ""
G4_filename = ""
GG4_filename = ""
A4_filename = ""
AA4_filename = ""
B4_filename = ""
C5_filename = ""
CC5_filename = ""
D5_filename = ""
DD5_filename = ""
E5_filename = ""

def note_F3():
	filetypes = (('wav files', '*.wav'),('All files', '*.*'))
	filename = fd.askopenfilename(title='Open a file',initialdir='/home/pi/.config/LMN-3/drum_kits/',filetypes=filetypes)
	showinfo(title='Selected File for F3-Midi 53',message=filename)
	global F3_filename
	F3_filename=filename

def note_FF3():
	filetypes = (('wav files', '*.wav'),('All files', '*.*'))
	filename = fd.askopenfilename(title='Open a file',initialdir='/home/pi/.config/LMN-3/drum_kits/',filetypes=filetypes)
	showinfo(title='Selected File for F#3-Midi 54',message=filename)
	global FF3_filename
	FF3_filename=filename

def note_G3():
	filetypes = (('wav files', '*.wav'),('All files', '*.*'))
	filename = fd.askopenfilename(title='Open a file',initialdir='/home/pi/.config/LMN-3/drum_kits/',filetypes=filetypes)
	showinfo(title='Selected File for G3-Midi 55',message=filename)
	global G3_filename
	G3_filename=filename

def note_GG3():
	filetypes = (('wav files', '*.wav'),('All files', '*.*'))
	filename = fd.askopenfilename(title='Open a file',initialdir='/home/pi/.config/LMN-3/drum_kits/',filetypes=filetypes)
	showinfo(title='Selected File for G#3-Midi 56',message=filename)
	global GG3_filename
	GG3_filename=filename

def note_A3():
	filetypes = (('wav files', '*.wav'),('All files', '*.*'))
	filename = fd.askopenfilename(title='Open a file',initialdir='/home/pi/.config/LMN-3/drum_kits/',filetypes=filetypes)
	showinfo(title='Selected File for A3-Midi 57',message=filename)
	global A3_filename
	A3_filename=filename

def note_AA3():
	filetypes = (('wav files', '*.wav'),('All files', '*.*'))
	filename = fd.askopenfilename(title='Open a file',initialdir='/home/pi/.config/LMN-3/drum_kits/',filetypes=filetypes)
	showinfo(title='Selected File for A#3-Midi 58',message=filename)
	global AA3_filename
	AA3_filename=filename

def note_B3():
	filetypes = (('wav files', '*.wav'),('All files', '*.*'))
	filename = fd.askopenfilename(title='Open a file',initialdir='/home/pi/.config/LMN-3/drum_kits/',filetypes=filetypes)
	showinfo(title='Selected File for B3-Midi 59',message=filename)
	global B3_filename
	B3_filename=filename

def note_C4():
	filetypes = (('wav files', '*.wav'),('All files', '*.*'))
	filename = fd.askopenfilename(title='Open a file',initialdir='/home/pi/.config/LMN-3/drum_kits/',filetypes=filetypes)
	showinfo(title='Selected File for C4-Midi 60',message=filename)
	global C4_filename
	C4_filename=filename

def note_CC4():
	filetypes = (('wav files', '*.wav'),('All files', '*.*'))
	filename = fd.askopenfilename(title='Open a file',initialdir='/home/pi/.config/LMN-3/drum_kits/',filetypes=filetypes)
	showinfo(title='Selected File for C#4-Midi 61',message=filename)
	global CC4_filename
	CC4_filename=filename

def note_D4():
	filetypes = (('wav files', '*.wav'),('All files', '*.*'))
	filename = fd.askopenfilename(title='Open a file',initialdir='/home/pi/.config/LMN-3/drum_kits/',filetypes=filetypes)
	showinfo(title='Selected File for D4-Midi 62',message=filename)
	global D4_filename
	D4_filename=filename
	
def note_DD4():
	filetypes = (('wav files', '*.wav'),('All files', '*.*'))
	filename = fd.askopenfilename(title='Open a file',initialdir='/home/pi/.config/LMN-3/drum_kits/',filetypes=filetypes)
	showinfo(title='Selected File for D#4-Midi 63',message=filename)
	global DD4_filename
	DD4_filename=filename

def note_E4():
	filetypes = (('wav files', '*.wav'),('All files', '*.*'))
	filename = fd.askopenfilename(title='Open a file',initialdir='/home/pi/.config/LMN-3/drum_kits/',filetypes=filetypes)
	showinfo(title='Selected File for E4-Midi 64',message=filename)
	global E4_filename
	E4_filename=filename

def note_F4():
	filetypes = (('wav files', '*.wav'),('All files', '*.*'))
	filename = fd.askopenfilename(title='Open a file',initialdir='/home/pi/.config/LMN-3/drum_kits/',filetypes=filetypes)
	showinfo(title='Selected File for F4-Midi 65',message=filename)
	global F4_filename
	F4_filename=filename

def note_FF4():
	filetypes = (('wav files', '*.wav'),('All files', '*.*'))
	filename = fd.askopenfilename(title='Open a file',initialdir='/home/pi/.config/LMN-3/drum_kits/',filetypes=filetypes)
	showinfo(title='Selected File for F#4-Midi 66',message=filename)
	global FF4_filename
	FF4_filename=filename

def note_G4():
	filetypes = (('wav files', '*.wav'),('All files', '*.*'))
	filename = fd.askopenfilename(title='Open a file',initialdir='/home/pi/.config/LMN-3/drum_kits/',filetypes=filetypes)
	showinfo(title='Selected File for G4-Midi 67',message=filename)
	global G4_filename
	G4_filename=filename

def note_GG4():
	filetypes = (('wav files', '*.wav'),('All files', '*.*'))
	filename = fd.askopenfilename(title='Open a file',initialdir='/home/pi/.config/LMN-3/drum_kits/',filetypes=filetypes)
	showinfo(title='Selected File for G#4-Midi 68',message=filename)
	global GG4_filename
	GG4_filename=filename

def note_A4():
	filetypes = (('wav files', '*.wav'),('All files', '*.*'))
	filename = fd.askopenfilename(title='Open a file',initialdir='/home/pi/.config/LMN-3/drum_kits/',filetypes=filetypes)
	showinfo(title='Selected File for A4-Midi 69',message=filename)
	global A4_filename
	A4_filename=filename

def note_AA4():
	filetypes = (('wav files', '*.wav'),('All files', '*.*'))
	filename = fd.askopenfilename(title='Open a file',initialdir='/home/pi/.config/LMN-3/drum_kits/',filetypes=filetypes)
	showinfo(title='Selected File for A#4-Midi 70',message=filename)
	global AA4_filename
	AA4_filename=filename

def note_B4():
	filetypes = (('wav files', '*.wav'),('All files', '*.*'))
	filename = fd.askopenfilename(title='Open a file',initialdir='/home/pi/.config/LMN-3/drum_kits/',filetypes=filetypes)
	showinfo(title='Selected File for B4-Midi 71',message=filename)
	global B4_filename
	B4_filename=filename

def note_C5():
	filetypes = (('wav files', '*.wav'),('All files', '*.*'))
	filename = fd.askopenfilename(title='Open a file',initialdir='/home/pi/.config/LMN-3/drum_kits/',filetypes=filetypes)
	showinfo(title='Selected File for C5-Midi 72',message=filename)
	global C5_filename
	C5_filename=filename

def note_CC5():
	filetypes = (('wav files', '*.wav'),('All files', '*.*'))
	filename = fd.askopenfilename(title='Open a file',initialdir='/home/pi/.config/LMN-3/drum_kits/',filetypes=filetypes)
	showinfo(title='Selected File for C#5-Midi 73',message=filename)
	global CC5_filename
	CC5_filename=filename

def note_D5():
	filetypes = (('wav files', '*.wav'),('All files', '*.*'))
	filename = fd.askopenfilename(title='Open a file',initialdir='/home/pi/.config/LMN-3/drum_kits/',filetypes=filetypes)
	showinfo(title='Selected File for D5-Midi 74',message=filename)
	global D5_filename
	D5_filename=filename
	
def note_DD5():
	filetypes = (('wav files', '*.wav'),('All files', '*.*'))
	filename = fd.askopenfilename(title='Open a file',initialdir='/home/pi/.config/LMN-3/drum_kits/',filetypes=filetypes)
	showinfo(title='Selected File for D#5-Midi 75',message=filename)
	global DD5_filename
	DD5_filename=filename

def note_E5():
	filetypes = (('wav files', '*.wav'),('All files', '*.*'))
	filename = fd.askopenfilename(title='Open a file',initialdir='/home/pi/.config/LMN-3/drum_kits/',filetypes=filetypes)
	showinfo(title='Selected File for E5-Midi 76',message=filename)
	global E5_filename
	E5_filename=filename

def make_yaml():
        user_in = askstring('LMN3 Dialog', "Enter directory name:")

        # specify your path of drum kit directory
        path = "/home/pi/.config/LMN-3/drum_kits/"+user_in

        if os.path.exists('/home/pi/'+user_in+'.yaml'):
                os.remove('/home/pi/'+user_in+'.yaml')
        f = open('/home/pi/'+user_in+'.yaml','w')
        f.write('name: "'+user_in+'"\n')
        f.write('mappings:\n')

        f.write('  - note_number: "53"\n')
        if F3_filename:
        	f.write('    file_name: "'+F3_filename+'"\n')
        else:
                f.write('    file_name: ""\n')
        f.write('  - note_number: "54"\n')
        if FF3_filename:
               f.write('    file_name: "'+FF3_filename+'"\n')
        else:
                f.write('    file_name: ""\n')
        f.write('  - note_number: "55"\n')
        if G3_filename:
                f.write('    file_name: "'+G3_filename+'"\n')
        else:
                f.write('    file_name: ""\n')
        f.write('  - note_number: "56"\n')
        if GG3_filename:
                f.write('    file_name: "'+GG3_filename+'"\n')
        else:
                f.write('    file_name: ""\n')
        f.write('  - note_number: "57"\n')
        if A3_filename:
                f.write('    file_name: "'+A3_filename+'"\n')
        else:
                f.write('    file_name: ""\n')
        f.write('  - note_number: "58"\n')
        if AA3_filename:
                f.write('    file_name: "'+AA3_filename+'"\n')
        else:
                f.write('    file_name: ""\n')
        f.write('  - note_number: "59"\n')
        if B3_filename:
                f.write('    file_name: "'+B3_filename+'"\n')
        else:
                f.write('    file_name: ""\n')
        f.write('  - note_number: "60"\n')
        if C4_filename:
                f.write('    file_name: "'+C4_filename+'"\n')
        else:
                f.write('    file_name: ""\n')
        f.write('  - note_number: "61"\n')
        if CC4_filename:
                f.write('    file_name: "'+CC4_filename+'"\n')
        else:
                f.write('    file_name: ""\n')
        f.write('  - note_number: "62"\n')
        if D4_filename:
                f.write('    file_name: "'+D4_filename+'"\n')
        else:
                f.write('    file_name: ""\n')
        f.write('  - note_number: "63"\n')
        if DD4_filename:
                f.write('    file_name: "'+DD4_filename+'"\n')
        else:
                f.write('    file_name: ""\n')
        f.write('  - note_number: "64"\n')
        if E4_filename:
                f.write('    file_name: "'+E4_filename+'"\n')
        else:
                f.write('    file_name: ""\n')
        f.write('  - note_number: "65"\n')
        if F4_filename:
                f.write('    file_name: "'+F4_filename+'"\n')
        else:
                f.write('    file_name: ""\n')
        f.write('  - note_number: "66"\n')
        if FF4_filename:
                f.write('    file_name: "'+FF4_filename+'"\n')
        else:
                f.write('    file_name: ""\n')
        f.write('  - note_number: "67"\n')
        if G4_filename:
                f.write('    file_name: "'+G4_filename+'"\n')
        else:
                f.write('    file_name: ""\n')
        f.write('  - note_number: "68"\n')
        if GG4_filename:
                f.write('    file_name: "'+GG4_filename+'"\n')
        else:
                f.write('    file_name: ""\n')
        f.write('  - note_number: "69"\n')
        if A4_filename:
                f.write('    file_name: "'+A4_filename+'"\n')
        else:
                f.write('    file_name: ""\n')
        f.write('  - note_number: "70"\n')
        if AA4_filename:
                f.write('    file_name: "'+AA4_filename+'"\n')
        else:
                f.write('    file_name: ""\n')
        f.write('  - note_number: "71"\n')
        if B4_filename:
                f.write('    file_name: "'+B4_filename+'"\n')
        else:
                f.write('    file_name: ""\n')
        f.write('  - note_number: "72"\n')
        if C5_filename:
                f.write('    file_name: "'+C5_filename+'"\n')
        else:
                f.write('    file_name: ""\n')
        f.write('  - note_number: "73"\n')
        if CC5_filename:
                f.write('    file_name: "'+CC5_filename+'"\n')
        else:
                f.write('    file_name: ""\n')
        f.write('  - note_number: "74"\n')
        if D5_filename:
                f.write('    file_name: "'+D5_filename+'"\n')
        else:
                f.write('    file_name: ""\n')
        f.write('  - note_number: "75"\n')
        if DD5_filename:
                f.write('    file_name: "'+DD5_filename+'"\n')
        else:
                f.write('    file_name: ""\n')
        f.write('  - note_number: "76"\n')
        if E5_filename:
                f.write('    file_name: "'+E5_filename+'"\n')
        else:
                f.write('    file_name: ""\n')
        f.close()

        cpy = askquestion('LMN3 Dialog', "Do you want to copy the YAML file to the drumkit directory?")
        if cpy == 'yes' :
                cmd = 'cp '+user_in+'.yaml /home/pi/.config/LMN-3/drum_kits/'+user_in+'/'+user_in+'.yaml'
                resp = os.system(cmd)
                print('Copied')
                showinfo(title='LMN3 Dialog',message='Copied!')
                cmd = 'rm /home/pi/'+user_in+'.yaml'
                os.system(cmd)
        else:
                print("OK, not copied")
                showinfo(title='LMN3 Dialog',message='Not Copied!')
                cmd = 'rm /home/pi/'+user_in+'.yaml'
                os.system(cmd)
	
class MyFirstGUI:
	def __init__(self, master):
		self.master = master
		master.title("LMN3")        

		self.Label = Label(master , text="DRUMKIT Mapper - YAML")
		self.Label.grid(row=0 , columnspan=60)

		#Buttons for keyboard         

		self.F_3_button = Button(master, bg="white", text="F_3" ,command=note_F3,height=10 , width=3)
		self.F_3_button.grid(row=5 , column=0)

		self.FF_3_button = Button(master , bg="black", fg="white",text="F#_3" , command=note_FF3,height=10 ,width=3)
		self.FF_3_button.grid(row=1,columnspan=2)

		self.GG_3_button = Button(master,bg="black" ,fg="white",text="G#_3" , command=note_GG3,height=10 ,width=3)
		self.GG_3_button.grid(row=1,columnspan=4)

		self.AA_3_button = Button(master,bg="black" ,fg="white",text="A#_3" , command=note_AA3,height=10 ,width=3)
		self.AA_3_button.grid(row=1,column=2,columnspan=2)

		self.G_3_button = Button(master, bg="white",text="G_3" ,command=note_G3,height=10 , width=3)
		self.G_3_button.grid(row=5 , column=1)

		self.A_3_button = Button(master, bg="white",text="A_3" ,command=note_A3,height=10 , width=3)
		self.A_3_button.grid(row=5 , column=2)

		self.B_3_button = Button(master, bg="white",text="B_3" ,command=note_B3,height=10 , width=3)
		self.B_3_button.grid(row=5 , column=3)

		self.C_4_button = Button(master, bg="white",text="C_4" ,command=note_C4,height=10 , width=3)
		self.C_4_button.grid(row=5 , column=4)

		self.CC_4_button = Button(master ,bg="black" , fg="white",text="C#_4" ,command=note_CC4 ,height=10 ,width=3)
		self.CC_4_button.grid(row=1,column=4,columnspan=3)
		
		self.DD_4_button = Button(master ,bg="black" , fg="white",text="D#_4" ,command=note_DD4 ,height=10 ,width=3)
		self.DD_4_button.grid(row=1,column=4,columnspan=5)

		self.D_4_button = Button(master, bg="white",text="D_4" ,command=note_D4,height=10 , width=3)
		self.D_4_button.grid(row=5 , column=6)

		self.E_4_button = Button(master, bg="white",text="E_4" ,command=note_E4,height=10 , width=3)
		self.E_4_button.grid(row=5 , column=7)

		self.F_4_button = Button(master, bg="white",text="F_4" ,command=note_F4,height=10 , width=3)
		self.F_4_button.grid(row=5 , column=8)

		self.FF_4_button = Button(master , bg="black", fg="white",text="F#_4" , command=note_FF4,height=10 ,width=3)
		self.FF_4_button.grid(row=1,column=8,columnspan=2)

		self.GG_4_button = Button(master , bg="black", fg="white",text="G#_4" , command=note_GG4,height=10 ,width=3)
		self.GG_4_button.grid(row=1,column=9,columnspan=2)

		self.AA_4_button = Button(master , bg="black", fg="white",text="A#_4" , command=note_AA4,height=10 ,width=3)
		self.AA_4_button.grid(row=1,column=10,columnspan=2)

		self.G_4_button = Button(master, bg="white",text="G_4" ,command=note_G4,height=10 , width=3)
		self.G_4_button.grid(row=5 , column=9)

		self.A_4_button = Button(master, bg="white",text="A_4" ,command=note_A4,height=10 , width=3)
		self.A_4_button.grid(row=5 , column=10)

		self.B_4_button = Button(master, bg="white",text="B_4" ,command=note_B4,height=10 , width=3)
		self.B_4_button.grid(row=5 , column=11)

		self.C_5_button = Button(master, bg="white",text="C_5" ,command=note_C5,height=10 , width=3)
		self.C_5_button.grid(row=5 , column=12)

		self.CC_5_button = Button(master ,bg="black" , fg="white",text="C#_5" ,command=note_CC5 ,height=10 ,width=3)
		self.CC_5_button.grid(row=1,column=12,columnspan=2)
		
		self.DD_5_button = Button(master ,bg="black" , fg="white",text="D#_5" ,command=note_DD5 ,height=10 ,width=3)
		self.DD_5_button.grid(row=1,column=13,columnspan=2)

		self.D_5_button = Button(master, bg="white",text="D_5" ,command=note_D5,height=10 , width=3)
		self.D_5_button.grid(row=5 , column=13)

		self.E_5_button = Button(master, bg="white",text="E_5" ,command=note_E5,height=10 , width=3)
		self.E_5_button.grid(row=5 , column=14)

		self.make_button = Button(master, bg="yellow",text="Make YAML" ,command=make_yaml,height=6 , width=6)
		self.make_button.grid(row=5 , column=20)



root = Tk()
#root.iconbitmap(r'/home/pi/ico.ico')
my_gui = MyFirstGUI(root)
num1 = StringVar()

root.mainloop()
