from flask import Flask, request, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
import sqlite3
app = Flask(__name__)
app.debug = True
conn = sqlite3.connect('bom.db')
cursor = conn.execute("select scheme from data")
for row in cursor:
    print("scheme=", row[0])
conn.close()
if __name__ == '__main__':
	app.run()
