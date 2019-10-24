# layout all of the main containers
top_frame.grid(row=0, sticky="ew")
menu_frame.grid(row=1, sticky="new")
center.grid(row=2, sticky="ew")


# create the center widgets
ctr_left = Frame(center, bg='blue', width=70, height=190)
ctr_left.grid(row=0, column=0, sticky="nw")

# adding a scrollbar
c = Canvas(center, bg="cyan",  width=450, height=50)
vsb = Scrollbar(c, orient=VERTICAL)
c.grid(row=0, column=1, sticky="nw")
c.configure(yscrollcommand=vsb.set)
ctr_mid = Frame(c, bg='cyan', width=450, height=50, pady=3)
ctr_mid.grid(row=0, column=0, sticky="nw")
vsb.grid(row=0, column=7, sticky="ns")
vsb.config(command=c.yview)
c.yview_moveto(20)
c.update_idletasks()
c.config(scrollregion=c.bbox("all"))
