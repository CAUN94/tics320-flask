from flask import Flask, render_template, request, redirect, session
import psycopg2
app = Flask(__name__) 
app.secret_key = 'keep it secret, keep it safe'

conn = psycopg2.connect(
    database="dcth13s0gio0s4",
    user="garovzdkeoturn",
    password="f2266ce9ca11d4a6120fad3c87892197a6761ea228cf6dcb9046cc94ef8a6ec3",
    host="ec2-18-215-44-132.compute-1.amazonaws.com",
    port="5432")

cur = conn.cursor()

#Usted solo modifique de aqui para abajo

@app.route('/')
def sql():
    cur.execute("""SELECT * from city limit 20""")
    rows = cur.fetchall()
    my_list = []
    for row in rows:
        my_list.append(row)

    return render_template('template.html',  results=my_list)

#Usted solo modifique de aqui para arriba

if __name__=="__main__":
    app.run(debug=True)

