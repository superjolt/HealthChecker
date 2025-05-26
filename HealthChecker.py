import schedule
import time
import threading
from tkinter import Tk, Label, Text, Button, BOTH, YES

def show_popup(title, message, duration=None):
    def close_after_delay():
        if duration:
            time.sleep(duration)
            root.destroy()

    root = Tk()
    root.title(title)
    root.geometry("500x400")
    root.configure(bg='white')

    label = Label(root, text=title, font=("Arial", 18, "bold"), bg='white')
    label.pack(pady=10)

    text_box = Text(root, font=("Arial", 14), bg='white')
    text_box.insert("1.0", message)
    text_box.config(state="disabled", wrap="word")
    text_box.pack(expand=YES, fill=BOTH, padx=20, pady=10)

    btn = Button(root, text="Close", font=("Arial", 14), command=root.destroy)
    btn.pack(pady=10)

    if duration:
        threading.Thread(target=close_after_delay, daemon=True).start()

    root.mainloop()

neck_stretch_msg = """
1. Sit or stand tall, shoulders relaxed.
2. Slowly tuck your chin in (make a double chin).
3. Tilt your head gently back, looking up toward the ceiling.
4. You should feel a stretch along the front of your neck and upper chest.
5. Hold for 15 seconds while breathing deeply.
6. Return your head to a neutral position.
7. Repeat 2-3 times.
8. Slowly turn your head left and right, as if looking behind your shoulders.
9. Hold each turn for 10 seconds.
10. Do not force any movements or twist abruptly.
"""

eye_break_msg = """
1. Look away from your screen.
2. Focus on an object at least 20 feet (6 meters) away.
3. Blink slowly and deeply.
4. Relax your eyes.
5. Hold this gaze for 20 seconds.
6. Repeat every 20-30 minutes to prevent eye strain.
"""

def neck_stretch_task():
    show_popup("Neck Stretch Reminder", neck_stretch_msg)

def eye_break_task():
    show_popup("Eye Break Reminder", eye_break_msg, duration=20)

def run_scheduler():
    schedule.every(1).hours.do(neck_stretch_task)
    schedule.every(30).minutes.do(eye_break_task)
    print("Reminder scheduler started. Press Ctrl+C to stop.")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    run_scheduler()
