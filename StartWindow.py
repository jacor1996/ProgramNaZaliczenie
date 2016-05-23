from tkinter import *
import CourseWindow
import EditWindow
import HelpWindow

class StartWindow(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Nauka języka angielskiego")
        self.parent.resizable(0,0)

        self.labelFrame = LabelFrame(self.parent, text='Created by Jacek Noga',
                                     labelanchor='s', font='Luicida', height=300)
        self.labelFrame.pack(fill='both', padx=5, pady=5)

        self.canvas = Canvas(self.labelFrame, width=350, height=350)
        self.canvas.pack(fill='both')
        self.background = PhotoImage(file='img/background.png')
        self.canvas.create_image(-5, -20, anchor=NW, image=self.background)

        self.startCourseButton = Button(self.canvas, text="Rozpocznij naukę", command=CourseWindow.main)
        self.startCourseButton.pack(pady = 10)

        self.editDatabaseButton = Button(self.canvas, text="Edytuj bazę danych", command=EditWindow.main)
        self.editDatabaseButton.pack(pady = 10)

        self.helpButton = Button(self.canvas, text="Pomoc i informacje o programie", command=HelpWindow.main)
        self.helpButton.pack(pady = 10)

        self.exitButton = Button(self.canvas, text='Wyjście', command=sys.exit)
        self.exitButton.pack(pady = 30)


def fun():
    root = Tk()
    root.iconbitmap("img/icon.ico")
    root.geometry("350x250")
    app = StartWindow(root)
    root.mainloop()


if __name__ == '__main__':
    fun()