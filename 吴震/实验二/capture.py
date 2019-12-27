import cv2

#打开笔记本内置摄像头
#camera = cv2.VideoCapture(0)
#读取视频
camera = cv2.VideoCapture('C:/Users/17806/Desktop/sea.avi')
#定义窗口
cv2.namedWindow('MyCamera')
#读取显示视频
while True:
    success, frame = camera.read()
    if success == True:
      cv2.imshow('MyCamera',frame)
      camera1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 换换成灰度图
      cv2.imshow('frame', camera1)
      #慢速播放（按键播放）
      cv2.waitKey()
      #按键退出（esc的ASCII码是27）
    else:
        break
    if cv2.waitKey()  == 27:
        break
#关闭窗口
cv2.destroyWindow('MyCamera')
#释放摄像头
camera.release()