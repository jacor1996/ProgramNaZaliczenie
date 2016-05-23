from tkinter import *

class HelpWindow:
    def __init__(self, master):
        self.master = master
        self.master.resizable(0,0)
        master.title("Pomoc")

        self.mainFrame = Frame(master, pady=10, padx=10)
        self.mainFrame.pack(fill='both')

        self.labelFrame1 = LabelFrame(self.mainFrame, text='Pomoc')
        self.labelFrame1.pack(fill='both')
        self.text = "   Program został stworzony w celu ułatwienia nauki" \
                    "słówek w języku angielskim. W widoku kursu możemy wybrać " \
                    "interesującą nas kategorię oraz ilość słów do powtórki. " \
                    "Program sprawdza poprawność wprowadzonych słów. W przypadku " \
                    "poprawnej odpowiedzi, użytkownik usłyszy charakterystyczny " \
                    "dźwięk oraz zostanie wyświetlone kolejne słowo. W przypadku " \
                    "podania błędnej odpowiedzi, program wyświetli komunikat o " \
                    "podaniu niewłaściwej odpowiedzi oraz pozwoli na ponowne wpisanie " \
                    "słowa, aż do jego poprawnego wprowadzenia.\n"

        self.label1 = Label(self.labelFrame1, text=self.text, pady=3, justify='left', font='new', wraplength=350)
        self.label1.pack(fill='both')


        self.labelFrame2 = LabelFrame(self.mainFrame, text='Informacje')
        self.labelFrame2.pack(fill='both')
        self.info = "   Program napisany w języku Python 3.5.1 na platformie \"Windows 7\", " \
                    "przy użyciu IDE \"PyCharm\", w razie problemów proszę o kontakt e-mailowy " \
                    "pod adresem jaceknoga11@gmail.com\n"
        self.label2 = Label(self.labelFrame2, text=self.info, pady=3,justify='left', font='new', wraplength=350)
        self.label2.pack(fill='both')


def main():
    root = Tk()
    root.geometry("400x400+15+15")
    root.iconbitmap("img/icon.ico")
    helpWindow = HelpWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()