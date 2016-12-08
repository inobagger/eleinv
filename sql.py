import sqlite3
class DB:
    def __init__(self, name):
        conn = sqlite3.connect(name)
        self.c = conn.cursor()
    def __ExecuteScript(self, file):
        script = open("sql/" + file, 'r')
        text = script.read()
        script.close()
        self.c.executescript(text)
    def InitDB(self):
        self.__ExecuteScript("init.sql")