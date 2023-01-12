from tkinter import *
import tkinter as Adtink
import tkinter.ttk as ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import json

def Admin():
    login = Toplevel()
    login.title("Login")
    login.geometry("200x200")
    with open("Flights and Passanger.json") as file:
        fpdata = json.load(file)
    userlable=Label(login, text="Username") ; userentry=Entry(login)
    userentry.pack(side="top") ; userlable.pack(side="top")

    pdwlable=Label(login, text="Password");pdwrentry=Entry(login)
    pdwrentry.pack(side="top") ; pdwlable.pack(side="top")

    def AdminM():
        
        with open("Flights and Passanger.json") as file:
                pfdata = json.load(file)

        uname = userentry.get()
        pdw=pdwrentry.get()
        dic={uname:pdw}
        if dic in pfdata[2]:
            adwin = Toplevel()
            adwin.title("Admin")
            adwin.geometry("1300x700")
            frame=Adtink.Frame(adwin,width= 130000,height=700000)
            frame.pack()
            frame.place(anchor="s",relx=03.5,rely=1.0)
            img = ImageTk.PhotoImage(Image.open("Image1.jpeg"))
            mylable = Label(frame,image = img)
            mylable.pack()

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

            flightcheck = Button(adwin,text="Check Flights",font=("elephant",10,"italic"),height=2,width=10,command=flights)
            flightcheck.pack(side="top",ipadx=15,ipady=3)
            
            #Check Passangers
            def passangers():
                passanger = Toplevel()
                passanger.title("Passangers")
                passanger.geometry("1300x700")
                passanger.configure(bg="green")


                with open("Passangers.json") as file:
                    passangerdata = json.load(file)


                PassangerTable = ttk.Treeview(passanger, show="headings", columns=("Serial No.","Name","Flight","Age","Gender"))
                        
                PassangerTable.heading("#1", text="Serial No.")
                PassangerTable.heading("#2", text="Name")
                PassangerTable.heading("#3", text="Flight")
                PassangerTable.heading("#4", text="Age")
                PassangerTable.heading("#5", text="Gender")
                PassangerTable.grid()

                for row in passangerdata:
                    PassangerTable.insert("","end",values=(row["Serial No."],row["Name"],row["Flight"],row["Age"],row["Gender"]))

                passanger.mainloop()

            passangercheck = Button(adwin,text="Check Passangers",font=("elephant",10,"italic"),height=2,width=10,command=passangers)
            passangercheck.pack(side="top",ipadx=15,ipady=3)
            
            def Addingflight():
                AddFlight = Toplevel()
                AddFlight.title("Add Flight")
                AddFlight.geometry("1300x700")
                AddFlight.configure(bg="blue")

                frame1 = Frame(AddFlight,width=1000,height=1000,bg="red")
                frame1.pack(side="left")

                with open("Flights.json") as file:
                    flightsdata = json.load(file)

                with open("Flights and Passanger.json") as file:
                    fplist = json.load(file)

                SerialLable = Adtink.Label(frame1,text="Serial No.",font="Vibes",width=10,height=2,bg="blue")
                SerialTextbox = Adtink.Entry(frame1,bg="Green",justify=LEFT,width= 20)
                SerialLable.pack(side="top")
                SerialTextbox.pack(side="top",ipady=12)

                FromLable = Adtink.Label(frame1,text="From",font="Vibes",width=10,height=2,bg="blue")
                FromTextbox = Adtink.Entry(frame1,bg="Green",justify=LEFT,width= 20)
                FromLable.pack(side="top")
                FromTextbox.pack(side="top",ipady=12)

                DestinationLable = Adtink.Label(frame1,text="Destination",font="Vibes",width=10,height=2,bg="blue")
                DestinationTextbox = Adtink.Entry(frame1,bg="Green",justify=LEFT,width= 20)
                DestinationLable.pack(side="top")
                DestinationTextbox.pack(side="top",ipady=12)

                BoardingTimeLable = Adtink.Label(frame1,text="Boarding Time",font="Vibes",width=10,height=2,bg="blue")
                BoardingTimeTextbox = Adtink.Entry(frame1,bg="Green",justify=LEFT,width= 20)
                BoardingTimeLable.pack(side="top")
                BoardingTimeTextbox.pack(side="top",ipady=12)

                ArivalTimeLable = Adtink.Label(frame1,text="Arival Time",font="Vibes",width=10,height=2,bg="blue")
                ArivalTimeTextbox = Adtink.Entry(frame1,bg="Green",justify=LEFT,width= 20)
                ArivalTimeLable.pack(side="top")
                ArivalTimeTextbox.pack(side="top",ipady=12)

                SeatsLeftLable = Adtink.Label(frame1,text="Seats Left",font="Vibes",width=10,height=2,bg="blue")
                SeatsLeftTextbox = Adtink.Entry(frame1,bg="Green",justify=LEFT,width= 20)
                SeatsLeftLable.pack(side="top")
                SeatsLeftTextbox.pack(side="top",ipady=12)

                def subbmit():
                    USerial = SerialTextbox.get()
                    UFrom = FromTextbox.get()
                    UDestination = DestinationTextbox.get()
                    UBoarding = BoardingTimeTextbox.get()
                    UArival = ArivalTimeTextbox.get()
                    USeats = SeatsLeftTextbox.get()

                    if int(USerial) not in fplist[0]:

                        insertdata = {"Serial no.":USerial,
                            "From":UFrom,
                            "Destination":UDestination,
                            "Boarding Time":UBoarding,
                            "Arival Time":UArival,
                            "Seats Left":USeats}

                        #print(flightsdata)
                        print(type(flightsdata))
                        flightsdata.append(insertdata.copy())

                        jsonflights = json.dumps(flightsdata)
                        with open("Flights.json","w") as outfile:
                            outfile.write(jsonflights)

                        fplist[0].append(int(USerial))
                        fpjson = json.dumps(fplist)
                        with open("Flights and Passanger.json","w") as outfile:
                            outfile.write(fpjson)
                        
                        messagebox.showinfo("Done","Your flight Has Been Added.")
                        AddFlight.destroy()

                    else:
                        messagebox.showerror("Error","A Flight With The Same Serial No. Already Exsists... Please Retry...")
                        AddFlight.destroy()

                Subbmitbutton = Button(frame1,text="Subbmit",command=subbmit)
                Subbmitbutton.pack(side="top")

                AddFlight.mainloop()

            Flightadd = Button(adwin,text="Add Flight",font=("elephant",10,"italic"),height=2,width=10,command=Addingflight)
            Flightadd.pack(side="top",ipadx=15,ipady=3)
            adwin.mainloop()
        else:
            messagebox.showerror("Error","Username Or Password Isn't correct please try again")
    logbutton=Button(login,text = "Login",command=AdminM)
    logbutton.pack(side="top")
    
    login.mainloop()