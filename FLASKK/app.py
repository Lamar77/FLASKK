from flask import Flask, render_template
import database

app = Flask(__name__)
db = database.NorthwindDatabase()

@app.route("/")
def suppliers():
    suppliers = db.get_all_supplier_data()
    return render_template('index.html', page_title="Suppliers", suppliers=suppliers)

@app.route("/suppliers/<int:supplier_id>")
def products(supplier_id):
    products = db.get_supplier_products(supplier_id)
    supplier_name = db.get_supplier_by_id(supplier_id)[0]["CompanyName"]
    return render_template('products.html', products=products, supplier_name=supplier_name)