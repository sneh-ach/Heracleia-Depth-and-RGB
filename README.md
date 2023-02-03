# Depth Video Generation using OpenCV and DepthAI

# Overview

This code is using the OpenCV and DepthAI libraries to create a stereo depth pipeline and output two videos: one of the color frame and another of the disparity frame in color map. The pipeline consists of several nodes that are linked together to process the video feed from the stereo cameras. The nodes handle the properties of the cameras, stereo depth calculation, and outputting the video frames. The output videos are saved using the VideoWriter object of the OpenCV library and are written in XVID format. The color map used for the disparity frame is "COLORMAP_BONE". The code also creates windows to display the video frames in real-time and waits for the user to press 'q' to stop the loop and release the VideoWriter objects.

# Dependencies

- OpenCV
- DepthAI
- NumPy

# Usage

Connect two stereo cameras to the device
Run the code
The depth and video streams will be displayed in two separate windows
The depth video stream will be saved as 'Depth1.avi' in the 'VIDEO' directory on the Desktop
The video stream will be saved as 'Video1.avi' in the 'VIDEO' directory on the Desktop

# Customization

The output resolution of the depth and video streams can be changed by modifying the 'cv2.resize' function arguments.
The codec used to save the video files can be changed by modifying the 'cv2.VideoWriter_fourcc' argument.
The color map used to visualize the depth data can be changed by modifying the 'cv2.applyColorMap' argument.
The output file names and directories can be changed by modifying the 'cv2.VideoWriter' argument.
