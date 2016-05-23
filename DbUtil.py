import sqlite3

class DbUtil:
    def __init__(self):
        self.getCategories()

    def getCategories(self):
        conn = sqlite3.connect('baza.db')
        c = conn.cursor()
        c.execute("SELECT DISTINCT category FROM Words")
        self.data = c.fetchall()
        conn.close()
        return (self.data)

    def getWords(self, category, amount):
        self.category = category[0]
        self.amount = amount
        conn = sqlite3.connect('baza.db')
        c = conn.cursor()
        c.execute("SELECT * FROM Words WHERE category=? ORDER BY RANDOM() LIMIT ?", (self.category, self.amount))
        self.words = c.fetchall()
        conn.close()
        return (self.words)

    def addWord(self, word, translation, category):
        self.word = word.lower()
        self.translation = translation.lower()
        self.category = category.lower()
        print(self.word)
        conn = sqlite3.connect('baza.db')
        c = conn.cursor()
        c.execute("INSERT INTO Words VALUES (?, ?, ?)", (self.word, self.translation, self.category))
        conn.commit()
        conn.close()

    def deleteWord(self, word):
        self.word = word
        conn = sqlite3.connect('baza.db')
        c = conn.cursor()
        c.execute("DELETE FROM Words WHERE word=?", (self.word,))
        conn.commit()
        conn.close()


