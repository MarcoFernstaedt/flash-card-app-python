from tkinter import *

from pygments import highlight
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# canvas
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img, )
canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"), )
canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
checkmark_img = PhotoImage(file="images/right.png")
known_button = Button(image=checkmark_img, highlightthickness=0)
known_button.grid(column=1, row=1)

cross_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_img, highlightthickness=0)
unknown_button.grid(column=0, row=1)


window.mainloop()