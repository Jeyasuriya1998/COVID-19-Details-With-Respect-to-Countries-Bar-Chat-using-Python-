# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 07:13:49 2020

@author: Jeyasuriya
"""


from tkinter import *
import sys

root = Tk()

root.geometry("400x200")
root.title("Get Covid-19 Data Country Wise")
    
def showdata():
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    from covid import Covid

    covid = Covid()
    countries_cases = []
    confirmed = []
    active = []
    deaths = []
    recovered = []

    try:
        root.update()
        country_names = data.get()
        country_names = country_names.strip()
        country_names = country_names.replace(" ", ",")
        country_names = country_names.split(",")
        
        for x in country_names:
            countries_cases.append(covid.get_status_by_country_name(x))
            root.update()
        
        for country in countries_cases:
            confirmed.append(country["confirmed"])
            active.append(country["active"])
            deaths.append(country["deaths"])
            recovered.append(country["recovered"])
            
        confirmed_patch = mpatches.Patch(color = 'green', label = 'confirmed')
        recovered_patch = mpatches.Patch(color = 'red', label = 'recovered')
        active_patch = mpatches.Patch(color = 'blue', label = 'active')
        deaths_patch = mpatches.Patch(color = 'black', label= 'deaths')
        plt.legend(handles = [confirmed_patch, recovered_patch, active_patch, 
                              deaths_patch])
        
        for x in range(len(country_names)):
            confirmed_bar = plt.bar(country_names[x], confirmed[x], color = 'green')
            for elem in confirmed_bar:
                plt.text(elem.get_x()+ (elem.get_width()/3.5) , elem.get_y() + (elem.get_height()), elem.get_height())
            if recovered[x] > active[x]:
                recovered_bar = plt.bar(country_names[x], recovered[x], color = 'red')
                for elem in recovered_bar:
                    plt.text(elem.get_x() + (elem.get_width()/3.5), elem.get_y() + (elem.get_height()), elem.get_height())
            
                active_bar = plt.bar(country_names[x], active[x], color = 'blue')
                for elem in active_bar:
                    plt.text(elem.get_x() + (elem.get_width()/3.5), elem.get_y() + (elem.get_height()), elem.get_height())
            
            else:
                active_bar = plt.bar(country_names[x], active[x], color = 'blue')
                for elem in active_bar:
                    plt.text(elem.get_x() + (elem.get_width()/3.5), elem.get_y() + (elem.get_height()), elem.get_height())
            
                recovered_bar = plt.bar(country_names[x], recovered[x], color = 'red')
                for elem in recovered_bar:
                    plt.text(elem.get_x() + (elem.get_width()/3.5), elem.get_y() + (elem.get_height()), elem.get_height())
            
            deaths_bar = plt.bar(country_names[x], deaths[x], color = 'black')
            for elem in deaths_bar:
                plt.text(elem.get_x() + (elem.get_width()/3.5), elem.get_y() + elem.get_height(), elem.get_height())
            
        plt.title('Current Covid Cases')
        plt.xlabel('Country Name')
        plt.ylabel('Cases(in millions)')
        plt.show()
    except :
        print("Enter the Correct Format")
        
Label(root, text = "Enter all countries names\nfor whom you want to get\ncovid-19 data",
      font = "Consolas 15 bold").pack()
Label(root, text = "Enter country names:").pack()
data = StringVar()
data.set("Seperate country names using comma or space(not both)")
entry = Entry(root, textvariable=data, width = 50).pack()
Button(root, text = "Get Data", command = showdata).pack()
root.mainloop()
