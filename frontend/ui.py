import customtkinter as ctk 
from tkinter import filedialog, messagebox

def create_ui(window, select_mp4_file, run_deface, clear_input_file, delete_mp4_origin):
    window.title("Anonymizer Pro")
    window.geometry("500x300")

    input_label = ctk.CTkLabel(window, text="No file selected.")
    input_label.pack(pady=20)

    # The button selects the video to anonymize.
    button_selectmp4_file = ctk.CTkButton(window, text="Select an mp4 file", command=select_mp4_file)
    button_selectmp4_file.pack(pady=10)

    # the button runs the "deface" script and deletes the source file, the video is not anonymized.
    button_run_deface = ctk.CTkButton(window, text="Select an mp4 file", command=run_deface)
    button_run_deface.pack(pady=10)

    # The button clears the selected file, so the user can insert another video into the script.
    button_clearinput_file = ctk.CTkButton(window, text="Select an mp4 file", command=clear_input_file)
    button_clearinput_file.pack(pady=10)

    return input_label