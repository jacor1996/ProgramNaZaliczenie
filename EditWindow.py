from tkinter import *
from tkinter import messagebox
import DbUtil

class EditWindow:
    def refresh(self):
        self.master.destroy()
        main()

    def selectCategory(self, event):
        self.showWords.delete(0, END)
        self.categoryName = self.selectCategoty.get(self.selectCategoty.curselection())
        self.words = self.data.getWords(self.categoryName, 50)
        for i in self.words:
            self.showWords.insert(END, [i[0], '-', i[1]])
        self.showWords.select_set(0)

    def commit(self):
        #print("Word:", self.wordInput.get(), "Translation:", self.translationInput.get(), 'Category:', self.categoryInput.get())
        self.data.addWord(self.wordInput.get(), self.translationInput.get(), self.categoryInput.get())
        self.refresh()

    def getWordToDelete(self):
        self.wordToDelete = self.showWords.get(self.showWords.curselection())
        self.data.deleteWord(self.wordToDelete[0])
        self.string1 = 'Pomyślnie usunieto słowo: '
        self.string2 = self.wordToDelete[0] + ' - ' + self.wordToDelete[2]
        self.string1 += self.string2
        messagebox.showinfo("Pop up", self.string1 )
        self.refresh()

    def __init__(self, master):
        self.data = DbUtil.DbUtil()
        self.master = master
        self.master.resizable(0 ,0)
        master.title("Edycja")

        self.mainFrame = Frame(master)
        self.mainFrame.pack()

        self.bottomFrame = Frame(master, borderwidth=10)
        self.bottomFrame.pack()

        self.leftFrame = Frame(self.mainFrame, borderwidth = 5)
        self.leftFrame.pack(side='left')

        self.rightFrame = Frame(self.mainFrame, borderwidth = 5)
        self.rightFrame.pack(side='right')

        self.label = Label(self.leftFrame, text="Wybierz kategorię")
        self.label.pack()

        #Stwórz listę kategorii
        self.selectCategotyScrollbarY = Scrollbar(self.leftFrame)
        self.selectCategotyScrollbarY.pack(side=RIGHT, fill=Y)
        self.selectCategotyScrollbarX = Scrollbar(self.leftFrame, orient=HORIZONTAL)
        self.selectCategotyScrollbarX.pack(side=BOTTOM, fill=X)
        self.selectCategoty = Listbox(self.leftFrame, selectmode=SINGLE, yscrollcommand=self.selectCategotyScrollbarY.set, xscrollcommand=self.selectCategotyScrollbarX.set, exportselection=0)

        for i in self.data.data:
            self.selectCategoty.insert(0, i)
        self.selectCategoty.bind('<<ListboxSelect>>', self.selectCategory)
        self.selectCategoty.pack()

        self.selectCategotyScrollbarY.config(command=self.selectCategoty.yview)
        self.selectCategotyScrollbarX.config(command=self.selectCategoty.xview)
        #-----------------------#

        self.label2 = Label(self.rightFrame, text='Słowa')
        self.label2.pack()

        #Wyświetl listę słów z danej kategorii
        self.showWordsScrollbarY = Scrollbar(self.rightFrame)
        self.showWordsScrollbarY.pack(side=RIGHT, fill=Y)
        self.showWordsScrollbarX = Scrollbar(self.rightFrame, orient=HORIZONTAL)
        self.showWordsScrollbarX.pack(side=BOTTOM, fill=X)
        self.showWords = Listbox(self.rightFrame, selectmode=SINGLE, yscrollcommand=self.showWordsScrollbarY.set, xscrollcommand=self.showWordsScrollbarX.set, exportselection=0)

        self.showWords = Listbox(self.rightFrame, selectmode=SINGLE)
        self.showWords.select_set(0)
        self.showWords.pack()
        self.showWords.bind('<<ListboxSelect>>')

        self.showWordsScrollbarY.config(command=self.showWords.yview)
        self.showWordsScrollbarX.config(command=self.showWords.xview)
        #-----------------------#

        self.deleteButton = Button(self.bottomFrame, text='Usuń', command=self.getWordToDelete)
        self.deleteButton.pack()

        self.labelEdit = LabelFrame(self.bottomFrame, text='Edycja - wpisz słowo i jego tłumaczenie')
        self.labelEdit.pack(side='bottom')

        self.wordInfo = Label(self.labelEdit, text='Słowo:')
        self.wordInfo.pack()
        self.wordData = StringVar()
        self.wordInput = Entry(self.labelEdit, textvariable=self.wordData)
        self.wordInput.pack()

        self.translationInfo = Label(self.labelEdit, text='Tłumaczenie:')
        self.translationInfo.pack()
        self.translationData = StringVar()
        self.translationInput = Entry(self.labelEdit, textvariable=self.translationData)
        self.translationInput.pack()

        self.categoryInfo = Label(self.labelEdit, text='Kategoria:')
        self.categoryInfo.pack()
        self.categoryData = StringVar()
        self.categoryInput = Entry(self.labelEdit, textvariable=self.categoryData)
        self.categoryInput.pack()

        self.commitButton = Button(self.labelEdit, text='Dodaj', command=self.commit)
        self.commitButton.pack(pady = 5)


def main():
    root = Tk()
    root.geometry("400x450+15+15")
    root.iconbitmap("img/icon.ico")
    editDb = EditWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()

