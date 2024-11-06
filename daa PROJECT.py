import tkinter as tk
from tkinter import ttk
import random
import time

# Colors
BAR_COLOR = "cyan"
BACKGROUND_COLOR = "black"
HIGHLIGHT_COLOR = "yellow"

# Initialize the main window
root = tk.Tk()
root.title("Sorting Algorithm Visualizer")
root.geometry("800x600")
root.config(bg=BACKGROUND_COLOR)

# Variables
data = []

# Create the canvas for drawing the bars
canvas = tk.Canvas(root, width=700, height=400, bg=BACKGROUND_COLOR)
canvas.pack(pady=20)

# Draw the data bars on the canvas
def draw_data(data, highlight=[]):
    canvas.delete("all")
    c_width = 700
    c_height = 400
    bar_width = c_width / (len(data) + 1)
    offset = 10
    spacing = 5
    max_height = max(data) if data else 1

    for i, height in enumerate(data):
        x0 = i * bar_width + offset + spacing
        y0 = c_height - (height / max_height * c_height)
        x1 = (i + 1) * bar_width + offset
        y1 = c_height

        color = HIGHLIGHT_COLOR if i in highlight else BAR_COLOR
        canvas.create_rectangle(x0, y0, x1, y1, fill=color)
    root.update_idletasks()

# Generate random data
def generate_data():
    global data
    data = [random.randint(10, 100) for _ in range(50)]
    draw_data(data)

# Bubble Sort Algorithm
def bubble_sort(data, draw_data, delay):
    for i in range(len(data) - 1):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                draw_data(data, [j, j + 1])
                time.sleep(delay)
    draw_data(data)

# Selection Sort Algorithm
def selection_sort(data, draw_data, delay):
    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
        draw_data(data, [i, min_idx])
        time.sleep(delay)
    draw_data(data)

# Insertion Sort Algorithm
def insertion_sort(data, draw_data, delay):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
            draw_data(data, [j + 1, i])
            time.sleep(delay)
        data[j + 1] = key
        draw_data(data, [j + 1, i])
    draw_data(data)

# Sorting function dispatcher
def start_sort():
    global data
    if algo_choice.get() == "Bubble Sort":
        bubble_sort(data, draw_data, speed_scale.get())
    elif algo_choice.get() == "Selection Sort":
        selection_sort(data, draw_data, speed_scale.get())
    elif algo_choice.get() == "Insertion Sort":
        insertion_sort(data, draw_data, speed_scale.get())

# UI Elements
ui_frame = tk.Frame(root, bg=BACKGROUND_COLOR)
ui_frame.pack(pady=10)

# Dropdown for algorithm selection
algo_choice = tk.StringVar()
algo_menu = ttk.Combobox(ui_frame, textvariable=algo_choice, values=["Bubble Sort", "Selection Sort", "Insertion Sort"], state="readonly")
algo_menu.grid(row=0, column=0, padx=5, pady=5)
algo_menu.current(0)

# Speed scale for controlling the sorting speed
speed_scale = tk.Scale(ui_frame, from_=0.01, to=0.5, length=200, digits=2, resolution=0.01, orient="horizontal", label="Sorting Speed [s]", bg=BACKGROUND_COLOR, fg="white")
speed_scale.grid(row=0, column=1, padx=5, pady=5)
speed_scale.set(0.1)

# Generate and Start buttons
generate_button = tk.Button(ui_frame, text="Generate Data", command=generate_data, bg="orange", fg="black")
generate_button.grid(row=0, column=2, padx=5, pady=5)

start_button = tk.Button(ui_frame, text="Start Sorting", command=start_sort, bg="cyan", fg="black")
start_button.grid(row=0, column=3, padx=5, pady=5)

# Run the application
generate_data()
root.mainloop()
