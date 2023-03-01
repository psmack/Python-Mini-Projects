"""Convert your text into voice

This application uses Google Text-to-Speech (gTTS) to convert text to speech.

Dependencies:
    pip install tkinter
    pip install gTTS
"""
import tkinter as tk
from tkinter import ttk
from gtts import gTTS
import os


class App(tk.Tk):
    def __init__(self):
        # Call __init__() of the tk.Tk class
        super().__init__()

        # MACROS
        BG_COLOR = "ghost white"
        H_FONT = "arial 20 bold"
        B_FONT = "arial 15 bold"
        TITLE = "Text to Speech"

        # Configure the root window
        self.title(TITLE)
        self.geometry("350x300")
        self.resizable(0, 0)
        self.config(bg=BG_COLOR)

        # Labels
        # Header label
        self.header_label = ttk.Label(
            self, text=TITLE, font=H_FONT, background=BG_COLOR
        )
        self.header_label.pack()

        # Footer label
        self.photo = tk.PhotoImage(file="./assets/alliance.png")
        self.footer_label = ttk.Label(self, image=self.photo, background=BG_COLOR)
        self.footer_label.pack(side=tk.BOTTOM, pady=25)

        # Entry box label
        self.input_label = ttk.Label(
            self, text="Enter Text", font=B_FONT, background=BG_COLOR
        )
        self.input_label.place(x=20, y=60)

        # Text variable
        self.msg = tk.StringVar()

        # Input box
        self.input_box = tk.Entry(self, textvariable=self.msg, width="50")
        self.input_box.place(x=20, y=100)

        # Buttons
        self.play_btn = ttk.Button(self, text="PLAY")
        self.play_btn["command"] = self.text_to_speech
        self.play_btn.place(x=60, y=140)

        self.reset_btn = ttk.Button(self, text="RESET")
        self.reset_btn["command"] = self.reset
        self.reset_btn.place(x=135, y=140)

        self.exit_btn = ttk.Button(self, text="EXIT")
        self.exit_btn["command"] = self.exit
        self.exit_btn.place(x=210, y=140)

    def text_to_speech(self):
        self.message = self.input_box.get()

        # Create a gTTS object and pass the text message and language
        # Set the speed to high speed
        self.speech = gTTS(text=self.message, lang="en", slow=False)

        # Save the converted audio in a mp3 file
        self.speech.save("text.mp3")

        # Use Windows command 'start' to play the converted file
        os.system("start text.mp3")

    def reset(self):
        self.msg.set("")

    def exit(self):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
