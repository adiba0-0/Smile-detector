# Smile Detector using OpenCV

A beginner Computer Vision project that performs **real-time face and smile detection** using **OpenCV** and **Haar Cascade Classifiers** through a live webcam feed.

---

## Overview

This application captures frames from the webcam, detects faces in each frame, and then searches for smiles within the detected face region. When a smile is identified, the text **"Smiling"** is displayed above the face.

The project demonstrates the fundamentals of Computer Vision, including image preprocessing, object detection, and real-time video processing.

---

## Features

* Live webcam capture
* Face detection using Haar Cascades
* Smile detection within detected faces
* Bounding box around detected faces
* Displays **"Smiling"** upon successful smile detection
* Real-time processing

---

## 🛠️ Built With

* Python
* OpenCV
* NumPy
* Haar Cascade Classifiers

---

## Project Structure

```text
Smile_detector/
│
├── smile_detector.py
├── haarcascade_frontalface_default.xml
├── haarcascade_smile.xml
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Getting Started

### Clone the repository

```bash
git clone https://github.com/adiba0-0/Smile-detector.git
cd <repo folder>
```

### Create a virtual environment

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python smile_detector.py
```

Press **ESC** to close the webcam window.

---

## Concepts Practiced

* Image processing
* Grayscale conversion
* Haar Cascade face detection
* Haar Cascade smile detection
* Region of Interest (ROI)
* Real-time video processing
* Bounding box visualization

---

## Future Improvements

* Improve smile detection accuracy
* Capture photos automatically when smiling
* Add emotion recognition
* Replace Haar Cascades with modern deep learning models
* Build a desktop GUI

## 👩‍💻 Author

Built while learning **Computer Vision with Python and OpenCV**.

If you found this project helpful, consider giving it a ⭐.
