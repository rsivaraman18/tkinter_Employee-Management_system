import sqlite3

#()
class Mydatabase:
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        query1 = '''
         CREATE TABLE IF NOT EXISTS employees(
         ID Integer Primary key,
         Name text,
         Age text,
         Doj text,
         email text,
         gender text,
         contact text,
         Location text
         ) 
         '''
        self.cur.execute(query1)
        self.con.commit()


    def Insert(self,name,age,doj,email,gender,contact,address):
        query2 = "INSERT INTO employees VALUES(NULL,?,?,?,?,?,?,?)"
        data2 = (name,age,doj,email,gender,contact,address)
        self.cur.execute(query2,data2)
        self.con.commit()

    def Getalldata(self):
        self.cur.execute('SELECT * FROM employees')
        resdata = self.cur.fetchall()
        #print(resdata)
        return resdata

    def Delete_record(self,id):
        self.cur.execute('DELETE FROM employees WHERE Id=?',(id,))
        self.con.commit()

    def Update_record(self,id,name,age,doj,email,gender,contact,location):
        query3 = "UPDATE employees SET name=?,age=?,doj=?,email=?,gender=?,contact=?,location=? WHERE id=?"
        data3 = (name,age,doj,email,gender,contact,location,id)

        self.cur.execute(query3,data3)
        self.con.commit()


'''
Emp = Database('employee.db')
#Emp.Insert('kulathongan','27','23-02-2023','kulothangana@gmail.com','male','965465645','Tanjovore')
#Emp.Delete_record('3')
#Emp.Getalldata()
Emp.Update_record('4','Paramasivam','50','2000-01-02','kulo@gmail.com','male','9555','Tanj' )


'''
