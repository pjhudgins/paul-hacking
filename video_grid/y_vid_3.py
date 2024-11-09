import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget

class VideoPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Video Player")
        self.setGeometry(100, 100, 800, 600)
        
        # Set up the video player widget
        self.media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        video_widget = QVideoWidget()

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(video_widget)

        # Play/Pause button
        self.play_button = QPushButton("Play")
        self.play_button.clicked.connect(self.play_pause)
        layout.addWidget(self.play_button)

        # Set up the media player
        self.media_player.setVideoOutput(video_widget)

        # Load video button
        load_button = QPushButton("Load Video")
        load_button.clicked.connect(self.load_video)
        layout.addWidget(load_button)

        self.setLayout(layout)

    def load_video(self):
        # Open file dialog to select a video
        file_dialog = QFileDialog()
        video_path, _ = file_dialog.getOpenFileName(self, "Open Video File", "", "Video Files (*.mp4 *.avi)")
        if video_path:
            self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(video_path)))

    def play_pause(self):
        # Toggle play/pause
        if self.media_player.state() == QMediaPlayer.PlayingState:
            self.media_player.pause()
            self.play_button.setText("Play")
        else:
            self.media_player.play()
            self.play_button.setText("Pause")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = VideoPlayer()
    player.show()
    sys.exit(app.exec_())
