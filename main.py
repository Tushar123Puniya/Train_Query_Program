import tkinter as tk
from tkinter import PhotoImage, simpledialog, messagebox
import sqlite3
import csv
import userdetails as usd
from tkinter import ttk  # Import ttk for themed widgets
import train_utils as tu
Days={
    1:"Monday",
    2:"Tuesday",
    3:"Wednesday",
    4:"Thursday",
    5:"Friday",
    6:"Saturday",
    7:"Sunday"
}

def function_(a):
   s=""
   for i in range(len(a)):
      t='Number: '+str(a[i][0])+'\n'+'Name: '+str(a[i][1])+'\n'+'Destination: '+str(a[i][2])+'\n'+'Depature Time: '+str(a[i][3])+'\n'+'Boarding Days: '
      x=4
      for x in range(4,len(a[i])):
         if(a[i][x]=='1'):
            t=t+Days[x-3]+' '
      s=s+t+'\n'+'\n'
   return s

def function(a):
    # print(a)
    s='Number: '+str(a[0][0])+'\n'+'Name: '+str(a[0][1])+'\n'+'Destination: '+str(a[0][2])+'\n'+'Depature Time: '+str(a[0][3])+'\n'+'Boarding Days: '
    x=4
    for x in range(4,len(a[0])):
        if(a[0][x]=='1'):
            s=s+Days[x-3]+' '
    return s

def run_function(func,s):
    s="'"+s+"'"
    result = function(func(s))
    # print(result)
    output_window = tk.Tk()
    output_window.title("Details")
    
    # Set the size of the window (width x height)
    output_window.geometry("1080x920")  # Adjust the dimensions as needed

    # Make the window resizable
    output_window.resizable(True, True)

    # Create a label with custom styling to display the list
    formatted_result=result
    
    output_label = tk.Label(output_window, text=formatted_result, bg="white", fg="black", font=("Helvetica", 14))
    output_label.pack(expand=True, fill='both')  # Make the label expand to fill the window
    
def search_it(destination):
    s = destination.get()
    s = "'" + s + "'"
    result = function_(tu.query_on_location(s))

    # Create the output window
    output_window = tk.Tk()
    output_window.title("Details")

    # Set the size of the window (width x height)
    output_window.geometry("800x600")  # Adjust the dimensions as needed

    # Make the window resizable
    output_window.resizable(True, True)

    # Create a canvas widget for scrolling
    canvas = tk.Canvas(output_window)
    canvas.pack(fill="both", expand=True)

    # Create vertical scrollbar
    vscrollbar = tk.Scrollbar(output_window, orient="vertical", command=canvas.yview)
    vscrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=vscrollbar.set)

    # Create horizontal scrollbar
    hscrollbar = tk.Scrollbar(output_window, orient="horizontal", command=canvas.xview)
    hscrollbar.pack(side="bottom", fill="x")
    canvas.configure(xscrollcommand=hscrollbar.set)

    # Create a frame to hold the output label
    output_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=output_frame, anchor="nw")

    # Create a label with custom styling to display the result
    formatted_result = result

    output_label = tk.Label(output_frame, text=formatted_result, bg="white", fg="black", font=("Helvetica", 14))
    output_label.pack(expand=True, fill='both')  # Make the label expand to fill the frame

    # Configure canvas to update scroll region when resized
    def on_canvas_configure(event):
        canvas.config(scrollregion=canvas.bbox("all"))

    canvas.bind("<Configure>", on_canvas_configure)

    output_window.mainloop()
    
def search_train_destination():
    # Create the main window
    root = tk.Tk()
    root.title("Search Train by Destination")
    root.geometry("400x200")

    # Create a label to provide instructions
    label = ttk.Label(root, text="Enter the destination station:")
    label.pack(pady=10)

    # Create an entry field for user input
    destination_entry = ttk.Entry(root)
    destination_entry.pack()

    # Create a label to display the result
    result_label = ttk.Label(root, text="")
    result_label.pack()

    # Create a button to perform the search
    search_button = ttk.Button(root, text="Search", command=lambda: search_it(destination_entry))
    search_button.pack()

    # Start the Tkinter main loop
    root.mainloop()

# Call the search_train_destination function to run the GUI
    output_window.mainloop()


def get_details(option_var, result_label, entry):
    selected_option = option_var.get()
    if selected_option == "By Train Name":
        train_name = entry.get()
        # Implement functionality to fetch details by train name
        result_label.config(text=f"Fetching details for train name: {train_name}")
        run_function(tu.query_on_train_name, train_name)
    elif selected_option == "By Train Number":
        train_number = entry.get()
        # Implement functionality to fetch details by train number
        result_label.config(text=f"Fetching details for train number: {train_number}")
        run_function(tu.query_on_train_number, train_number)
        
def set_this_option(option,selected):
    selected.set(option)
    
def get_train_details():
    # Create the main window
    root = tk.Tk()
    root.title("Train Details")
    root.geometry("400x200")

    # Create a label to provide instructions
    label = ttk.Label(root, text="Select an option to get train details:")
    label.pack(pady=10)

    # Create a variable to store the selected option
    option_var = tk.StringVar()
    option_var.set("By Train Name")
    
    # Create radio buttons for selecting the option
    train_name_radio = ttk.Radiobutton(root, text="By Train Name", variable=option_var, value="By Train Name",
                                       command=lambda: set_this_option("By Train Name",option_var))
    train_number_radio = ttk.Radiobutton(root, text="By Train Number", variable=option_var, value="By Train Number",
                                         command=lambda: set_this_option("By Train Number",option_var))

    # Create an entry field for user input
    entry_label = ttk.Label(root, text="Enter Train Name or Train Number:")
    entry = ttk.Entry(root)

    # Create a label to display the result
    result_label = ttk.Label(root, text="")

    # Create a button to perform the selected action
    action_button = ttk.Button(root, text="Get Train Details", command=lambda: get_details(option_var, result_label, entry))

    # Place widgets in the window
    train_name_radio.pack()
    train_number_radio.pack()
    entry_label.pack()
    entry.pack()
    action_button.pack()
    result_label.pack()

    # Start the Tkinter main loop
    root.mainloop()


def on_button_click(selected_option, result_label):
    # Get the selected option
    option = selected_option.get()
    
    # Perform an action based on the selected option
    if option == "Getting Details":
        result_label.config(text="Getting Details selected")
        get_train_details()
        # Add code for the "Getting Details" action here
    elif option == "Searching Train":
        result_label.config(text="Searching Train selected")
        search_train_destination()
        # Add code for the "Searching Train" action here

def set_selected_option(option, selected_option):
    selected_option.set(option)

def queries():
    # Create the main window
    root = tk.Tk()
    root.title("Query")
    root.geometry("400x200")

    # Create a label to provide instructions
    label = ttk.Label(root, text="Select the query:")
    label.pack(pady=10)

    # Create a variable to store the selected option
    selected_option = tk.StringVar()
    selected_option.set("Getting Details")  # Set the default option

    # Create radio buttons
    getting_details_radio = ttk.Radiobutton(root, text="Getting Details", variable=selected_option, value="Getting Details",
                                            command=lambda: set_selected_option("Getting Details", selected_option))
    searching_train_radio = ttk.Radiobutton(root, text="Searching Train", variable=selected_option, value="Searching Train",
                                            command=lambda: set_selected_option("Searching Train", selected_option))

    # Create a label to display the result
    result_label = ttk.Label(root, text="")

    # Create a button to perform the selected action
    action_button = ttk.Button(root, text="Perform query", command=lambda: on_button_click(selected_option, result_label))

    # Place widgets in the window
    getting_details_radio.pack()
    searching_train_radio.pack()
    action_button.pack()
    result_label.pack()

    # Start the Tkinter main loop
    root.mainloop()

  
def show_user_status():
    user_status = var.get()
    if user_status == 1:
        messagebox.showinfo("User Status", "Welcome, New User!")
        new_data()
    elif user_status == 2:
        show_login_details()
    else:
        messagebox.showwarning("User Status", "Please select an option.")

def validate_signup(username_entry,password_entry) :
    username=username_entry.get()
    password=password_entry.get()
    if usd.read(username,password)==False:
        usd.write(username,password)
        messagebox.showinfo("Signup Successful","Your information is saved")
    else:
        messagebox.showwarning("Signup Failed", "Use different Username or Password.")

def validate_login(username_entry,password_entry) :
    username=username_entry.get()
    password=password_entry.get()
    if usd.read(username,password):
        messagebox.showinfo("Login Successful", "Welcome back, Old User!")
        queries()
    else:
        messagebox.showwarning("Login Failed", "Invalid username or password.")


def new_data():
    signup_window = tk.Toplevel(root)
    signup_window.title("Sign Up")
    signup_window.geometry("300x250")  # Larger window size

    username_label = tk.Label(signup_window, text="Username:", font=("Helvetica", 12))
    username_label.pack(pady=10)

    username_entry = tk.Entry(signup_window, font=("Helvetica", 12))
    username_entry.pack(pady=5)

    password_label = tk.Label(signup_window, text="Password:", font=("Helvetica", 12))
    password_label.pack(pady=10)

    password_entry = tk.Entry(signup_window, font=("Helvetica", 12), show='*')
    password_entry.pack(pady=5)

    # Pass a function reference without calling it
    submit_button = tk.Button(signup_window, text="Submit", command=lambda: validate_signup(username_entry, password_entry), font=("Helvetica", 12))
    submit_button.pack(pady=20)

    
        
def show_login_details():
    login_window = tk.Toplevel(root)
    login_window.title("Login")
    login_window.geometry("300x250")  # Larger window size
    username_label = tk.Label(login_window, text="Username:", font=("Helvetica", 12))
    username_label.pack(pady=10)
    username_entry = tk.Entry(login_window, font=("Helvetica", 12))
    username_entry.pack(pady=5)

    password_label = tk.Label(login_window, text="Password:", font=("Helvetica", 12))
    password_label.pack(pady=10)
    password_entry = tk.Entry(login_window, font=("Helvetica", 12), show='*')
    password_entry.pack(pady=5)

    submit_button = tk.Button(login_window, text="Submit", command=lambda: validate_login(username_entry,password_entry), font=("Helvetica", 12))
    submit_button.pack(pady=20)
    
# Create the main window
root = tk.Tk()
root.title("User Status")

# Increase the window size
root.geometry("700x400")  # New size: 800x600

# Load the background image
background_image = PhotoImage(file="train__.png")

# Create a Label with the background image
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)  # Cover the entire window

# Display greeting message
greeting_label = tk.Label(root, text="Welcome to our App!", font=("Helvetica", 16), fg="Red")
greeting_label.pack(pady=40)  # Increased padding

# User status options
var = tk.IntVar()
var.set(1)  # Default value
new_user_button = tk.Radiobutton(root, text="New User", variable=var, value=1, font=("Helvetica", 12), bg="white", fg="black", padx=20)
old_user_button = tk.Radiobutton(root, text="Old User", variable=var, value=2, font=("Helvetica", 12), bg="white", fg="black", padx=20)
new_user_button.pack(pady=10)  # Adjusted gap
old_user_button.pack(pady=10)  # Adjusted gap

# Submit button
submit_button = tk.Button(root, text="Submit",fg="blue", command=show_user_status, font=("Helvetica", 12))
submit_button.pack(pady=30)  # Increased padding

# Start the Tkinter event loop
root.mainloop()
