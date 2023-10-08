import tkinter as tk

def label_click(event):
    clicked_label = event.widget  # Get the label widget that triggered the event
    parent_frame = clicked_label.master  # Get the parent frame of the label

    if parent_frame == frame1:
        print("Label in Frame 1 clicked!")
    elif parent_frame == frame2:
        print("Label in Frame 2 clicked!")

# Create the main Tkinter window
root = tk.Tk()
root.title("Click Detection")

# Create Frame 1 widget
frame1 = tk.Frame(root, width=200, height=100, bg="lightblue")
frame1.pack()

# Add a Label widget to Frame 1
label1 = tk.Label(frame1, background="red", text="Click me (Frame 1)!", padx=10, pady=10)
label1.setvar
label1.pack()

# Bind a click event to Label 1
label1.bind("<Button-1>", label_click)

# Create Frame 2 widget
frame2 = tk.Frame(root, width=200, height=100, bg="lightgreen")
frame2.pack()

# Add a Label widget to Frame 2
label2 = tk.Label(frame2, background="blue", text="Click me (Frame 2)!", padx=10, pady=10)
label2.pack()

# Bind a click event to Label 2
label2.bind("<Button-1>", label_click)

# Start the Tkinter event loop
root.mainloop()