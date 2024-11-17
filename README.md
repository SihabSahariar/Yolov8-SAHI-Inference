
# SAHI & YOLOv8 Integration for Enhanced Object Detection

This repository provides a Python project that integrates **SAHI (Slicing Aided Hyper Inference)** with **YOLOv8** for enhanced object detection. The project supports detection on images, video files, and real-time webcam feeds, enabling more accurate results even in high-resolution and complex scenes.

## Getting Started

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/SihabSahariar/Yolov8-SAHI-Inference/
   cd Yolov8-SAHI-Inference
2. Install the required dependencies:
	 ```bash
	pip install -r requirements.txt
3. Run the main script:
	 ```bash
	 python main.py
## Yolov8 vs Yolov8+SAHI

![-   This mode runs standard YOLOv8 detection without using SAHI slicing. It processes entire images or frames in one go, which is suitable for low-resolution or simpler scenarios.](https://cdn-ilcabpl.nitrocdn.com/XTpGTaZWYQSxctfMHQPVOQKOsBspWTQi/assets/images/optimized/rev-a0beb67/learnopencv.com/wp-content/uploads/2023/06/result-2-1.jpg)

## Features

-   **Supports Multiple Inputs**: Works with images, video files, and webcam streams.
-   **Enhanced Detection**: Integrates SAHI to better handle large images.
-   **Real-Time Processing**: Provides real-time object tracking and detection.
-   **Extensible Code**: Easy to modify and extend with additional features.

## Use Cases

-   **Small Object Detection**: SAHI helps in detecting smaller objects in large images by slicing the image into manageable sections, ensuring that small objects are not missed.
-   **Drone-Based Object Detection**: Ideal for aerial imagery captured by drones where the field of view is wide, and objects may appear small due to altitude.
-   **Surveillance Systems**: Effective in analyzing high-resolution security footage for identifying people, vehicles, or unusual activities.
-   **Wildlife Monitoring**: Useful for detecting animals in high-resolution aerial or ground camera images where details matter.
-   **Industrial Inspections**: Assists in detecting defects or items in large-scale images captured for quality control.
## Project Structure

    Yolov8-SAHI-Inference/
    ├── helper.py          # Custom Draw Box Function
    ├── sort.py            # Implementation of the SORT (Simple Online and Realtime Tracking) algorithm for object tracking
    ├── test.jpg           # Sample image for testing the object detection functionality
    ├── YoloSahi.py        # Script that integrates SAHI with YOLOv8, handles input sources (image, video, webcam), and processes detections
    ├── main.py            # Main Script to run inference on Webcam/RTSP/Video/Image
    ├── yolov8n.pt         # YOLOv8 pre-trained model file used for detection (YOLOv8 nano model)
    └── README.md          # (Recommended) Project description and usage instructions
  
## Contributing
Contributions, suggestions, and feature requests are welcome! Please open an issue or submit a pull request.
## License
This project is licensed under the MIT License. 
## Contact
For any questions or support, please contact me at: sihabsahariarcse@gmail.com
