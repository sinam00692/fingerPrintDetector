import os
import sqlite3


class DBHandler:
    def __init__(self, dbname="db.sqlite"):
        self.conn = sqlite3.connect(dbname)

    def setup(self):
        self.conn.execute(
            'CREATE TABLE users (id integer primary key autoincrement, name text,phone integer, username text, password text)')
        self.conn.execute(
            'CREATE TABLE fingers (num integer primary key autoincrement, id integer, path text)')

    def insertUsers(self, name, phone, username, password):
        exist = False
        u = self.findusername(username)
        if len(u) != 0:
            exist = True
        u = self.findphone(phone)
        if len(u) != 0:
            exist = True

        if not exist:
            stmt = 'INSERT INTO users(name, phone, username, password)values(?, ?, ?, ?)'
            args = (name, phone, username, password)
            self.conn.execute(stmt, args)
            self.conn.commit()

        return exist

    def findId(self, username):
        stmt = 'SELECT id FROM users WHERE (username) = (?)'
        args = (username,)
        cur = self.conn.cursor()
        cur.execute(stmt, args)
        result = cur.fetchone()
        return result

    def update(self, userId, password):
        stmt = '''UPDATE users SET password = (?) WHERE id = (?)'''
        args = (password, userId)
        self.conn.execute(stmt, args)
        self.conn.commit()

    def readUser(self, userId):
        stmt = 'SELECT name, phone, username, password FROM users WHERE id = (?)'
        args = (userId,)
        cur = self.conn.cursor()
        cur.execute(stmt, args)
        result = cur.fetchall()
        return result

    def findusername(self, username):
        stmt = 'SELECT id FROM users WHERE username = (?)'
        args = (username,)
        cur = self.conn.cursor()
        cur.execute(stmt, args)
        result = cur.fetchall()
        return result

    def findphone(self, phone):
        stmt = 'SELECT id FROM users WHERE phone = (?)'
        args = (phone,)
        cur = self.conn.cursor()
        cur.execute(stmt, args)
        result = cur.fetchall()
        return result

    def insertFinger(self, userid, path):
        exist = False
        u = self.findPath(path)
        if len(u) != 0:
            exist = True
        u = self.find(userid)
        if len(u) != 0:
            exist = True

        if not exist:
            print("inserted")
            stmt = 'INSERT INTO fingers(id, path)values(?, ?)'
            args = (userid, path)
            self.conn.execute(stmt, args)
            self.conn.commit()
        return exist

    def findPath(self, path):
        stmt = 'SELECT num FROM fingers WHERE path = (?)'
        args = (path,)
        cur = self.conn.cursor()
        cur.execute(stmt, args)
        result = cur.fetchall()
        return result

    def find(self, id):
        stmt = 'SELECT id FROM fingers WHERE id = (?)'
        args = (id,)
        cur = self.conn.cursor()
        cur.execute(stmt, args)
        result = cur.fetchall()
        return result

    def findfingerId(self, path):
        stmt = 'SELECT id FROM fingers WHERE path = (?)'
        args = (path,)
        cur = self.conn.cursor()
        cur.execute(stmt, args)
        result = cur.fetchall()
        return result

    def compare(self):
        stmt = 'SELECT path FROM fingers'
        cur = self.conn.cursor()
        cur.execute(stmt)
        result = cur.fetchall()
        return result

    def deleteUser(self, username):
        exist = False
        u = self.findusername(username)
        if len(u) != 0:
            exist = True

        if exist:
            ID = self.findId(username)
            stmt = 'DELETE FROM fingers WHERE id=(?)'
            cur = self.conn.cursor()
            cur.execute(stmt, (ID[0],))
            self.conn.commit()
            sql = 'DELETE FROM users WHERE username=(?)'
            cur = self.conn.cursor()
            cur.execute(sql, (username,))
        return exist


file = os.path.join(os.getcwd(), 'db.sqlite')
if not os.path.exists(file):
    db = DBHandler()
    db.setup()
