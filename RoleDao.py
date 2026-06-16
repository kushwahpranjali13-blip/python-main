from com.base.BaseDao import BaseDao


class RoleDao(BaseDao):

    def CreateTable(self):
        super().__init__()
        table="create table if not exists Role(role_id int primary key auto_increment, role_name varchar(255) not null unique)"
        self.cursor.execute(table)


    def SaveData(self, data):
        insert="insert into Role(role_name)value(%s)"
        self.cursor.execute(insert,data)
        self.con.commit()


    def UpdateData(self, data):
        update="update Role set role_name=%s where role_id=%s"
        self.cursor.execute(update,data)



    def ShowData(self):
        search="select * from Role"
        self.cursor.execute(search)
        return self.cursor.fetchall()

    def DeleteData(self, id):
        delete ="delete from Role where role_id=%s"
        self.cursor.execute(delete,id)


    def SearchById(self, id):
        searchid = "select * from Role where role_id=%s"
        self.cursor.execute(searchid,id)
        return  self.cursor.fetchone()
