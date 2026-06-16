from com.base.BaseDao import BaseDao


class InventoryDao(BaseDao):

    def CreateTable(self):
        super().__init__()
        table = "create table if not exists inventory(inventory_Id int primary key auto_increment, product_id int not null, quantity int not null)"
        self.cursor.execute(table)

    def SaveData(self, data):
        insert = "insert into inventory(product_id,quantity) values(%s ,%s)"
        self.cursor.execute(insert, data)
        self.con.commit()

    def UpdateData(self, data):
        update = "update inventory set product_id=%s,quantity=%s where inventory_Id=%s"
        self.cursor.execute(update, data)
        self.con.commit()

    def ShowData(self):
        search = "select * from inventory"
        self.cursor.execute(search)
        return self.cursor.fetchall()

    def SearchById(self, id):
        search = "select * from inventory where inventory_Id=%s"
        self.cursor.execute(search, (id,))
        return self.cursor.fetchone()

    def DeleteData(self, id):
        delete = "delete from inventory where inventory_Id=%s"
        self.cursor.execute(delete, (id,))
        self.con.commit()