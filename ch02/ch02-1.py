import cv2

# 视频来源摄像头，参数0为笔记本摄像头，也可以写入读取的视频路径（参考实验一的三种方法）
capture = cv2.VideoCapture(0)

# 设置视频分辨率与帧率
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 设置视频的帧率
# capture.set(cv2.CAP_PROP_FRAME_COUNT, 30)

while (True):

    # 按帧读取
    ref, frame = capture.read()
    cv2.imshow("captureSrc", frame)

    # 灰度转换
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('captureGray', grayFrame)

    # 等待1ms显示图像，若过程中按“Esc”或者视频到最后一帧退出
    c = cv2.waitKey(1) & 0xff
    if c == 27 or ref == False:
        capture.release()

        break



