# Description:  
Facial detection on an image file, or of a video from your webcam using OpenCV.

# Requirements:
OpenCV for python  

# `detector.py`  
Run this program: `python3 detector.py <type> <object-flag> <image-path>` from src directory.  

type | object-flag | image-path 
------------- | ------------- | -------------
image | -c or -f | ../assets/file.png
video | -c or -f | N/A

# Running the code examples:
Facial detection of human faces in a file named face.jpg:  
`python3 detector.py image -f ../assets/face.jpg`  

Facial detection of cat faces in a file named cat.png:  
`python3 detectior.py image -c ../assets/cat.png`  

Facial detection of human faces using webcam:  
`python3 detector.py video -f` 

Facial detection of cat faces using webcam:  
`python3 detector.py video -c` 
