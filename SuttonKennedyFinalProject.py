# Mouse Lab Tracker by Kennedy Stokes-Sutton
#3/7/2024
#This application allows users to input data collected in a laboartory setting during their work with mice.
#Features in this application include an agreement to the ethical guidlines of workinging with laboratory
#animals, a calendar window, and a window for data entry where data is submited. 

from tkinter import*
import calendar

# function to open window for data entry
def open_data_window():
    data_window = Toplevel(root)
    data_window.title("Data")
    data_window.geometry("400x400")
    new_window_label = Label(data_window, text="Data")
    new_window_label.pack()

    # Date entry field
    date_entry_label = Label(data_window, text="Enter Date (YYYY-MM-DD):")
    date_entry_label.pack()
    date_entry = Entry(data_window)
    date_entry.pack()

    # Mouse ID number entry field 
    id_entry_label = Label(data_window, text="Enter mouse identification number:")
    id_entry_label.pack()
    id_entry = Entry(data_window)
    id_entry.pack()

    # Treatment information entry field
    treatment_label = Label(data_window, text="Treatment information:")
    treatment_label.pack()
    treatment_entry = Text(data_window, height=10, width=40)
    treatment_entry.pack()

    # Health status and mouse behavior entry field 
    health_status_label = Label(data_window, text="Health status/Mouse behavior:")
    health_status_label.pack()
    health_status_entry = Text(data_window, height=10, width=40)
    health_status_entry.pack()

    # other notes entry field
    notes_label = Label(data_window, text="Other notes:")
    notes_label.pack()
    notes_entry = Text(data_window, height=10, width=40)
    notes_entry.pack()

   # submit button to submit entered data
    submit_button = Button(data_window, text="Submit", command=lambda: submit(date_entry.get(), id_entry.get(), treatment_entry.get("1.0", "end-1c"), health_status_entry.get("1.0", "end-1c"), notes_entry.get("1.0", "end-1c")))
    submit_button.pack()


# function to show a window indicating invalid input if guidelines aggrement checkbox is not checked
def show_invalid_input_window():
    invalid_input_window = Toplevel(root)
    invalid_input_window.title("Invalid Input")
    invalid_input_window.geometry("300x100")
    invalid_input_label = Label(invalid_input_window, text="Please accept the guidelines.")
    invalid_input_label.pack()

# function to submit guideline agreement and open calendar window if guidlines are accepted
def submit():
    if var1.get() == 1:
        calendar_window = Toplevel(root)
        calendar_window.title("Calendar")
        calendar_window.geometry("800x800")

        yy = 2024
        cal_str = calendar.calendar(yy)
        calendar_label = Label(calendar_window, text=cal_str, font=("Courier", 12), justify="left")
        calendar_label.pack(padx=10, pady=10)

        open_window_button = Button(calendar_window, text="Input Data", command=open_data_window)
        open_window_button.pack()

    else:
        show_invalid_input_window()



#root window
root = Tk()
root.title("Ethical Guidlines")
root.minsize(400, 400)




title_label = Label(root, text="Ethical Guidlines for the Use of Animals in Research")
title_label.pack()

#listbox to display guidelines 
guidelines_list = Listbox(root, width=200, height=20)
guidelines_list.pack()



#guidelines list
guidelines = [ "1. Respect for animals' dignity: Researchers must respect animals' worth and interests, choosing methods and topics carefully and providing appropriate care.",

"2. Responsibility for considering options: Researchers should explore alternatives to animal experiments, prioritizing non-animal methods and considering postponement if alternatives are lacking.",

"3. The principle of proportionality: Researchers must balance animal suffering with research benefits, ensuring scientific quality and considering both short-term and long-term benefits.",

"4. Responsibility for reducing the number of animals: Researchers must minimize the number of animals used, conducting literature reviews and considering alternative designs.",

"5. Responsibility for minimizing suffering and improving welfare: Researchers must assess and minimize suffering, considering the entire experimental process and adapting care to individual animals' needs.",

"6. Responsibility for maintaining biological diversity: Researchers must safeguard biodiversity, minimizing the use of endangered species and following the precautionary principle.",

"7. Responsibility when intervening in a habitat: Researchers should minimize disruption to animals' natural behavior and surroundings, considering the impact of their activities.",

"8. Responsibility for openness and sharing of data: Researchers should ensure transparency and share research findings and data, including negative results, to avoid unnecessary repetition and inform the public.",

"9. Requirement of expertise on animals: Researchers handling animals must have up-to-date expertise on animal biology and welfare.",

"10. Requirement of due care: Researchers and managers must comply with laws and regulations regarding laboratory animal use, familiarizing themselves with current guidelines.",





]



for guideline in guidelines:
    guidelines_list.insert(END, guideline)

# variable for value of checkbox, variable = 1 if checked
var1 = IntVar()
Checkbutton(root, text="I accept these guidelines", variable=var1).pack(anchor="center")

# submit button for guidelines agreement
submit_button = Button(root, text="Submit", command=submit)
submit_button.pack()



root.mainloop()