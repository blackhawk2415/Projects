import sqlite3
import datetime
import time


conn = sqlite3.connect('tutorial.db')
c = conn.cursor()
sql = "SELECT * FROM "