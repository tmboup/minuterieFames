####################################################################  written by fenix  ###############################################################################################




from PIL import Image, ImageTk
import tkinter as tk
import tkinter.messagebox

class Application(tk.Frame):
    

    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.running = False
        self.time = 0
        self.hours = 0
        self.mins = 0
        self.secs = 0
        self.build_interface()


    def build_interface(self):
       
        self.config(background="#154c79")
        self.frame0 = tk.Frame(self, bg="#154c79")
        self.frame0.pack(side="top")

        self.time_entry = tk.Entry(self.frame0)
        self.time_entry.pack(side="top")

        self.clock = tk.Label(self.frame0, text="Finale de la comptition THE BEST", font=("Courier", 30),bg="#154c79",bd=1,fg="white")
        self.clock.pack(pady=25)

        self.frame1 = tk.Frame(self, bg="#154c79")
        self.frame1.pack(pady=50)
        self.clock = tk.Label(self.frame1, text="2S VS LSH", font=("Courier", 50),bg="#154c79",bd=2,fg="white")
        self.clock.pack(pady=25)


        self.frame2 = tk.Frame(self, bg="#154c79",bd=2,relief="sunken")
        self.frame2.pack()

        self.clock = tk.Label(self.frame1, text="00:00:00", font=("Courier", 100),bg="white",bd=2,relief="sunken")
        self.clock.pack(pady=25)

        self.power_button = tk.Button(self.frame2, text="Start", command=lambda: self.start(),bg="white",width=10,height=3)
        self.power_button.pack(side="left",padx=10,pady=20)

        self.reset_button = tk.Button(self.frame2, text="Reset", command=lambda: self.reset(),bg="white",width=10,height=3)
        self.reset_button.pack(side="left",padx=10,pady=20)

        self.quit_button = tk.Button(self.frame2, text="Quit", command=lambda: self.quit(),bg="white",width=10,height=3)
        self.quit_button.pack(side="left",padx=10,pady=20)

        self.master.bind("<Return>", lambda x: self.start())
        self.time_entry.bind("<Key>", lambda v: self.update())

    def calculate(self):
    
        self.hours = self.time // 3600
        self.mins = (self.time // 60) % 60
        self.secs = self.time % 60
        return "{:02d}:{:02d}:{:02d}".format(self.hours, self.mins, self.secs)

    def update(self):
    
        self.time = int(self.time_entry.get())
        try:
            self.clock.configure(text=self.calculate())
        except:
            self.clock.configure(text="00:00:00")

    def timer(self):

        if self.running:
            if self.time <= 0:
                self.clock.configure(text="Temps écoulé")

            else:
                self.clock.configure(text=self.calculate())
                self.time -= 1
                self.after(1000, self.timer)
                if(self.time<=30):
                    self.clock.configure(bg="red")

    def start(self):

        try:
            self.time = int(self.time_entry.get())
            self.time_entry.delete(0, 'end')
        except:
            self.time = self.time
        self.power_button.configure(text="Stop", command=lambda: self.stop())
        self.master.bind("<Return>", lambda x: self.stop())
        self.running = True
        self.timer()

    def stop(self):

        self.power_button.configure(text="Start", command=lambda: self.start())
        self.master.bind("<Return>", lambda x: self.start())
        self.running = False

    def reset(self):

        self.power_button.configure(text="Start", command=lambda: self.start())
        self.master.bind("<Return>", lambda x: self.start())
        self.running = False
        self.time = 0
        self.clock["text"] = "00:00:00"
        self.clock.configure(bg="white")

    def quit(self):

        if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()




if __name__ == "__main__":

    root = tk.Tk()
    root.geometry("900x700")
    root.config(background="#154c79")
    root.title("Debatons")
    Application(root).pack()        
    root.mainloop()





















####################################################################  written by fenix  ###############################################################################################