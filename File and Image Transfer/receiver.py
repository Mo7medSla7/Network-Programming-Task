import socket
import tkinter as tk

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Transfer Files - Receiver")
        self.root.geometry("400x170")
        self.root.minsize(300, 160)

        self.send_button = tk.Button(self.root, text="Receive", font=("Helvetica", 16), bg="#007acc", fg="white", padx=10,
                                    pady=5, command=self.receive)
        self.send_button.pack(padx=8, pady=8)
        # self.status_label = tk.Label(self.root, text="No file is received now.", font=("Helvetica", 16))
        # self.status_label.pack(padx=8, pady=8)

    def build(self):
        self.root.mainloop()

    def receive(self):
        client = socket.socket(socket.AF_INET,
                               socket.SOCK_STREAM)
        host = socket.gethostname()
        port = 12321
        client.connect((host, port))
        file_name = client.recv(1024).decode('utf-8')
        file = open(file_name, "wb")
        data = client.recv(2048)
        while data:
            file.write(data)
            data = client.recv(2048)
        file.close()
        # self.status_label.text = file_name + 'is saved'
        print(f'{file_name} is saved')


if __name__ == "__main__":
    GUI().build()
