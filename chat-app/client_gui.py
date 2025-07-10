import socket
import threading
import tkinter as tk
from tkinter import simpledialog, scrolledtext

HOST = '127.0.0.1'
PORT = 12345

class ClientGUI:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((HOST, PORT))

        self.window = tk.Tk()
        self.window.title("Chat App")

        self.chat_box = scrolledtext.ScrolledText(self.window, state='disabled')
        self.chat_box.pack(padx=10, pady=10)

        self.input_area = tk.Entry(self.window)
        self.input_area.pack(padx=10, pady=5)
        self.input_area.bind("<Return>", self.send_message)

        self.username = simpledialog.askstring("Username", "Enter your username", parent=self.window)
        self.client.send(self.username.encode('utf-8'))

        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

        self.window.protocol("WM_DELETE_WINDOW", self.close)
        self.window.mainloop()

    def receive(self):
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                self.chat_box.config(state='normal')
                self.chat_box.insert('end', message + '\n')
                self.chat_box.yview('end')
                self.chat_box.config(state='disabled')
            except:
                break

    def send_message(self, event=None):
        message = self.input_area.get()
        self.input_area.delete(0, 'end')
        self.client.send(message.encode('utf-8'))

    def close(self):
        self.client.send("/exit".encode('utf-8'))
        self.client.close()
        self.window.destroy()

if __name__ == "__main__":
    ClientGUI()
