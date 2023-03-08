import cv2  
  
  
def main():  
  
    # initialize front face classifier  
    cascade = cv2.CascadeClassifier("C:/Users/anton/PycharmProjects/Facial_Recognition_Emotion_Detection/emotion based filter/assets/haarcascade_frontalface_default.xml")
  
    frame = cv2.imread('C:/Users/anton/PycharmProjects/Facial_Recognition_Emotion_Detection/emotion based filter/assets/children.png')  
  
    # Convert to black-and-white  
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
    blackwhite = cv2.equalizeHist(gray)  
  
    rects = cascade.detectMultiScale(  
        blackwhite, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30),  
    flags=cv2.CASCADE_SCALE_IMAGE)  
  
    for x, y, w, h in rects:  
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  
  
    cv2.imwrite('C:/Users/anton/PycharmProjects/Facial_Recognition_Emotion_Detection/emotion based filter/outputs/children_detected.png', frame)  
  
if __name__ == '__main__':  
    main()
