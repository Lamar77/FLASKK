import sqlite3

class NorthwindDatabase:

    def __init__(self):
        # self.conn = sqlite3.connect('Northwind_large.sqlite')
        # self.cur = conn.cursor()
        pass
        

    def get_all_supplier_data(self):
        return self.execute_query("SELECT * FROM supplier")

    def execute_query(self, query_text, *parameters):
        conn = sqlite3.connect('Northwind_large.sqlite')
        cur = conn.cursor()
        cur.execute(query_text, parameters)

        column_names = []
        for column in cur.description:
            column_names.append(column[0])

        rows = cur.fetchall()
        dicts = []

        for row in rows:
            d = dict(zip(column_names, row))
            dicts.append(d)
        conn.close()
        return dicts

    def get_supplier_products(self, supplier_id):
        return self.execute_query("SELECT * FROM Product WHERE SupplierId = ?", supplier_id)

    def get_supplier_by_id(self, id):
        return self.execute_query("SELECT CompanyName FROM Supplier WHERE Id = ?", id)