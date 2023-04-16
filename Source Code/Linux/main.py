import schedule
import time
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QDesktopWidget
import os
from PyQt5.QtGui import QFontDatabase
from PyQt5 import uic
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty, QTimer
import platform
import sys


def run_program():

    # Import the audio library if Windows OS or else exiting the program if not Windows OS
    if platform.system() == "Linux":
        import alsaaudio
    else:
        sys.exit(1)

    class OptiBreak(QMainWindow):
        def __init__(self):
            super().__init__()

            # Import Font (Source Sans Pro - Regular)
            QFontDatabase.addApplicationFont(os.path.abspath(
                os.path.join("ui", "fonts", "SourceSansPro-Regular.ttf")))

            # Loading the Ui
            uic.loadUi((os.path.abspath(os.path.join("ui", "main.ui"))), self)

            # Creates the Seconds Counter Label and aligns it in the center
            self.counterlabel = QLabel(self)
            self.counterlabel.setText("20")
            self.counterlabel.setStyleSheet("""
            font-size:160px;
            background-color:None;
            """)
            self.counterlabel.setAlignment(Qt.AlignCenter)
            self.counterlabel.setGeometry(200, 200, 200, 200)
            self.moveWidgetCenter(self.counterlabel)

            # Brings the window on the top other windows
            self.setWindowFlags(Qt.WindowStaysOnTopHint)

            # Main Windows Appearance - Animation
            self.opacityAnimation()

            # Updates the counterlabel after every second 20,19,18........
            timer = QTimer(self)
            timer.timeout.connect(self.waitingTime)
            timer.start(1000)

            # Muting the Sound of Speakers
            self.mixer = alsaaudio.Mixer()
            self.mixer.setmute(1)

        def moveWidgetCenter(self, widget):
            # Get the dimensions of the screen
            screen = QDesktopWidget().screenGeometry()
            # Get the dimensions of the widget
            widget_size = widget.geometry()
            # Calculate the center position of the widget
            center_x = int((screen.width() - widget_size.width()) / 2)
            center_y = int((screen.height() - widget_size.height()) / 2)
            # Set the position of the widget
            widget.move(center_x, center_y)

        def opacityAnimation(self):
            # Opacity Animation
            self.anim = QPropertyAnimation(self, b"opacity")
            self.anim.setDuration(3000)
            self.anim.setLoopCount(1)
            self.anim.setStartValue(0.0)
            self.anim.setEndValue(1.0)
            self.anim.start()

        def windowOpacity(self):
            return super().windowOpacity()

        def setWindowOpacity(self, opacity):
            super().setWindowOpacity(opacity)

        opacity = pyqtProperty(float, windowOpacity, setWindowOpacity)

        def waitingTime(self):
            # if counterlabel becames 0 exit the main window
            if int(self.counterlabel.text()) > 0:
                self.counterlabel.setText(str(int(self.counterlabel.text())-1))
            else:
                # unmute the system sound
                self.mixer = alsaaudio.Mixer('Master')
                self.mixer.setmute(0)
                # close the main window
                self.close()

    # PyQt5 syntax for intialization object of class OptiBreak and showing it in fullscreen
    app = QApplication([])
    window = OptiBreak()
    window.showFullScreen()
    app.exec_()


# schedule the job to run every 20 minutes
schedule.every(20).minutes.do(run_program)

# run the scheduler loop
while True:
    schedule.run_pending()
    time.sleep(1)
