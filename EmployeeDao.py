from com.base.BaseDao import BaseDao

class EmployeeDao(BaseDao):
    def CreateTable(self):
        pass

    def SaveData(self, bean):
        sql = "INSERT INTO Employee (id, name, salary) VALUES (%s, %s, %s)"
        params = (bean.getId(), bean.getName(), bean.getSalary())
        self.cursor.execute(sql, params)
        self.con.commit()
        print("Employee Data saved Successfully")

    def UpdateData(self, bean):
        # Yahan salary ki jagah bean.getName() likha tha, maine bean.getSalary() kar diya hai
        sql = "UPDATE Employee SET name=%s, salary=%s WHERE id=%s"
        params = (bean.getName(), bean.getSalary(), bean.getId())
        self.cursor.execute(sql, params)
        self.con.commit()
        print("Employee Data Updated Successfully")

    def ShowData(self):
        self.cursor.execute("SELECT * FROM Employee")
        result = self.cursor.fetchall()
        return result

    def assignProject(self, empId, projId):
        sql = "INSERT INTO Employee_Project (emp_id, proj_id) VALUES (%s, %s)"
        params = (empId, projId)
        self.cursor.execute(sql, params)
        self.con.commit()
        print(f"Project {projId} assigned to Employee {empId} Successfully")


    def DeleteData(self, id):
        sql = "DELETE FROM Employee WHERE id=%s"
        self.cursor.execute(sql, (id,))
        self.con.commit()
        print(f"Employee with ID {id} Deleted Successfully")

    def SearchById(self, id):
        sql = "SELECT * FROM Employee WHERE id=%s"
        self.cursor.execute(sql, (id,))
        result = self.cursor.fetchone()
        return result