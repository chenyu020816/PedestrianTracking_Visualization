import tkinter as tk

from Constant import *
from PedestrianTrackingPage import PedestrianTrackingPage
from RealTimeTrackingPage import RealTimeTrackingPage


class MainView(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Pedestrian Tracking Visualization")
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.container = tk.Frame(self)
        self.container.grid(row=0, column=0, sticky="nsew")

        self.pages = {
            "PedestrianTrackingPage": PedestrianTrackingPage(self.container, self),
            "RealTimeTrackingPage": RealTimeTrackingPage(self.container, self),
        }

        self.start()

    def start(self):
        self.pages["PedestrianTrackingPage"].grid(row=0, column=0, sticky="nsew")

    def show_pedestrian_tracking_page(self):
        self.pages["RealTimeTrackingPage"].grid_forget()
        self.pages["PedestrianTrackingPage"].grid(row=0, column=0, sticky="nsew")
        self.pages["RealTimeTrackingPage"].stop_camera()

    def show_rt_tracking_page(self):
        self.pages["PedestrianTrackingPage"].grid_forget()
        self.pages["RealTimeTrackingPage"].grid(row=0, column=0, sticky="nsew")
        self.pages["RealTimeTrackingPage"].resume_show_frame()


if __name__ == "__main__":
    app = MainView()
    app.mainloop()
