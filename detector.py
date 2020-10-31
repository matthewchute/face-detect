import cv2, os, sys 

class detector():
    
    def __init__(self):

        self.faceHarr = "haarcascade_frontalface_default.xml"
        self.catHarr = "haarcascade_frontalcatface.xml"
        
        # verify type
        if sys.argv[1] == "image" or sys.argv[1] == "video":
            self.type = sys.argv[1]
        else:
            print("Type Error")
            sys.exit()

        # verify object flag
        if sys.argv[2] == "-f" or sys.argv[2] == "-c":
            self.obj = sys.argv[2]
        else:
            print("Object Error")
            sys.exit()

        # verify image file
        if self.type == "image" and len(sys.argv) > 3 and os.path.isfile(sys.argv[3]):
            self.image = sys.argv[3]
        elif self.type == "video":
            pass
        else:
            print("Image File Error")
            sys.exit()

    # to add border around face  
    def addBorder(self, detected, image, color):
        for (x, y, w, h) in detected:
            cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)

    # determine which cascade to return depending on object flag
    def getCascade(self):
        if self.obj == "-f":
            return cv2.CascadeClassifier(cv2.data.haarcascades + self.faceHarr)
        else:
            return cv2.CascadeClassifier(cv2.data.haarcascades + self.catHarr)

if __name__ == "__main__":

    det = detector()

    # facial detection of image:
    if det.type == "image":
        imagecopy = cv2.imread(det.image)
        cascade = det.getCascade()
        grayscale = cv2.cvtColor(imagecopy, cv2.COLOR_BGR2GRAY)
        faces = cascade.detectMultiScale(grayscale, 1.3, 4)
        det.addBorder(faces, imagecopy, (0, 255, 0)) 
        cv2.imshow("Facial Detection", imagecopy)
        cv2.waitKey(0) 
        cv2.destroyAllWindows()

    # facial detection of video:
    else:
        video = cv2.VideoCapture(0)
        cascade = det.getCascade()
        while True:
            _, frame = video.read()
            grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = cascade.detectMultiScale(grayscale, 1.3, 4)
            det.addBorder(faces, frame, (0, 255, 0))
            cv2.imshow('Facial Detection', frame)
            if cv2.waitKey(1) == 27:
                break
        video.release()
        cv2.destroyAllWindows()