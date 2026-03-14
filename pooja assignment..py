import tkinter as tk

window = tk.Tk()
window.title("Student Registration Form")
window.geometry("400x400")

def show_data():
    name = e1.get()
    age = e2.get()
    gender = gender_var.get()
    dob = e3.get()
    phone = e4.get()
    qualification = qual_var.get()
    address = e5.get()

    print("Student Details")
    print("Name:", name)
    print("Age:", age)
    print("Gender:", gender)
    print("Date of Birth:", dob)
    print("Phone Number:", phone)
    print("Qualification:", qualification)
    print("Address:", address)

l1 = tk.Label(window, text="Name")
l1.pack()
e1 = tk.Entry(window)
e1.pack()

l2 = tk.Label(window, text="Age")
l2.pack()
e2 = tk.Entry(window)
e2.pack()

l3 = tk.Label(window, text="Gender")
l3.pack()

gender_var = tk.StringVar()

r1 = tk.Radiobutton(window, text="Male", variable=gender_var, value="Male")
r1.pack()

r2 = tk.Radiobutton(window, text="Female", variable=gender_var, value="Female")
r2.pack()

l4 = tk.Label(window, text="DOB")
l4.pack()
e3 = tk.Entry(window)
e3.pack()

l5 = tk.Label(window, text="Phone Number")
l5.pack()
e4 = tk.Entry(window)
e4.pack()

l6 = tk.Label(window, text="Qualification")
l6.pack()

qual_var = tk.StringVar()
qual_var.set("Select Qualification")

q1 = tk.OptionMenu(window, qual_var, "SSLC", "Plus Two", "Diploma", "Degree", "PG")
q1.pack()

l7 = tk.Label(window, text="Address")
l7.pack()
e5 = tk.Entry(window)
e5.pack()

b1 = tk.Button(window, text="Register", command=show_data)
b1.pack()

window.mainloop()