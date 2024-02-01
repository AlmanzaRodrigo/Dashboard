import ttkbootstrap as tk
from ttkbootstrap import font, Style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from data import CAPTURE_BY_MONTH, CAPTURE_BY_SPECIES, CAPTURE_BY_STATE, CAPTURE_BY_PORT
from data import SIDEBAR_TEXT

class Dashboard():
    def __init__(self):
        plt.rcParams["axes.prop_cycle"] = plt.cycler(color=["#76a7f4",
                                                            "#6b8ce6",
                                                            "#6071d7",
                                                            "#6878CF",
                                                            "#2C40B2"])
        self.PARAGRAPH = SIDEBAR_TEXT

    
    def create_gui(self):
        style1 = Style()
        style1.configure("primary.TFrame")

        # create window
        self.root = tk.Window()
        self.root.title("Dashboard")

        # crate widgets
        sidebar_frame = tk.Frame(self.root, bootstyle="primary", style="primary.TFrame")
        charts_frame = tk.Frame(self.root)
        upper_frame = tk.Frame(charts_frame)
        lower_frame = tk.Frame(charts_frame)
        chart1 = FigureCanvasTkAgg(self.chart_by_month, upper_frame)
        chart2 = FigureCanvasTkAgg(self.chart_by_species, upper_frame)
        chart3 = FigureCanvasTkAgg(self.chart_by_state, lower_frame)
        chart4 = FigureCanvasTkAgg(self.chart_by_port, lower_frame)
        sidebar_paragraph = tk.Label(sidebar_frame, text=self.PARAGRAPH,
                                     font=("default", 9, font.BOLD),
                                     background="#6071d7", foreground="#caf0f8",
                                     padding=(20,20))
        
        # draw widgets
        sidebar_frame.pack(side="left", fill="y")
        charts_frame.pack(side="left", fill="both", expand="yes")
        upper_frame.pack()
        lower_frame.pack()
        chart1.draw()
        chart1.get_tk_widget().pack(side="left", fill="both", padx=20, pady=20)
        chart2.draw()
        chart2.get_tk_widget().pack(side="left", fill="both", padx=20, pady=20)
        chart3.draw()
        chart3.get_tk_widget().pack(side="left", fill="both", padx=20, pady=20)
        chart4.draw()
        chart4.get_tk_widget().pack(side="left", fill="both", padx=20, pady=20)
        sidebar_paragraph.pack(fill="both", expand="yes")
    
    def plot_bar_chart(self, data, title, xlabel, ylabel, xticks_fontsize=11):
        chart, axes = plt.subplots(figsize=(4,3), layout='constrained')
        axes.bar(data.keys(), data.values())
        axes.set_title(title)
        axes.set_xlabel(xlabel)
        axes.set_ylabel(ylabel)
        plt.xticks(rotation=90, fontsize=xticks_fontsize)
        return chart
    
    def plot_area_chart(self, data, title, xlabel, ylabel, xticks_fontsize=11):
        chart, axes = plt.subplots(figsize=(4,3), layout="constrained")
        axes.fill_between(data.keys(), data.values())
        axes.set_title(title)
        axes.set_xlabel(xlabel)
        axes.set_ylabel(ylabel)
        plt.xticks(rotation=90, fontsize=xticks_fontsize)
        return chart
    
    def plot_line_chart(self, data, title, xlabel, ylabel, xticks_fontsize=11):
        chart, axes = plt.subplots(figsize=(4,3), layout="constrained")
        axes.plot(data.keys(), data.values())
        axes.set_title(title)
        axes.set_xlabel(xlabel)
        axes.set_ylabel(ylabel)
        plt.xticks(rotation=90, fontsize=xticks_fontsize)
        return chart
    
    def plot_pie_chart(self, data, title):
        chart, axes = plt.subplots(figsize=(4,3), layout="constrained")
        axes.pie(data.values(), labels=data.keys())
        axes.set_title(title)
        return chart
    
    def create_chart_objects(self):
        self.chart_by_month = self.plot_line_chart(CAPTURE_BY_MONTH,
                                                  "Capture by Month",
                                                  "Month",
                                                  "Capture")
        self.chart_by_species = self.plot_bar_chart(CAPTURE_BY_SPECIES,
                                                    "Capture by Species",
                                                    "Species",
                                                    "Capture",
                                                    7)
        self.chart_by_state = self.plot_pie_chart(CAPTURE_BY_STATE,
                                                    "Capture by State")
        self.chart_by_port = self.plot_bar_chart(CAPTURE_BY_PORT,
                                                    "Capture by State",
                                                    "State",
                                                    "Capture",
                                                    7)
    
    def run(self):
        self.create_chart_objects()
        self.create_gui()
        self.root.mainloop()

if __name__ == "__main__":
    app = Dashboard()
    app.run()   