from com.base.BaseDao import BaseDao


class UserDao(BaseDao):

    def CreateTable(self):
        super().__init__()
        table = "create table if not exists usertable(user_id int primary key auto_increment,user_name varchar(255) not null,user_age int,user_city varchar(255),role_id int,department_id int,create_date datetime,update_date datetime, foreign key(role_id) references Role(role_id), foreign key(department_id) references Department(department_id))"
        self.cursor.execute(table)

    def SaveData(self, data):
        insert = "insert into usertable(user_name,user_age,user_city,role_id,department_id,create_date,update_date) values(%s,%s,%s,%s,%s,%s,%s)"
        self.cursor.execute(insert, data)
        self.con.commit()

    def UpdateData(self, data):
        update = "update usertable set user_name=%s,user_age=%s,user_city=%s,role_id=%s,department_id=%s,update_date=%s where user_id=%s"
        self.cursor.execute(update, data)
        self.con.commit()

    def ShowData(self):
        search = "select * from usertable"
        self.cursor.execute(search)
        return self.cursor.fetchall()

    def DeleteData(self, id):
        delete = "delete from usertable where user_id=%s"
        self.cursor.execute(delete, id)
        self.con.commit()

    def SearchById(self, id):
        search = "select * from usertable where user_id=%s"
        self.cursor.execute(search, id)
        return self.cursor.fetchone()