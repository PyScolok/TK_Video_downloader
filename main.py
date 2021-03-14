from tkinter import Tk

from gui import Gui


window = Tk()
window.title('EasyVizzy')
window.geometry('720x440')
app = Gui(window).place_start_frame()
window.mainloop()
