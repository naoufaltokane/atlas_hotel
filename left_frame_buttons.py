from tkinter import *
import query as queries


# fonction add meal
def add_meal():
    _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
    _fgcolor = '#000000'  # X11 color: 'black'
    _compcolor = '#d9d9d9'  # X11 color: 'gray85'
    _ana1color = '#d9d9d9'  # X11 color: 'gray85'
    _ana2color = '#ececec'  # Closest X11 color: 'gray92'
    font11 = "-family {Segoe UI} -size 14 -weight bold -slant " \
             "roman -underline 0 -overstrike 0"
    font12 = "-family {Courier New} -size 14 -weight normal -slant" \
             " roman -underline 0 -overstrike 0"
    font13 = "-family {Segoe UI} -size 13 -weight normal -slant " \
             "roman -underline 0 -overstrike 0"

    root = Tk()
    root.geometry("360x370+458+130")
    root.title("Add Meal")
    root.configure(background="#99CCFF")

    fr = LabelFrame(root)
    fr.place(relx=0.0, rely=-0.014, relheight=0.986, relwidth=1.0)
    fr.configure(relief='groove')
    fr.configure(foreground="black")
    fr.configure(text='''Add a Meal''')
    fr.configure(background="#99CCFF")
    fr.configure(width=360)

    name = Label(fr)
    name.place(relx=0.069, rely=0.137, height=21, width=83
               , bordermode='ignore')
    name.configure(anchor='w')
    name.configure(background="#99CCFF")
    name.configure(disabledforeground="#a3a3a3")
    name.configure(font=font11)
    name.configure(foreground="#000000")
    name.configure(text='''Name''')
    name.configure(width=83)

    price = Label(fr)
    price.place(relx=0.069, rely=0.342, height=21, width=83
                , bordermode='ignore')
    price.configure(activebackground="#f9f9f9")
    price.configure(activeforeground="black")
    price.configure(anchor='w')
    price.configure(background="#99CCFF")
    price.configure(disabledforeground="#a3a3a3")
    price.configure(font=font11)
    price.configure(foreground="#000000")
    price.configure(highlightbackground="#d9d9d9")
    price.configure(highlightcolor="black")
    price.configure(text='''Price''')

    type_label = Label(fr)
    type_label.place(relx=0.069, rely=0.233, height=21, width=103
                     , bordermode='ignore')
    type_label.configure(activebackground="#f9f9f9")
    type_label.configure(activeforeground="black")
    type_label.configure(anchor='w')
    type_label.configure(background="#99CCFF")
    type_label.configure(disabledforeground="#a3a3a3")
    type_label.configure(font=font11)
    type_label.configure(foreground="#000000")
    type_label.configure(highlightbackground="#d9d9d9")
    type_label.configure(highlightcolor="black")
    type_label.configure(text='''Meal Type''')
    type_label.configure(width=103)

    OPT = ["breakfast", "lunch", "dinner"]
    type = StringVar(root)
    type.set(OPT[0])  # default value
    type_list = OptionMenu(fr, type, *OPT)
    type_list.place(relx=0.417, rely=0.200)

    m_name = StringVar(root)
    name_entry = Entry(fr)
    name_entry.place(relx=0.403, rely=0.123, height=30, relwidth=0.483
                     , bordermode='ignore')
    name_entry.configure(background="white")
    name_entry.configure(disabledforeground="#a3a3a3")
    name_entry.configure(font=font12)
    name_entry.configure(foreground="#000000")
    name_entry.configure(insertbackground="black")
    name_entry.configure(width=174)
    name_entry.configure(textvariable=m_name)

    pr = StringVar(root)
    price_entry = Entry(fr)
    price_entry.place(relx=0.417, rely=0.329, height=30, relwidth=0.483
                      , bordermode='ignore')
    price_entry.configure(background="white")
    price_entry.configure(disabledforeground="#a3a3a3")
    price_entry.configure(font=font12)
    price_entry.configure(foreground="#000000")
    price_entry.configure(highlightbackground="#d9d9d9")
    price_entry.configure(highlightcolor="black")
    price_entry.configure(insertbackground="black")
    price_entry.configure(selectbackground="#c4c4c4")
    price_entry.configure(selectforeground="black")
    price_entry.configure(textvariable=pr)

    description = Label(fr)
    description.place(relx=0.069, rely=0.479, height=21, width=123, bordermode='ignore')
    description.configure(activebackground="#f9f9f9")
    description.configure(activeforeground="black")
    description.configure(anchor='w')
    description.configure(background="#99CCFF")
    description.configure(disabledforeground="#a3a3a3")
    description.configure(font=font11)
    description.configure(foreground="#000000")
    description.configure(highlightbackground="#d9d9d9")
    description.configure(highlightcolor="black")
    description.configure(text='''Components''')
    description.configure(width=123)

    text_field = Text(fr)
    text_field.place(relx=0.417, rely=0.425, relheight=0.312, relwidth=0.483, bordermode='ignore')
    text_field.configure(background="white")
    text_field.configure(font=font13)
    text_field.configure(foreground="black")
    text_field.configure(highlightbackground="#d9d9d9")
    text_field.configure(highlightcolor="black")
    text_field.configure(insertbackground="black")
    text_field.configure(selectbackground="#c4c4c4")
    text_field.configure(selectforeground="black")
    text_field.configure(width=174)
    text_field.configure(wrap='word')

    Button1 = Button(fr,
                     command=lambda: queries.valid_meal(m_name.get(), text_field.get("1.0", END), pr.get(), type.get()))
    Button1.place(relx=0.222, rely=0.822, height=44, width=177
                  , bordermode='ignore')
    Button1.configure(activebackground="#ececec")
    Button1.configure(activeforeground="#000000")
    Button1.configure(background="#d9d9d9")
    Button1.configure(disabledforeground="#a3a3a3")
    Button1.configure(font=font11)
    Button1.configure(foreground="#1a9126")
    Button1.configure(highlightbackground="#d9d9d9")
    Button1.configure(highlightcolor="black")
    Button1.configure(pady="0")
    Button1.configure(text='''Validate''')
    Button1.configure(width=177)


# fonction add event
def add_event(Frame):
    _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
    _fgcolor = '#000000'  # X11 color: 'black'


    _compcolor = '#d9d9d9'  # X11 color: 'gray85'
    _ana1color = '#d9d9d9'  # X11 color: 'gray85'
    _ana2color = '#ececec'  # Closest X11 color: 'gray92'
    font11 = "-family {Segoe UI} -size 14 -weight bold -slant " \
             "roman -underline 0 -overstrike 0"
    font12 = "-family {Courier New} -size 14 -weight normal -slant" \
             " roman -underline 0 -overstrike 0"
    font13 = "-family {Segoe UI} -size 13 -weight normal -slant " \
             "roman -underline 0 -overstrike 0"

    root = Tk()
    root.geometry("350x360+568+155")
    root.title("Add An Event")
    root.configure(background="#99CCFF")

    fr = LabelFrame(root)
    fr.place(relx=0.0, rely=-0.014, relheight=1.014, relwidth=1.0)
    fr.configure(relief='groove')
    fr.configure(foreground="black")
    fr.configure(text='''Add an Event''')
    fr.configure(background="#99CCFF")
    fr.configure(width=350)

    name = Label(fr)
    name.place(relx=0.086, rely=0.137, height=21, width=83, bordermode='ignore')
    name.configure(anchor='w')
    name.configure(background="#99CCFF")
    name.configure(disabledforeground="#a3a3a3")
    name.configure(font=font11)
    name.configure(foreground="#000000")
    name.configure(text='''Name''')
    name.configure(width=83)

    local = Label(fr)
    local.place(relx=0.086, rely=0.342, height=21, width=83, bordermode='ignore')
    local.configure(activebackground="#f9f9f9")
    local.configure(activeforeground="black")
    local.configure(anchor='w')
    local.configure(background="#99CCFF")
    local.configure(disabledforeground="#a3a3a3")
    local.configure(font=font11)
    local.configure(foreground="#000000")
    local.configure(highlightbackground="#d9d9d9")
    local.configure(highlightcolor="black")
    local.configure(text='''Local''')

    date = Label(fr)
    date.place(relx=0.086, rely=0.233, height=21, width=83
               , bordermode='ignore')
    date.configure(activebackground="#f9f9f9")
    date.configure(activeforeground="black")
    date.configure(anchor='w')
    date.configure(background="#99CCFF")
    date.configure(disabledforeground="#a3a3a3")
    date.configure(font=font11)
    date.configure(foreground="#000000")
    date.configure(highlightbackground="#d9d9d9")
    date.configure(highlightcolor="black")
    date.configure(text='''Date''')

    name_entry = Entry(fr)
    ename = StringVar(root)
    name_entry.place(relx=0.414, rely=0.123, height=30, relwidth=0.497, bordermode='ignore')
    name_entry.configure(background="white")
    name_entry.configure(disabledforeground="#a3a3a3")
    name_entry.configure(font=font12)
    name_entry.configure(foreground="#000000")
    name_entry.configure(insertbackground="black")
    name_entry.configure(width=174)
    name_entry.configure(textvariable=ename)

    lcl = Entry(fr)
    local_entry = Entry(fr)
    local_entry.place(relx=0.414, rely=0.329, height=30, relwidth=0.497, bordermode='ignore')
    local_entry.configure(background="white")
    local_entry.configure(disabledforeground="#a3a3a3")
    local_entry.configure(font=font12)
    local_entry.configure(foreground="#000000")
    local_entry.configure(highlightbackground="#d9d9d9")
    local_entry.configure(highlightcolor="black")
    local_entry.configure(insertbackground="black")
    local_entry.configure(selectbackground="#c4c4c4")
    local_entry.configure(selectforeground="black")
    local_entry.configure(textvariable=lcl)

    dt = StringVar(root)
    date_entry = Entry(fr)
    date_entry.place(relx=0.414, rely=0.219, height=30, relwidth=0.497, bordermode='ignore')
    date_entry.configure(background="white")
    date_entry.configure(disabledforeground="#a3a3a3")
    date_entry.configure(font=font12)
    date_entry.configure(foreground="#000000")
    date_entry.configure(highlightbackground="#d9d9d9")
    date_entry.configure(highlightcolor="black")
    date_entry.configure(insertbackground="black")
    date_entry.configure(selectbackground="#c4c4c4")
    date_entry.configure(selectforeground="black")
    date_entry.configure(textvariable=dt)

    description = Label(fr)
    description.place(relx=0.086, rely=0.479, height=21, width=113, bordermode='ignore')
    description.configure(activebackground="#f9f9f9")
    description.configure(activeforeground="black")
    description.configure(anchor='w')
    description.configure(background="#99CCFF")
    description.configure(disabledforeground="#a3a3a3")
    description.configure(font=font11)
    description.configure(foreground="#000000")
    description.configure(highlightbackground="#d9d9d9")
    description.configure(highlightcolor="black")
    description.configure(text='''Description''')
    description.configure(width=113)

    text_field = Text(fr)
    text_field.place(relx=0.414, rely=0.425, relheight=0.312, relwidth=0.497, bordermode='ignore')
    text_field.configure(background="white")
    text_field.configure(font=font13)
    text_field.configure(foreground="black")
    text_field.configure(highlightbackground="#d9d9d9")
    text_field.configure(highlightcolor="black")
    text_field.configure(insertbackground="black")
    text_field.configure(selectbackground="#c4c4c4")
    text_field.configure(selectforeground="black")
    text_field.configure(width=174)
    text_field.configure(wrap='word')

    Button1 = Button(fr, command=lambda: queries.valid_event(ename.get(), dt.get(), text_field.get("1.0", END), lcl.get()))
    Button1.place(relx=0.229, rely=0.822, height=44, width=177, bordermode='ignore')
    Button1.configure(activebackground="#ececec")
    Button1.configure(activeforeground="#000000")
    Button1.configure(background="#d9d9d9")
    Button1.configure(disabledforeground="#a3a3a3")
    Button1.configure(font=font11)
    Button1.configure(foreground="#1a9126")
    Button1.configure(highlightbackground="#d9d9d9")
    Button1.configure(highlightcolor="black")
    Button1.configure(pady="0")
    Button1.configure(text='''Validate''')
    Button1.configure(width=177)

#window to fill complain form

def add_complain(id):
    _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
    _fgcolor = '#000000'  # X11 color: 'black'
    _compcolor = '#d9d9d9'  # X11 color: 'gray85'
    _ana1color = '#d9d9d9'  # X11 color: 'gray85'
    _ana2color = '#ececec'  # Closest X11 color: 'gray92'
    font11 = "-family {Segoe UI} -size 14 -weight bold -slant " \
             "roman -underline 0 -overstrike 0"
    font12 = "-family {Courier New} -size 14 -weight normal -slant" \
             " roman -underline 0 -overstrike 0"
    font13 = "-family {Segoe UI} -size 13 -weight normal -slant " \
             "roman -underline 0 -overstrike 0"

    root = Tk()
    root.title('Fill A Complain')
    root.geometry("360x370+539+177")
    root.configure(background="#99CCFF")
    root.configure(highlightbackground="#d9d9d9")
    root.configure(highlightcolor="black")

    fr = LabelFrame(root)
    fr.place(relx=0.0, rely=-0.014, relheight=0.986
             , relwidth=1.0)
    fr.configure(relief='groove')
    fr.configure(foreground="black")
    fr.configure(text='''Fill a Complain''')
    fr.configure(background="#99CCFF")
    fr.configure(highlightbackground="#d9d9d9")
    fr.configure(highlightcolor="black")
    fr.configure(width=360)

    resultats = queries.get_db_cond("clients", "id", id)
    for lig in resultats:
        room_number = str(lig[9])
        fname = str(lig[0])
        lname = str(lig[1])

    name = Label(fr)
    name.place(relx=0.069, rely=0.137, height=21, width=113
               , bordermode='ignore')
    name.configure(activebackground="#f9f9f9")
    name.configure(activeforeground="black")
    name.configure(anchor='w')
    name.configure(background="#99CCFF")
    name.configure(disabledforeground="#a3a3a3")
    name.configure(font=font11)
    name.configure(foreground="#000000")
    name.configure(highlightbackground="#d9d9d9")
    name.configure(highlightcolor="black")
    name.configure(text='''Client Name''')
    name.configure(width=113)

    l_name = Label(fr)
    l_name.place(relx=0.417, rely=0.123, height=30, relwidth=0.483
                 , bordermode='ignore')
    l_name.configure(background="#99CCFF")
    l_name.configure(disabledforeground="#a3a3a3")
    l_name.configure(font=font12)
    l_name.configure(foreground="#000000")
    l_name.configure(highlightbackground="#d9d9d9")
    l_name.configure(highlightcolor="black")
    l_name.configure(text=fname + " " + lname)

    room = Label(fr)
    room.place(relx=0.069, rely=0.233, height=21, width=113
               , bordermode='ignore')
    room.configure(activebackground="#f9f9f9")
    room.configure(activeforeground="black")
    room.configure(anchor='w')
    room.configure(background="#99CCFF")
    room.configure(disabledforeground="#a3a3a3")
    room.configure(font=font11)
    room.configure(foreground="#000000")
    room.configure(highlightbackground="#d9d9d9")
    room.configure(highlightcolor="black")
    room.configure(text='''Room N°''')
    room.configure(width=113)

    l_room = Label(fr)
    l_room.place(relx=0.417, rely=0.219, height=30, relwidth=0.483
                 , bordermode='ignore')
    l_room.configure(background="#99CCFF")
    l_room.configure(disabledforeground="#a3a3a3")
    l_room.configure(font=font12)
    l_room.configure(foreground="#000000")
    l_room.configure(highlightbackground="#d9d9d9")
    l_room.configure(highlightcolor="black")
    l_room.configure(text=room_number)

    subject = Label(fr)
    subject.place(relx=0.069, rely=0.342, height=21, width=83
                  , bordermode='ignore')
    subject.configure(activebackground="#f9f9f9")
    subject.configure(activeforeground="black")
    subject.configure(anchor='w')
    subject.configure(background="#99CCFF")
    subject.configure(disabledforeground="#a3a3a3")
    subject.configure(font=font11)
    subject.configure(foreground="#000000")
    subject.configure(highlightbackground="#d9d9d9")
    subject.configure(highlightcolor="black")
    subject.configure(text='''Subject''')

    subj = StringVar(fr)
    subject_entry = Entry(fr)
    subject_entry.place(relx=0.417, rely=0.329, height=30, relwidth=0.483, bordermode='ignore')
    subject_entry.configure(background="white")
    subject_entry.configure(disabledforeground="#a3a3a3")
    subject_entry.configure(font=font12)
    subject_entry.configure(foreground="#000000")
    subject_entry.configure(highlightbackground="#d9d9d9")
    subject_entry.configure(highlightcolor="black")
    subject_entry.configure(textvariable=subj)

    description = Label(fr)
    description.place(relx=0.069, rely=0.479, height=21, width=123
                      , bordermode='ignore')
    description.configure(activebackground="#f9f9f9")
    description.configure(activeforeground="black")
    description.configure(anchor='w')
    description.configure(background="#99CCFF")
    description.configure(disabledforeground="#a3a3a3")
    description.configure(font=font11)
    description.configure(foreground="#000000")
    description.configure(highlightbackground="#d9d9d9")
    description.configure(highlightcolor="black")
    description.configure(text='''Description''')

    text_field = Text(fr)
    text_field.place(relx=0.417, rely=0.425, relheight=0.312, relwidth=0.483, bordermode='ignore')
    text_field.configure(background="white")
    text_field.configure(font=font13)
    text_field.configure(foreground="black")
    text_field.configure(highlightbackground="#d9d9d9")
    text_field.configure(highlightcolor="black")
    text_field.configure(width=174)
    text_field.configure(wrap='word')

    BtnValidate = Button(fr, command=lambda: queries.valid_report(subj.get(), text_field.get("1.0", END), id))
    BtnValidate.place(relx=0.222, rely=0.822, height=44, width=177, bordermode='ignore')
    BtnValidate.configure(activebackground="#ececec")
    BtnValidate.configure(activeforeground="#000000")
    BtnValidate.configure(background="#d9d9d9")
    BtnValidate.configure(disabledforeground="#a3a3a3")
    BtnValidate.configure(font=font11)
    BtnValidate.configure(foreground="#1a9126")
    BtnValidate.configure(highlightbackground="#d9d9d9")
    BtnValidate.configure(highlightcolor="black")
    BtnValidate.configure(pady="0")
    BtnValidate.configure(text='''Validate''')


#hotel policy window
def get_policy():

    root = Tk()
    root.title('Hotel Policy')
    root.geometry('{}x{}'.format(918, 570))

    # layout all of the main containers
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.configure(background="#99CCFF")


    fr = LabelFrame(root, bg='#99CCFF', text='Hotel Policy', width=900, height=700, pady=3, bd=4)
    fr.grid(row=0, sticky="ew")

    resultats = queries.get_from_db("policy")
    i = 0
    for lig in resultats:
        Label(fr, text=str(lig[0]), bg='#2894FF', font="Times", width=100).grid(column=0, row=i, sticky='nw')
        Label(fr, text=str(lig[1]), bg='#99CCFF', wraplength=777, justify=LEFT).grid(column=0, row=i+2, sticky='nw')
        i += 4
