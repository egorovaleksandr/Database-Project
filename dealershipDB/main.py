from tkinter import Tk

from frontend import Frontend

if __name__ == '__main__':
    window = Tk()
    application = Frontend(window)
    window.mainloop()
