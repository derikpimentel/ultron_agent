from tkinter import Tk

class Application:
    def __init__(self, master=None):
        self.master = master

if __name__ == "__main__":
    root = Tk()
    Application(root)
    root.mainloop()