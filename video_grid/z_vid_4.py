import pygame
from moviepy.editor import VideoFileClip

pygame.mixer.init()  # Initialize the mixer

def play_audio(filename):
    try:
        clip = VideoFileClip(filename)
        audio_clip = clip.audio
        audio_array = audio_clip.to_soundarray()

        # Convert the NumPy array to a bytes object
        audio_bytes = audio_array.tobytes() 

        sound = pygame.sndarray.make_sound(audio_bytes)
        sound.play()

        while pygame.mixer.get_busy():  # Wait for audio to finish
            pygame.time.delay(100)

        clip.close()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_file = r"C:\Users\pjhudgins\OneDrive\Documents\programming\stem\video_grid\fruit.mp4"
    play_audio(video_file)