from tkinter import *
import query as queries

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = '#d9d9d9'  # X11 color: 'gray85'
_ana1color = '#d9d9d9'  # X11 color: 'gray85'
_ana2color = '#ececec'  # Closest X11 color: 'gray92'

font10 = "-family {Courier New} -size 10 -weight normal -slant" \
         " roman -underline 0 -overstrike 0"
font12 = "-family {Segoe UI} -size 10 -weight bold -slant " \
         "roman -underline 0 -overstrike 0"
font14 = "-family {Segoe UI} -size 16 -weight bold -slant " \
         "roman -underline 0 -overstrike 0"
font9 = "-family {Segoe UI} -size 9 -weight normal -slant " \
        "roman -underline 0 -overstrike 0"


# fonction pour calculer le nombre des jours en hotel

def nb_days(date1, date2):
    return abs(date2 - date1).days


def book_room(id):
    root = Tk()
    root.title('Book a Room')
    root.configure(background="#99CCFF")
    root.configure(highlightbackground="#ffffff")
    root.configure(highlightcolor="#000000")
    root.geometry("399x620+607+23")

    # room information frame
    room_frame = LabelFrame(root)
    room_frame.place(relx=0.025, rely=0.016, relheight=0.234, relwidth=0.952)
    room_frame.configure(relief='groove')
    room_frame.configure(foreground="black")
    room_frame.configure(text='''Reservation Information''')
    room_frame.configure(background="#99CCFF")
    room_frame.configure(width=380)

    # create all of the main containers

    # layout all of the main containers
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # get room info from database

    resultats = queries.get_db_cond("rooms", "number", id)
    for lig in resultats:
        number = str(lig[1])
        sizee = str(lig[2])
        fl = str(lig[3])
        ph = str(lig[6])

    r_num = Label(room_frame)
    r_num.place(relx=0.0, rely=0.207, height=17, width=97, bordermode='ignore')
    r_num.configure(activebackground="#99CCFF")
    r_num.configure(background="#99CCFF")
    r_num.configure(disabledforeground="#a3a3a3")
    r_num.configure(font=font12)
    r_num.configure(foreground="#000000")
    r_num.configure(text='''Room Number''')
    r_num.configure(width=97)

    num = Label(room_frame)
    num.place(relx=0.263, rely=0.207, height=21, width=70, bordermode='ignore')
    num.configure(activebackground="#f9f9f9")
    num.configure(activeforeground="black")
    num.configure(background="#99CCFF")
    num.configure(disabledforeground="#a3a3a3")
    num.configure(foreground="#000000")
    num.configure(highlightbackground="#d9d9d9")
    num.configure(highlightcolor="black")
    num.configure(text=number)

    r_size = Label(room_frame)
    r_size.place(relx=0.013, rely=0.448, height=21, width=64, bordermode='ignore')
    r_size.configure(activebackground="#f9f9f9")
    r_size.configure(activeforeground="black")
    r_size.configure(background="#99CCFF")
    r_size.configure(disabledforeground="#a3a3a3")
    r_size.configure(font=font12)
    r_size.configure(foreground="#000000")
    r_size.configure(highlightbackground="#d9d9d9")
    r_size.configure(highlightcolor="black")
    r_size.configure(text="size :")

    size = Label(room_frame)
    size.place(relx=0.276, rely=0.448, height=21, width=100, bordermode='ignore')
    size.configure(activebackground="#f9f9f9")
    size.configure(activeforeground="black")
    size.configure(background="#99CCFF")
    size.configure(disabledforeground="#a3a3a3")
    size.configure(foreground="#000000")
    size.configure(highlightbackground="#d9d9d9")
    size.configure(highlightcolor="black")
    size.configure(text=sizee)

    r_floor = Label(room_frame)
    r_floor.place(relx=0.0, rely=0.69, height=21, width=74, bordermode='ignore')
    r_floor.configure(activebackground="#f9f9f9")
    r_floor.configure(activeforeground="black")
    r_floor.configure(background="#99CCFF")
    r_floor.configure(disabledforeground="#a3a3a3")
    r_floor.configure(font=font12)
    r_floor.configure(foreground="#000000")
    r_floor.configure(highlightbackground="#d9d9d9")
    r_floor.configure(highlightcolor="black")
    r_floor.configure(text='''Room Floor''')
    r_floor.configure(width=74)

    floor = Label(room_frame)
    floor.place(relx=0.276, rely=0.69, height=21, width=100, bordermode='ignore')
    floor.configure(activebackground="#f9f9f9")
    floor.configure(activeforeground="black")
    floor.configure(background="#99CCFF")
    floor.configure(disabledforeground="#a3a3a3")
    floor.configure(foreground="#000000")
    floor.configure(highlightbackground="#d9d9d9")
    floor.configure(highlightcolor="black")
    floor.configure(text=fl)

    #    TSeparator1 =Separator(room_frame)
    #    TSeparator1.place(relx=0.474, rely=0.172, relheight=0.621, bordermode='ignore')
    #    TSeparator1.configure(orient="vertical")

    r_phone = Label(room_frame)
    r_phone.place(relx=0.526, rely=0.207, height=23, width=85, bordermode='ignore')
    r_phone.configure(background="#99CCFF")
    r_phone.configure(disabledforeground="#a3a3a3")
    r_phone.configure(font=font12)
    r_phone.configure(foreground="#000000")
    r_phone.configure(text='''Room Phone''')

    phone = Label(room_frame)
    phone.place(relx=0.7, rely=0.207, height=21, width=120, bordermode='ignore')
    phone.configure(activebackground="#f9f9f9")
    phone.configure(activeforeground="black")
    phone.configure(background="#99CCFF")
    phone.configure(disabledforeground="#a3a3a3")
    phone.configure(foreground="#000000")
    phone.configure(highlightbackground="#d9d9d9")
    phone.configure(highlightcolor="black")
    phone.configure(text=ph)

    r_date_out = Label(room_frame)
    r_date_out.place(relx=0.526, rely=0.69, height=23, width=69, bordermode='ignore')
    r_date_out.configure(activebackground="#f9f9f9")
    r_date_out.configure(activeforeground="black")
    r_date_out.configure(background="#99CCFF")
    r_date_out.configure(disabledforeground="#a3a3a3")
    r_date_out.configure(font=font12)
    r_date_out.configure(foreground="#000000")
    r_date_out.configure(highlightbackground="#d9d9d9")
    r_date_out.configure(highlightcolor="black")
    r_date_out.configure(text='''Date Out''')
    r_date_out.configure(width=69)

    # show date ou from the hotel
    date_out = StringVar(root)
    d_out = Entry(room_frame)
    d_out.place(relx=0.763, rely=0.69, relheight=0.145, relwidth=0.2, bordermode='ignore')
    d_out.configure(textvariable=date_out)
    d_out.configure(takefocus="")
    d_out.configure(cursor="ibeam")

    r_date_in = Label(room_frame)
    r_date_in.place(relx=0.526, rely=0.448, height=23, width=59, bordermode='ignore')
    r_date_in.configure(activebackground="#f9f9f9")
    r_date_in.configure(activeforeground="black")
    r_date_in.configure(background="#99CCFF")
    r_date_in.configure(disabledforeground="#a3a3a3")
    r_date_in.configure(font=font12)
    r_date_in.configure(foreground="#000000")
    r_date_in.configure(highlightbackground="#d9d9d9")
    r_date_in.configure(highlightcolor="black")
    r_date_in.configure(text='''Date In''')
    r_date_in.configure(width=59)
    # show date in to hotel
    date_in = StringVar(root)
    d_in = Entry(room_frame)
    d_in.place(relx=0.763, rely=0.448, relheight=0.145, relwidth=0.2, bordermode='ignore')
    d_in.configure(textvariable=date_in)
    d_in.configure(width=76)
    d_in.configure(takefocus="")
    d_in.configure(cursor="ibeam")

    # client information form
    client_frame = LabelFrame(root)
    client_frame.place(relx=0.025, rely=0.258, relheight=0.734, relwidth=0.952)
    client_frame.configure(relief='groove')
    client_frame.configure(foreground="black")
    client_frame.configure(text='''Client Information''')
    client_frame.configure(background="#99CCFF")
    client_frame.configure(width=380)

    label1 = Label(client_frame)
    label1.place(relx=0.105, rely=0.066, height=23, width=73, bordermode='ignore')
    label1.configure(background="#99CCFF")
    label1.configure(disabledforeground="#a3a3a3")
    label1.configure(font=font12)
    label1.configure(foreground="#000000")
    label1.configure(text='''First Name''')

    label12 = Label(client_frame)
    label12.place(relx=0.105, rely=0.78, height=23, width=49
                  , bordermode='ignore')
    label12.configure(activebackground="#f9f9f9")
    label12.configure(activeforeground="black")
    label12.configure(background="#99CCFF")
    label12.configure(disabledforeground="#a3a3a3")
    label12.configure(font=font12)
    label12.configure(foreground="#000000")
    label12.configure(highlightbackground="#d9d9d9")
    label12.configure(highlightcolor="black")
    label12.configure(text='''Dinner''')
    label12.configure(width=49)

    label11 = Label(client_frame)
    label11.place(relx=0.105, rely=0.725, height=23, width=49
                  , bordermode='ignore')
    label11.configure(activebackground="#f9f9f9")
    label11.configure(activeforeground="black")
    label11.configure(background="#99CCFF")
    label11.configure(disabledforeground="#a3a3a3")
    label11.configure(font=font12)
    label11.configure(foreground="#000000")
    label11.configure(highlightbackground="#d9d9d9")
    label11.configure(highlightcolor="black")
    label11.configure(text='''Lunch''')
    label11.configure(width=49)

    label10 = Label(client_frame)
    label10.place(relx=0.105, rely=0.681, height=23, width=69
                  , bordermode='ignore')
    label10.configure(activebackground="#f9f9f9")
    label10.configure(activeforeground="black")
    label10.configure(background="#99CCFF")
    label10.configure(disabledforeground="#a3a3a3")
    label10.configure(font=font12)
    label10.configure(foreground="#000000")
    label10.configure(highlightbackground="#d9d9d9")
    label10.configure(highlightcolor="black")
    label10.configure(text='''Breakfast''')
    label10.configure(width=69)

    label9 = Label(client_frame)
    label9.place(relx=0.105, rely=0.615, height=23, width=39
                 , bordermode='ignore')
    label9.configure(activebackground="#f9f9f9")
    label9.configure(activeforeground="black")
    label9.configure(background="#99CCFF")
    label9.configure(disabledforeground="#a3a3a3")
    label9.configure(font=font12)
    label9.configure(foreground="#000000")
    label9.configure(highlightbackground="#d9d9d9")
    label9.configure(highlightcolor="black")
    label9.configure(text='''Type''')

    label8 = Label(client_frame)
    label8.place(relx=0.105, rely=0.484, height=23, width=79
                 , bordermode='ignore')
    label8.configure(activebackground="#f9f9f9")
    label8.configure(activeforeground="black")
    label8.configure(background="#99CCFF")
    label8.configure(disabledforeground="#a3a3a3")
    label8.configure(font=font12)
    label8.configure(foreground="#000000")
    label8.configure(highlightbackground="#d9d9d9")
    label8.configure(highlightcolor="black")
    label8.configure(takefocus="")
    label8.configure(text='''Comments''')
    label8.configure(width=79)

    label7 = Label(client_frame)
    label7.place(relx=0.092, rely=0.363, height=23, width=59
                 , bordermode='ignore')
    label7.configure(activebackground="#f9f9f9")
    label7.configure(activeforeground="black")
    label7.configure(background="#99CCFF")
    label7.configure(disabledforeground="#a3a3a3")
    label7.configure(font=font12)
    label7.configure(foreground="#000000")
    label7.configure(highlightbackground="#d9d9d9")
    label7.configure(highlightcolor="black")
    label7.configure(text='''Card ID''')
    label7.configure(width=59)

    label6 = Label(client_frame)
    label6.place(relx=0.105, rely=0.308, height=23, width=49
                 , bordermode='ignore')
    label6.configure(activebackground="#f9f9f9")
    label6.configure(activeforeground="black")
    label6.configure(background="#99CCFF")
    label6.configure(disabledforeground="#a3a3a3")
    label6.configure(font=font12)
    label6.configure(foreground="#000000")
    label6.configure(highlightbackground="#d9d9d9")
    label6.configure(highlightcolor="black")
    label6.configure(text='''Phone''')
    label6.configure(width=49)

    label5 = Label(client_frame)
    label5.place(relx=0.105, rely=0.264, height=23, width=49
                 , bordermode='ignore')
    label5.configure(activebackground="#f9f9f9")
    label5.configure(activeforeground="black")
    label5.configure(background="#99CCFF")
    label5.configure(disabledforeground="#a3a3a3")
    label5.configure(font=font12)
    label5.configure(foreground="#000000")
    label5.configure(highlightbackground="#d9d9d9")
    label5.configure(highlightcolor="black")
    label5.configure(text='''Adress''')
    label5.configure(width=49)

    label4 = Label(client_frame)
    label4.place(relx=0.105, rely=0.22, height=23, width=39
                 , bordermode='ignore')
    label4.configure(activebackground="#f9f9f9")
    label4.configure(activeforeground="black")
    label4.configure(background="#99CCFF")
    label4.configure(disabledforeground="#a3a3a3")
    label4.configure(font=font12)
    label4.configure(foreground="#000000")
    label4.configure(highlightbackground="#d9d9d9")
    label4.configure(highlightcolor="black")
    label4.configure(text='''Email''')

    label3 = Label(client_frame)
    label3.place(relx=0.092, rely=0.165, height=23, width=59
                 , bordermode='ignore')
    label3.configure(activebackground="#f9f9f9")
    label3.configure(activeforeground="black")
    label3.configure(background="#99CCFF")
    label3.configure(disabledforeground="#a3a3a3")
    label3.configure(font=font12)
    label3.configure(foreground="#000000")
    label3.configure(highlightbackground="#d9d9d9")
    label3.configure(highlightcolor="black")
    label3.configure(text='''Country''')
    label3.configure(width=59)

    label2 = Label(client_frame)
    label2.place(relx=0.105, rely=0.121, height=23, width=69
                 , bordermode='ignore')
    label2.configure(activebackground="#f9f9f9")
    label2.configure(activeforeground="black")
    label2.configure(background="#99CCFF")
    label2.configure(disabledforeground="#a3a3a3")
    label2.configure(font=font12)
    label2.configure(foreground="#000000")
    label2.configure(highlightbackground="#d9d9d9")
    label2.configure(highlightcolor="black")
    label2.configure(text='''Last Name''')
    label2.configure(width=69)

    Nom = StringVar(root)
    Champ = Entry(client_frame)
    Champ.place(relx=0.421, rely=0.066, height=20, relwidth=0.537
                , bordermode='ignore')
    Champ.configure(background="white")
    Champ.configure(disabledforeground="#a3a3a3")
    Champ.configure(font=font10)
    Champ.configure(foreground="#000000")
    Champ.configure(insertbackground="black")
    Champ.configure(textvariable=Nom)
    Champ.configure(width=204)

    card = StringVar(root)
    Champ7 = Entry(client_frame)
    Champ7.place(relx=0.421, rely=0.363, height=20, relwidth=0.537
                 , bordermode='ignore')
    Champ7.configure(background="white")
    Champ7.configure(disabledforeground="#a3a3a3")
    Champ7.configure(font=font10)
    Champ7.configure(foreground="#000000")
    Champ7.configure(highlightbackground="#d9d9d9")
    Champ7.configure(highlightcolor="black")
    Champ7.configure(insertbackground="black")
    Champ7.configure(selectbackground="#c4c4c4")
    Champ7.configure(selectforeground="black")
    Champ7.configure(textvariable=card)

    country = StringVar(root)
    Champ3 = Entry(client_frame)
    Champ3.place(relx=0.421, rely=0.165, height=20, relwidth=0.537
                 , bordermode='ignore')
    Champ3.configure(background="white")
    Champ3.configure(disabledforeground="#a3a3a3")
    Champ3.configure(font=font10)
    Champ3.configure(foreground="#000000")
    Champ3.configure(highlightbackground="#d9d9d9")
    Champ3.configure(highlightcolor="black")
    Champ3.configure(insertbackground="black")
    Champ3.configure(selectbackground="#c4c4c4")
    Champ3.configure(selectforeground="black")
    Champ3.configure(textvariable=country)

    adr = StringVar(root)
    Champ5 = Entry(client_frame)
    Champ5.place(relx=0.421, rely=0.264, height=20, relwidth=0.537
                 , bordermode='ignore')
    Champ5.configure(background="white")
    Champ5.configure(disabledforeground="#a3a3a3")
    Champ5.configure(font=font10)
    Champ5.configure(foreground="#000000")
    Champ5.configure(highlightbackground="#d9d9d9")
    Champ5.configure(highlightcolor="black")
    Champ5.configure(insertbackground="black")
    Champ5.configure(selectbackground="#c4c4c4")
    Champ5.configure(selectforeground="black")
    Champ5.configure(textvariable=adr)

    email = StringVar(root)
    Champ4 = Entry(client_frame)
    Champ4.place(relx=0.421, rely=0.209, height=20, relwidth=0.537
                 , bordermode='ignore')
    Champ4.configure(background="white")
    Champ4.configure(disabledforeground="#a3a3a3")
    Champ4.configure(font=font10)
    Champ4.configure(foreground="#000000")
    Champ4.configure(highlightbackground="#d9d9d9")
    Champ4.configure(highlightcolor="black")
    Champ4.configure(insertbackground="black")
    Champ4.configure(selectbackground="#c4c4c4")
    Champ4.configure(selectforeground="black")
    Champ4.configure(textvariable=email)

    Prenom = StringVar(root)
    Champ2 = Entry(client_frame)
    Champ2.place(relx=0.421, rely=0.121, height=20, relwidth=0.537
                 , bordermode='ignore')
    Champ2.configure(background="white")
    Champ2.configure(disabledforeground="#a3a3a3")
    Champ2.configure(font=font10)
    Champ2.configure(foreground="#000000")
    Champ2.configure(highlightbackground="#d9d9d9")
    Champ2.configure(highlightcolor="black")
    Champ2.configure(insertbackground="black")
    Champ2.configure(selectbackground="#c4c4c4")
    Champ2.configure(selectforeground="black")
    Champ2.configure(textvariable=Prenom)

    pho = StringVar(root)
    Champ6 = Entry(client_frame)
    Champ6.place(relx=0.421, rely=0.308, height=20, relwidth=0.537
                 , bordermode='ignore')
    Champ6.configure(background="white")
    Champ6.configure(disabledforeground="#a3a3a3")
    Champ6.configure(font=font10)
    Champ6.configure(foreground="#000000")
    Champ6.configure(highlightbackground="#d9d9d9")
    Champ6.configure(highlightcolor="black")
    Champ6.configure(insertbackground="black")
    Champ6.configure(selectbackground="#c4c4c4")
    Champ6.configure(selectforeground="black")
    Champ6.configure(textvariable=pho)

    text_field = Text(client_frame)
    text_field.place(relx=0.421, rely=0.44, relheight=0.141
                     , relwidth=0.537, bordermode='ignore')
    text_field.configure(background="white")
    text_field.configure(font=font9)
    text_field.configure(foreground="black")
    text_field.configure(highlightbackground="#d9d9d9")
    text_field.configure(highlightcolor="black")
    text_field.configure(insertbackground="black")
    text_field.configure(selectbackground="#c4c4c4")
    text_field.configure(selectforeground="black")
    text_field.configure(width=204)
    text_field.configure(wrap='word')

    ty = StringVar()
    person = Radiobutton(client_frame)
    person.place(relx=0.474, rely=0.615, relheight=0.055, relwidth=0.192, bordermode='ignore')
    person.configure(activebackground="#ececec")
    person.configure(activeforeground="#000000")
    person.configure(background="#99CCFF")
    person.configure(disabledforeground="#a3a3a3")
    person.configure(foreground="#000000")
    person.configure(highlightbackground="#d9d9d9")
    person.configure(highlightcolor="black")
    person.configure(justify='left')
    person.configure(text='''Personal''')
    person.configure(variable=ty, value="personal")


    business = Radiobutton(client_frame)
    business.place(relx=0.684, rely=0.615, relheight=0.055, relwidth=0.192, bordermode='ignore')
    business.configure(activebackground="#ececec")
    business.configure(activeforeground="#000000")
    business.configure(background="#99CCFF")
    business.configure(disabledforeground="#a3a3a3")
    business.configure(foreground="#000000")
    business.configure(highlightbackground="#d9d9d9")
    business.configure(highlightcolor="black")
    business.configure(justify='left')
    business.configure(text='''Business''')
    business.configure(variable=ty, value="business")

    #client_type = "null"
    #if (ty.get() == 1):
    #    client_type = 'Person'
    #if (ty.get() == 2):
    #    client_type = 'business'

    # option lists
    # get breakfast meals
    resultats = queries.get_db_cond("meals", "type", "breakfast")
    OPT1 = []
    for lig in resultats:
        OPT1.append(lig[0])

    # get lunch meals

    resultats = queries.get_db_cond("meals", "type", "lunch")
    OPT2 = []
    for lig in resultats:
        OPT2.append(lig[0])

    # get dinner meals

    resultats = queries.get_db_cond("meals", "type", "dinner")
    OPT3 = []
    for lig in resultats:
        OPT3.append(lig[0])

    Label4 = Label(client_frame)
    Label4.place(relx=0.370, rely=0.681, height=21, width=114
                 , bordermode='ignore')
    Label4.configure(background="#d9d9d9")
    Label4.configure(disabledforeground="#a3a3a3")
    Label4.configure(foreground="#000000")
    Label4.configure(text='''Breakfast''')
    Label4.configure(width=114)

    breakfast = StringVar(root)
    breakfast.set(OPT1[0])  # default value
    breakf = OptionMenu(client_frame, breakfast, *OPT1)
    breakf.place(relx=0.630, rely=0.681, height=21, width=140, bordermode='ignore')

    Label5 = Label(client_frame)
    Label5.place(relx=0.370, rely=0.725, height=21, width=114
                 , bordermode='ignore')
    Label5.configure(background="#d9d9d9")
    Label5.configure(disabledforeground="#a3a3a3")
    Label5.configure(foreground="#000000")
    Label5.configure(text='''Lunch''')
    Label5.configure(width=114)

    lunch = StringVar(root)
    lunch.set(OPT2[0])  # default value
    lnch = OptionMenu(client_frame, lunch, *OPT2)
    lnch.place(relx=0.630, rely=0.725, height=21, width=140, bordermode='ignore')

    Label6 = Label(client_frame)
    Label6.place(relx=0.370, rely=0.78, height=21, width=114
                 , bordermode='ignore')
    Label6.configure(background="#d9d9d9")
    Label6.configure(disabledforeground="#a3a3a3")
    Label6.configure(foreground="#000000")
    Label6.configure(text='''Dinner''')
    Label6.configure(width=114)

    dinner = StringVar(root)
    dinner.set(OPT3[0])  # default value
    din = OptionMenu(client_frame, dinner, *OPT3)
    din.place(relx=0.630, rely=0.78, height=21, width=140, bordermode='ignore')

    # les bouttons
    bouton1 = Button(client_frame, command=lambda: queries.Validate(Nom.get(), Prenom.get(), country.get(), email.get(),
                                                                    adr.get(),
                                                                    pho.get(), card.get(), text_field.get("1.0", END),
                                                                    ty.get(), breakfast.get(),
                                                                    lunch.get(), dinner.get(), date_in.get(),
                                                                    date_out.get(),
                                                                    number))

    bouton1.place(relx=0.132, rely=0.879, height=44, width=127
                  , bordermode='ignore')
    bouton1.configure(activebackground="#ececec")
    bouton1.configure(activeforeground="#000000")
    bouton1.configure(background="#d9d9d9")
    bouton1.configure(disabledforeground="#a3a3a3")
    bouton1.configure(font=font14)
    bouton1.configure(foreground="#278913")
    bouton1.configure(highlightbackground="#d9d9d9")
    bouton1.configure(highlightcolor="black")
    bouton1.configure(pady="0")
    bouton1.configure(text='''Validate''')
    bouton1.configure(width=127)

    bouton2 = Button(client_frame,
                     command=lambda: effacer(Champ, Champ2, Champ3, Champ4, Champ5, Champ6, Champ7, text_field, person,
                                             business))
    bouton2.place(relx=0.605, rely=0.879, height=44, width=117
                  , bordermode='ignore')
    bouton2.configure(activebackground="#ececec")
    bouton2.configure(activeforeground="#000000")
    bouton2.configure(background="#d9d9d9")
    bouton2.configure(disabledforeground="#a3a3a3")
    bouton2.configure(font=font14)
    bouton2.configure(foreground="#961400")
    bouton2.configure(highlightbackground="#d9d9d9")
    bouton2.configure(highlightcolor="black")
    bouton2.configure(pady="0")
    bouton2.configure(text='''Reset''')
    bouton2.configure(width=117)


def effacer(Champ, Champ2, Champ3, Champ4, Champ5, Champ6, Champ7, Champ8, person, business):
    Champ.delete(0, END)
    Champ2.delete(0, END)
    Champ3.delete(0, END)
    Champ4.delete(0, END)
    Champ5.delete(0, END)
    Champ6.delete(0, END)
    Champ7.delete(0, END)
    Champ8.delete(0, END)
    person.deselect()
    business.deselect()

