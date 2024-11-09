import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QGridLayout
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget

class BabyVideoApp(QWidget):
    def __init__(self):
        super().__init__()
        
        # Fullscreen and quit on Esc
        self.setWindowTitle("Baby Video Player")
        self.showFullScreen()
        self.setStyleSheet("background-color: black;")

        # Set up media player and video widget
        self.media_player = QMediaPlayer()
        self.video_widget = QVideoWidget()
        self.media_player.setVideoOutput(self.video_widget)
        self.media_player.setMuted(True)  # Muted for baby-friendly playback
        
        # Video files
        self.video_paths = [
            "video_grid/babyshark.mp4",  # Replace these paths with your actual video paths
            "video_grid/babyshark.mp4",
            "video_grid/bluey.mp4",
            "video_grid/bluey.mp4"
        ]

        # Layout for buttons
        layout = QGridLayout()
        self.setLayout(layout)

        # Button configuration
        button_styles = "font-size: 24px; height: 100%; width: 100%; background-color: lightblue;"
        button_texts = ["Video 1", "Video 2", "Video 3", "Video 4"]
        for i in range(4):
            button = QPushButton(button_texts[i])
            button.setStyleSheet(button_styles)
            button.clicked.connect(lambda checked, index=i: self.play_video(index))
            layout.addWidget(button, i // 2, i % 2)

    def play_video(self, index):
        # Stop current video (if any) and load the selected one
        self.media_player.stop()
        self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(self.video_paths[index])))
        self.media_player.play()
        self.video_widget.showFullScreen()
        self.media_player.setVideoOutput(self.video_widget)
        
    def keyPressEvent(self, event):
        # Close app on Esc key
        if event.key() == Qt.Key_Escape:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = BabyVideoApp()
    player.show()
    sys.exit(app.exec_())
