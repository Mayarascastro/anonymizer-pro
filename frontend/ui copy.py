import customtkinter as ctk

def create_ui(window, select_input_file, run_deface, clear_input_file):
    window.title("Anonymizer Pro")
    window.geometry("500x300")

    input_label = ctk.CTkLabel(window, text="No file selected.")
    input_label.pack(pady=20)

    # The button selects the video to anonymize.
    button_selectinput_file = ctk.CTkButton(window, text="Select an mp4 file", command=select_input_file(input_label, status_label))
    button_selectinput_file.pack(pady=10)

    # the button runs the "deface" script and deletes the source file, the video is not anonymized.
    button_run_deface = ctk.CTkButton(window, text="Run deface", command=run_deface(input_label, status_label))
    button_run_deface.pack(pady=10)

    # The button clears the selected file, so the user can insert another video into the script.
    button_clearinput_file = ctk.CTkButton(window, text="Clear input file", command=clear_input_file(input_label, status_label))
    button_clearinput_file.pack(pady=10)

    status_label = ctk.CTkLabel(window, text="Status: Waiting for .mp4 video selection...")
    status_label.pack(pady=10)

    return input_label, status_label