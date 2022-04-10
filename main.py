# INSTALLING LIBRARIES
import pip
from image_processor import ImageProcessor

pip.main(["install", "pillow"])

# IMPORTING LIBRARIES
import tkinter  # IF TKINTER IS NOT INSTALLED, YOU CAN INSTALL IT BY RUNNING "sudo apt install python3-tk"
from tkinter import filedialog

# VARIABLES
image_file_path = "None"
watermark_file_path = "None"
save_path = "None"

processor = None

# CONSTANTS
WINDOW_PADX = 25
WINDOW_PADY = 30
WINDOW_BACKGROUND_COLOR = "#FFFF00"

TEXT_COLOR = "#000000"

FONT_NAME = "monospace"


# FUNCTIONS
def browse_files_for_image():
    global image_file_path

    file_types = (
        ("JPEG Files", "*.jpg"),
        ("PNG Files", "*.png"),
        ("All Files", "*.*")
    )

    image_file_path = filedialog.askopenfilename(initialdir=".", title="Select an Image", filetypes=file_types)

    if image_file_path == "" or not image_file_path:
        selection_path_data.config(text="Select A File!", fg="#FF0000")
    else:
        selection_path_data.config(text=image_file_path)


def browse_files_for_watermark():
    global watermark_file_path

    file_types = (
        ("JPEG Files", "*.jpg"),
        ("PNG Files", "*.png"),
        ("All Files", "*.*")
    )

    watermark_file_path = filedialog.askopenfilename(initialdir=".", title="Select an Image", filetypes=file_types)

    if watermark_file_path == "" or not watermark_file_path:
        watermark_selection_path_data.config(text="Select A File", fg="#FF0000")
    else:
        watermark_selection_path_data.config(text=watermark_file_path)


def browse_save_path():
    global save_path

    file_types = ()

    save_path = filedialog.askopenfilename(initialdir=".", title="Select an Image", filetypes=file_types)

    if save_path == "" or not save_path:
        save_path_data.config(text="Using Program Directory", fg="#FF09A0")
    else:
        save_path_data.config(text=save_path)


def add_water_mark():
    global processor
    global save_path

    processor = ImageProcessor(image_path=image_file_path, watermark_path=watermark_file_path, save_path=save_path)

    processor.merge_image()
    # processor.save_merged_image()

    show_button.config(state="active")
    save_button.config(state="active")


def show_image():
    processor.show_merged_image()


def save_image():
    global save_path

    print(f"SAVE PATH: {save_path}")

    if save_path == "":
        save_path = "."
        processor.save_path = "."

    processor.save_merged_image()

# MAKING GUI

# MAKING THE WINDOW
window = tkinter.Tk()

window.title("Image Water Marker")
window.minsize(width=400, height=400)
window.config(padx=WINDOW_PADX, pady=WINDOW_PADY, bg=WINDOW_BACKGROUND_COLOR)

# ADDING TITLE
title = tkinter.Label(text="Image Water Marker", bg=WINDOW_BACKGROUND_COLOR, fg=TEXT_COLOR,
                      font=(FONT_NAME, 25, "bold"))
title.grid(column=0, row=0, columnspan=4, pady=(50-WINDOW_PADY))

# ADDING THE IMAGE SELECTION OPTION
image_selection_label = tkinter.Label(text="Select Image", bg=WINDOW_BACKGROUND_COLOR, fg=TEXT_COLOR,
                                      font=(FONT_NAME, 10))
image_selection_label.grid(column=0, row=1)

image_selection_button = tkinter.Button(text="Select Path", command=browse_files_for_image, bg=WINDOW_BACKGROUND_COLOR, fg=TEXT_COLOR, font=(FONT_NAME, 8), highlightthickness=1, activebackground="#000000", activeforeground="#FFFFFF", highlightbackground=TEXT_COLOR)
image_selection_button.grid(column=1, row=1)

# Selection Path
selection_path_label = tkinter.Label(text="Selected Image Path", bg=WINDOW_BACKGROUND_COLOR, fg=TEXT_COLOR,
                                      font=(FONT_NAME, 10))
selection_path_label.grid(column=0, row=2)

selection_path_data = tkinter.Label(text="Nothing Selected!", bg=WINDOW_BACKGROUND_COLOR, fg=TEXT_COLOR,
                                      font=(FONT_NAME, 8))
selection_path_data.grid(column=1, row=2)

# EMPTY WIDGET THAT WILL ACT LIKE A SEPERATOR
sep = tkinter.Label(text="", bg=WINDOW_BACKGROUND_COLOR, fg=WINDOW_BACKGROUND_COLOR)
sep.grid(column=0, row=3, columnspan=2)

# SELECTING WATERMARK
watermark_selection_label = tkinter.Label(text="Select Water Mark Image", bg=WINDOW_BACKGROUND_COLOR, fg=TEXT_COLOR,
                                      font=(FONT_NAME, 10))
watermark_selection_label.grid(column=0, row=4)

watermark_selection_button = tkinter.Button(text="Select Path", command=browse_files_for_watermark, bg=WINDOW_BACKGROUND_COLOR, fg=TEXT_COLOR, font=(FONT_NAME, 8), highlightthickness=1, activebackground="#000000", activeforeground="#FFFFFF", highlightbackground=TEXT_COLOR)
watermark_selection_button.grid(column=1, row=4)

# SELECTION PATH

watermark_selection_path_label = tkinter.Label(text="Selected WaterMark Path", bg=WINDOW_BACKGROUND_COLOR, fg=TEXT_COLOR,
                                      font=(FONT_NAME, 10))
watermark_selection_path_label.grid(column=0, row=5)

watermark_selection_path_data = tkinter.Label(text="Nothing Selected!", bg=WINDOW_BACKGROUND_COLOR, fg=TEXT_COLOR,
                                      font=(FONT_NAME, 8))
watermark_selection_path_data.grid(column=1, row=5)

# THE SEPERATOR
sep2 = tkinter.Label(text="", bg=WINDOW_BACKGROUND_COLOR, fg=WINDOW_BACKGROUND_COLOR)
sep2.grid(column=0, row=6, columnspan=2)

# WHERE THE RESULT IMAGE WILL BE SAVED
save_selection_label = tkinter.Label(text="Select Save Path", bg=WINDOW_BACKGROUND_COLOR, fg=TEXT_COLOR,
                                      font=(FONT_NAME, 10))
save_selection_label.grid(column=0, row=7)

save_selection_button = tkinter.Button(text="Select Path", command=browse_save_path, bg=WINDOW_BACKGROUND_COLOR, fg=TEXT_COLOR, font=(FONT_NAME, 8), highlightthickness=1, activebackground="#000000", activeforeground="#FFFFFF", highlightbackground=TEXT_COLOR)
save_selection_button.grid(column=1, row=7)

# SELECTION PATH
save_path_label = tkinter.Label(text="Selected Save Path", bg=WINDOW_BACKGROUND_COLOR, fg=TEXT_COLOR,
                                      font=(FONT_NAME, 10))
save_path_label.grid(column=0, row=8)

save_path_data = tkinter.Label(text="Nothing Selected!", bg=WINDOW_BACKGROUND_COLOR, fg=TEXT_COLOR,
                                      font=(FONT_NAME, 8))
save_path_data.grid(column=1, row=8)

# THE SEPERATOR
sep3 = tkinter.Label(text="", bg=WINDOW_BACKGROUND_COLOR, fg=WINDOW_BACKGROUND_COLOR)
sep3.grid(column=0, row=9, columnspan=2)

# Add Water Mark Button
add_button =  tkinter.Button(text="Add Water Mark", command=add_water_mark, bg=WINDOW_BACKGROUND_COLOR, fg=TEXT_COLOR, font=(FONT_NAME, 8), highlightthickness=1, activebackground="#000000", activeforeground="#FFFFFF", highlightbackground=TEXT_COLOR)
add_button.grid(column=0, row=10, columnspan=2)

# Show Image Button
show_button = tkinter.Button(text="Show Image",  command=show_image, bg=WINDOW_BACKGROUND_COLOR, fg=TEXT_COLOR, font=(FONT_NAME, 8), highlightthickness=1, activebackground="#000000", activeforeground="#FFFFFF", highlightbackground=TEXT_COLOR, state="disabled")
show_button.grid(column=0, row=11, columnspan=2, pady=20)

# Save Image Button
save_button = tkinter.Button(text="Save Image",  command=save_image, bg=WINDOW_BACKGROUND_COLOR, fg=TEXT_COLOR, font=(FONT_NAME, 8), highlightthickness=1, activebackground="#000000", activeforeground="#FFFFFF", highlightbackground=TEXT_COLOR, state="disabled")
save_button.grid(column=0, row=12, columnspan=2)

# RUNNING THE WINDOW IN AN LOOP
window.mainloop()
