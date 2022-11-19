import sqlite3

conn = sqlite3.connect('job_database.db')
print("opended database successfully")

conn.execute('CREATE TABLE job_recomdation(name TEXT, email TEXT, password TEXT)')
print("Table create successfully")
conn.close()
