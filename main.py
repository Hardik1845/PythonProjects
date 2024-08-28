from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
FONT = ("Arial", 15, "normal")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)
    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)
    # Pyperclip is a module and .copy is a function which would automatically copy the
    # password to clipboard so user does not need to copy paste it.
def search():
    web = website_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            search_email = data[web]["email"]
            search_password = data[web]["password"]

            messagebox.showinfo(title="Search", message=f"Email:{search_email}\nPassword:{search_password}")
            pyperclip.copy(search_password)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No data file found")
    except KeyError:
        # Case if entered key is not present in dictionary
        messagebox.showinfo(title="No match found",message=f"No details for website {web} exists")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = website_entry.get()  # Used to get data entered by user in entry field
    passw = password_entry.get()
    e = email_entry.get()
    new_data = {
        web: {
            "email": e,
            "password": passw
        }
    }

    if len(passw) == 0 or len(web) == 0:
        messagebox.showinfo(title="Empty", message="Please fill the required details.")
    else:
        # Askokcancel works on a boolean format . If user clicks OK it is true else false
        is_ok = messagebox.askokcancel(title="Confirm",
                                       message=f"Website :{web}\nEmail:{e}\nPassword:{passw}\nClick OK to confirm")
        if is_ok:
            # Show Info displays message
            messagebox.showinfo(title="Confirm", message="Your Password has been added successfully\n"
                                                         "Thanks for visiting .")
            try:
                with open("data.json", "r") as file:
                    # Reading the file and saving it in a dictionary named data
                    data = json.load(file)
                    # UPDATING with new data
                    data.update(new_data)

            except FileNotFoundError:
                # Case if file is not created
                with open("data.json","w") as file:
                    # Writing to the file using . dump()
                    json.dump(new_data,file,indent=4)
            else:
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:

                website_entry.delete(0, END)  # Deletes the text written in entry field
                password_entry.delete(0, END)








# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

canvas = Canvas()
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

website = Label(text="Website:", font=FONT)
website.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

search_button = Button(text="Search",command=search,width=13)
search_button.grid(row=1,column=2)

email = Label(text="Email/Username:", font=FONT)

email.grid(row=2, column=0)


email_entry = Entry(width=35)
email_entry.insert(0, "aggarwalhardik862@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:", font=FONT)
password_label.grid(row=3, column=0)

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, columnspan=2)

generate_password_label = Button(text="Generate Password", command=generate_password)
generate_password_label.grid(row=3, column=2,)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()
