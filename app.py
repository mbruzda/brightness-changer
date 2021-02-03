import tkinter as tk
import cogs

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
                #settings
        self.master = master
        self.master.maxsize(300,100)
        self.master.minsize(300,100)
        self.master.title('Change your brightness')

        self.pack(fill='both', expand=True)
        self.create_widgets()
             
    def create_widgets(self):
        self.switch = tk.Button(self, text='Switch Brightness', command = self.switch_kill)
        self.switch.place(relx=0.1, rely=0.7)

        self.slider = tk.Scale(self, from_=0, to=100,orient="horizontal",length=250, variable='IntVar')
        self.slider.pack(side='top', pady=10)
        self.slider.set(cogs.get_brightness())
        self.slider.bind("<ButtonRelease-1>", self.update_brightness)

        self.quit = tk.Button(self, text="Quit", command = self.master.destroy)
        self.quit.place(relx=0.75, rely=0.7)

    def update_brightness(self, luminance):
        luminance=self.slider.get()
        cogs.set(luminance)
     
    def switch_kill(self):
        cogs.switch()
        self.master.destroy()

root = tk.Tk()
app = Application(master=root)
app.mainloop()
