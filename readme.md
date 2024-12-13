



# Smile Detector with Photography  

## Description  
This project uses computer vision techniques to detect smiles in real-time through a webcam. When a smile is detected, the program automatically captures a photo and saves it locally. This application can be used in photo booths, interactive applications, or as a fun way to take candid photos.  

The project leverages **Python**, **OpenCV**, and pre-trained Haar Cascade classifiers for smile detection.  

---

## Features  
- Real-time smile detection using a webcam.  
- Automatic photo capture upon smile detection.  
- Saves captured photos with a timestamp in the local directory.  

---

## Prerequisites  
Ensure you have the following installed:  
- Python 3.7 or above  
- OpenCV  

Install dependencies using the command:  

pip install opencv-python  
  

---

## How It Works  
1. **Haar Cascade Classifiers**:  
   - Pre-trained Haar Cascades are used for face and smile detection.  
   - The face is detected first, then the region of interest (ROI) is analyzed for a smile.  

2. **Photo Capture**:  
   - When a smile is detected, the program captures a photo from the webcam.  
   - The photo is saved with a unique timestamp in the specified folder.  

---

## Usage  
1. Clone the repository or download the script.  
2. Ensure the Haar Cascade XML files (`haarcascade_frontalface_default.xml` and `haarcascade_smile.xml`) are in the project directory.  
   You can download them from OpenCV's GitHub:  
   - [Face Detector](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)  
   - [Smile Detector](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_smile.xml)  

3. Run the script:  
   
   python smile_detector.py  
  

4. The webcam feed will open. Smile to capture photos!  

---

## Applications  
- Automated photo booths.  
- Fun applications for parties or events.  
- Interactive systems for candid photography.  

---

## Future Enhancements  
- Add emotion detection for broader facial expressions.  
- Include real-time filters or effects on the captured photos.  
- Integrate with cloud storage to save photos online.  

---

## Acknowledgments  
This project is built using **OpenCV** and leverages the power of Haar Cascade classifiers for efficient smile detection. Thanks to the open-source community for the tools and resources that made this project possible.  

---  

