import cv2

def play_video(filename):
  """
  Plays an MP4 video using OpenCV.

  Args:
    filename: The path to the MP4 video file.
  """
  cap = cv2.VideoCapture(filename)

  if not cap.isOpened():
    print(f"Error opening video file: {filename}")
    return

  while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
      print("Can't receive frame (stream end?). Exiting ...")
      break
    cv2.imshow('Video Player', frame)

    # Press 'q' to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break

  cap.release()
  cv2.destroyAllWindows()

if __name__ == "__main__":
  video_file = "fruit.mp4"  # Replace with your video file path
  play_video(video_file)