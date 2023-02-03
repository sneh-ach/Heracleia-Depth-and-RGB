import cv2
import depthai as dai
import numpy as np
from cv2 import VideoWriter
from cv2 import VideoWriter_fourcc


extended_disparity = False
subpixel = False
lr_check = True

pipeline = dai.Pipeline()

monoLeft = pipeline.create(dai.node.MonoCamera)
monoRight = pipeline.create(dai.node.MonoCamera)
depth = pipeline.create(dai.node.StereoDepth)
xout = pipeline.create(dai.node.XLinkOut)

# Define source and output
camRgb = pipeline.create(dai.node.ColorCamera)
xoutVideo = pipeline.create(dai.node.XLinkOut)

# Properties
camRgb.setBoardSocket(dai.CameraBoardSocket.RGB)
camRgb.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P)
camRgb.setVideoSize(1920, 1080)

xoutVideo.input.setBlocking(False)
xoutVideo.input.setQueueSize(1)

camRgb.video.link(xoutVideo.input)

xoutVideo.setStreamName("video")
xout.setStreamName("disparity")

monoLeft.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)
monoLeft.setBoardSocket(dai.CameraBoardSocket.LEFT)
monoRight.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)
monoRight.setBoardSocket(dai.CameraBoardSocket.RIGHT)

depth.setDefaultProfilePreset(dai.node.StereoDepth.PresetMode.HIGH_DENSITY)
depth.initialConfig.setMedianFilter(dai.MedianFilter.KERNEL_7x7)
depth.setLeftRightCheck(lr_check)
depth.setExtendedDisparity(extended_disparity)
depth.setSubpixel(subpixel)

monoRight.out.link(depth.right)
monoLeft.out.link(depth.left)
depth.disparity.link(xout.input)

with dai.Device(pipeline) as device:

    q = device.getOutputQueue(name="Depth GreyScale", maxSize=4, blocking=False)
    video = device.getOutputQueue(name="Video RGB", maxSize=4, blocking=False)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    output = cv2.VideoWriter('/Users/snehacharya/Desktop/VIDEO/Depth1.avi',fourcc, 20, (640, 400))
    output1 = cv2.VideoWriter('/Users/snehacharya/Desktop/VIDEO/Video1.avi',fourcc, 20, (640, 400))

    while True:
        videoIn = video.get()
        inDisparity = q.get()
        frame = inDisparity.getFrame()
        frame = (frame * (255 / depth.initialConfig.getMaxDisparity())).astype(np.uint8)

#       color_frame = cv2.applyColorMap(frame, cv2.COLORMAP_JET)
        color_frame = cv2.applyColorMap(frame, cv2.COLORMAP_BONE)
        color_frame = cv2.resize(color_frame, (640, 400))
        videoIn = videoIn.getCvFrame()
        videoIn = cv2.resize(videoIn, (640, 400))
        
        
        output.write(color_frame)
        output1.write(videoIn)
        
        
        cv2.imshow("video", videoIn)
        
#        cv2.imshow("disparity", frame)
        cv2.imshow("disparity_color", color_frame)

        if cv2.waitKey(1) == ord('q'):
            break

    # release the VideoWriter object
    output.release()
