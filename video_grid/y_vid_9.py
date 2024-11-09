import sys
from PyQt5.QtCore import Qt, QUrl, QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget

class BabyVideoApp(QWidget):
    def __init__(self):
        super().__init__()
        
        # Parameters defined at the top
        self.video_paths = [
            "video_grid/bluey.mp4", 
            "video_grid/babyshark.mp4",
            "video_grid/fruit.mp4",
            "video_grid/sesame.mp4"
        ]
        self.button_icons = [
            "video_grid/bluey.png", 
            "video_grid/babyshark.png",
            "video_grid/fruit.png",
            "video_grid/sesame.png"
        ]
        self.playback_time_ms = 10000  # Playback duration in milliseconds
        self.start_positions = [0, 20000, 2000, 0]  # Configurable original start time for each video in milliseconds  # Playback duration in milliseconds

        # Flag to ignore clicks during playback
        self.is_playing = False

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

        # Store last play positions for each video
        self.last_positions = [0] * len(self.video_paths)

        # Layout for video widget and buttons
        main_layout = QVBoxLayout()
        
        # Add video widget to the layout
        main_layout.addWidget(self.video_widget)

        # Layout for buttons at the bottom
        button_layout = QHBoxLayout()

        # Create and add buttons to the button layout
        for i in range(len(self.video_paths)):
            button = QPushButton()
            button.setIcon(QIcon(self.button_icons[i]))
            button.setIconSize(button.sizeHint() * 10)
            button.setFixedSize(300, 300)  # Set buttons to be larger equally sized squares  # Set buttons to be equally sized squares
            button.clicked.connect(lambda checked, index=i: self.play_video(index) if not self.is_playing else None)
            button_layout.addWidget(button)

        # Add button layout to the main layout
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def play_video(self, index):
        # Ignore clicks if a video is already playing
        if self.is_playing:
            return

        # Set the flag to indicate playback is in progress
        self.is_playing = True

        # Stop current video (if any) and load the selected one
        self.media_player.stop()
        
        # Set media and position to last known position
        self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(self.video_paths[index])))
        self.media_player.setPosition(self.start_positions[index] if self.last_positions[index] == 0 else self.last_positions[index])
        self.media_player.play()
        self.video_widget.showFullScreen()

        # Set a timer to stop the video after specified time
        QTimer.singleShot(self.playback_time_ms, lambda: self.stop_video(index))
        
    def stop_video(self, index):
        # Store the current position before stopping
        self.last_positions[index] = self.media_player.position()
        self.media_player.stop()

        # Reset the flag to allow new clicks
        self.is_playing = False

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
