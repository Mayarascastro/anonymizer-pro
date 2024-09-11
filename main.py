import customtkinter as ctk 
from frontend.ui import create_ui
from backend.deface_handler import select_mp4_file, run_deface, clear_input_file


window = ctk.CTk()

input_label = create_ui(
    window=window,
    select_mp4_file=lambda: select_mp4_file(window, input_label),
    run_deface=lambda: run_deface(window, input_label),
    clear_input_file=lambda: clear_input_file(window, input_label)
)

window.mainloop()