# Description:  
Facial detection of an image or video using OpenCV.

# Requirements:
OpenCV for python  

# How to run:
`python3 detector.py <type> <object-flag> <image>`

type | object-flag | image 
------------- | ------------- | -------------
image | -c or -f | file.png
video | -c or -f | N/A

# Running the code examples:
Facial detection of human faces in a file named face.jpg:  
`python3 detector.py image -f face.jpg`  

Facial detection of cat faces in a file named cat.png:  
`python3 detectior.py image -c cat.png`  

Facial detection of human faces using webcam:  
`python3 detector.py video -f` 

Facial detection of cat faces using webcam:  
`python3 detector.py video -c` 
