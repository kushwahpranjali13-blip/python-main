from com.base.BaseDao import BaseDao


class DepartmentDao(BaseDao):



    def CreateTable(self):
        super().__init__()
        table="create table if not exists Department(department_Id int primary key auto_increment,department_name varchar(255) not null unique, department_code varchar(255) not null unique)"
        self.cursor.execute(table)


    def SaveData(self,data):
        insert="insert into Department(department_name,department_code) value(%s ,%s)"
        self.cursor.execute(insert,data)
        self.con.commit()

    def UpdateData(self,data):
        update = "update Department set department_name %s,department_code %s where department_Id=%s"
        self.cursor.execute(update,data)
        self.con.commit()

    def ShowData(self):
        search= "select * from Department"
        self.cursor.execute(search)
        return  self.cursor.fetchall()


    def SearchById(self, id):
        search = "select * from Department where department_Id=%s"
        self.cursor.execute(search,id)
        return self.cursor.fetchone()

    def DeleteData(self ,id):
        delete = "delete from Department where department_Id=%s"
        self.cursor.execute(delete,id)
