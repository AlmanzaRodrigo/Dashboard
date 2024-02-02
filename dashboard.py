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
        upper_frame = tk.Frame(charts_frame)
        lower_frame = tk.Frame(charts_frame)
        chart1 = FigureCanvasTkAgg(self.chart_by_month, upper_frame)
        chart2 = FigureCanvasTkAgg(self.chart_by_species, upper_frame)
        chart3 = FigureCanvasTkAgg(self.chart_by_state, lower_frame)
        chart4 = FigureCanvasTkAgg(self.chart_by_port, lower_frame)
        sidebar_paragraph = tk.Label(sidebar_frame, text=SIDEBAR_TEXT,
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
        """
        The plot_bar_chart function plots a bar chart.
        
        :param data: The data that will be plotted
        :param title: Set the title of the bar chart
        :param xlabel: Set the label for the x-axis
        :param ylabel: Set the label for the y-axis
        :param xticks_fontsize: Set the font size of the x axis labels
        :return: A chart object
        """
        chart, axes = plt.subplots(figsize=(4,3), layout='constrained')
        axes.bar(data.keys(), data.values())
        axes.set_title(title)
        axes.set_xlabel(xlabel)
        axes.set_ylabel(ylabel)
        plt.xticks(rotation=90, fontsize=xticks_fontsize)
        return chart
    
    def plot_area_chart(self, data, title, xlabel, ylabel, xticks_fontsize=11):
        """
        The plot_area_chart function plots an area chart.
        
        :param data: The data that will be used to plot the chart
        :param title: Set the title of the chart
        :param xlabel: Set the label of the x-axis
        :param ylabel: Set the y-axis label
        :param xticks_fontsize: Set the font size of the x-axis ticks
        :return: A chart object
        """
        chart, axes = plt.subplots(figsize=(4,3), layout="constrained")
        axes.fill_between(data.keys(), data.values())
        axes.set_title(title)
        axes.set_xlabel(xlabel)
        axes.set_ylabel(ylabel)
        plt.xticks(rotation=90, fontsize=xticks_fontsize)
        return chart
    
    def plot_line_chart(self, data, title, xlabel, ylabel, xticks_fontsize=11):
        """
        The plot_line_chart function plots a line chart.
        
        :param data: The data that will be used to plot the chart
        :param title: Set the title of the chart
        :param xlabel: Set the label of the x-axis
        :param ylabel: Set the y-axis label
        :param xticks_fontsize: Set the font size of the x-axis ticks
        :return: A chart object
        """
        chart, axes = plt.subplots(figsize=(4,3), layout="constrained")
        axes.plot(data.keys(), data.values())
        axes.set_title(title)
        axes.set_xlabel(xlabel)
        axes.set_ylabel(ylabel)
        plt.xticks(rotation=90, fontsize=xticks_fontsize)
        return chart
    
    def plot_pie_chart(self, data, title):
        """
        The plot_pie_chart function plots a pie chart.
        
        :param data: The data that will be used to plot the chart
        :param title: Set the title of the chart
        :param xlabel: Set the label of the x-axis
        :param ylabel: Set the y-axis label
        :param xticks_fontsize: Set the font size of the x-axis ticks
        :return: A chart object
        """
        chart, axes = plt.subplots(figsize=(4,3), layout="constrained")
        axes.pie(data.values(), labels=data.keys())
        axes.set_title(title)
        return chart

    def create_chart_objects(self):
        """
        The create_chart_objects function creates the chart objects for each of the charts.
        
        :return: None
        """
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