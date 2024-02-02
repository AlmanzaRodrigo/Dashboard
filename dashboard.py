import ttkbootstrap as tk
from ttkbootstrap import font
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
    
    def create_gui(self):
        """
        The create_gui function creates the GUI for the dashboard.
        
        :return: None
        """
        # create window
        self.root = tk.Window()
        self.root.title("Dashboard")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # crate widgets
        sidebar_frame = tk.Frame(self.root, bootstyle="primary")
        charts_frame = tk.Frame(self.root)
        charts = FigureCanvasTkAgg(self.charts_frame, charts_frame)
        sidebar_title = tk.Label(sidebar_frame, text="Dashboard",
                                 font=("default", 15, font.BOLD),
                                 background="#6071D7", foreground="#caf0f8",
                                 padding=(20,15))
        sidebar_paragraph = tk.Label(sidebar_frame, text=SIDEBAR_TEXT,
                                     font=("default", 9, font.BOLD),
                                     background="#6071D7", foreground="#caf0f8",
                                     anchor="n", padding=(20,0))
        sidebar_author = tk.Label(sidebar_frame, text="Author: Almanza Rodrigo Hernan",
                                 font=("default", 7, font.BOLD),
                                 background="#6071D7", foreground="#caf0f8",
                                 padding=(20,10))
        
        # draw widgets
        sidebar_frame.pack(side="left", fill="y")
        charts_frame.pack(side="left", fill="both", expand=True, ipadx=100)
        charts.get_tk_widget().pack(side="left", fill="both", expand=True, pady="0,10")
        sidebar_title.pack(fill="x")
        sidebar_paragraph.pack(fill="both", expand=True)
        sidebar_author.pack(fill="both", expand=True)
    
    def plot_bar_chart(self, chart, data, title, xlabel, ylabel, xticks_fontsize):
        """
        The plot_bar_chart function sets up a bar chart to be plotted.
        
        :param chart: A chart object
        :param data: The data that will be plotted
        :param title: Set the title of the bar chart
        :param xlabel: Set the label for the x-axis
        :param ylabel: Set the label for the y-axis
        :param xticks_fontsize: Set the font size of the x axis labels
        """
        data_keys = [key[:10] for key in data.keys()]
        chart.bar(data_keys, data.values())
        chart.set(title=title, xlabel=xlabel, ylabel=ylabel)
        for label in chart.get_xticklabels():
            label.set_rotation(90)    
            label.set_fontsize(xticks_fontsize)

    def plot_line_chart(self, chart, data, title, xlabel, ylabel, xticks_fontsize):
        """
        The plot_line_chart function sets up a line chart to be plotted.
        
        :param chart: A chart object
        :param data: The data that will be plotted
        :param title: Set the title of the bar chart
        :param xlabel: Set the label for the x-axis
        :param ylabel: Set the label for the y-axis
        :param xticks_fontsize: Set the font size of the x axis labels
        """
        data_keys = [key[:3] for key in data.keys()]
        chart.plot(data_keys, data.values())
        chart.set(title=title, xlabel=xlabel, ylabel=ylabel)
        for label in chart.get_xticklabels():
            label.set_rotation(90)
            label.set_fontsize(xticks_fontsize)
    
    def plot_pie_chart(self, chart, data, title):
        """
        The plot_pie_chart function sets up a pie chart to be plotted.
        
        :param chart: A chart object
        :param data: The data that will be plotted
        :param title: Set the title of the bar chart
        """
        chart.pie(data.values(), labels=data.keys())
        chart.set_title(title)

    def create_chart_objects(self):
        """
        The create_chart_objects function creates the chart objects for each imported data.
        
        :return: None
        """
        cframe, ((chart1, chart2),(chart3, chart4)) = plt.subplots(nrows=2, ncols=2)
        self.plot_line_chart(chart1, CAPTURE_BY_MONTH, "Capture by Month", "Month", "Capture","x-small")
        self.plot_bar_chart(chart2, CAPTURE_BY_SPECIES, "Capture by Species", "Species", "Capture", "x-small")
        self.plot_pie_chart(chart3, CAPTURE_BY_STATE, "Capture by State")
        self.plot_bar_chart(chart4, CAPTURE_BY_PORT, "Capture by Port", "Port", "Capture", "x-small")
        plt.tight_layout()
        self.charts_frame = cframe
        
    def on_closing(self):
        """
        The on_closing function is called when the user clicks on the 'X' button in
        the upper right corner of a window.  It closes all open figures and destroys
        the root window, which causes the program to exit.
        
        :return: None
        """
        plt.close("all")
        self.root.destroy()
    
    def run(self):
        """
        The run function is the main function of the class. It creates the GUI
        and chart objects.
            
        :return: None
        """
        self.create_chart_objects()
        self.create_gui()
        self.root.mainloop()

if __name__ == "__main__":
    app = Dashboard()
    app.run()   