import sys
from PyQt5.QtCore import Qt, QUrl, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QVBoxLayout
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
        self.media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.video_widget = QVideoWidget()
        self.media_player.setVideoOutput(self.video_widget)
        self.media_player.setMuted(False)  # Ensure audio is not muted
        
        # Listen for key events in the video widget
        self.video_widget.installEventFilter(self)

        # Video files
        self.video_paths = [
            "video_grid/bluey.mp4",  # Replace these paths with your actual video paths
            "video_grid/babyshark.mp4",
            "video_grid/fruit.mp4",
            "video_grid/sesame.mp4"
        ]

        # Store last play positions for each video
        self.last_positions = [0, 0, 0, 0]

        # Layout for buttons and video widget
        main_layout = QVBoxLayout()
        
        # Add video widget to the layout
        main_layout.addWidget(self.video_widget)

        # Layout for buttons
        button_layout = QGridLayout()

        # Button configuration
        button_styles = "font-size: 24px; height: 100%; width: 100%; background-color: lightblue;"
        button_texts = ["Video 1", "Video 2", "Video 3", "Video 4"]
        for i in range(4):
            button = QPushButton(button_texts[i])
            button.setStyleSheet(button_styles)
            button.clicked.connect(lambda checked, index=i: self.play_video(index))
            button_layout.addWidget(button, i // 2, i % 2)

        # Add button layout to the main layout
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def play_video(self, index):
        # Stop current video (if any) and load the selected one
        self.media_player.stop()
        
        # Set media and position to last known position
        self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(self.video_paths[index])))
        self.media_player.setPosition(self.last_positions[index])
        self.media_player.play()
        self.video_widget.showFullScreen()

        # Set a timer to stop the video after 5 seconds
        QTimer.singleShot(10000, lambda: self.stop_video(index))
        
    def stop_video(self, index):
        # Store the current position before stopping
        self.last_positions[index] = self.media_player.position()
        self.media_player.stop()

    def keyPressEvent(self, event):
        # Close app on Esc key
        if event.key() == Qt.Key_Escape:
            self.media_player.stop()
            self.close()

    def eventFilter(self, source, event):
        # Capture Esc key in the video widget to exit fullscreen and stop playback
        if source == self.video_widget and event.type() == event.KeyPress:
            if event.key() == Qt.Key_Escape:
                self.media_player.stop()
                self.video_widget.close()
                self.showFullScreen()
                return True
        return super().eventFilter(source, event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = BabyVideoApp()
    player.show()
    sys.exit(app.exec_())
