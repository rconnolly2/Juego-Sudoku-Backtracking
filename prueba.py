import tkinter as tk

# Define the aspect ratio for the grid (1:1)
aspect_ratio = 1

# Width reserved for the menu
menu_width = 200



root = tk.Tk()
root.title("Fixed Aspect Ratio Grid with Menu")

# Calculate the initial size based on the aspect ratio and menu width
initial_height = 400
initial_width = initial_height * aspect_ratio + menu_width

# Set the window size and enforce the aspect ratio
root.geometry(f"{int(initial_width)}x{initial_height}")
root.minsize(width=initial_width, height=initial_height)

# Create a 2D list to hold the grid cells (Frames)
rows = 3
cols = 3
grid_cells = [[None for _ in range(cols)] for _ in range(rows)]

# Create the grid of resizable boxes
for row in range(rows):
    for col in range(cols):
        cell = tk.Frame(root, bg="green" if (row + col) % 2 == 0 else "red")
        cell.grid(row=row, column=col, sticky="nsew")  # Use sticky to expand cells
        grid_cells[row][col] = cell

# Configure row and column weights to make the cells expand with the window
for row in range(rows):
    root.grid_rowconfigure(row, weight=1)
for col in range(cols):
    root.grid_columnconfigure(col, weight=1)

# Create a menu on the right side
menu_frame = tk.Frame(root, bg="blue", width=menu_width, height=400)
menu_frame.grid(row=0, column=cols, rowspan=rows, sticky="nw")

# Configure column weight for the menu frame
root.grid_columnconfigure(cols, weight=0)

print(grid_cells)
root.mainloop()