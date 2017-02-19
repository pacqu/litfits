import sqlite3

DATABASE = 'database/litfit.db'

class DatabaseManager():
    def __init__(self, database):
        self.database = database
    
    @staticmethod
    def create_users():
        connection = sqlite3.connect(DATABASE);
        c = connection.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS users (
        email text NOT NULL PRIMARY KEY,
        fullname text NOT NULL,
        password text NOT NULL);
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

if __name__== '__main__':
    pass
