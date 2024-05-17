from tkinter import *
from tkinter import ttk 

root = Tk()
root.geometry("800x1045")
root.title("Bio Data")
root.configure(bg="black")
root.resizable(False, False)

frame1 = Frame(root, relief="ridge", highlightbackground="black", highlightthickness=2, bg="whitesmoke").place(x=20, y=12, width=760, height=1020)
title = Label(root, text="BIO-DATA", bg="whitesmoke", font=("Arial Black", 30, "bold")).place(x=270, y=20)
title2 = Label(root, text="PERSONAL INFORMATION", bg="black", fg="whitesmoke", font=("Arial Black", 10, "bold")).place(x= 40,y= 90)
title3 = Label(root, text="EDUCATIONAL BACKGROUND", bg="black", fg="whitesmoke", font=("Arial Black", 10, "bold")).place(x= 40,y= 780)
photo_frame = Frame(root, relief="ridge", highlightbackground="black", highlightthickness=2, bg="white").place(x=630, y=32, width=120, height=120)
insert_photo_button = Button(root,text=("+"),font=("Arial", 15), bg="white", relief="flat").place(x=675, y=70)

#==================== Information for Personal Information ================
position = Label(root, text="Position Desired: ", bg="whitesmoke", font=("Arial", 10, "bold")).place(x=40, y=130)
date = Label(root, text="Date: ", bg="whitesmoke", font=("Arial", 9, "bold")).place(x=420, y=130)
name = Label(root, text="Name: ", bg="whitesmoke", font=("Arial", 9, "bold")).place(x=40, y=170)
nickname = Label(root, text="Nickname: ", bg="whitesmoke", font=("Arial", 10, "bold")).place(x=420, y=170)
present_address = Label(root, text="Present Address: ", bg="whitesmoke", font=("Arial", 9, "bold")).place(x=40, y=210)
permanent_address = Label(root, text="Permanent Address: ", bg="whitesmoke", font=("Arial", 9, "bold")).place(x=40, y=250)
place_of_birth = Label(root, text="Place of Birth: ", bg="whitesmoke", font=("Arial", 9, "bold")).place(x=40, y=290)
contact_no = Label(root, text="Contact No(s): ", bg="whitesmoke", font=("Arial", 9, "bold")).place(x=420, y=290)
gender = Label(root, text="Gender: ", bg="whitesmoke", font=("Arial", 9, "bold")).place(x=40, y=330)
civil_status = Label(root, text="Civil Status: ", bg="whitesmoke", font=("Arial", 9, "bold")).place(x=420, y=330)
religion = Label(root, text="Religion: ", bg="whitesmoke", font=("Arial", 9, "bold")).place(x=40, y=370)
citizenship = Label(root, text="Citizenship: ", bg="whitesmoke", font=("Arial", 9, "bold")).place(x=420, y=370)
language = Label(root, text="Language Spoken: ", bg="whitesmoke", font=("Arial", 9, "bold")).place(x=40, y=410)
height = Label(root, text="Height: ", bg="whitesmoke", font=("Arial", 9, "bold")).place(x=290, y=410)
weight = Label(root, text="Weight: ", bg="whitesmoke", font=("Arial", 9, "bold")).place(x=500, y=410)
spouse = Label(root, text="Name of Spouse: ", bg="whitesmoke", font=("Arial", 9, "bold")).place(x=40, y=450)
occupation = Label(root, text="Ocupation: ", bg="whitesmoke", font=("Arial", 9, "bold")).place(x=450, y=450)
children = Label(root, text="Children's name/s and date of birth: ", bg="whitesmoke", font=("Arial", 9, "bold")).place(x=40, y=490)
fathers_name = Label(root, text="Father's Name: ", bg="whitesmoke", font=("Arial", 9, "bold")).place(x=40, y=570)
occupation = Label(root, text="Ocupation: ", bg="whitesmoke", font=("Arial", 9, "bold")).place(x=450, y=570)
mothers_name = Label(root, text="Mother's Name: ", bg="whitesmoke", font=("Arial", 9, "bold")).place(x=40, y=610)
occupation = Label(root, text="Ocupation: ", bg="whitesmoke", font=("Arial", 9, "bold")).place(x=450, y=610)
person_to_call = Label(root, text="Person to be contacted in case of emergency: ", bg="whitesmoke", font=("Arial", 9, "bold")).place(x=40, y=650)
address = Label(root, text="Address: ", bg="whitesmoke", font=("Arial", 9, "bold")).place(x=40, y=690)
relationship = Label(root, text="Relationship: ", bg="whitesmoke", font=("Arial", 9, "bold")).place(x=40, y=730)
contact_no = Label(root, text="Contact No(s): ", bg="whitesmoke", font=("Arial", 9, "bold")).place(x=450, y=730)

#==================== Information for Educational Background ================

elementary = Label(root, text="Elementary: ", bg="whitesmoke", font=("Arial", 9, "bold")).place(x=40, y=820)
year = Label(root, text="Year Attended: ", bg="whitesmoke", font=("Arial", 9, "bold")).place(x=500, y=820)
highschool = Label(root, text="High School: ", bg="whitesmoke", font=("Arial", 9, "bold")).place(x=40, y=860)
year = Label(root, text="Year Attended: ", bg="whitesmoke", font=("Arial", 9, "bold")).place(x=500, y=860)
college = Label(root, text="College: ", bg="whitesmoke", font=("Arial", 9, "bold")).place(x=40, y=900)
college_entry = Entry(root, highlightbackground="black", highlightthickness=1, bg="white", bd=0).place(x=130, y=902, width=320)
year = Label(root, text="Year Attended: ", bg="whitesmoke", font=("Arial", 9, "bold")).place(x=500, y=900)
course = Label(root, text="Course/Degree Received: ", bg="whitesmoke", font=("Arial", 9, "bold")).place(x=40, y=940)
skills = Label(root, text="Skills: ", bg="whitesmoke", font=("Arial", 9, "bold")).place(x=40, y=980)

#=========================== Entries ============================
position = Entry(root, highlightbackground="black",highlightthickness=1, bg="white", bd=0).place(x=180, y=132, width=210)
name = Entry(root, bg="white", highlightbackground="black", highlightthickness=1, bd=0).place(x=100, y=172, width=290)
nickname = Entry(root, bg="white", highlightbackground="black", highlightthickness=1, bd=0).place(x=520, y=172, width=220)
place_of_birth_entry = Entry(root, highlightbackground="black", highlightthickness=1, bg="white", bd=0).place(x=160, y=292, width=250)
contact_no_entry = Entry(root, highlightbackground="black", highlightthickness=1, bg="white", bd=0).place(x=520, y=292, width=220)
spouse_entry = Entry(root, highlightbackground="black", highlightthickness=1, bg="white", bd=0).place(x=180, y=452, width=240)
children_entry = Entry(root, highlightbackground="black", highlightthickness=1, bg="white", bd=0).place(x=40, y=515, width=700, height=40)
fathers_name_entry = Entry(root, highlightbackground="black", highlightthickness=1, bg="white", bd=0).place(x=160, y=572, width=240)
father_occupation_entry = Entry(root, highlightbackground="black", highlightthickness=1, bg="white", bd=0).place(x=540, y=572, width=200)
mothers_name_entry = Entry(root, highlightbackground="black", highlightthickness=1, bg="white", bd=0).place(x=160, y=612, width=240)
mother_occupation_entry = Entry(root, highlightbackground="black", highlightthickness=1, bg="white", bd=0).place(x=540, y=612, width=200)
person_to_call_entry = Entry(root, highlightbackground="black", highlightthickness=1, bg="white", bd=0).place(x=330, y=652, width=410)
emergency_address_entry = Entry(root, highlightbackground="black", highlightthickness=1, bg="white", bd=0).place(x=160, y=692, width=580)
emergency_relationship_entry = Entry(root, highlightbackground="black", highlightthickness=1, bg="white", bd=0).place(x=160, y=732, width=240)
emergency_contact_no_entry = Entry(root, highlightbackground="black", highlightthickness=1, bg="white", bd=0).place(x=540, y=732, width=200)
course_degree_entry = Entry(root, highlightbackground="black", highlightthickness=1, bg="white", bd=0).place(x=240, y=942, width=500)
skills_entry = Entry(root, highlightbackground="black", highlightthickness=1, bg="white", bd=0).place(x=100, y=982, width=640)
permanent_address = Entry(root, highlightbackground="black",highlightthickness=1, bg="white", bd=0).place(x= 170, y= 212, width=570)
permanent_address = Entry(root, highlightbackground="black",highlightthickness=1, bg="white", bd=0).place(x= 180, y= 252, width=560)
spouse_occupation_entry = Entry(root, highlightbackground="black", highlightthickness=1, bg="white", bd=0).place(x=545, y=450, width=195)
elementary_entry = Entry(root, highlightbackground="black", highlightthickness=1, bg="white", bd=0).place(x=130, y=822, width=320)
highschool_entry = Entry(root, highlightbackground="black", highlightthickness=1, bg="white", bd=0).place(x=130, y=862, width=320)
college_entry = Entry(root, highlightbackground="black", highlightthickness=1, bg="white", bd=0).place(x=130, y=902, width=320)

#=============== Other Widgets ===================================
date_values = [str(i).zfill(2) for i in range(1, 32)]
month_values = [str(i).zfill(2) for i in range(1, 13)]
year_values = [str(i).zfill(2) for i in range(22, 100)]

date_combo = ttk.Combobox(root, values=date_values, width=4).place(x=470, y=131)
month_combo = ttk.Combobox(root, values=month_values, width=4).place(x=520, y=131)
year_combo = ttk.Combobox(root, values=year_values, width=4, ).place(x=570, y=131)

gender_values = ['Male', 'Female', '']
gender_combo = ttk.Combobox(root, values=gender_values, width=10)
gender_combo.place(x=100, y=331)

age = Spinbox(root, from_= 13, to= 99, width=6).place(x=280, y=331)

civil_status_values = ['Single', 'Married', 'Divorced', 'Widowed', 'Separated']
civil_status_combo = ttk.Combobox(root, values=civil_status_values, width=10)
civil_status_combo.place(x=520, y=331)

language_values = ['English', 'Tagalog', 'Korean', 'Chinese', 'Japanese', 'Others']
language_combo = ttk.Combobox(root, values=language_values, width=15).place(x=160, y=411)

height_values = [str(i).zfill(3) for i in range(100, 250)]  
height_combo = ttk.Combobox(root, values=height_values, width=6).place(x=350, y=411)

weight_values = [str(i).zfill(3) for i in range(20, 300)]  
weight_combo = ttk.Combobox(root, values=weight_values, width=6).place(x=570, y=411)

religion_values = ['Christianity', 'Islam', 'Hinduism', 'Buddhism', 'Judaism', 'Others']
religion_combo = ttk.Combobox(root, values=religion_values, width=15).place(x=160, y=371)

citizenship_values = ['American', 'Filipino', 'Korean', 'Australian', 'Indian', 'Others']
citizenship_combo = ttk.Combobox(root, values=citizenship_values, width=15).place(x=540, y=371)

elementary_year_values = [str(i) for i in range(1950, 2051)]  
elementary_year_combo = ttk.Combobox(root, values=elementary_year_values, width=8).place(x=620, y=822)

highschool_year_values = [str(i) for i in range(1950, 2051)]  
highschool_year_combo = ttk.Combobox(root, values=highschool_year_values, width=8).place(x=620, y=862)

college_year_values = [str(i) for i in range(1950, 2051)]  
college_year_combo = ttk.Combobox(root, values=college_year_values, width=8).place(x=620, y=902)
college_year_values = [str(i) for i in range(1950, 2051)]  
college_year_combo = ttk.Combobox(root, values=college_year_values, width=8).place(x=620, y=902)

root.mainloop()