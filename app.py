import tkinter as tk
import cogs

class Application(tk.Frame):
    def __init__(self, master=None, geometry='300x300'):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        
    def create_widgets(self):
        self.switch = tk.Button(self, text='Switch Brightness', command = self.switch_kill)
        self.switch.pack()

        self.input = tk.Entry()
        self.input.pack()
        
        self.luminance = tk.IntVar()
        self.input["textvariable"] = self.luminance 

        self.input.bind('<Key-Return>',self.set_kill)
     
    def switch_kill(self):
        cogs.switch()
        self.master.destroy()

    def set_kill(self, luminance):
        cogs.set(int(self.luminance.get()))
        self.master.destroy()



root = tk.Tk()
root.geometry('300x300')
root.title("Change your brightness")
app = Application(master=root)
app.mainloop()
