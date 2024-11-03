#pip install moviepy
import os
import shutil
import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip


# Function to convert mkv files to mp4
def convert_mkv_to_mp4(src_folder, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    for file_name in os.listdir(src_folder):
        if file_name.endswith(".mkv"):
            full_path = os.path.join(src_folder, file_name)
            mp4_file_name = file_name.replace(".mkv", ".mp4")
            output_path = os.path.join(dest_folder, mp4_file_name)

            try:
                # Convert mkv to mp4 using moviepy
                clip = VideoFileClip(full_path)
                clip.write_videofile(output_path, codec="libx264")
                print(f"Converted {file_name} to {mp4_file_name}")
            except Exception as e:
                print(f"Error converting {file_name}: {e}")


# Create tkinter window for folder selection
def select_folder():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    src_folder = filedialog.askdirectory(title="Select Folder Containing .mkv Files")
    if not src_folder:
        print("No folder selected. Exiting...")
        return
    dest_folder = filedialog.askdirectory(title="Select Destination Folder for .mp4 Files")
    if not dest_folder:
        print("No destination folder selected. Exiting...")
        return

    convert_mkv_to_mp4(src_folder, dest_folder)
    print("Conversion complete!")


if __name__ == "__main__":
    select_folder()
