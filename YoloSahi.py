# Developed By Sihab Sahariar
import cv2
from sahi import AutoDetectionModel
from sahi.predict import get_prediction, get_sliced_prediction, predict
from sahi.utils.yolov8 import download_yolov8n_model, download_yolov8m_model, download_yolov8l_model, download_yolov8x_model
from sort import *
from helper import draw_bbox

def video_infer_sahi(cap, frame_skip, detection_model, tracker, slice_width=512, slice_height=512, overlap_height_ratio=0.2, overlap_width_ratio=0.2, scale_percent=50):
    
    while True:
        c = 0
        ret, frame = cap.read()
        if not ret:
            break
        if c % frame_skip != 0:
            continue
        c += 1

        w = int(frame.shape[1] * scale_percent / 100)
        h = int(frame.shape[0] * scale_percent / 100)

        dim = (w, h)

        # resize image
        frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

        # SAHI Prediction
        results = get_sliced_prediction(frame,
                                        detection_model,
                                        slice_width=512,
                                        slice_height=512,         # slice height and width which means the image will be divided into 512x512 slices
                                        overlap_height_ratio=0.2, # overlap ratio for height which means 20% of the height will be overlapped
                                        overlap_width_ratio=0.2) # overlap ratio for width which means 20% of the width will be overlapped
                                        
        # Sahi Prediction
        object_prediction_list = results.object_prediction_list

        # Initialize detections array
        detections = np.empty((0, 5))
        confidences = []


        for ind, _ in enumerate(object_prediction_list):
            box = int(object_prediction_list[ind].bbox.minx),int(object_prediction_list[ind].bbox.miny),int(object_prediction_list[ind].bbox.maxx), int(object_prediction_list[ind].bbox.maxy)
            clss = object_prediction_list[ind].category.name

            if clss == 'person': # Only consider 'person' class
                detections = np.vstack((detections, [box[0], box[1], box[2], box[3], object_prediction_list[ind].score.value]))
                confidences.append(object_prediction_list[ind].score.value*100)


        # Update the tracker with the new detections
        resultsTracker = tracker.update(detections)

        # Draw bounding boxes and labels on the frame
        for i,obj in enumerate(resultsTracker):
            x1, y1, x2, y2, id = obj # Get coordinates and ID
            w, h = x2 - x1, y2 - y1  # Calculate width and height

            label = f"Person #{id}"  # Label for the bounding box
            draw_bbox(frame, int(x1), int(y1), int(x2), int(y2), label, confidences[i])

        # Display the frame
        cv2.imshow("Yolov8+SAHI Inference", frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Release the video and close all windows
    cap.release()
    cv2.destroyAllWindows()


def image_infer(image_path, detection_model, tracker, slice_width=512, slice_height=512, overlap_height_ratio=0.2, overlap_width_ratio=0.2, scale_percent=50):
    frame = cv2.imread(image_path)
    w = int(frame.shape[1] * scale_percent / 100)
    h = int(frame.shape[0] * scale_percent / 100)

    dim = (w, h)

    # resize image
    frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

    # SAHI Prediction
    results = get_sliced_prediction(frame,
                                    detection_model,
                                    slice_width=512,
                                    slice_height=512,         # slice height and width which means the image will be divided into 512x512 slices
                                    overlap_height_ratio=0.2, # overlap ratio for height which means 20% of the height will be overlapped
                                    overlap_width_ratio=0.2) # overlap ratio for width which means 20% of the width will be overlapped
                                    
    # Sahi Prediction
    object_prediction_list = results.object_prediction_list

    # Initialize detections array
    detections = np.empty((0, 5))
    confidences = []

    for ind, _ in enumerate(object_prediction_list):
        box = int(object_prediction_list[ind].bbox.minx),int(object_prediction_list[ind].bbox.miny),int(object_prediction_list[ind].bbox.maxx), int(object_prediction_list[ind].bbox.maxy)
        clss = object_prediction_list[ind].category.name

        if clss == 'person': # Only consider 'person' class
            detections = np.vstack((detections, [box[0], box[1], box[2], box[3], object_prediction_list[ind].score.value]))
            confidences.append(object_prediction_list[ind].score.value)


    # Update the tracker with the new detections
    resultsTracker = tracker.update(detections)

    # Draw bounding boxes and labels on the frame
    for i,obj in enumerate(resultsTracker):
        x1, y1, x2, y2, id = obj # Get coordinates and ID
        w, h = x2 - x1, y2 - y1  # Calculate width and height

        label = f"Person #{id}"  # Label for the bounding box
        draw_bbox(frame, int(x1), int(y1), int(x2), int(y2), label, confidences[i])


    # Display the frame
    cv2.imshow("Yolov8+SAHI Inference", frame)

    cv2.waitKey(0)
    cv2.destroyAllWindows()



