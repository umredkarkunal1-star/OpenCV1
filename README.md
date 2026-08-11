# 🖼️ OpenCV Image Editor

A simple **menu-driven image editing application built with Python and OpenCV**.
This project provides several basic image processing and editing operations through an easy-to-use command-line menu.

## 🚀 Features

The application provides the following image editing operations:

1. **Add Text** – Add custom text to an image with selectable position, size, color, and thickness.
2. **Blur Image** – Apply Gaussian blur to an image.
3. **Convert to B/W** – Convert a color image into grayscale.
4. **Crop Image** – Crop an image using user-defined coordinates.
5. **Draw Line** – Draw a line between two points.
6. **Draw Shape** – Draw a circle with a custom position, radius, color, and thickness.
7. **Flip Image** – Flip an image horizontally, vertically, or in both directions.
8. **Resize Image** – Change the width and height of an image.
9. **Rotate Image** – Rotate an image by 90°, 180°, or 270°.
10. **Edge Detection** – Detect edges using the Canny edge detection algorithm.
11. **Exit** – Close the application.

## 🛠️ Technologies Used

* **Python**
* **OpenCV (cv2)**

## 📦 Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the project folder

```bash
cd <project-folder>
```

### 3. Install OpenCV

```bash
pip install opencv-python
```

## ▶️ How to Run

Run the Python file:

```bash
python project1.py
```

After running the program, the following menu will appear:

```text
===== IMAGE EDITOR =====
1. ADD TEXT
2. BLUR IMAGE
3. CONVERT INTO B/W
4. CROP IMAGE
5. DRAW LINE
6. DRAW SHAPE
7. FLIP IMAGE
8. RESIZE IMAGE
9. ROTATE IMAGE
10. EDGE DETECTION
11. EXIT
```

Enter the option number and follow the instructions displayed by the program.

## 📂 Project Structure

```text
OpenCV-Image-Editor/
│
├── project1.py
└── README.md
```

## 🔍 OpenCV Functions Used

| Function                  | Purpose                    |
| ------------------------- | -------------------------- |
| `cv2.imread()`            | Reads an image             |
| `cv2.putText()`           | Adds text                  |
| `cv2.GaussianBlur()`      | Applies Gaussian blur      |
| `cv2.cvtColor()`          | Converts image color space |
| `cv2.line()`              | Draws a line               |
| `cv2.circle()`            | Draws a circle             |
| `cv2.flip()`              | Flips an image             |
| `cv2.resize()`            | Resizes an image           |
| `cv2.rotate()`            | Rotates an image           |
| `cv2.Canny()`             | Performs edge detection    |
| `cv2.imshow()`            | Displays an image          |
| `cv2.waitKey()`           | Waits for keyboard input   |
| `cv2.destroyAllWindows()` | Closes OpenCV windows      |

## 🎯 Project Purpose

The purpose of this project is to practice **Python programming and basic image processing using OpenCV**. It demonstrates how different OpenCV functions can be combined into a single menu-driven application.

## 👨‍💻 Author

**Kunal**

Built with 🐍 Python and 👁️ OpenCV.
