from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city= city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=bdc88daf62053635122802c20264921f"
"").json()
    w_label1.config(text=data["weather"][0]["main"])
    wd_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(data["main"]["temp"]-273.15))
    per_label1.config(text=data["main"]["pressure"])


win = Tk()

win.title("Weather App")
win.config(bg = "blue")
win.geometry("500x500")

name_label = Label(win,text = "Weather App",
                   font=("Time New Roman",40,"bold"))

name_label.place(x=25,y =50,height=50,width=450)

city_name = StringVar()

list_name= ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win,text = "Weather App",values = list_name,
                   font=("Time New Roman",15,"bold"),textvariable=city_name)
com.place(x=25,y=110,height=40,width=450)



w_label = Label(win,text = "Weather Update",
                   font=("Time New Roman",10,"bold"))

w_label.place(x=50,y =220,height=50,width=150)
w_label1 = Label(win,text = "",
                   font=("Time New Roman",10,"bold"))

w_label1.place(x=300,y =220,height=50,width=150)

wd_label = Label(win,text = "Weather Description",
                   font=("Time New Roman",10,"bold"))

wd_label.place(x=50,y =280,height=50,width=150)
wd_label1 = Label(win,text = "",
                   font=("Time New Roman",10,"bold"))

wd_label1.place(x=300,y =280,height=50,width=150)

temp_label = Label(win,text = "Temperature",
                   font=("Time New Roman",10,"bold"))

temp_label.place(x=50,y =340,height=50,width=150)
temp_label1 = Label(win,text = "",
                   font=("Time New Roman",10,"bold"))

temp_label1.place(x=300,y =340,height=50,width=150)
per_label = Label(win,text = "Pressure",
                   font=("Time New Roman",10,"bold"))

per_label.place(x=50,y =400,height=50,width=150)
per_label1 = Label(win,text = "",
                   font=("Time New Roman",10,"bold"))

per_label1.place(x=300,y =400,height=50,width=150)

done_button = Button(win,text = "Done",
                   font=("Time New Roman",15,"bold"),command=data_get)
done_button.place(x=150,y=160,height=50,width=200)


win.mainloop()