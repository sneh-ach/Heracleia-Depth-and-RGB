# Depth Video Generation using OpenCV and DepthAI

# Overview

This code is written in Python and uses the OpenCV and DepthAI libraries to generate depth videos from stereo cameras. It also saves the depth and video streams as avi files.

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

#Customization

The output resolution of the depth and video streams can be changed by modifying the 'cv2.resize' function arguments.
The codec used to save the video files can be changed by modifying the 'cv2.VideoWriter_fourcc' argument.
The color map used to visualize the depth data can be changed by modifying the 'cv2.applyColorMap' argument.
The output file names and directories can be changed by modifying the 'cv2.VideoWriter' argument.
