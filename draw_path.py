import numpy as np
import cv2

# Configurations
canvas_size = 100
scale = 5  # Display scaling (for easier drawing)
drawing = False
path_points = []

# Create white canvas
img = np.ones((canvas_size * scale, canvas_size * scale), dtype=np.uint8) * 255
img_color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

def draw(event, x, y, flags, param):
    global drawing, path_points, img_color

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        path_points.append((x, y))
        cv2.circle(img_color, (x, y), 1, (0, 0, 255), -1)

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            path_points.append((x, y))
            cv2.line(img_color, path_points[-2], path_points[-1], (0, 0, 255), 1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

cv2.namedWindow("Draw Path")
cv2.setMouseCallback("Draw Path", draw)

print("Draw by dragging the mouse like in MS Paint. Press ESC when finished.")

while True:
    cv2.imshow("Draw Path", img_color)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC
        break

cv2.destroyAllWindows()

# Downscale to

