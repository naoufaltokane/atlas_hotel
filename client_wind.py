from tkinter import *
import query as queries
from tkinter import messagebox
from datetime import date

_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = '#d9d9d9'  # X11 color: 'gray85'
_ana1color = '#d9d9d9'  # X11 color: 'gray85'
_ana2color = '#ececec'  # Closest X11 color: 'gray92'
font11 = "-family {Segoe UI} -size 9 -weight bold -slant roman" \
         " -underline 0 -overstrike 0"
font9 = "-family {Segoe UI} -size 9 -weight normal -slant " \
        "roman -underline 0 -overstrike 0"


# function calcul nbr of days of resident
def nbr_days(date1, date2):
    d1 = date(int(date1[2]), int(date1[1]), int(date1[0]))
    d2 = date(int(date2[2]), int(date2[1]), int(date2[0]))
    delta = d1 - d2
    return delta.days


# client info and invoice
def aff_client_info(idd):
    root = Tk()
    root.geometry("542x632+387+23")
    root.title("Client Reservation Information")
    root.configure(background="#99CCFF")

    # get information from db
    resultats = queries.get_db_cond("clients", "id", idd)
    for lig in resultats:
        fname = str(lig[0])
        lname = str(lig[1])
        country = str(lig[2])
        mail = str(lig[3])
        adr = str(lig[4])
        phone = str(lig[5])
        card = str(lig[6])
        type = str(lig[8])
        com = str(lig[7])
        room = str(lig[9])
        inn = str(lig[13])
        out = str(lig[14])
        breakfast = str(lig[10])
        lunch = str(lig[11])
        dinner = str(lig[12])

    # get breakfast price
    res = queries.get_db_2cond("meals", "type", "name", "breakfast", breakfast)
    br_price = res[2]

    # get lunch price
    res = queries.get_db_2cond("meals", "type", "name", "lunch", lunch)
    lnch_price = res[2]

    # get dinner price
    res = queries.get_db_2cond("meals", "type", "name", "dinner", dinner)
    din_price = res[2]

    info_frame = LabelFrame(root)
    info_frame.place(relx=0.037, rely=0.032, relheight=0.403, relwidth=0.923)
    info_frame.configure(relief='groove')
    info_frame.configure(foreground="black")
    info_frame.configure(text='''Reservation Information''')
    info_frame.configure(background="#99CCFF")
    info_frame.configure(width=500)

    l1_nom = Label(info_frame)
    l1_nom.place(relx=0.04, rely=0.078, height=21, width=66
                 , bordermode='ignore')
    l1_nom.configure(background="#99CCFF")
    l1_nom.configure(disabledforeground="#a3a3a3")
    l1_nom.configure(font=font11)
    l1_nom.configure(foreground="#000000")
    l1_nom.configure(text='''First Name''')

    l1_prenom = Label(info_frame)
    l1_prenom.place(relx=0.04, rely=0.176, height=21, width=65
                    , bordermode='ignore')
    l1_prenom.configure(activebackground="#f9f9f9")
    l1_prenom.configure(activeforeground="black")
    l1_prenom.configure(background="#99CCFF")
    l1_prenom.configure(disabledforeground="#a3a3a3")
    l1_prenom.configure(font=font11)
    l1_prenom.configure(foreground="#000000")
    l1_prenom.configure(highlightbackground="#d9d9d9")
    l1_prenom.configure(highlightcolor="black")
    l1_prenom.configure(text='''Last Name''')
    l1_prenom.configure(width=65)

    l1_country = Label(info_frame)
    l1_country.place(relx=0.04, rely=0.275, height=21, width=55
                     , bordermode='ignore')
    l1_country.configure(activebackground="#f9f9f9")
    l1_country.configure(activeforeground="black")
    l1_country.configure(background="#99CCFF")
    l1_country.configure(disabledforeground="#a3a3a3")
    l1_country.configure(font=font11)
    l1_country.configure(foreground="#000000")
    l1_country.configure(highlightbackground="#d9d9d9")
    l1_country.configure(highlightcolor="black")
    l1_country.configure(text='''Country''')
    l1_country.configure(width=55)

    l1_mail = Label(info_frame)
    l1_mail.place(relx=0.04, rely=0.373, height=21, width=45
                  , bordermode='ignore')
    l1_mail.configure(activebackground="#f9f9f9")
    l1_mail.configure(activeforeground="black")
    l1_mail.configure(background="#99CCFF")
    l1_mail.configure(disabledforeground="#a3a3a3")
    l1_mail.configure(font=font11)
    l1_mail.configure(foreground="#000000")
    l1_mail.configure(highlightbackground="#d9d9d9")
    l1_mail.configure(highlightcolor="black")
    l1_mail.configure(text='''Email''')
    l1_mail.configure(width=45)

    l1_adr = Label(info_frame)
    l1_adr.place(relx=0.04, rely=0.471, height=21, width=45, bordermode='ignore')
    l1_adr.configure(activebackground="#f9f9f9")
    l1_adr.configure(activeforeground="black")
    l1_adr.configure(background="#99CCFF")
    l1_adr.configure(disabledforeground="#a3a3a3")
    l1_adr.configure(font=font11)
    l1_adr.configure(foreground="#000000")
    l1_adr.configure(highlightbackground="#d9d9d9")
    l1_adr.configure(highlightcolor="black")
    l1_adr.configure(text='''Address''')
    l1_adr.configure(width=45)

    l1_phone = Label(info_frame)
    l1_phone.place(relx=0.04, rely=0.569, height=21, width=45
                   , bordermode='ignore')
    l1_phone.configure(activebackground="#f9f9f9")
    l1_phone.configure(activeforeground="black")
    l1_phone.configure(background="#99CCFF")
    l1_phone.configure(disabledforeground="#a3a3a3")
    l1_phone.configure(font=font11)
    l1_phone.configure(foreground="#000000")
    l1_phone.configure(highlightbackground="#d9d9d9")
    l1_phone.configure(highlightcolor="black")
    l1_phone.configure(text='''Phone''')
    l1_phone.configure(width=45)

    l1_card = Label(info_frame)
    l1_card.place(relx=0.04, rely=0.686, height=21, width=55
                  , bordermode='ignore')
    l1_card.configure(activebackground="#f9f9f9")
    l1_card.configure(activeforeground="black")
    l1_card.configure(background="#99CCFF")
    l1_card.configure(disabledforeground="#a3a3a3")
    l1_card.configure(font=font11)
    l1_card.configure(foreground="#000000")
    l1_card.configure(highlightbackground="#d9d9d9")
    l1_card.configure(highlightcolor="black")
    l1_card.configure(text='''Card ID''')
    l1_card.configure(width=55)

    l1_type = Label(info_frame)
    l1_type.place(relx=0.04, rely=0.784, height=21, width=35
                  , bordermode='ignore')
    l1_type.configure(activebackground="#f9f9f9")
    l1_type.configure(activeforeground="black")
    l1_type.configure(background="#99CCFF")
    l1_type.configure(disabledforeground="#a3a3a3")
    l1_type.configure(font=font11)
    l1_type.configure(foreground="#000000")
    l1_type.configure(highlightbackground="#d9d9d9")
    l1_type.configure(highlightcolor="black")
    l1_type.configure(text='''Type''')
    l1_type.configure(width=35)

    l1_com = Label(info_frame)
    l1_com.place(relx=0.52, rely=0.078, height=21, width=65
                 , bordermode='ignore')
    l1_com.configure(activebackground="#f9f9f9")
    l1_com.configure(activeforeground="black")
    l1_com.configure(background="#99CCFF")
    l1_com.configure(disabledforeground="#a3a3a3")
    l1_com.configure(font=font11)
    l1_com.configure(foreground="#000000")
    l1_com.configure(highlightbackground="#d9d9d9")
    l1_com.configure(highlightcolor="black")
    l1_com.configure(text='''Comments''')
    l1_com.configure(width=65)

    l1_room = Label(info_frame)
    l1_room.place(relx=0.52, rely=0.157, height=21, width=85
                  , bordermode='ignore')
    l1_room.configure(activebackground="#f9f9f9")
    l1_room.configure(activeforeground="black")
    l1_room.configure(background="#99CCFF")
    l1_room.configure(disabledforeground="#a3a3a3")
    l1_room.configure(font=font11)
    l1_room.configure(foreground="#000000")
    l1_room.configure(highlightbackground="#d9d9d9")
    l1_room.configure(highlightcolor="black")
    l1_room.configure(text='''Room Number''')
    l1_room.configure(width=85)

    l1_dateIn = Label(info_frame)
    l1_dateIn.place(relx=0.51, rely=0.235, height=21, width=55
                    , bordermode='ignore')
    l1_dateIn.configure(activebackground="#f9f9f9")
    l1_dateIn.configure(activeforeground="black")
    l1_dateIn.configure(background="#99CCFF")
    l1_dateIn.configure(disabledforeground="#a3a3a3")
    l1_dateIn.configure(font=font11)
    l1_dateIn.configure(foreground="#000000")
    l1_dateIn.configure(highlightbackground="#d9d9d9")
    l1_dateIn.configure(highlightcolor="black")
    l1_dateIn.configure(text='''Date In''')
    l1_dateIn.configure(width=55)

    l1_dateOut = Label(info_frame)
    l1_dateOut.place(relx=0.51, rely=0.333, height=21, width=65
                     , bordermode='ignore')
    l1_dateOut.configure(activebackground="#f9f9f9")
    l1_dateOut.configure(activeforeground="black")
    l1_dateOut.configure(background="#99CCFF")
    l1_dateOut.configure(disabledforeground="#a3a3a3")
    l1_dateOut.configure(font=font11)
    l1_dateOut.configure(foreground="#000000")
    l1_dateOut.configure(highlightbackground="#d9d9d9")
    l1_dateOut.configure(highlightcolor="black")
    l1_dateOut.configure(text='''Date Out''')
    l1_dateOut.configure(width=65)

    l2_nom = Label(info_frame)
    l2_nom.place(relx=0.21, rely=0.078, height=21, width=70
                 , bordermode='ignore')
    l2_nom.configure(background="#99CCFF")
    l2_nom.configure(disabledforeground="#a3a3a3")
    l2_nom.configure(foreground="#000000")
    l2_nom.configure(text=fname)

    l2_prenom = Label(info_frame)
    l2_prenom.place(relx=0.21, rely=0.176, height=21, width=70
                    , bordermode='ignore')
    l2_prenom.configure(activebackground="#f9f9f9")
    l2_prenom.configure(activeforeground="black")
    l2_prenom.configure(background="#99CCFF")
    l2_prenom.configure(disabledforeground="#a3a3a3")
    l2_prenom.configure(foreground="#000000")
    l2_prenom.configure(highlightbackground="#d9d9d9")
    l2_prenom.configure(highlightcolor="black")
    l2_prenom.configure(text=lname)

    l2_country = Label(info_frame)
    l2_country.place(relx=0.21, rely=0.275, height=21, width=70
                     , bordermode='ignore')
    l2_country.configure(activebackground="#f9f9f9")
    l2_country.configure(activeforeground="black")
    l2_country.configure(background="#99CCFF")
    l2_country.configure(disabledforeground="#a3a3a3")
    l2_country.configure(foreground="#000000")
    l2_country.configure(highlightbackground="#d9d9d9")
    l2_country.configure(highlightcolor="black")
    l2_country.configure(text=country)

    l2_mail = Label(info_frame)
    l2_mail.place(relx=0.14, rely=0.373, height=21, width=180
                  , bordermode='ignore')
    l2_mail.configure(activebackground="#f9f9f9")
    l2_mail.configure(activeforeground="black")
    l2_mail.configure(background="#99CCFF")
    l2_mail.configure(disabledforeground="#a3a3a3")
    l2_mail.configure(foreground="#000000")
    l2_mail.configure(highlightbackground="#d9d9d9")
    l2_mail.configure(highlightcolor="black")
    l2_mail.configure(text=mail)

    l2_adr = Label(info_frame)
    l2_adr.place(relx=0.21, rely=0.471, height=21, width=140
                 , bordermode='ignore')
    l2_adr.configure(activebackground="#f9f9f9")
    l2_adr.configure(activeforeground="black")
    l2_adr.configure(background="#99CCFF")
    l2_adr.configure(disabledforeground="#a3a3a3")
    l2_adr.configure(foreground="#000000")
    l2_adr.configure(highlightbackground="#d9d9d9")
    l2_adr.configure(highlightcolor="black")
    l2_adr.configure(text=adr)

    l2_phone = Label(info_frame)
    l2_phone.place(relx=0.21, rely=0.569, height=21, width=110
                   , bordermode='ignore')
    l2_phone.configure(activebackground="#f9f9f9")
    l2_phone.configure(activeforeground="black")
    l2_phone.configure(background="#99CCFF")
    l2_phone.configure(disabledforeground="#a3a3a3")
    l2_phone.configure(foreground="#000000")
    l2_phone.configure(highlightbackground="#d9d9d9")
    l2_phone.configure(highlightcolor="black")
    l2_phone.configure(text=phone)

    l2_card = Label(info_frame)
    l2_card.place(relx=0.21, rely=0.686, height=21, width=70
                  , bordermode='ignore')
    l2_card.configure(activebackground="#f9f9f9")
    l2_card.configure(activeforeground="black")
    l2_card.configure(background="#99CCFF")
    l2_card.configure(disabledforeground="#a3a3a3")
    l2_card.configure(foreground="#000000")
    l2_card.configure(highlightbackground="#d9d9d9")
    l2_card.configure(highlightcolor="black")
    l2_card.configure(text=card)

    l2_type = Label(info_frame)
    l2_type.place(relx=0.2, rely=0.784, height=21, width=70, bordermode='ignore')
    l2_type.configure(activebackground="#f9f9f9")
    l2_type.configure(activeforeground="black")
    l2_type.configure(background="#99CCFF")
    l2_type.configure(disabledforeground="#a3a3a3")
    l2_type.configure(foreground="#000000")
    l2_type.configure(highlightbackground="#d9d9d9")
    l2_type.configure(highlightcolor="black")
    l2_type.configure(text=type)

    l2_room = Label(info_frame)
    l2_room.place(relx=0.69, rely=0.157, height=21, width=70
                  , bordermode='ignore')
    l2_room.configure(activebackground="#f9f9f9")
    l2_room.configure(activeforeground="black")
    l2_room.configure(background="#99CCFF")
    l2_room.configure(disabledforeground="#a3a3a3")
    l2_room.configure(foreground="#000000")
    l2_room.configure(highlightbackground="#d9d9d9")
    l2_room.configure(highlightcolor="black")
    l2_room.configure(text=room)

    l2_dateIn = Label(info_frame)
    l2_dateIn.place(relx=0.69, rely=0.255, height=21, width=70
                    , bordermode='ignore')
    l2_dateIn.configure(activebackground="#f9f9f9")
    l2_dateIn.configure(activeforeground="black")
    l2_dateIn.configure(background="#99CCFF")
    l2_dateIn.configure(disabledforeground="#a3a3a3")
    l2_dateIn.configure(foreground="#000000")
    l2_dateIn.configure(highlightbackground="#d9d9d9")
    l2_dateIn.configure(highlightcolor="black")
    l2_dateIn.configure(text=inn)

    l2_dateOut = Label(info_frame)
    l2_dateOut.place(relx=0.7, rely=0.353, height=21, width=70
                     , bordermode='ignore')
    l2_dateOut.configure(activebackground="#f9f9f9")
    l2_dateOut.configure(activeforeground="black")
    l2_dateOut.configure(background="#99CCFF")
    l2_dateOut.configure(disabledforeground="#a3a3a3")
    l2_dateOut.configure(foreground="#000000")
    l2_dateOut.configure(highlightbackground="#d9d9d9")
    l2_dateOut.configure(highlightcolor="black")
    l2_dateOut.configure(text=out)

    l2_com = Label(info_frame)
    l2_com.place(relx=0.69, rely=0.097, height=21, width=90
                 , bordermode='ignore')
    l2_com.configure(activebackground="#f9f9f9")
    l2_com.configure(activeforeground="black")
    l2_com.configure(background="#99CCFF")
    l2_com.configure(disabledforeground="#a3a3a3")
    l2_com.configure(foreground="#000000")
    l2_com.configure(highlightbackground="#d9d9d9")
    l2_com.configure(highlightcolor="black")
    l2_com.configure(text=com)

    l_breakfast = Label(info_frame)
    l_breakfast.place(relx=0.51, rely=0.588, height=21, width=154
                      , bordermode='ignore')
    l_breakfast.configure(activebackground="#f9f9f9")
    l_breakfast.configure(activeforeground="black")
    l_breakfast.configure(anchor='w')
    l_breakfast.configure(background="#99CCFF")
    l_breakfast.configure(disabledforeground="#a3a3a3")
    l_breakfast.configure(foreground="#000000")
    l_breakfast.configure(highlightbackground="#d9d9d9")
    l_breakfast.configure(highlightcolor="black")
    l_breakfast.configure(text="Breakfast : " + breakfast + "  Price: " + str(br_price) + "$")
    l_breakfast.configure(width=154)

    l_lunch = Label(info_frame)
    l_lunch.place(relx=0.51, rely=0.706, height=21, width=174
                  , bordermode='ignore')
    l_lunch.configure(activebackground="#f9f9f9")
    l_lunch.configure(activeforeground="black")
    l_lunch.configure(anchor='w')
    l_lunch.configure(background="#99CCFF")
    l_lunch.configure(disabledforeground="#a3a3a3")
    l_lunch.configure(foreground="#000000")
    l_lunch.configure(highlightbackground="#d9d9d9")
    l_lunch.configure(highlightcolor="black")
    l_lunch.configure(text= "Lunch: " + lunch + " Price: " + str(lnch_price) + "$")
    l_lunch.configure(width=174)

    l_dinner = Label(info_frame)
    l_dinner.place(relx=0.51, rely=0.824, height=21, width=174
                   , bordermode='ignore')
    l_dinner.configure(activebackground="#f9f9f9")
    l_dinner.configure(activeforeground="black")
    l_dinner.configure(anchor='w')
    l_dinner.configure(background="#99CCFF")
    l_dinner.configure(disabledforeground="#a3a3a3")
    l_dinner.configure(foreground="#000000")
    l_dinner.configure(highlightbackground="#d9d9d9")
    l_dinner.configure(highlightcolor="black")
    l_dinner.configure(text="Dinner : " + dinner + "== Price: " + str(din_price) + "$")
    l_dinner.configure(width=174)

    # Create the second frame and its widgets
    invoice_frame = LabelFrame(root)
    invoice_frame.place(relx=0.037, rely=0.443, relheight=0.53, relwidth=0.923)
    invoice_frame.configure(relief='groove')
    invoice_frame.configure(foreground="black")
    invoice_frame.configure(text='''Invoice''')
    invoice_frame.configure(background="#99CCFF")
    invoice_frame.configure(width=500)

    label1 = Label(invoice_frame)
    label1.place(relx=0.15, rely=0.075, height=21, width=180
                 , bordermode='ignore')
    label1.configure(activebackground="#f9f9f9")
    label1.configure(activeforeground="black")
    label1.configure(anchor='w')
    label1.configure(background="#99CCFF")
    label1.configure(disabledforeground="#a3a3a3")
    label1.configure(font=font11)
    label1.configure(foreground="#000000")
    label1.configure(highlightbackground="#d9d9d9")
    label1.configure(highlightcolor="black")
    label1.configure(text = "Full Name : " + fname + " " + lname)

    label2 = Label(invoice_frame)
    label2.place(relx=0.15, rely=0.149, height=21, width=170
                 , bordermode='ignore')
    label2.configure(activebackground="#f9f9f9")
    label2.configure(activeforeground="black")
    label2.configure(anchor='w')
    label2.configure(background="#99CCFF")
    label2.configure(disabledforeground="#a3a3a3")
    label2.configure(font=font11)
    label2.configure(foreground="#000000")
    label2.configure(highlightbackground="#d9d9d9")
    label2.configure(highlightcolor="black")
    label2.configure(text="Phone Number : " + phone)

    label3 = Label(invoice_frame)
    label3.place(relx=0.15, rely=0.209, height=21, width=170
                 , bordermode='ignore')
    label3.configure(activebackground="#f9f9f9")
    label3.configure(activeforeground="black")
    label3.configure(anchor='w')
    label3.configure(background="#99CCFF")
    label3.configure(disabledforeground="#a3a3a3")
    label3.configure(font=font11)
    label3.configure(foreground="#000000")
    label3.configure(highlightbackground="#d9d9d9")
    label3.configure(highlightcolor="black")
    label3.configure(text="IDcard : " + card)
    label3.configure(width=170)

    label4 = Label(invoice_frame)
    label4.place(relx=0.15, rely=0.269, height=21, width=170
                 , bordermode='ignore')
    label4.configure(activebackground="#f9f9f9")
    label4.configure(activeforeground="black")
    label4.configure(anchor='w')
    label4.configure(background="#99CCFF")
    label4.configure(disabledforeground="#a3a3a3")
    label4.configure(font=font11)
    label4.configure(foreground="#000000")
    label4.configure(highlightbackground="#d9d9d9")
    label4.configure(highlightcolor="black")
    label4.configure(text="Room Number : " + room)
    label4.configure(width=170)

    # appel fucntion to get number of days
    date1 = inn.split('/')
    date2 = out.split('/')
    nb = nbr_days(date2, date1)

    label5 = Label(invoice_frame)
    label5.place(relx=0.15, rely=0.328, height=21, width=170
                 , bordermode='ignore')
    label5.configure(activebackground="#f9f9f9")
    label5.configure(activeforeground="black")
    label5.configure(anchor='w')
    label5.configure(background="#99CCFF")
    label5.configure(disabledforeground="#a3a3a3")
    label5.configure(font=font11)
    label5.configure(foreground="#000000")
    label5.configure(highlightbackground="#d9d9d9")
    label5.configure(highlightcolor="black")
    label5.configure(text="Duration : " + str(nb))
    label5.configure(width=170)

    # get room price
    resultats = queries.get_db_cond("rooms", "number", room)
    for lig in resultats:
        room_price = lig[11]

    # totatl amount to pay for room
    room_total = room_price * nb

    label6 = Label(invoice_frame)
    label6.place(relx=0.15, rely=0.388, height=21, width=170
                 , bordermode='ignore')
    label6.configure(activebackground="#f9f9f9")
    label6.configure(activeforeground="black")
    label6.configure(anchor='w')
    label6.configure(background="#99CCFF")
    label6.configure(disabledforeground="#a3a3a3")
    label6.configure(font=font11)
    label6.configure(foreground="#000000")
    label6.configure(highlightbackground="#d9d9d9")
    label6.configure(highlightcolor="black")
    label6.configure(text="Room Costs :" + str(room_total))
    label6.configure(width=170)

    label7 = Label(invoice_frame)
    label7.place(relx=0.15, rely=0.448, height=21, width=70
                 , bordermode='ignore')
    label7.configure(activebackground="#f9f9f9")
    label7.configure(activeforeground="black")
    label7.configure(background="#99CCFF")
    label7.configure(disabledforeground="#a3a3a3")
    label7.configure(font=font11)
    label7.configure(foreground="#000000")
    label7.configure(highlightbackground="#d9d9d9")
    label7.configure(highlightcolor="black")
    label7.configure(text='''Meals Costs''')

    # totatl amount to pay for breakfast
    breakfast_total = br_price * nb

    label8 = Label(invoice_frame)
    label8.place(relx=0.3, rely=0.507, height=21, width=170
                 , bordermode='ignore')
    label8.configure(activebackground="#f9f9f9")
    label8.configure(activeforeground="black")
    label8.configure(anchor='w')
    label8.configure(background="#99CCFF")
    label8.configure(disabledforeground="#a3a3a3")
    label8.configure(font=font9)
    label8.configure(foreground="#000000")
    label8.configure(highlightbackground="#d9d9d9")
    label8.configure(highlightcolor="black")
    label8.configure(text="Breakfast :" + str(breakfast_total))
    label8.configure(width=170)

    # totatl amount to pay for lunch
    lunch_total = lnch_price * nb

    label9 = Label(invoice_frame)
    label9.place(relx=0.3, rely=0.567, height=21, width=170
                 , bordermode='ignore')
    label9.configure(activebackground="#f9f9f9")
    label9.configure(activeforeground="black")
    label9.configure(anchor='w')
    label9.configure(background="#99CCFF")
    label9.configure(disabledforeground="#a3a3a3")
    label9.configure(font=font9)
    label9.configure(foreground="#000000")
    label9.configure(highlightbackground="#d9d9d9")
    label9.configure(highlightcolor="black")
    label9.configure(text="Lunch :" + str(lunch_total))
    label9.configure(width=170)

    # totatl amount to pay for dinner
    dinner_total = din_price * nb

    label10 = Label(invoice_frame)
    label10.place(relx=0.3, rely=0.642, height=21, width=170
                  , bordermode='ignore')
    label10.configure(activebackground="#f9f9f9")
    label10.configure(activeforeground="black")
    label10.configure(anchor='w')
    label10.configure(background="#99CCFF")
    label10.configure(disabledforeground="#a3a3a3")
    label10.configure(font=font9)
    label10.configure(foreground="#000000")
    label10.configure(highlightbackground="#d9d9d9")
    label10.configure(highlightcolor="black")
    label10.configure(text="Dinner :" + str(dinner_total))
    label10.configure(width=170)

    # totatl amount to pay
    total = room_total + breakfast_total + lunch_total + dinner_total

    label11 = Label(invoice_frame)
    label11.place(relx=0.62, rely=0.687, height=21, width=170
                  , bordermode='ignore')
    label11.configure(activebackground="#f9f9f9")
    label11.configure(activeforeground="black")
    label11.configure(anchor='w')
    label11.configure(background="#99CCFF")
    label11.configure(disabledforeground="#a3a3a3")
    label11.configure(font=font11)
    label11.configure(foreground="#000000")
    label11.configure(highlightbackground="#d9d9d9")
    label11.configure(highlightcolor="black")
    label11.configure(justify='left')
    label11.configure(text="Total Amount : " + str(total))
    label11.configure(width=170)

    Button1 = Button(invoice_frame, command=lambda: queries.Checkout(room))
    Button1.place(relx=0.1, rely=0.806, height=54, width=167
                  , bordermode='ignore')
    Button1.configure(activebackground="#ececec")
    Button1.configure(activeforeground="#000000")
    Button1.configure(background="#d9d9d9")
    Button1.configure(disabledforeground="#a3a3a3")
    Button1.configure(foreground="#000000")
    Button1.configure(highlightbackground="#d9d9d9")
    Button1.configure(highlightcolor="black")
    Button1.configure(pady="0")
    Button1.configure(text='''Checkout & Delete Client''')
    Button1.configure(width=167)

    Button2 = Button(invoice_frame,
                     command=lambda: invoice(fname, lname, adr, card, room, inn, out, room_total, breakfast_total,
                                             lunch_total, dinner_total, total))
    Button2.place(relx=0.58, rely=0.806, height=54, width=167
                  , bordermode='ignore')
    Button2.configure(activebackground="#ececec")
    Button2.configure(activeforeground="#000000")
    Button2.configure(background="#d9d9d9")
    Button2.configure(disabledforeground="#a3a3a3")
    Button2.configure(foreground="#000000")
    Button2.configure(highlightbackground="#d9d9d9")
    Button2.configure(highlightcolor="black")
    Button2.configure(pady="0")
    Button2.configure(text='''Print Invoice''')
    Button2.configure(width=167)


def invoice(fname, lname, adr, card, room, inn, out, room_total, breakfast_total, lunch_total, dinner_total, total):
    filename = str(fname) + str(lname) + "invoice.txt"
    f = open(filename, "w+")
    f.write("====================================Hotel XXXXXX============================================")
    f.write("\n")
    f.write("Thank you for statying in our hotel, here is your invoice")
    f.write("\n")
    f.write("Client Full Nmae" + str(fname) + " " + str(lname))
    f.write("\n")
    f.write("Address :" + str(adr))
    f.write("\n")
    f.write("IDcard : " + str(card))
    f.write("\n")
    f.write("Room number : " + str(room))
    f.write("\n")
    f.write("Date Checked in : " + str(inn))
    f.write("\n")
    f.write("Date Checked out : " + str(out))
    f.write("\n")
    f.write("room amount : " + str(room_total))
    f.write("\n")
    f.write("Meals Costs : ")
    f.write("\n")
    f.write("                     Breakfast :" + str(breakfast_total))
    f.write("\n")
    f.write("                     Lunch :" + str(lunch_total))
    f.write("\n")
    f.write("                     Dinner :" + str(dinner_total))
    f.write("\n")
    f.write("Total Amount To Pay : " + str(total))
    f.write("\n")
    f.write("We Hope To See You Very Soon")
    f.close()
    messagebox.showinfo("done", "Invoice Printed :)")
