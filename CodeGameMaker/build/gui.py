from pathlib import Path
from tkinter import Tk, Canvas, Text, Button, PhotoImage
import os

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
os.system("python CodingLanguage.src.bartmain.py")
window.geometry("1440x1024")
window.configure(bg = "#505050")

canvas = Canvas(
    window,
    bg = "#505050",
    height = 1020,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=0.0,
    y=0.0,
    width=63.0,
    height=54.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=73.0,
    y=0.0,
    width=93.0,
    height=54.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=176.0,
    y=0.0,
    width=106.0,
    height=54.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=102.0,
    y=968.0,
    width=34.0,
    height=39.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=0.0,
    y=951.0,
    width=73.0,
    height=73.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    480.0,
    502.5,
    image=entry_image_1
)

entry_1 = Text(
    bd=0,
    bg="#484848",
    font= ('Helvetica 20'),
    highlightthickness=0
)
entry_1.place(
x=0.0,
y=54.0,
width=960.0,
height=895.0,
)

canvas.create_text(
    1059.0,
    58.0,
    anchor="nw",
    text="Asset Inspector",
    fill="#FFFFFF",
    font=("Roboto", 40 * -1)
)
window.resizable(True, True)
window.mainloop()