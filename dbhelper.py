import mysql.connector as connector

class DBHelper:
    
    def __init__(self):
        self.con = connector.connect(host='localhost',
                  port='3306',
                  user='root',
                  password='root',
                  database='pythontest')
        # create table
        query = 'create table if not exists user(userId int primary key, name varchar(50), phone varchar(10))'
        cur = self.con.cursor() # Cursors are used to execute SQL queries.
        cur.execute(query) # Cursors are used to execute SQL queries against the database. The execute() method of the cursor is #################### used to send SQL statements to the MySQL server for execution.
        print("Created")

    # Insert into 
    def insert_user(self, userid, username, phone):
        query = f"insert into user(userId, name, phone) values({userid}, '{username}', '{phone}')" # 'f' string is use to make string dynamic, To show the dynamic data.
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit() # Use to physically change(permanent changes) the data in database
        print("User saved to DB: ")
    
    # Fetch all data from table
    def fetch_all(self):
        query = 'SELECT * FROM user'
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("User Id: ", row[0])
            print("User Name: ", row[1])
            print("User No.: ", row[2])
            print()

    # Fetch one data from table using useId
    def fetch_one(self, userid):
        query = f'SELECT * FROM user WHERE userId = {userid}'
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("User Id: ", row[0])
            print("User Name: ", row[1])
            print("Phone No.: ", row[2])
            print()

    # Delete data in table
    def delete_user(self, userid):
        query = f'DELETE FROM user WHERE userId = {userid}'
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("User Deleted: ") 

    # Update data in table
    def update_user(self,userId, newName, newPhone):
        query = f"UPDATE user SET name = '{newName}', phone = '{newPhone}' WHERE userId = {userId}"
        cur = self.con.cursor()       
        cur.execute(query)
        self.con.commit()
        print("Update User: ")

              
# main coding
# helper = DBHelper()
# To insert a data in table
# helper.insert_user(101, 'Shahid', '2530')
# helper.insert_user(102, 'Armaan', '2540')
# helper.insert_user(103, 'Faizan', '2560')
# helper.insert_user(104, 'Aslam', '2580')
# helper.insert_user(105, 'Sarfaraz', '2590')
# helper.insert_user(106, 'Abdul', '2525')

# To get all data from table
# helper.fetch_all()

# To get one data in table
# helper.fetch_one(104)

# To delete data in table
# helper.delete_user(104)

# # To update data in table
# helper.update_user(104, 'Shabaz', '2025')
# helper.fetch_all()