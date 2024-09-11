import customtkinter as ctk
from tkinter import Tk
from frontend.ui import create_ui
from backend.deface_handler import select_input_file, run_deface, clear_input_file


def main():
    window = ctk.CTk()

    window.input_mp4_file = None

    input_label, status_label = create_ui(
        window,
        select_input_file=lambda: select_input_file(window, input_label),
        run_deface=lambda: run_deface(window, input_label, status_label),
        clear_input_file=lambda: clear_input_file(window, input_label, status_label)
    )
    
    window.mainloop()

if __name__ == "__main__":
    main()