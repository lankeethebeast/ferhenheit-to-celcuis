from tkinter import *

def fahrenheit_to_celcius():
    fahrenheit = ent_temperature.get()
    celsius = (5/9) *(float(fahrenheit) -32)
    lbl_result["text"] = f"{round(celsius, 2)}\N{DEGREE CELSIUS}"

screen = Tk()
screen.title("Temperature Converter")
window_width = 200
window_height = 50
screen_width = screen.winfo_screenwidth()
screen_height = screen.winfo_screenheight()

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

screen.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
screen.resizable(False, False)
frame = Frame(master=screen)
ent_temperature = Entry(master=frame, width=10)
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp = Label(master=frame, text="\N{DEGREE FAHRENHEIT}")
lbl_temp.grid(row=0, column=1, sticky="w")
frame.grid(row=0, column=0, padx=10)
btn_convert = Button(master=screen, text="\N{RIGHTWARDS BLACK ARROW}", command=fahrenheit_to_celcius)
btn_convert.grid(row=0, column=1, padx=10)
lbl_result = Label(master=screen)
lbl_result.grid(row=0, column=2, padx=10)

screen.mainloop()
