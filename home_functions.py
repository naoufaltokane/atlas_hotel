from tkinter import *
import room_wind as r_wind
import client_wind as c_wind
import query as queries
import left_frame_buttons as Add


#function of home button
def home(Frame):

    for widget in Frame.winfo_children():
        widget.destroy()

    home_frame = LabelFrame(Frame, bg='#99CCFF', text='', width=450, height=50, pady=3, bd=4)
    home_frame.grid(row=0, sticky="ew")
    Label(home_frame, text="*******************************HOTEL TONIGHT**************************************", width=100, borderwidth=2, relief="groove").grid(row=0, column=0)
    Label(home_frame, text="Booked Rooms", width=20, borderwidth=2, relief="groove").grid(row=1, column=0)
    Label(home_frame, text="", width=20, borderwidth=2, relief="groove").grid(row=1, column=0)
    Label(home_frame, text="Available Rooms", width=20, borderwidth=2, relief="groove").grid(row=2, column=0)
    Label(home_frame, text="", width=20, borderwidth=2, relief="groove").grid(row=2, column=0)
    Label(home_frame, text="Upcoming Events", width=20, borderwidth=2, relief="groove").grid(row=3, column=0)
    Label(home_frame, text="", width=20, borderwidth=2, relief="groove").grid(row=3, column=0)





#function select client to fill a complain
def fill_complain(Frame):

    for widget in Frame.winfo_children():
        widget.destroy()

    ligne1 = ['First Name', 'Last Name','Room Number']
    for i in range(len(ligne1)):
        Label(Frame, text="" + str(ligne1[i]) + "", font = "Verdana 9", bg="#2894FF", width=17, borderwidth=2, relief="groove").grid(row=1, column=i)

    resultats = queries.get_from_db("clients")
    i = 2
    for lig in resultats:
        txt = str(lig[15])
        Label(Frame, text="" + lig[0] + "", width=17, borderwidth=2, relief="groove").grid(row=i, column=0)
        Label(Frame, text="" + lig[1] + "", width=17, borderwidth=2, relief="groove").grid(row=i, column=1)
        Label(Frame, text="" + lig[9] + "", width=17, borderwidth=2, relief="groove").grid(row=i, column=2)

        Button(Frame, text="Fill A Complain", command=lambda arg1=txt : Add.add_complain(arg1), width=17, borderwidth=2, relief="groove").grid(row=i, column=3)
        i += 1


#fonction affiche listes des clients
def get_clients(Frame):

    for widget in Frame.winfo_children():
        widget.destroy()
    ligne1 = ['First Name', 'Last Name','Country', 'Email', 'IDcard']
    for i in range(len(ligne1)):
        Label(Frame, text="" + str(ligne1[i]) + "", font = "Verdana 9", bg="#2894FF", width=10, borderwidth=2, relief="groove").grid(row=1, column=i)

    resultats = queries.get_from_db('clients')
    i = 2
    for lig in resultats:
        txt = str(lig[15])
        Label(Frame, text="" + lig[0] + "", width=10, borderwidth=2, relief="groove").grid(row=i, column=0)
        Label(Frame, text="" + lig[1] + "", width=10, borderwidth=2, relief="groove").grid(row=i, column=1)
        Label(Frame, text="" + lig[2] + "", width=10, borderwidth=2, relief="groove").grid(row=i, column=2)
        Label(Frame, text="" + lig[3] + "", width=10, borderwidth=2, relief="groove").grid(row=i, column=3)
        Label(Frame, text="" + lig[4] + "", width=10, borderwidth=2, relief="groove").grid(row=i, column=4)

        Button(Frame, text="View", command=lambda arg1=txt: c_wind.aff_client_info(arg1), width=10, borderwidth=2, relief="groove", bg="light green").grid(row=i, column=5)
        i += 1




def get_rooms(Frame):
    for widget in Frame.winfo_children():
        widget.destroy()

    ligne1 = ['Room Number', 'Size', 'Floor', 'View', 'Type', 'Status']

    for i in range(len(ligne1)):
        Label(Frame, text="" + str(ligne1[i]) + "", width=10, borderwidth=2, font = "Verdana 9", bg="#2894FF", relief="groove").grid(row=1, column=i)

    resultats = queries.get_from_db('rooms')
    i = 2
    for lig in resultats:
        txt = str(lig[1])
        Label(Frame, text="" + str(lig[1]) + "", width=10, borderwidth=2, relief="groove").grid(row=i, column=0)
        Label(Frame, text="" + lig[2] + "", width=10, borderwidth=2, relief="groove").grid(row=i, column=1)
        Label(Frame, text="" + lig[3] + "", width=10, borderwidth=2, relief="groove").grid(row=i, column=2)
        Label(Frame, text="" + lig[4] + "", width=10, borderwidth=2, relief="groove").grid(row=i, column=3)
        Label(Frame, text="" + lig[5] + "", width=10, borderwidth=2, relief="groove").grid(row=i, column=4)
        Label(Frame, text="" + lig[9] + "", width=10, borderwidth=2, relief="groove").grid(row=i, column=5)

        button= Button(Frame, text="View", command=lambda  arg1=txt: r_wind.book_room(arg1), width=10, borderwidth=2, relief="groove", bg="light green")
        button.grid(row=i, column=6)
        if str(lig[9]) == "booked":
            button.config(state=DISABLED)
        i += 1



#fonction affiche repas(meals)


def get_meals(Frame):
        for widget in Frame.winfo_children():
            widget.destroy()

        # create  the containers
        breakfast_frame = LabelFrame(Frame, bg='#99CCFF', text='Breakfast Meals', width=450, height=50, pady=3, bd=4)
        lunch_frame = LabelFrame(Frame, bg='#99CCFF', text='Lunch Meals', width=450, height=50, pady=3, bd=4)
        dinner_frame = LabelFrame(Frame, bg='#99CCFF', text='Dinner Meals', width=450, height=50, pady=3, bd=4)

        # layout all of the containers
        breakfast_frame.grid(row=0, sticky="ew")
        lunch_frame.grid(row=1, sticky="new")
        dinner_frame.grid(row=2, sticky="new")

        #get breakfast meals info from database

        resultats = queries.get_db_cond("meals", "type", "breakfast")
        i = 0
        for lig in resultats:
            Label(breakfast_frame, text="" + str(lig[0]) + "", width=30, relief="groove").grid(row=i, column=0,padx=6)
            Label(breakfast_frame, text="Meals Components", width=15, borderwidth=1, relief="groove").grid(row=i, column=1)
            Label(breakfast_frame, text="" + str(lig[1]) + "", width=30,borderwidth=1, relief="groove").grid(row=i, column=2)
            Label(breakfast_frame, text="" + str(lig[2]) + "$", width=20, relief="groove", bg="red").grid(row=i, column=3,padx=6)
            i+=1

#get lunch meals info from database

        resultats=queries.get_db_cond("meals", "type", "lunch")
        i = 1
        for lig in resultats:

            Label(lunch_frame, text="" + str(lig[0]) + "", width=30, relief="groove").grid(row=i, column=0,padx=6)

            Label(lunch_frame, text="Meals Components", width=15, borderwidth=1, relief="groove").grid(row=i, column=1)
            Label(lunch_frame, text="" + lig[1] + "", width=30, borderwidth=1,  relief="groove").grid(row=i, column=2)

            Label(lunch_frame, text="" + str(lig[2]) + "$", width=20, relief="groove", bg="red").grid(row=i, column=3,padx=6)
            i += 1

#get dinner meals info from database

        resultats=queries.get_db_cond("meals", "type", "dinner")
        i = 1
        for lig in resultats:
            Label(dinner_frame, text="" + str(lig[0]) + "", width=30, relief="groove").grid(row=i, column=0,padx=6)
            Label(dinner_frame, text="Meals Components", width=15, borderwidth=1, relief="groove").grid(row=i, column=1)
            Label(dinner_frame, text="" + lig[1] + "", width=30, borderwidth=1, relief="groove").grid(row=i, column=2)
            Label(dinner_frame, text="" + str(lig[2]) + "$", width=20, relief="groove", bg="red").grid(row=i, column=3,padx=6)
            i += 1


#fonction get events from db
def get_events(Frame):
    for widget in Frame.winfo_children():
        widget.destroy()

    # create  the containers
    events_frame = LabelFrame(Frame, bg='#99CCFF', text='Hotel Events', width=700, height=50, pady=3, bd=4)
    events_frame.grid(row=0, sticky="ew")

# get events info from database

    resultats = queries.get_from_db("events")
    i = 1
    for lig in resultats:
        Label(events_frame, text="Event : " + str(lig[0]) + "", width=100, relief="flat", bg="#99CCFF").grid(row=i, column=0)
        Label(events_frame, text="Date : " + str(lig[1]) + "", width=100, borderwidth=1, relief="flat", bg="#99CCFF").grid(row=i+1, column=0)
        Label(events_frame, text="Local : " + str(lig[3]) + "", width=100, borderwidth=1, relief="flat", bg="#99CCFF").grid(row=i+2, column=0)
        Label(events_frame, text="" + str(lig[2]) + "", width=100, relief="flat", bg="#99CCFF").grid(row=i+3, column=0)
        Label(events_frame, text="", width=100, borderwidth=0.1, relief="sunken").grid(row=i+4, column=0)

        i += 5


#function get complains

def get_complains(Frame):
    for widget in Frame.winfo_children():
        widget.destroy()

    complain_frame = LabelFrame(Frame, bg='#99CCFF', text='Complains', width=700, height=50, pady=3, bd=4)
    complain_frame.grid(row=0, sticky="ew")
# get complains info from database

    resultats = queries.get_from_db("complains")
    i = 1
    for lig in resultats:
        client_id = str(lig[0])
        #get client namez by id from db
        res = queries.get_db_cond("clients", "id", client_id)
        for row in res:
            lname =  str(row[0])
            fname =  str(row[1])

            Label(complain_frame, text="Client Name : " + lname + " " + fname + " ", width=100, relief="flat", bg="#99CCFF", wraplength=320).grid(row=i, column=0)
            Label(complain_frame, text="Subject : " + str(lig[1]) + "",  borderwidth=1, relief="flat", bg="#99CCFF", wraplength=444, justify=LEFT).grid(row=i+1, column=0)
            Label(complain_frame, text="Description : ", width=15, borderwidth=1, relief="flat", bg="#99CCFF").grid(row=i+2, column=0)
            Label(complain_frame, text="" + str(lig[2]) + "", width=100, relief="flat", bg="#99CCFF", wraplength=444, justify=LEFT).grid(row=i+3, column=0)
            Label(complain_frame, text="", width=100, relief="sunken").grid(row=i+4, column=0)
            i += 5
