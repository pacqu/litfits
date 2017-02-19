import sqlite3

DATABASE = 'database/litfit.db'

class DatabaseManager():
    def __init__(self, database):
        self.database = database
    
    @staticmethod
    def create():
        connection = sqlite3.connect(DATABASE);
        c = connection.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS users (
        email text NOT NULL PRIMARY KEY,
        fullname text NOT NULL,
        password text NOT NULL);
        """)
        c.execute("""CREATE TABLE IF NOT EXISTS clothes (
        name text NOT NULL PRIMARY KEY,
        email text NOT NULL,
        category text NOT NULL,
        subcategory text NOT NULL);
        """)
        connection.commit()
        connection.close()
        return DatabaseManager(DATABASE)

    def register_user(self, email, fullname, password,):
        connection = sqlite3.connect(self.database);
        c = connection.cursor()
        result = True
        try:
            c.execute('INSERT INTO users VALUES (?, ?, ?)',
                    (email, fullname, password))
        except sqlite3.IntegrityError:
            result = False
        connection.commit()
        connection.close()
        return result
  
    def is_user_authorized(self, email, password):
        connection = sqlite3.connect(self.database)
        c = connection.cursor()
        c.execute('SELECT password FROM users WHERE email=?',
              (email,))
        actual_password = c.fetchone()
        connection.close()
        if actual_password:
            return actual_password[0] == password
        return False
    
    def register_cloth(self, name, email, category, subcategory):
        connection = sqlite3.connect(self.database);
        c = connection.cursor()
        result = True
        try:
            c.execute('INSERT INTO clothes VALUES (?, ?, ?, ?)',
                    (name, email, category, subcategory))
        except sqlite3.IntegrityError:
            result = False
        connection.commit()
        connection.close()
        return result

    def fetch_all_users(self):
        connection = sqlite3.connect(self.database)
        c = connection.cursor()
        c.execute('SELECT * FROM users');
        users = c.fetchall()
        connection.close()
        return users

    def fetch_all_clothes(self):
        connection = sqlite3.connect(self.database)
        c = connection.cursor()
        c.execute('SELECT * FROM clothes');
        users = c.fetchall()
        connection.close()
        return users

    def get_closet(self, email):
        connection = sqlite3.connect(self.database)
        c = connection.cursor()
        c.execute('SELECT * FROM clothes WHERE email=?',
                  (email,));
        closet = c.fetchall()
        connection.close()
        return closet

    def get_cloth(self, cloth):
        connection = sqlite3.connect(self.database)
        c = connection.cursor()
        c.execute('SELECT * FROM clothes WHERE name=?',
                  (cloth,));
        cloth = c.fetchone()
        connection.close()
        return cloth


if __name__== '__main__':
  d = DatabaseManager.create()
  d.register_cloth("black shirt", "test@email.com", "top", "tshirt")
  d.register_cloth("black pants", "test@email.com", "bottom", "slacks")
  #test = d.get_cloth("black shirt")
  test = d.get_closet("test@email.com")
  print test
  
