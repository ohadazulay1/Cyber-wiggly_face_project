import sqlite3
import bcrypt

class ServerHelper:

    def __init__(self):
        self.DB_connection = sqlite3.connect('database.db', check_same_thread=False)
        self.DB_cursor = self.DB_connection.cursor()

    def signUp(self, newData, STARTING_SCORE):
            splited_data = newData.split(",")
            username = splited_data[0]
            password = splited_data[1]

            self.DB_cursor.execute("SELECT * FROM users WHERE username=?", (username,))

            rows = self.DB_cursor.fetchall()
            if not rows:
                self.DB_cursor.execute("INSERT INTO users VALUES(?,?,?);", (username, self._encryptPassword(password), STARTING_SCORE))
                self.DB_connection.commit()
                return True
            else:
                return False

    def _encryptPassword(self, strPassword) -> str:
        passwordBytes = strPassword.encode('utf-8')  # Convert the password to bytes
        salt = bcrypt.gensalt()  # Generate a salt
        hashed_password = bcrypt.hashpw(passwordBytes, salt)
        return hashed_password.decode('utf-8')


    def login(self, newData) -> bool:
        loginSuccess = False
        splited_data = newData.split(",")
        username = splited_data[0]
        password = splited_data[1]
        self.DB_cursor.execute("SELECT password FROM users WHERE username=?", (username,))
        row = self.DB_cursor.fetchone()
        if row: #user found
            passwordFromDB = row[0].encode('utf-8')
            password_to_check = password.encode('utf-8')
            if bcrypt.checkpw(password_to_check, passwordFromDB):
                loginSuccess = True

        return loginSuccess


    def topFive(self):
        self.DB_cursor.execute("SELECT username, highScore FROM users ORDER BY highScore desc")
        rows = self.DB_cursor.fetchall()
        counter = 0
        result_dict = {}
        preusername = ""
        firstTime = True
        for row in rows:
            if not firstTime:
                preusername = username
            else:
                firstTime = False
            username = row[0]
            highScore = row[1]
            result_dict[username] = highScore
            if preusername != username:
                counter = counter + 1
            if counter == 5:
                break
        return result_dict


    def getSelfHighScore(self, newData):
        username = newData
        self.DB_cursor.execute("SELECT highScore FROM users WHERE username=?", (username,))
        userHighScore = self.DB_cursor.fetchall()
        return str(userHighScore[0][0])


    def setSelfHighScore(self, newData):
        splited_data = newData.split(",")
        username = splited_data[0]
        newHighScore = splited_data[1]
        self.DB_cursor.execute("UPDATE users SET highScore =? WHERE username=?", (newHighScore, username))
        self.DB_connection.commit()
        return "True"