import cv2
def draw_bbox(frame, startX, startY, endX, endY, label, confidence):
    # Dimensions
    box_width = endX - startX
    box_height = endY - startY
    
    # Semi-transparent blue background (bounding box)
    overlay = frame.copy()
    cv2.rectangle(overlay, (startX, startY), (endX, endY), (255, 0, 0), -1)
    
    # Apply gradient opacity to the bounding box
    alpha = 0.15  # Transparency factor (change to your liking)
    cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)

    # Text to display inside the dark gray bar
    text = f"{label}: {confidence:.2f}%"
    font_scale = 0.5
    font_thickness = 1
    text_color = (255, 255, 255)
    
    # Draw the label text
    cv2.putText(frame, text, (startX, startY-15), cv2.FONT_HERSHEY_SIMPLEX, font_scale, text_color, font_thickness)

    colorC=(245, 141, 66)
    t=2
    l=20
    x, y, w, h = startX, startY, box_width, box_height
    x1, y1 = x + w, y + h
    cv2.line(frame, (x, y), (x + l, y), colorC, t)
    cv2.line(frame, (x, y), (x, y + l), colorC, t)
    # Top Right  x1,y
    cv2.line(frame, (x1, y), (x1 - l, y), colorC, t)
    cv2.line(frame, (x1, y), (x1, y + l), colorC, t)
    # Bottom Left  x,y1
    cv2.line(frame, (x, y1), (x + l, y1), colorC, t)
    cv2.line(frame, (x, y1), (x, y1 - l), colorC, t)
    # Bottom Right  x1,y1
    cv2.line(frame, (x1, y1), (x1 - l, y1), colorC, t)
    cv2.line(frame, (x1, y1), (x1, y1 - l), colorC, t)

    # Calculate the center of the bounding box
    cx, cy =int(startX + box_width // 2), int(startY + box_height // 2)
    cv2.circle(frame, (cx, cy), 5, (255, 0, 0), -1)  # Draw a circle at the center