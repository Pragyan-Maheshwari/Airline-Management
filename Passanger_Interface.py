from tkinter import *
import tkinter as Passtink
import tkinter.ttk as ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import json
import smtplib

def PassangerFunction():
    
    login = Toplevel()
    login.title("Login")
    login.geometry("200x200")
    with open("Flights and Passanger.json") as file:
        fpdata = json.load(file)
    userlable=Label(login, text="Username") ; userentry=Entry(login)
    userentry.pack(side="top") ; userlable.pack(side="top")

    pdwlable=Label(login, text="Password");pdwrentry=Entry(login)
    pdwrentry.pack(side="top") ; pdwlable.pack(side="top")

    def PassM():

        passwin = Toplevel()
        passwin.title("Passanger")
        passwin.geometry("1300x700")

        frame1=Passtink.Frame(passwin,width= 1300000000,height=70000000000)
        frame1.pack()
        frame1.place(anchor="s",relx=4.5,rely=3.8)
        img1 = ImageTk.PhotoImage(Image.open("Image2.jpeg"))
        mylable1 = Label(frame1,image = img1)
        mylable1.pack()

        #Check Flights
        def flights():
            flight = Toplevel()
            flight.title("Flights")
            flight.geometry("1300x700")
            flight.configure(bg="green")
            
            with open("Flights.json") as file:
                flightsdata = json.load(file)


            Flightstable = ttk.Treeview(flight, show="headings", columns=("Serial no.","From","Destination","Boarding Time","Arival Time","Seats Left"))
            
            Flightstable.heading("#1", text="Serial no.")
            Flightstable.heading("#2", text="From")
            Flightstable.heading("#3", text="Destination")
            Flightstable.heading("#4", text="Boarding Time")
            Flightstable.heading("#5", text="Arival Time")
            Flightstable.heading("#6", text="Seats Left")
            Flightstable.grid()

            for row in flightsdata:
                Flightstable.insert("","end",values=(row["Serial no."],row["From"],row["Destination"],row["Boarding Time"],row["Arival Time"],row["Seats Left"]))

            flight.mainloop()

        flightcheck = Button(passwin,text="Check Flights",font=("elephant",10,"italic"),height=2,width=10,command=flights)
        flightcheck.pack(side="top",ipadx=15,ipady=3)

        def Book():
            Booking = Toplevel()
            Booking.title("Ticket Booking")
            Booking.geometry("1300x700")

            with open("Passangers.json") as file:
                passdata = json.load(file)

            with open("Flights and Passanger.json") as file:
                fplist = json.load(file)
            
            frame1 = Frame(Booking,width=500,height=600,bg="red")
            frame1.pack(side="top")

            SerialLable = Label(frame1,text="Serial No.",font="Vibes",width=10,height=2,bg="blue")
            SerialTextbox = Entry(frame1,bg="Green",justify=LEFT,width= 20)
            SerialLable.pack(side="top")
            SerialTextbox.pack(side="top",ipady=12)

            NameLable = Label(frame1,text="Name",font="Vibes",width=10,height=2,bg="blue")
            NameTextbox = Entry(frame1,bg="Green",justify=LEFT,width= 20)
            NameLable.pack(side="top")
            NameTextbox.pack(side="top",ipady=12)

            FlightLable = Label(frame1,text="Flight no.",font="Vibes",width=10,height=2,bg="blue")
            FlightTextbox = Entry(frame1,bg="Green",justify=LEFT,width= 20)
            FlightLable.pack(side="top")
            FlightTextbox.pack(side="top",ipady=12)

            AgeLable = Label(frame1,text="Age",font="Vibes",width=10,height=2,bg="blue")
            AgeTextbox = Entry(frame1,bg="Green",justify=LEFT,width= 20)
            AgeLable.pack(side="top")
            AgeTextbox.pack(side="top",ipady=12)

            GenderLable = Label(frame1,text="Gender",font="Vibes",width=10,height=2,bg="blue")
            GenderTextbox = Entry(frame1,bg="Green",justify=LEFT,width= 20)
            GenderLable.pack(side="top")
            GenderTextbox.pack(side="top",ipady=12)

            GmailLable = Label(frame1,text="Gmail",font="Vibes",width=10,height=2,bg="blue")
            GmailTextbox = Entry(frame1,bg="Green",justify=LEFT,width= 20)
            GmailLable.pack(side="top")
            GmailTextbox.pack(side="top",ipady=12)

            def subbmit():
                USerial = SerialTextbox.get()
                UName = NameTextbox.get()
                UFlight = FlightTextbox.get()
                UAge = AgeTextbox.get()
                UGender = GenderTextbox.get()
                UGmail = GmailTextbox.get()

                if int(USerial) not in fplist[1]:

                    insertdata = {"Serial No.":USerial,
                        "Name":UName,
                        "Flight":UFlight,
                        "Status":"Yes",
                        "Age":UAge,
                        "Gender":UGender,
                        "Gmail":UGmail}

                    passdata.append(insertdata.copy())

                    jsonPassangers = json.dumps(passdata)
                    with open("Passangers.json","w") as outfile:
                        outfile.write(jsonPassangers)
                    
                    with open("Flights.json") as file:
                        flightsdata = json.load(file)

                    flightsdata[int(UFlight)-1]["Seats Left"] = int(flightsdata[int(UFlight)-1]["Seats Left"]) -1
                    flightsdata[int(UFlight)-1]["Seats Left"] = str(flightsdata[int(UFlight)-1]["Seats Left"])

                    jsonflights = json.dumps(flightsdata)
                    with open("Flights.json","w") as outfile:
                        outfile.write(jsonflights)

                    fplist[1].append(int(USerial))
                    fpjson = json.dumps(fplist)
                    with open("Flights and Passanger.json","w") as outfile:
                        outfile.write(fpjson)

                    mail=smtplib.SMTP("smtp.gmail.com",587)
                    mail.starttls()
                    mail.login("highskyairlines@gmail.com", "tbaznscvfshdsnqo")
                    message=f"""Dear Sir/Ma'am
    Your Booking has been confirmed !
    Your Ticket:-
    Serial No. :   {USerial}
    Name       :   {UName}
    Flight     :   {UFlight}
    Age        :   {UAge}
    Gender     :   {UGender}

    Have A Safe Journey"""
                    mail.sendmail("highskyairlines@gmail.com", UGmail, message)

                    messagebox.showinfo("Done","Your Ticket Has Been Booked")
                    Booking.destroy()

                else:
                    messagebox.showerror("Error","Error, The Serial Number Already Exsists.. Please Retry...")
                    Booking.destroy()

            Subbmitbutton = Button(Booking,text="Subbmit",command=subbmit)
            Subbmitbutton.pack(side="top")

            Booking.mainloop()

        FlightBook = Button(passwin,text="Book FLight",font=("elephant",10,"italic"),height=2,width=10,command=Book)
        FlightBook.pack(side="top",ipadx=15,ipady=3)

        def CancelBooking():
            Cancel = Toplevel()
            Cancel.geometry("1300x700")
            Cancel.title("Cancel Booking")

            with open("Passangers.json") as file:
                passdata = json.load(file)

            with open("Flights and Passanger.json") as file:
                fplist = json.load(file)

            frame1 = Frame(Cancel,width=500,height=600,bg="red")
            frame1.pack(side="left")

            SerialLable = Label(frame1,text="Serial No.",font="Vibes",width=10,height=2,bg="blue")
            SerialTextbox = Entry(frame1,bg="Green",justify=LEFT,width= 20)
            SerialLable.pack(side="top")
            SerialTextbox.pack(side="top",ipady=12)

            NameLable = Label(frame1,text="Name",font="Vibes",width=10,height=2,bg="blue")
            NameTextbox = Entry(frame1,bg="Green",justify=LEFT,width= 20)
            NameLable.pack(side="top")
            NameTextbox.pack(side="top",ipady=12)

            FlightLable = Label(frame1,text="Flight no.",font="Vibes",width=10,height=2,bg="blue")
            FlightTextbox = Entry(frame1,bg="Green",justify=LEFT,width= 20)
            FlightLable.pack(side="top")
            FlightTextbox.pack(side="top",ipady=12)

            AgeLable = Label(frame1,text="Age",font="Vibes",width=10,height=2,bg="blue")
            AgeTextbox = Entry(frame1,bg="Green",justify=LEFT,width= 20)
            AgeLable.pack(side="top")
            AgeTextbox.pack(side="top",ipady=12)

            GenderLable = Label(frame1,text="Gender",font="Vibes",width=10,height=2,bg="blue")
            GenderTextbox = Entry(frame1,bg="Green",justify=LEFT,width= 20)
            GenderLable.pack(side="top")
            GenderTextbox.pack(side="top",ipady=12)

            GmailLable = Label(frame1,text="Gmail",font="Vibes",width=10,height=2,bg="blue")
            GmailTextbox = Entry(frame1,bg="Green",justify=LEFT,width= 20)
            GmailLable.pack(side="top")
            GmailTextbox.pack(side="top",ipady=12)

            def change_color(color):
                "Change color of widgets."
                Cancel.config(bg=color)
                SerialTextbox.config(highlightbackground=color)
                SerialTextbox.config(fg=color, insertbackground=color)

                NameTextbox.config(highlightbackground=color)
                NameTextbox.config(fg=color, insertbackground=color)

                FlightTextbox.config(highlightbackground=color)
                FlightTextbox.config(fg=color, insertbackground=color)

                AgeTextbox.config(highlightbackground=color)
                AgeTextbox.config(fg=color, insertbackground=color)

                GenderTextbox.config(highlightbackground=color)
                GenderTextbox.config(fg=color, insertbackground=color)

                GmailTextbox.config(highlightbackground=color)
                GmailTextbox.config(fg=color, insertbackground=color)

            SerialTextbox.bind("<1>", lambda _: change_color("#99c9ff"))
            NameTextbox.bind("<1>", lambda _: change_color("#ffaf99"))
            FlightTextbox.bind("<1>", lambda _: change_color("green"))
            AgeTextbox.bind("<1>", lambda _: change_color("orange"))
            GenderTextbox.bind("<1>", lambda _: change_color("purple"))
            GmailTextbox.bind("<1>", lambda _: change_color("brown"))

            def subbmit():
                USerial = SerialTextbox.get()
                UName = NameTextbox.get()
                UFlight = FlightTextbox.get()
                UAge = AgeTextbox.get()
                UGender = GenderTextbox.get()
                UGmail=GmailTextbox.get()

                if int(USerial) in fplist[1]:

                    finalpassdata = [i for i in passdata if not (i["Serial No."] == str(USerial))]
                    jsonPassangers = json.dumps(finalpassdata)
                    with open("Passangers.json","w") as outfile:
                        outfile.write(jsonPassangers)
                    
                    with open("Flights.json") as file:
                        flightsdata = json.load(file)

                    flightsdata[int(UFlight)-1]["Seats Left"] = int(flightsdata[int(UFlight)-1]["Seats Left"]) +1
                    flightsdata[int(UFlight)-1]["Seats Left"] = str(flightsdata[int(UFlight)-1]["Seats Left"])

                    jsonflights = json.dumps(flightsdata)
                    with open("Flights.json","w") as outfile:
                        outfile.write(jsonflights)

                    index = fplist[1].index(int(USerial))
                    print(index)
                    fplist = fplist-index
                    fpjson = json.dumps(fplist)
                    with open("Flights and Passanger.json","w") as outfile:
                        outfile.write(fpjson)
                    
                    mail=smtplib.SMTP("smtp.gmail.com",587)
                    mail.starttls()
                    mail.login("highskyairlines@gmail.com", "tbaznscvfshdsnqo")
                    message=f"""Dear Sir/Ma'am
    Your Booking has been cancelled !"""
                    mail.sendmail("highskyairlines@gmail.com", UGmail, message)

                    messagebox.showinfo("Done","Your Ticket Has Been Cancelled.")
                    BookingCanceling.destroy()
                
                else:
                    messagebox.showerror("Error","The User Doesn't Exsist... Please check all Details...")
                    BookingCanceling.destroy()


            Subbmitbutton = Button(Cancel,text="Subbmit",command=subbmit)
            Subbmitbutton.pack(side="top")
            Cancel.mainloop()

        BookingCanceling = Button(passwin,text="Cancel Booking",font=("elephant",10,"italic"),height=2,width=10,command=CancelBooking)
        BookingCanceling.pack(side="top",ipadx=15,ipady=3)
    
    logbutton=Button(login,text = "Login",command=PassM)
    logbutton.pack(side="top")

    def CrelogFunction():
        login.destroy()
        Crelog=Toplevel()
        Crelog.title("Login")
        Crelog.geometry("200x200")

        with open("Flights and Passanger.json") as file:
            fplist = json.load(file)
        userlable=Label(Crelog, text="Username") ; userentry=Entry(Crelog)
        userlable.pack(side="top") ;userentry.pack(side="top")

        pdwlable=Label(Crelog, text="Password");pdwrentry=Entry(Crelog)
        pdwlable.pack(side="top") ; pdwrentry.pack(side="top")
        
        def Register():
            PassM()
            user=userentry.get()
            pdw=pdwrentry.get()
            fplist[3].append({user:pdw})
            fpjson = json.dumps(fplist)
            with open("Flights and Passanger.json","w") as outfile:
                outfile.write(fpjson)

        createbutton=Button(Crelog,text = "Register & Login",command= Register)
        createbutton.pack(side="top")

    Createlogbutton=Button(login,text="Create Login",command=CrelogFunction)
    Createlogbutton.pack(side="top")
    login.mainloop()