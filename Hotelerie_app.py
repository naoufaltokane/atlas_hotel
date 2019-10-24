from tkinter import *
import left_frame_buttons as Add
import home_functions as fct
from PIL import ImageTk, Image

#foncction de remplir the frame center

top = Tk()
top.title('Hotelerie Python App')




_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = '#d9d9d9'  # X11 color: 'gray85'
_ana1color = '#d9d9d9'  # X11 color: 'gray85'
_ana2color = '#ececec'  # Closest X11 color: 'gray92'

top.geometry("1200x562+267+82")
top.title("Hotel ATLAS")
top.configure(background="#99CCFF")
top.configure(highlightbackground="#d9d9d9")
top.configure(highlightcolor="black")

top_frame = Frame(top)
top_frame.place(relx=0.012, rely=0.018, relheight=0.222, relwidth=0.918)
top_frame.configure(relief='flat')
top_frame.configure(borderwidth="2")
top_frame.configure(background="#99CCFF")
top_frame.configure(width=775)

#add top image
model_label = Label(top_frame)
model_label.place(relx=0.103, rely=0.0, height=121, width=674)
model_label.configure(background="#99CCFF")
model_label.configure(disabledforeground="#a3a3a3")
model_label.configure(foreground="#000000")
img1 = PhotoImage(file='images/top.png')
model_label.configure(image=img1)
model_label.configure(text='''Label''')
model_label.configure(width=674)

menu_frame = Frame(top)
menu_frame.place(relx=0.012, rely=0.249, relheight=0.16, relwidth=0.948)
menu_frame.configure(relief='raised')
menu_frame.configure(borderwidth="2")
menu_frame.configure(relief='raised')
menu_frame.configure(background="#99CCFF")
menu_frame.configure(width=800)






#ajout des bouttons du bare de menu

#home buttons
logo1 = PhotoImage(file='images/home.png')
home = Button(menu_frame, font = "Times 12 bold", compound="left", command= lambda: fct.home(ctr_mid), image=logo1)
home.place(relx=0.1, rely=0.111, height=64, width=97)
home.configure(activebackground="#ececec")
home.configure(activeforeground="#000000")
home.configure(background="#d9d9d9")
home.configure(disabledforeground="#a3a3a3")
home.configure(foreground="#000000")
home.configure(highlightbackground="#d9d9d9")
home.configure(highlightcolor="black")
home.configure(pady="0")
home.configure(text='''Home''')
home.configure(width=97)
home.image = logo1

#clients button
logo2 = PhotoImage(file='images/clients.png')
clients = Button(menu_frame, font = "Times 12 bold", compound="left", command= lambda: fct.get_clients(ctr_mid), image=logo2)
clients.place(relx=0.238, rely=0.111, height=64, width=97)
clients.configure(activebackground="#ececec")
clients.configure(activeforeground="#000000")
clients.configure(background="#d9d9d9")
clients.configure(disabledforeground="#a3a3a3")
clients.configure(foreground="#000000")
clients.configure(highlightbackground="#d9d9d9")
clients.configure(highlightcolor="black")
clients.configure(pady="0")
clients.configure(text='''Clients''')
clients.configure(width=97)
clients.image = logo2


#room button
logo3 = PhotoImage(file='images/rooms.png')
rooms = Button(menu_frame, font = "Times 12 bold", compound="left", command = lambda: fct.get_rooms(ctr_mid), image=logo3)
rooms.place(relx=0.375, rely=0.111, height=64, width=97)
rooms.configure(activebackground="#ececec")
rooms.configure(activeforeground="#000000")
rooms.configure(background="#d9d9d9")
rooms.configure(disabledforeground="#a3a3a3")
rooms.configure(foreground="#000000")
rooms.configure(highlightbackground="#d9d9d9")
rooms.configure(highlightcolor="black")
rooms.configure(pady="0")
rooms.configure(text='''Rooms''')
rooms.configure(width=97)
rooms.image = logo3

#meals button
logo4 = PhotoImage(file='images/meals.png')
meals = Button(menu_frame, font = "Times 12 bold", compound="left",command = lambda: fct.get_meals(ctr_mid), image=logo4)
meals.place(relx=0.513, rely=0.111, height=64, width=97)
meals.configure(activebackground="#ececec")
meals.configure(activeforeground="#000000")
meals.configure(background="#d9d9d9")
meals.configure(disabledforeground="#a3a3a3")
meals.configure(foreground="#000000")
meals.configure(highlightbackground="#d9d9d9")
meals.configure(highlightcolor="black")
meals.configure(pady="0")
meals.configure(text='''Meals''')
meals.configure(width=97)
meals.image = logo4

#complains
logo6 = PhotoImage(file='images/complains.png')
complains = Button(menu_frame, font = "Times 12 bold", compound="left", command = lambda: fct.get_complains(ctr_mid), image=logo6)
complains.place(relx=0.788, rely=0.111, height=64, width=112)
complains.configure(activebackground="#ececec")
complains.configure(activeforeground="#000000")
complains.configure(background="#d9d9d9")
complains.configure(disabledforeground="#a3a3a3")
complains.configure(foreground="#000000")
complains.configure(highlightbackground="#d9d9d9")
complains.configure(highlightcolor="black")
complains.configure(pady="0")
complains.configure(text='''Complains''')
complains.configure(width=97)
complains.image = logo6

#events button
logo5 = PhotoImage(file='images/events.png')
events = Button(menu_frame, font = "Times 12 bold", compound="left", command = lambda: fct.get_events(ctr_mid), image=logo5)
events.place(relx=0.65, rely=0.111, height=64, width=97)
events.configure(activebackground="#ececec")
events.configure(activeforeground="#000000")
events.configure(background="#d9d9d9")
events.configure(disabledforeground="#a3a3a3")
events.configure(foreground="#000000")
events.configure(highlightbackground="#d9d9d9")
events.configure(highlightcolor="black")
events.configure(pady="0")
events.configure(text='''Events''')
events.configure(width=97)
events.image = logo5


#center frame
center = Frame(top)
center.place(relx=0.012, rely=0.427, relheight=0.489 , relwidth=0.954)
center.configure(relief='groove')
center.configure(borderwidth="2")
center.configure(relief='groove')
center.configure(background="#99CCFF")
center.configure(width=805)

ctr_left = Frame(center)
ctr_left.place(relx=0.012, rely=0.036, relheight=0.927, relwidth=0.155)
ctr_left.configure(relief='groove')
ctr_left.configure(borderwidth="2")
ctr_left.configure(relief='groove')
ctr_left.configure(background="#99CCFF")
ctr_left.configure(width=125)

Add_Event = Button(ctr_left, font = "Times", command = lambda: Add.add_event(ctr_mid))
Add_Event.place(relx=0.08, rely=0.039, height=54, width=107)
Add_Event.configure(activebackground="#ececec")
Add_Event.configure(activeforeground="#000000")
Add_Event.configure(background="#d9d9d9")
Add_Event.configure(disabledforeground="#a3a3a3")
Add_Event.configure(foreground="#000000")
Add_Event.configure(highlightbackground="#d9d9d9")
Add_Event.configure(highlightcolor="black")
Add_Event.configure(pady="0")
Add_Event.configure(text='''Add Event''')
Add_Event.configure(width=107)

Add_Meal = Button(ctr_left, font = "Times", command = lambda: Add.add_meal())
Add_Meal.place(relx=0.08, rely=0.275, height=54, width=107)
Add_Meal.configure(activebackground="#ececec")
Add_Meal.configure(activeforeground="#000000")
Add_Meal.configure(background="#d9d9d9")
Add_Meal.configure(disabledforeground="#a3a3a3")
Add_Meal.configure(foreground="#000000")
Add_Meal.configure(highlightbackground="#d9d9d9")
Add_Meal.configure(highlightcolor="black")
Add_Meal.configure(pady="0")
Add_Meal.configure(text='''Add Meal''')
Add_Meal.configure(width=107)

hotel_policy = Button(ctr_left, font = "Times", command = lambda: Add.get_policy())
hotel_policy.place(relx=0.08, rely=0.51, height=54, width=107)
hotel_policy.configure(activebackground="#ececec")
hotel_policy.configure(activeforeground="#000000")
hotel_policy.configure(background="#d9d9d9")
hotel_policy.configure(disabledforeground="#a3a3a3")
hotel_policy.configure(foreground="#000000")
hotel_policy.configure(highlightbackground="#d9d9d9")
hotel_policy.configure(highlightcolor="black")
hotel_policy.configure(pady="0")
hotel_policy.configure(text='''Hotel Policy''')
hotel_policy.configure(width=107)

report = Button(ctr_left, font = "Times", command = lambda: fct.fill_complain(ctr_mid))
report.place(relx=0.08, rely=0.745, height=54, width=107)
report.configure(activebackground="#ececec")
report.configure(activeforeground="#000000")
report.configure(background="#d9d9d9")
report.configure(disabledforeground="#a3a3a3")
report.configure(foreground="#000000")
report.configure(highlightbackground="#d9d9d9")
report.configure(highlightcolor="black")
report.configure(pady="0")
report.configure(text='''Fill a Complain''')
report.configure(width=107)

ctr_mid = Frame(center)
ctr_mid.place(relx=0.174, rely=0.036, relheight=0.927, relwidth=0.814)
ctr_mid.configure(relief='ridge')
ctr_mid.configure(borderwidth="2")
ctr_mid.configure(relief='ridge')
ctr_mid.configure(background="#99CCFF")
ctr_mid.configure(width=655)




Label2 = Label(top)
Label2.place(relx=0.184, rely=0.93, height=40, width=604)
Label2.configure(background="#99CCFF")
Label2.configure(disabledforeground="#a3a3a3")
Label2.configure(foreground="#000000")
img2 = PhotoImage(file="images/foot.png")
Label2.configure(image=img2)
Label2.configure(text='''''')
Label2.configure(width=674)



top.mainloop()


