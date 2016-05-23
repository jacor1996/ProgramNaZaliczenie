import sqlite3

class DbCreator:
    def __init__(self):
        self.create()

    def create(self):
        conn = sqlite3.connect('baza.db')
        c = conn.cursor()
        # Create table
        try:
            c.execute('''CREATE TABLE Words
                     (word text, translation text, category text)''')

            c.execute("INSERT INTO Words VALUES ('go', 'iść', 'czasowniki')")
            c.execute("INSERT INTO Words VALUES ('run', 'biec', 'czasowniki')")
            c.execute("INSERT INTO Words VALUES ('steal', 'kraść', 'czasowniki')")
            c.execute("INSERT INTO Words VALUES ('jump', 'skakać', 'czasowniki')")
            c.execute("INSERT INTO Words VALUES ('get', 'wziąć', 'czasowniki')")
            c.execute("INSERT INTO Words VALUES ('sleep', 'spać', 'czasowniki')")
            c.execute("INSERT INTO Words VALUES ('run away', 'uciekać', 'czasowniki')")
            c.execute("INSERT INTO Words VALUES ('tomato', 'pomidor', 'jedzenie')")
            c.execute("INSERT INTO Words VALUES ('potato', 'ziemniak', 'jedzenie')")
            c.execute("INSERT INTO Words VALUES ('banana', 'banan', 'jedzenie')")
            c.execute("INSERT INTO Words VALUES ('football', 'piłka nożna', 'sport')")
            c.execute("INSERT INTO Words VALUES ('basketball', 'koszykówka', 'sport')")
            c.execute("INSERT INTO Words VALUES ('volleyball', 'siatkówka', 'sport')")
            c.execute("INSERT INTO Words VALUES ('boxing', 'boks', 'sport')")
            # Save (commit) the changes
            conn.commit()
            # We can also close the connection if we are done with it.
            # Just be sure any changes have been committed or they will be lost.
            conn.close()

        except sqlite3.OperationalError:
                print('Baza już istnieje')
