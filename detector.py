import cv2, os, sys 

# python3 detector.py <type> <obj-flag> <image> 

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
        elif self.type == "video":
            pass
        else:
            print("Object Error")
            sys.exit()

        # verify image file
        if self.type == "image" and len(sys.argv) > 3 and os.path.isfile(sys.argv[3]):
            self.image = sys.argv[3]
        elif self.type == "video":
            pass
        else:
            print("File Error")
            sys.exit()

    # to add detection border around face  
    def addBorder(self, detected, image, color: tuple):
        for (x, y, w, h) in detected:
            cv2.rectangle(image, (x, y), (x + w, y + h), color, thickness = 2)

    # determine which haar to use
    def whichObject(self):
        if self.obj == "-f":
            return cv2.CascadeClassifier(cv2.data.haarcascades + self.faceHarr)
        else:
            return cv2.CascadeClassifier(cv2.data.haarcascades + self.catHarr)

if __name__ == "__main__":
    det = detector()

    if det.type == "image":
        imagecopy = cv2.imread(det.image)
        grayscale = cv2.cvtColor(imagecopy, cv2.COLOR_BGR2GRAY)
        face_cascade = det.whichObject()
        faces = face_cascade.detectMultiScale(grayscale, 1.3, 4)
        det.addBorder(faces, imagecopy, (0, 255, 0)) 
        cv2.imshow("Facial Detection", imagecopy)
        cv2.waitKey(0) 
        cv2.destroyAllWindows()

    else:
        # to add video 
        pass