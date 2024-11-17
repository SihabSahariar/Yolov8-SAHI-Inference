from YoloSahi import *

if __name__ == "__main__":

    detection_model = AutoDetectionModel.from_pretrained(model_type='yolov8',confidence_threshold=0.4,device='cpu',model_path="yolov8n.pt")
    
    tracker = Sort(max_age=20, min_hits=2, iou_threshold=0.3) # Initialize the SORT tracker for object tracking

    # For video inference
    # cap = cv2.VideoCapture('Computer Vision task Culture Hint.mp4') # load video
    cap = cv2.VideoCapture(0)
    frame_skip = 1 # Frame Skip
    video_infer_sahi(cap, frame_skip, detection_model, tracker,slice_height=512, slice_width=512, overlap_height_ratio=0.2, overlap_width_ratio=0.2, scale_percent=70)
    
    # For image inference
    # image_path = 'test.jpg'
    # image_infer(image_path, detection_model, tracker,slice_height=240, slice_width=240, overlap_height_ratio=0.2, overlap_width_ratio=0.2, scale_percent=100)