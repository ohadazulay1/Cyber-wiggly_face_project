from signInWin import Ui_firstWindow
from PyQt5.QtWidgets import QApplication
import sys

class Main:

    if __name__ == '__main__':
        app = QApplication(sys.argv)

        startingWindows = Ui_firstWindow()

        sys.exit(app.exec_())
