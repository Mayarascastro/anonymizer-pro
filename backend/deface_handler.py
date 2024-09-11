import os
import subprocess
from tkinter import filedialog, messagebox

def select_mp4_file(window, input_label):
    file_path = filedialog.askopenfilename(
        filetypes=[("MP4 files", "*mp4")], 
        title="Select the .mp4 file.")
    if file_path:
        input_label.config(text=f"Selected file: {os.path.basename(file_path)}")
        window.input_label = file_path


def run_deface(window, input_label):
    if hasattr(window, 'input_mp4_file'):
        output_file = filedialog.asksaveasfilename(
            defaultextension=".mp4",
            filetypes=[("MP4 files", "*mp4")],
            title="Save the anonymized file"
        )
        if output_file:
            try:
                subprocess.run(["deface", "-i", window.input_label, "-o", output_file], check=True)
                messagebox.showinfo("Success", "Complete anonymization process!")

                if os.path.exists(window.input_mp4_file):
                    os.remove(window.input_mp4_file)
                    messagebox.showinfo("File deleted!", "The original file was deleted successfully.")
                    input_label.configure(text="Original file deleted.")
                else:
                    messagebox.showwarning("Warning", "The original file was not found.")
            
            except subprocess.CalledProcessError:
                messagebox.showerror("Error", "Error runing deface.")

        else:
            messagebox.showwarning("Warning", "No .mp4 file was selected.")

def clear_input_file(window, input_label):
    input_label.configure(text="No file was selected.")
    if hasattr(window, 'input_mp4_file'):
        del window.input_mp4_file