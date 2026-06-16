from com.base.BaseDao import BaseDao


class VendorDao(BaseDao):

    def CreateTable(self):
        super().__init__()
        table = "create table if not exists Vendor(vendor_id int primary key auto_increment, vendor_name varchar(255) not null unique)"
        self.cursor.execute(table)

    def SaveData(self, data):
        insert = "insert into Vendor(vendor_name) value(%s)"
        self.cursor.execute(insert, data)
        self.con.commit()

    def UpdateData(self, data):
        update = "update Vendor set vendor_name=%s where vendor_id=%s"
        self.cursor.execute(update, data)
        self.con.commit()

    def ShowData(self):
        search = "select * from Vendor"
        self.cursor.execute(search)
        return self.cursor.fetchall()

    def SearchById(self, id):
        search = "select * from Vendor where vendor_id=%s"
        self.cursor.execute(search, id)
        return self.cursor.fetchone()

    def DeleteData(self, id):
        delete = "delete from Vendor where vendor_id=%s"
        self.cursor.execute(delete, id)
        self.con.commit()