import cv2
from ultralytics import YOLO
import time
import sys
import json

# Load YOLOv8 model (Ensure correct path for the YOLOv8 weights file)
model = YOLO("yolov8n.pt")  # Replace with your YOLOv8 model file path

# Initialize the webcam (0 is the default camera; adjust index for external cameras)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not cap.isOpened():
    print("Error: Could not access the webcam.")
    sys.exit()

start_time = time.time()

# Function to update HTML file with object counts
def update_html(counts):
    html_content = """<html>
    <head><title>Object Count</title></head>
    <body>
    <h1>Real-Time Object Detection Count</h1>
    <table border='1'>
        <tr><th>Object</th><th>Count</th></tr>
    """
    for obj, count in counts.items():
        html_content += f"<tr><td>{obj}</td><td>{count}</td></tr>"
    html_content += "</table></body></html>"
    with open("object_count.html", "w") as file:
        file.write(html_content)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture image from webcam.")
            break

        results = model(frame, conf=0.5)  # Perform detection
        annotated_frame = results[0].plot()  # Annotate frame
        
        # Reset object count for each frame
        object_counts = {}
        
        # Count detected objects
        for r in results:
            for box in r.boxes:
                obj_class = r.names[int(box.cls[0].item())]  # Get class name
                object_counts[obj_class] = object_counts.get(obj_class, 0) + 1
        
        update_html(object_counts)  # Update HTML file with new counts
        
        # Display FPS
        fps = 1 / (time.time() - start_time)
        start_time = time.time()
        cv2.putText(annotated_frame, f"FPS: {int(fps)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("YOLOv8 Real-Time Object Detection", annotated_frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Exiting detection loop...")
            break

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    cap.release()
    cv2.destroyAllWindows()
    print("Resources released successfully.")
