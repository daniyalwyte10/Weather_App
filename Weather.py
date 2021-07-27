#! python3
from tkinter import *
from tkinter import font
import requests

#HEIGHT=1280/2
#WIDTH=989/2

window=Tk()
window.wm_title("Weather")
window.geometry('640x470')

def format_label(weather):
    name=weather['name']
    desc=weather['weather'][0]['description']
    temp=weather['main']['temp']
    final_str= 'City: %s \nCondition: %s \nTemperature: %.2f °C' % (name, desc, temp-273.15)
    return final_str

def get_weather(city):
    weather_key='259b01b9526ff8c78fa68461a985d2d2'
    url=' http://api.openweathermap.org/data/2.5/weather'
    params={'APPID':weather_key, 'q' : city }
    response=requests.get(url, params=params)
    weather=response.json()

    lb['text']= format_label(weather)
#def test_function(e1):
    #print(e1)

background_image=PhotoImage(file='landscape.png')
background_label=Label(window, image=background_image)
background_label.place(relheight=1, relwidth=1)

#cs=Canvas(window, height=HEIGHT, width=WIDTH)
#cs.pack()

fr=Frame(window, bg='#03d3fc', bd=5)
fr.place(relx=0.5,rely=0.1,relwidth=0.75, relheight=0.1, anchor='n')

e1=Entry(fr, font=55)
e1.place(relwidth=0.68, relheight=1)

b1=Button(fr, text='Get Weather',font=5 , command=lambda : get_weather(e1.get()))
b1.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame=Frame(window, bg='#03d3fc', bd=10)
lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6, anchor='n')

lb=Label(lower_frame, font=('courier', 20), anchor='nw', justify='left')
lb.place(relheight=1, relwidth=1)

#ft= font.families()
#print(ft)
window.mainloop()

# command=lambda : get_weather(e1.get())