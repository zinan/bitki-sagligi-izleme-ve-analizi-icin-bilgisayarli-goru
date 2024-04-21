import tkinter as tk
import os

root = tk.Tk()
root.title("Realtime Sensor Data Optimization and Predictions")
root.geometry("500x600")

bg_color = "#f2f2f2"
root.configure(bg=bg_color)

title_label = tk.Label(root, text="Choose a model to train:", font=("Arial", 18), bg=bg_color, fg="#333")
title_label.pack(pady=20)

button_frame = tk.Frame(root, bg=bg_color)
button_frame.pack(pady=10)

button_width = 20
button_height = 2
button_bg = "#f5f5f5"
button_fg = "#333"

dt_button = tk.Button(button_frame, text="Train Decision Tree", width=button_width, height=button_height, bg=button_bg, fg=button_fg, font=("Arial", 12), command=lambda: os.system('python dt.py'))
lstm_button = tk.Button(button_frame, text="Train LSTM", width=button_width, height=button_height, bg=button_bg, fg=button_fg, font=("Arial", 12), command=lambda: os.system('python lstm.py'))
lr_button = tk.Button(button_frame, text="Train Linear Regression", width=button_width, height=button_height, bg=button_bg, fg=button_fg, font=("Arial", 12), command=lambda: os.system('python LR.py'))
rf_button = tk.Button(button_frame, text="Train Random Forest", width=button_width, height=button_height, bg=button_bg, fg=button_fg, font=("Arial", 12), command=lambda: os.system('python randomui.py'))
ds_button = tk.Button(button_frame, text="create new dataset", width=button_width, height=button_height, bg=button_bg, fg=button_fg, font=("Arial", 12), command=lambda: os.system('python dataset.py'))

dt_button.pack(pady=5)
lstm_button.pack(pady=5)
lr_button.pack(pady=5)
rf_button.pack(pady=5)
ds_button.pack(pady=5)

other_button_frame = tk.Frame(root, bg=bg_color)
other_button_frame.pack(pady=20)

test_button = tk.Button(other_button_frame, text="Test Models", width=button_width, height=button_height, bg=button_bg, fg=button_fg, font=("Arial", 12), command=lambda: os.system('python test_models.py'))
test_button.pack(side=tk.LEFT, padx=10)

dashboard_button = tk.Button(other_button_frame, text="Server Dashboard", width=button_width, height=button_height, bg=button_bg, fg=button_fg, font=("Arial", 12), command=lambda: os.system('python gui1.py'))
dashboard_button.pack(side=tk.RIGHT, padx=10)

root.mainloop()
