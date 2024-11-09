from moviepy.editor import VideoFileClip
import pygame

pygame.mixer.pre_init(frequency=44100, size=-16, channels=1)  # Force mono
pygame.mixer.init()

def play_video(filename):
  """
  Plays an MP4 video using MoviePy.

  Args:
    filename: The path to the MP4 video file.
  """
  try:
    # Load the video clip
    clip = VideoFileClip(filename)

    # Play the video in a preview window
    clip.preview()

    # Close the clip (important to release resources)
    clip.close()

  except Exception as e:
    print(f"An error occurred: {e}")

if __name__ == "__main__":
  video_file = r"C:\Users\pjhudgins\OneDrive\Documents\programming\stem\video_grid\fruit.mp4"  # Replace with your video file path
  play_video(video_file)