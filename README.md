🔍 Real-Time Object Detection with YOLOv8 and Live Web Dashboard
This project leverages YOLOv8, a state-of-the-art object detection model, to perform real-time object detection using a webcam. It not only displays the detected objects with bounding boxes on the video feed, but also dynamically updates an HTML dashboard showing the live count of detected objects.

📸 Features
🎯 Real-time object detection using YOLOv8 (yolov8n.pt)

📊 Live object counting per frame

🌐 Auto-updating HTML dashboard with detected object statistics

🖼️ Annotated video feed with bounding boxes and object labels

⚡ FPS (Frames Per Second) display for performance monitoring

🔁 Clean exit and resource management


🧰 Tech Stack
Python 3.x

OpenCV

Ultralytics YOLOv8

HTML (for dashboard)

📂 How It Works
Loads the YOLOv8 model using ultralytics.

Captures video frames from your system’s webcam.

Runs object detection on each frame.

Draws bounding boxes and labels on the frame.

Counts detected objects by category.

Writes the live count into an HTML file (object_count.html) for real-time web display.

Shows the annotated video feed with object labels and FPS.

Exits cleanly on pressing 'q'.

🛠️ Installation
bash
Copy
Edit
# Clone the repository
git clone https://github.com/yourusername/yolov8-live-detection.git
cd yolov8-live-detection

# Install required libraries
pip install opencv-python ultralytics
▶️ Run the Project
bash
Copy
Edit
python detect_and_count.py
Make sure your webcam is connected and accessible.
To view the object counts, open object_count.html in any browser.

📁 Output
Live Feed: Annotated webcam view with detected objects and FPS

HTML File: object_count.html showing real-time object counts

🔧 Customization
Replace "yolov8n.pt" with any custom or larger YOLOv8 model (yolov8s.pt, yolov8m.pt, etc.)

Tweak confidence threshold in model(frame, conf=0.5)

Modify HTML output structure in the update_html() function

💡 Future Improvements
Deploy on a local web server using Flask

Add support for video file or image input

Object tracking and motion path visualization

Logging and analytics over time

Deploy on edge devices like Raspberry Pi

🤝 Contributions
Contributions are welcome! Feel free to fork, submit issues or pull requests to improve this project.
