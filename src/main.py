from PySide6.QtWidgets import QApplication, QLabel
from display import Display
from PySide6.QtGui import QIcon
from main_window import MainWindow
from variables import WINDOW_ICON_PATH

import sys



if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    window = MainWindow()

    # #Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    #Display
    display = Display()
    window.addWidgetToVlayout(display)

    #Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
