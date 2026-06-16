from com.base.BaseDao import BaseDao


class OrderDao(BaseDao):

    def CreateTable(self):
        super().__init__()
        table = "create table if not exists OrderTable(order_Id int primary key auto_increment, product_id int not null, quantity int not null)"
        self.cursor.execute(table)

    def SaveData(self, data):
        insert = "insert into OrderTable(product_id,quantity) value(%s ,%s)"
        self.cursor.execute(insert, data)
        self.con.commit()

    def UpdateData(self, data):
        update = "update OrderTable set product_id=%s,quantity=%s where order_Id=%s"
        self.cursor.execute(update, data)
        self.con.commit()

    def ShowData(self):
        search = "select * from OrderTable"
        self.cursor.execute(search)
        return self.cursor.fetchall()

    def SearchById(self, id):
        search = "select * from OrderTable where order_Id=%s"
        self.cursor.execute(search, id)
        return self.cursor.fetchone()

    def DeleteData(self, id):
        delete = "delete from OrderTable where order_Id=%s"
        self.cursor.execute(delete, id)
        self.con.commit()