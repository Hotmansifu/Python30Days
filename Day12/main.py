import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTreeView, QFileSystemModel, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton

class DirectoryTreeGenerator(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the main window
        self.setWindowTitle("Directory Tree Generator")
        self.setGeometry(100, 100, 800, 600)

        # Create the file menu
        file_menu = self.menuBar().addMenu("&File")

        # Create the "Open" action
        open_action = file_menu.addAction("&Open")
        open_action.triggered.connect(self.show_dialog)

        # Create the widget to hold the input field and button
        widget = QWidget()
        self.setCentralWidget(widget)

        # Create the input field and button
        input_layout = QHBoxLayout()
        widget.setLayout(input_layout)

        input_label = QLabel("Directory:")
        input_layout.addWidget(input_label)

        self.input_field = QLineEdit()
        input_layout.addWidget(self.input_field)

        input_button = QPushButton("Generate Tree")
        input_button.clicked.connect(self.generate_tree)
        input_layout.addWidget(input_button)

        # Create the tree view
        self.tree_view = QTreeView(self)
        self.tree_view.setGeometry(0, 40, 800, 560)
        widget.layout().addWidget(self.tree_view)

    def show_dialog(self):
        # Show the file dialog and get the selected directory
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks
        dir_path = QFileDialog.getExistingDirectory(self, "Select Directory", options=options)

        # Set the selected directory in the input field
        self.input_field.setText(dir_path)

    def generate_tree(self):
        # Get the directory path from the input field
        dir_path = self.input_field.text()

        # Generate the directory tree and display it in the tree view
        model = QFileSystemModel()
        model.setRootPath(dir_path)
        self.tree_view.setModel(model)
        self.tree_view.setRootIndex(model.index(dir_path))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DirectoryTreeGenerator()
    window.show()
    sys.exit(app.exec_())
