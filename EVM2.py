from tkinter import *

# Initialize the root window
root = Tk()
root.title("EVM")
root.geometry("700x500")

# Initialize vote counts
v1 = 0
v2 = 0

# Define the functions for voting and result
def vote1():
    global v1
    v1 += 1
    print("Value of v1:", v1)

def vote2():
    global v2
    v2 += 1
    print("Value of v2:", v2)

def result():
    # Clear any existing result label
    for widget in root.grid_slaves(row=3, column=2):
        widget.grid_forget()

    if v1 > v2:
        Label(root, text="Winner: party-1", height=2, width=20).grid(row=3, column=2)
    elif v2 > v1:
        Label(root, text="Winner: party-2", height=2, width=20).grid(row=3, column=2)
    else:
        Label(root, text="Result: Tie", height=2, width=20).grid(row=3, column=2)

# Create labels and buttons for Party-1
Label(root, text="Party-1", height=2, width=10).grid(row=1, column=1)
Button(root, text="Vote", command=vote1).grid(row=1, column=2)

# Create labels and buttons for Party-2
Label(root, text="Party-2", height=2, width=10).grid(row=2, column=1)
Button(root, text="Vote", command=vote2).grid(row=2, column=2)

# Create button to display the result
Button(root, text="Show Result", command=result).grid(row=3, column=3)

# Start the main loop
root.mainloop()
