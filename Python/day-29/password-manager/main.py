from tkinter import *
from tkinter import messagebox
import random
import json

def find_pass():
     website = website_entry.get()
     try:
       with open("data.json") as data_file:
        data = json.load(data_file)
     except FileNotFoundError:
         messagebox.showerror("Error", "No data found")
     else:
         if website in data:
             email = data[website]["email"]
             password = data[website]["password"]
             messagebox.showinfo(title=website, message=f"password : {password} \n email : {email}")
         else:
             messagebox.showerror(title="Error", message="No details found")
     




def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website : {
         "email": email,
         "password": password
    }}


    if len(website) == 0 or len(email) == 0 or len(password) == 0 :
        messagebox.showerror("Oops", "Please fill out all fields")

    else:
           try:
                with open("data.json","r") as data_file:
                    data = json.load(data_file)
                

           except FileNotFoundError:
                with open("data.json","w") as data_file:
                     json.dump(new_data, data_file, indent=4)
           else:
              data.update(new_data)
              with open("data.json","w") as data_file:
                 json.dump(data, data_file, indent=4)

           finally:
               website_entry.delete(0,END)
               password_entry.delete(0,END)
               email_entry.delete(0,END)

   
def genrate_passowrd():
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



        password_letters = [random.choice(letters) for _ in range(random.randint(8,10))]
        password_symbols = [random.choice(symbols) for _ in range(random.randint(2,4))]
        password_numbers = [random.choice(numbers) for _ in range(random.randint(2,4))]

        password_list = password_letters + password_symbols + password_numbers

        random.shuffle(password_list)

        password = "".join(password_list)
        password_entry.insert(0,password)
       







window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas = Canvas(height=200,width=200)
logo_image = PhotoImage(file="day-29/password-manager/logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(row=0,column=1)


website_lable = Label(text="Website :")
website_lable.grid(row=1,column=0)
email_lable = Label(text="email/username :")
email_lable.grid(row=2,column=0)
password_lable = Label(text="Password :")
password_lable.grid(row=3,column=0)

website_entry = Entry(width=23)
website_entry.focus()
website_entry.grid(row=1,column=1)
email_entry = Entry(width=42)
email_entry.grid(row=2,column=1,columnspan=2)
password_entry = Entry(width=23)
password_entry.grid(row=3,column=1)

generate_password_button = Button(text="Genrate Password",command=genrate_passowrd)
generate_password_button.grid(row=3,column=2)
generate_add_button =Button(text = "add",width=45, command=save)
generate_add_button.grid(row=4,column=1,columnspan=3)
search_button = Button(text="Search",width=14,command=find_pass)
search_button.grid(row=1,column=2,columnspan=1)


window.mainloop()