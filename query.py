import pymysql
from tkinter import messagebox

#connect do db
def connection():
    con = pymysql.connect(user="root", password="", host='127.0.0.1', db='test')
    return con


#fonction add meal to bd
def valid_meal(name, components, price, type):

    con = connection()
    q = "insert into meals(name, description, price, type) values('%s','%s','%s','%s')" % (name, components, price, type)

    try:
        c = con.cursor()
        c.execute(q)
        con.commit()
        messagebox.showinfo("done", "You Have Added A Meal :)")

    except Exception as e:
        print(e)
        con.rollback()
        raise

#fonction add event to db
def valid_event(name, date, description, local):

    con = connection()
    q = "insert into events(name, date, description, local) values('%s','%s','%s','%s')" % (name, date, description, local)

    try:
        c = con.cursor()
        c.execute(q)
        con.commit()
        messagebox.showinfo("done", "You Have Added A Event :)")
    except Exception as e:
        print(e)
        con.rollback()
        raise




#fonction add report to db
def valid_report(subj, description, id):
    con = connection()
    q = "insert into complains(client_id, subject, description) values('%s','%s','%s')" % (id, subj, description)

    try:
        c = con.cursor()
        c.execute(q)
        con.commit()
        messagebox.showinfo("done", "Your Complain Has Been Added :)")
    except Exception as e:
        print(e)
        con.rollback()
        raise



#function add client info to db

def Validate(Nom, Prenom, country, email, adr, pho, card, Comments, client_type, breakfast, lunch, dinner, date_in, date_out, number):


    con = connection()
    q = "insert into clients(Nom, Prenom, Country, Email, Address, Phone, IDcard, Comments, Type, Room, breakfast, lunch, dinner, date_in, date_out) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
    Nom, Prenom, country, email, adr, pho, card, Comments, client_type, number, breakfast, lunch, dinner, date_in,
    date_out)

    try:
        c = con.cursor()
        c.execute("update rooms set status=%s WHERE number=%s", ["booked", number])
        c.execute(q)
        con.commit()
        messagebox.showinfo("done", "The Room is Booked:)")

    except Exception as e:
        print(e)
        con.rollback()
        raise


#fucntion checkout

def Checkout(room):

    con = connection()
    c=con.cursor()
    c.execute("DELETE FROM clients WHERE Room=%s", [room])
    c.execute("UPDATE rooms set status='available' WHERE number=%s", [room])
    con.commit()
    messagebox.showinfo("done", "Client Is Out :)")


#get from db

def get_from_db(table):

    con = connection()
    c = con.cursor()
    c.execute("select * from "+ str(table))
    resultats = c.fetchall()
    c.close()
    return resultats

def get_db_cond(table, champ, condition):

    con = connection()
    c = con.cursor()
    c.execute("select * from " + str(table) + " where " + str(champ) + "=%s", [condition])
    resultats = c.fetchall()
    c.close()
    return resultats


def get_db_2cond(table, champ1, champ2, condition1, condition2):

    con = connection()
    c = con.cursor()
    c.execute("select * from " + str(table) + " where " + str(champ1) + "=%s and " + str(champ2) + "=%s ", [condition1, condition2])
    res = c.fetchone()
    c.close()
    return res