import GitHubUploader

app = GitHubUploader.QApplication(GitHubUploader.sys.argv)
main_window = GitHubUploader.GitHubUploader()
main_window.show()
app.exec_()
