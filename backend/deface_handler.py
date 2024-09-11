import os
import subprocess
from tkinter import filedialog, messagebox

def select_input_file(window, input_label):
    file_path = filedialog.askopenfilename(
        filetypes=[("MP4 files", "*.mp4")])
    if file_path:
        input_label.configure(text=f"Selected file: {os.path.basename(file_path)}")
        window.input_mp4_file = file_path
        print(f"File selected: {file_path}")


def run_deface(window, input_label, status_label):
    file_path = getattr(window, 'input_mp4_file', None)
    if not file_path:
        messagebox.showerror("Error", "No file selected.")
        print("Error: No file selected")
        return 

        file_name, file_extension = os.path.splitext(file_path)
        output_file = f"{file_name}_anonymized{file_extension}"
        print(f"Running deface on file: {file_path}, output: {output_file}")

        status_label.configure(text="Status: In progress")

        try:                
            subprocess.run(
            ["deface", file_path, "--output", output_file, "--replacewith", "mosaic"],
            check=True
            )

            # Update status
            status_label.configure(text="Status: Completed successfully!")
            messagebox.showinfo("Success", "Anonymization process completed!\nOutput file: {output_file}")

            # Delete origin file
            if os.path.exists(file_path):
                os.remove(file_path)
                input_label.configure(text="Original file deleted.")
                status_label.configure(text="Status: Original file deleted!")
                print(f"Original file {file_path} deleted.")
            else:
                messagebox.showwarning("Warning", "The original file was not found.")
                status_label.configure(text="Status: Original file deleted!")
                print(f"Original file {file_path} not found for deletion.")
            
        except subprocess.CalledProcessError as e:
            status_label.configure(text="Status: Processing error.")
            messagebox.showerror("Error", f"Error running deface: {str(e)}")

def clear_input_file(window, input_label, status_label):
    input_label.configure(text="No file was selected.")
    if hasattr(window, 'input_mp4_file'):
        del window.input_mp4_file
        status_label.configure(text="Status: Input fil cleared.")
        print("Input file cleared.")