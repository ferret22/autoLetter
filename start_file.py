from window_file import ProgramWindow, QApplication
import sys


def start_program():
    app = QApplication(sys.argv)
    screen_rect = app.primaryScreen().availableGeometry()
    window = ProgramWindow(screen_rect.width(), screen_rect.height())
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    start_program()
