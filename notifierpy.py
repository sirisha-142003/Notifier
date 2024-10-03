from plyer import notification
from tkinter import messagebox, Label, Entry, Button, Tk
from PIL import Image, ImageTk  # Corrected import
import time

t = Tk()
t.title('Notifier')
t.geometry("500x300")
img = Image.open("notifier-label.png")
tkimage = ImageTk.PhotoImage(img)

# Get details
def get_details():
    get_title = title.get()
    get_msg = msg.get()
    get_time = time1.get()

    if get_title == "" or get_msg == "" or get_time == "":
        messagebox.showerror("Alert", "All fields are required!")
    else:
        int_time = float(get_time)
        seco = int_time
        messagebox.showinfo("Notifier set", "Set notification?")
        t.destroy()
        time.sleep(seco)

        notification.notify(
            title=get_title,
            message=get_msg,
            app_name="Notifier",
            app_icon="ico.ico",
            toast=True,
            timeout=10
        )

img_label = Label(t, image=tkimage).grid()

# Label - Title
t_label = Label(t, text="Title to Notify", font=("times new roman", 10))
t_label.place(x=12, y=70)

# ENTRY - Title
title = Entry(t, width="25", font=("times new roman", 13))
title.place(x=123, y=70)

# Label - Message
m_label = Label(t, text="Display Message", font=("times new roman", 10))
m_label.place(x=12, y=120)

# ENTRY - Message
msg = Entry(t, width="40", font=("times new roman", 13))
msg.place(x=123, height=30, y=120)

# Label - Time
time_label = Label(t, text="Set Time", font=("times new roman", 10))
time_label.place(x=12, y=175)

# ENTRY - Time
time1 = Entry(t, width="5", font=("times new roman", 13))
time1.place(x=123, y=175)

# Label - sec
time_sec_label = Label(t, text="sec", font=("times new roman", 10))
time_sec_label.place(x=175, y=180)

but = Button(t, text="SET", font=("times new roman", 14, "bold"), fg="#ffffff", bg="#528DFF", width=20,
             relief="raised", command=get_details)
but.place(x=170, y=230)

t.resizable(0, 0)
t.mainloop()
