from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon
import sys
import subprocess
import psutil

def execute_script():
    subprocess.Popen(["C:\\Users\\denis\\AppData\\Local\\Programs\\Python\\Python312\\python.exe", "main.py"])

def quit_script_main():
    for proc in psutil.process_iter():
            try:
                if proc.name() == "python.exe" and "main.py" in proc.cmdline():
                    proc.terminate()
                    break
            except psutil.AccessDenied:
                pass

def quit_script():
    tray_icon.hide()  # Hide the tray icon from the system tray
    app.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    icon_path = "icon.png"

    tray_icon = QSystemTrayIcon(QIcon(icon_path), app)

    tray_menu = QMenu()
    execute_action = QAction("Run", tray_menu)
    execute_action.triggered.connect(execute_script)
    tray_menu.addAction(execute_action)

    quit_action = QAction("Quit", tray_menu)
    quit_action.triggered.connect(quit_script_main)
    tray_menu.addAction(quit_action)

    quit_action = QAction("EXIT", tray_menu)
    quit_action.triggered.connect(quit_script)
    tray_menu.addAction(quit_action)

    tray_icon.setContextMenu(tray_menu)
    tray_icon.show()

    sys.exit(app.exec_())
