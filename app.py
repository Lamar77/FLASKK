from flask import Flask, render_template
import database

app = Flask(__name__)
db = database.NorthwindDatabase()

@app.route("/")
def suppliers():
    suppliers = db.get_all_data()
    return render_template('index.html', page_title="Suppliers", suppliers=suppliers)