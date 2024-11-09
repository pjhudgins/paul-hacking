import cv2
from moviepy.editor import VideoFileClip

def play_video(filename):
    """
    Plays an MP4 video using MoviePy without the preview() method.

    Args:
      filename: The path to the MP4 video file.
    """
    try:
        # Load the video clip
        clip = VideoFileClip(filename)

        # Get video properties
        fps = clip.fps
        duration = clip.duration

        # Iterate through frames and display them using OpenCV
        for frame in clip.iter_frames():
            # Convert frame from RGB to BGR (OpenCV uses BGR)
            frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR) 

            cv2.imshow('MP4 Video', frame_bgr)

            # Calculate wait time based on FPS
            wait_time = int(1000 / fps)  # milliseconds

            if cv2.waitKey(wait_time) & 0xFF == ord('q'):
                break

        # Close the clip
        clip.close()
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_file = r"C:\Users\pjhudgins\OneDrive\Documents\programming\stem\video_grid\fruit.mp4"  # Replace with your video file path
    play_video(video_file)