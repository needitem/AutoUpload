import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLineEdit, QLabel, QPushButton, QVBoxLayout, QWidget
from github import Github

class GitHubUploader(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # UI 요소 생성
        self.setWindowTitle("GitHub 자동 업로더")
        central_widget = QWidget()
        layout = QVBoxLayout()

        self.folder_label = QLabel("프로젝트 폴더:")
        self.folder_edit = QLineEdit()
        self.folder_edit.setReadOnly(True)
        self.folder_button = QPushButton("폴더 선택")
        self.folder_button.clicked.connect(self.selectFolder)

        self.name_label = QLabel("프로젝트 이름:")
        self.name_edit = QLineEdit()

        self.desc_label = QLabel("프로젝트 설명:")
        self.desc_edit = QLineEdit()

        self.login_button = QPushButton("GitHub 로그인")
        self.login_button.clicked.connect(self.loginGitHub)

        self.upload_button = QPushButton("업로드")
        self.upload_button.clicked.connect(self.uploadToGitHub)
        self.upload_button.setEnabled(False)

        layout.addWidget(self.folder_label)
        layout.addWidget(self.folder_edit)
        layout.addWidget(self.folder_button)
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_edit)
        layout.addWidget(self.desc_label)
        layout.addWidget(self.desc_edit)
        layout.addWidget(self.login_button)
        layout.addWidget(self.upload_button)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def selectFolder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "프로젝트 폴더 선택")
        self.folder_edit.setText(folder_path)

    def loginGitHub(self):
        # Request GitHub Login
        
        pass

    def uploadToGitHub(self):
        # GitHub 업로드 코드 작성
        pass
