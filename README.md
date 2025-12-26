#  Virtual Painter

Virtual Painter is a computer vision project that allows users to draw in real time using only hand gestures captured by a webcam. The system detects finger positions to switch between selection and drawing modes, removing the need for a mouse or touchscreen.

The project uses OpenCV and MediaPipe for accurate hand tracking and gesture interpretation.


##  Features

- Real-time hand detection via webcam  
- Drawing mode using the index finger  
- Selection mode using two raised fingers  
- Color selection through gestures  
- Eraser tool  
- Virtual canvas separated from the camera feed  
- Real-time FPS display  


##  How it works

The system operates based on the detected finger states:

- **Selection Mode**  
  Index and middle fingers raised.  
  Allows selecting colors or the eraser by interacting with the side menu.

- **Drawing Mode**  
  Only the index finger raised.  
  The finger movement is translated into strokes on the virtual canvas.

Finger detection is performed by comparing hand landmark positions provided by MediaPipe.


##  Technologies

- Python  
- OpenCV  
- MediaPipe Hands  
- NumPy
- Blender


## Running the project

Install dependencies:

pip install opencv-python mediapipe numpy




