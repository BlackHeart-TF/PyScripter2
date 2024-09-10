from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget
import sys
from script_engine import run_user_script
class MacroTool(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Macro Tool")

        # Create a central widget and layout
        central_widget = QWidget()
        layout = QVBoxLayout()

        # Create a text box for macro input
        self.textbox = QTextEdit(self)
        layout.addWidget(self.textbox)

        # Create a button to run the macro
        self.run_button = QPushButton("Run", self)
        self.run_button.clicked.connect(self.run_macro)
        layout.addWidget(self.run_button)

        # Set the central widget and layout
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def run_macro(self):
        macro_code = self.textbox.toPlainText()
        # Here you would parse and execute the macro code
        run_user_script(macro_code)

def main():
    app = QApplication(sys.argv)
    mainWin = MacroTool()
    mainWin.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
