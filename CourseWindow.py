from tkinter import *
from tkinter import messagebox
import winsound as sfx

import DbCreator
import DbUtil

class Menu:
    def __init__(self, master):
        self.data = DbUtil.DbUtil()
        self.master = master
        self.master.resizable(0,0)
        master.title("Menu")

        self.mainFrame = Frame(master)
        self.mainFrame.pack()

        self.label = Label(self.mainFrame, text="Wybierz kategorię")
        self.label.pack()

        #Stwórz listę kategorii
        self.selectCategoty = Listbox(self.mainFrame, selectmode=SINGLE)
        for i in self.data.data:
            self.selectCategoty.insert(0, i)
        self.selectCategoty.select_set(0)
        self.selectCategoty.pack(fill=X)
        #-----------------------#

        self.scale = Scale(self.mainFrame, from_=5, to=15, orient=HORIZONTAL, label='       Ilość słówek')
        self.scale.pack(fill=X)

        self.startButton = Button(self.mainFrame, text="Start", command=self.openCurseWindow)
        self.startButton.pack()

        self.wordCounter = 0
        self.mistakeCounter = 0
        self.gotWords = False

    def wordGetter(self):
        self.choosenCategory = self.selectCategoty.get(self.selectCategoty.curselection())
        self.choosenAmount = str(self.scale.get())
        #print("Scale amount = ", self.choosenAmount)
        self.wordsContainer = self.data.getWords(self.choosenCategory, self.choosenAmount)
        self.wordsList = []
        self.translationsList = []
        self.isCorrectList = []

        #print(len(data.getWords(self.choosenCategory, self.choosenAmount))) #Debugging
        for i in range(len(self.data.getWords(self.choosenCategory, self.choosenAmount))):
            self.wordsList.append(self.wordsContainer[i][0]) #Debugging
            self.translationsList.append(self.wordsContainer[i][1])
            self.isCorrectList.append(False)
        print("Dane pobrane z bazy", self.wordsList, self.translationsList, self.isCorrectList) #Debugging

    def openNewWindow(self):
        self.window = Toplevel()
        self.window.geometry("400x250+5+5")
        self.window.resizable(0,0)
        self.window.iconbitmap("img/icon.ico")
        self.window.title('Nauka - ilość słówek = %d/%d' % (self.wordCounter+1, len(self.wordsList)))
        self.labelFrame = LabelFrame(self.window, text='Wprowadź tłumaczenie słowa')
        self.labelFrame.pack(fill=BOTH, expand=YES)

        self.wordLabel = Label(self.labelFrame, text=["Przetłumacz:", self.translationsList[self.wordCounter]], borderwidth=5)
        self.wordLabel.pack(pady = 15)

        self.input = Entry(self.labelFrame, textvariable=StringVar, relief='flat', borderwidth=3)
        self.input.delete(0, 'end')
        self.input.pack(pady=15)
        self.input.bind("<Return>", self.getText)

        self.nextButton = Button(self.labelFrame, text='Następne', command=self.getText)
        self.nextButton.pack(pady = 15)


    def deleteWindow(self):
        self.window.destroy()

    def openCurseWindow(self):
        if (self.gotWords == False):
            self.wordGetter()
            self.choosenCategory = self.selectCategoty.get(self.selectCategoty.curselection())
            self.openNewWindow()
            self.window.focus_set()
            self.input.focus_force()

    def getText(self, event=0):
        self.userTranslation = self.input.get().lower()

        if (self.userTranslation == self.wordsList[self.wordCounter]):
            sfx.PlaySound("System asterisk", sfx.SND_ASYNC)
            print("Dobra odpowiedź")
            if (self.wordCounter < len(self.wordsList) - 1):
                self.wordCounter += 1
                #self.deleteWindow()
                self.window.destroy()
                self.openNewWindow()
                self.window.focus_set()
                self.input.focus_force()
            else:
                self.deleteWindow()
                self.msg1 = "Koniec nauki.\nPoprawne odpowiedzi: "
                #self.msg2 = str(self.wordCounter) + ' / ' + str(self.wordCounter + self.mistakeCounter)
                self.msg2 = self.wordCounter/(self.wordCounter+self.mistakeCounter)*100
                self.msg2 = "%.2f" % self.msg2 ###
                self.msg1 += str(self.msg2)
                self.msg1 += " %"
                messagebox.showinfo("Koniec", self.msg1)
        else:
            self.mistakeCounter += 1
            self.message1 = "Podano błędną odpowiedź: "
            self.message2 = self.userTranslation
            self.message1 += self.userTranslation
            messagebox.showinfo("Błąd", self.message1)
            self.input.delete(0, 'end')
            self.window.focus_set()
            self.input.focus_set()


def main():
    DbCreator.DbCreator() #Stwórz bazę lub nic nie rób jeśli baza już istnieje
    root = Tk()
    root.geometry("200x300")
    root.iconbitmap("img/icon.ico")
    myGui = Menu(root)
    root.mainloop()


if __name__ == '__main__':
    main()
