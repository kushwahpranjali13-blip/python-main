from com.base.BaseDao import BaseDao


class ProductDao(BaseDao):

    def CreateTable(self):
        super().__init__()
        table = "create table if not exists Product(product_Id int primary key auto_increment, product_name varchar(255) not null unique, vendor_id int not null, foreign key (vendor_id) references vendor(vendor_id))"
        self.cursor.execute(table)

    def SaveData(self, data):
        insert = "insert into Product(product_name,vendor_id) value(%s ,%s)"
        self.cursor.execute(insert, data)
        self.con.commit()

    def UpdateData(self, data):
        update = "update Product set product_name=%s,vendor_id=%s where product_Id=%s"
        self.cursor.execute(update, data)
        self.con.commit()

    def ShowData(self):
        search = "select * from Product"
        self.cursor.execute(search)
        return self.cursor.fetchall()

    def SearchById(self, id):
        search = "select * from Product where product_Id=%s"
        self.cursor.execute(search, id)
        return self.cursor.fetchone()

    def DeleteData(self, id):
        delete = "delete from Product where product_Id=%s"
        self.cursor.execute(delete, id)
        self.con.commit()