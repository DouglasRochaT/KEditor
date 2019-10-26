from tkinter import *
from tkinter import filedialog
import cv2
from matplotlib import pyplot as plt

root = Tk()
root.title('Image Editor by Douglas')
cmaps={'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds', 
        'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu', 'GnBu',
        'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn'}

var = StringVar()
var.set("Greys")

class Application:
    def __init__(self, master=None):
        self.titulo = Frame(master)
        self.titulo.pack()
        self.msg = Label(self.titulo, text = "Image Editor")
        self.msg["font"] = ("Verdana", "15", "bold")
        self.msg.pack()

        self.cont1 = Frame(master)
        self.cont1.pack()
        self.paths = Entry(self.cont1)
        self.paths["width"] = 50
        self.paths["font"] = ("Comic Sans MS", "10")
        self.paths.pack(side = LEFT)
        self.fonte = Button(self.cont1)
        self.fonte["text"] = "..."
        self.fonte["font"] = ("Calibri", "10")
        self.fonte["width"] = 5
        self.fonte.bind("<Button-1>",self.selecionarimagem)
        self.fonte.pack (side = LEFT)

        self.filtro = Frame(master)
        self.filtro.pack()
        self.tfiltro = Label(self.filtro, text='Filtro:')
        self.tfiltro.pack(side = LEFT)
        self.tfiltro["font"] = ("Calibri", "10", "bold")
        self.filtro = OptionMenu(self.filtro, var, *cmaps)
        self.filtro.pack(side = TOP)

        self.widget4 = Frame(master)
        self.widget4.pack()
        self.gerar = Button(self.widget4)
        self.gerar["text"] = "Show Result"
        self.gerar["font"] = ("Calibri", "10")
        self.gerar["width"] = 10
        self.gerar.bind("<Button-1>",self.exibirimagem)
        self.gerar.pack (side=BOTTOM)
    
    def selecionarimagem(self, Event):
        path = filedialog.askopenfilename(initialdir = "/",title = "Select an Image",filetypes = (("image files","*.jpg *.png"),("all files","*.*")))
        self.paths.delete(0,END)
        self.paths.insert(0, path)
    
    def exibirimagem(self, Event):
        img = cv2.imread(self.paths.get(), cv2.IMREAD_COLOR)
        img2 = img[:,:,::-1]
        img3 = cv2.imread(self.paths.get(), 0)
        plt.subplot(121),plt.imshow(img2)
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(img3, cmap = var.get())
        plt.title('Result'), plt.xticks([]), plt.yticks([])

        plt.show(block=False)

Application(root)
root.mainloop()