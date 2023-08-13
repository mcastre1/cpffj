# importing Qt widgets
from PyQt5.QtWidgets import *
import sys

import time
import random

# importing pyqtgraph as pg
import pyqtgraph as pg
 
 
 
class Window(QMainWindow):
 
    def __init__(self):
        super().__init__()

        self.n = 10
        # create list for y-axis
        self.y1 = [random.randint(1,100) for i in range(1,self.n+1)]
 
        # create horizontal list i.e x-axis
        self.x = [n for n in range(1,self.n+1)]
 
        # setting title
        self.setWindowTitle("PyQtGraph")
 
        # setting geometry
        self.setGeometry(100, 100, 600, 500)
 
        # calling method
        self.UiComponents()
 
        # showing all the widgets
        self.show()

        for i in range(1,100):
            self.y1[0] = random.randint(1,100)
            time.sleep(.2)

 
    # method for components
    def UiComponents(self):
 
        # creating a widget object
        widget = QWidget()
 
        # creating a push button object
        btn = QPushButton('Push Button')
 
        # creating a line edit widget
        text = QLineEdit("Line Edit")
 
        # creating a check box widget
        check = QCheckBox("Check Box")
 
        # creating a plot window
        plot = pg.plot()
 
        
 
        # create pyqt5graph bar graph item
        # with width = 0.6
        # with bar colors = green
        self.bargraph = pg.BarGraphItem(x = self.x, height = self.y1, width = 1, brush ='g')
 
        # add item to plot window
        # adding bargraph item to the plot window
        plot.addItem(self.bargraph)
 
        # Creating a grid layout
        layout = QGridLayout()
 
        # setting this layout to the widget
        widget.setLayout(layout)
 
        # plot window goes on right side, spanning 3 rows
        layout.addWidget(plot, 0, 1, 3, 1)
 
        # setting this widget as central widget of the main window
        self.setCentralWidget(widget)

        
 
 
if __name__ == "__main__":
    # create pyqt5 app
    App = QApplication(sys.argv)
    
    # create the instance of our Window
    window = Window()
    
    # start the app
    sys.exit(App.exec())
