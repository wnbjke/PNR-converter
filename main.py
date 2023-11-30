import sys
import styles
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from test import parse_pnr_data

app = QApplication(sys.argv)
# resolution CONSTANTS
screen_resolution = app.desktop().screenGeometry()
screen_width, screen_height = screen_resolution.width(), screen_resolution.height()
min_screen_width = screen_width // 2
min_screen_height = screen_height // 2

# QMainWindow


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.initUI()

    def initUI(self):
        # Window properties
        self.setWindowTitle("PNR Converter")
        self.setGeometry(0, 0, screen_width, screen_height)
        self.setMinimumSize(min_screen_width, min_screen_height)
        # rgb(119,136,153)
        self.setStyleSheet("background-color: rgb(141, 144, 158);")

        self.vbox = QVBoxLayout()

        # input widget
        self.input_field = QTextEdit()
        self.input_field.setContentsMargins(0, 0, 0, 20)
        self.input_field.setFixedSize(700, 150)
        self.input_field.setAutoFormatting(QTextEdit.AutoBulletList)
        self.input_field.setPlaceholderText("Enter PNR")
        self.input_field.setStyleSheet(styles.input_field_style)

        # button widget
        self.button = QPushButton("Press to convert")
        self.button.clicked.connect(self.on_button_clicked)
        self.button.setFixedSize(150, 25)
        self.button.setStyleSheet(styles.button_style)

        # table
        self.creatingTable()
        # layout box
        self.vbox.addWidget(self.input_field, alignment=Qt.AlignCenter)

        self.vbox.addWidget(self.button, alignment=Qt.AlignCenter)
        self.vbox.addWidget(self.tableNew)
        self.setLayout(self.vbox)

        self.vbox.setContentsMargins(25, 25, 25, 25)
        # self.vbox.addStretch()

        # init the window

        self.show()

    def creatingTable(self):
        self.tableNew = QTableWidget()
        # self.tableNew.setRowCount(2)
        self.tableNew.setColumnCount(7)

        self.tableNew.setHorizontalHeaderLabels(
            ["Airline", "Flight Number", "Depart", "From", "Arrive", "Flight Time", "Layover time"])
        self.tableNew.horizontalHeader().setStretchLastSection(True)
        self.tableNew.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)

    # run the convertion
    def on_button_clicked(self):
        passed_pnr = self.input_field.toPlainText()
        if "\n" in passed_pnr:
            pss1 = passed_pnr.split("\n")
            print(pss1)
            for item in pss1:
                parsed1 = parse_pnr_data(item)
                for row, data in enumerate(parsed1):
                    self.tableNew.insertRow(row)
                    for col, value in enumerate(data):
                        self.tableNew.setItem(row, col, QTableWidgetItem(value))
        else:
            try:
                parsed = parse_pnr_data(passed_pnr)
                for row, item in enumerate(parsed):
                    self.tableNew.insertRow(row)
                    for col, value in enumerate(item):
                        self.tableNew.setItem(row, col, QTableWidgetItem(value))
            except:
                msg = QMessageBox()
                msg.setText("Something went wrong, try again")
                x = msg.exec_()
        
        '''
        if parsed:
            for key, value in parsed.items():
                print(f"{key}: {value}")
        else:
            print("Unable to parse PNR")
        '''
    # copying converted pnr

    def copy_converted_pnr(self):
        pass


window = Window()
sys.exit(app.exec_())
