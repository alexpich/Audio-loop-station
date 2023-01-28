import time
import threading
import tkinter as tk
from audioLoopStation_processor import AudioRecorder

# Based on 'Simple audio recorder with Tkinter GUI'
# https://www.youtube.com/watch?v=u_xNvC9PpHA


class GUI:
    def __init__(self):
        self.recording = False
        self.window = tk.Tk()
        self.button = tk.Button(text="🎤", font=("Arial", 80, "bold"), command=self.click_handler)
        self.button.pack()
        self.label = tk.Label(text="00:00:00")
        self.label.pack()
        self.window.mainloop()

    def click_handler(self):
        if self.recording:
            self.recording = False
            self.window.config(background="black")
            self.label.config(background="black")
        else:
            self.recording = True
            self.window.config(background="red")
            self.label.config(background="red")
            threading.Thread(target=self.record).start()

    def record(self):
        audio = AudioRecorder()
        start = time.time()
        while self.recording:
            audio.rec_chunk()
            self.calc_rec_time(start)
        audio.stop_recording()
        audio.save_recording()

    def calc_rec_time(self, start: float):
        elapsed_time = time.time() - start
        secs = elapsed_time % 60
        minutes = elapsed_time // 60
        hrs = minutes // 60
        self.label.configure(text=f"{int(hrs):02d}:{int(minutes):02d}:{int(secs):02d}")


if __name__ == "__main__":

    GUI()
