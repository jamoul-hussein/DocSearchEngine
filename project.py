from tkinter import *
import tkinter.font as font

unified_background = "#333333"
unified_purple_color = "#8A2BE2"

window = Tk()
window.title("GUI created with tkinter")
window.geometry("800x800")
window.configure(bg=unified_background)

screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()

# =========================================================
# Header Section
# =========================================================
bold25 = font.Font(size=25, weight=font.BOLD)
var = StringVar()
Label_header = Label(window, textvariable=var, bg=unified_background, font=bold25, fg=unified_purple_color)
var.set("Doc Search Engine")
Label_header.pack(pady=40)

# =========================================================
# Search Frame
# =========================================================
search_frame = Frame(window, bg=unified_background)

search_input = Entry(search_frame, font=("arial", 20), highlightthickness=4, width=40, bg="#706f6f", fg="white")
search_input.config(highlightbackground="grey", highlightcolor="grey")
search_input.grid(row=0, column=0)

buttonText = StringVar()
search_button = Button(search_frame, textvariable=buttonText, font=font.Font(size=17, weight=font.BOLD), bg=unified_purple_color, fg="white")
buttonText.set("Search")
search_button.grid(row=0, column=1, padx=10)

search_frame.pack(pady=40)

# =========================================================
# Output Search Frame
# =========================================================

window.mainloop()
