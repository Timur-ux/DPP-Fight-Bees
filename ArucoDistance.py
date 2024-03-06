import numpy as np
import cv2
from cv2 import aruco


def load_camera_configurations(video_path):
    return focal_length_x, focal_length_y, principal_point_x, principal_point_x, k1, k2, p1, p2, k3

    pass


# Camera calibration parameters (intrinsic matrix and distortion coefficients)
# You need to replace these values with your calibrated camera parameters
camera_matrix = np.array([[focal_length_x, 0, principal_point_x],
                          [0, focal_length_y, principal_point_y],
                          [0, 0, 1]])
dist_coeffs = np.array([k1, k2, p1, p2, k3])

# Load ArUco dictionary
aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)

# Capture video from camera
cap = cv2.VideoCapture(0)
marker_size = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect ArUco markers
    corners, ids, _ = aruco.detectMarkers(frame, aruco_dict)

    if ids is not None:
        # Estimate pose
        rvecs, tvecs, _ = aruco.estimatePoseSingleMarkers(corners, marker_size, camera_matrix, dist_coeffs)

        for i in range(len(ids)):
            # Calculate distance
            distance = np.linalg.norm(tvecs[i])

            # Draw axis and distance on the image
            aruco.drawAxis(frame, camera_matrix, dist_coeffs, rvecs[i], tvecs[i], marker_size * 0.5)
            cv2.putText(frame, f"Distance: {distance:.2f} units", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
