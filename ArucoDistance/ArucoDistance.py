import numpy as np
import cv2
from cv2 import aruco
import zmq
import CameraCalibrator

if __name__ != "__main__":
    print("Error: ArucoDistance can be started only as main script, not module")
    exit(1)

camera_config = CameraCalibrator.calibrateUsingCamera(0, "./samples", True)
camera_matrix = camera_config["camera_matrix"]
dist_coeffs = camera_config["distortion"]

# Load ArUco dictionary
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
detector_parameters = aruco.DetectorParameters()
detector = aruco.ArucoDetector(aruco_dict, detector_parameters)

# Capture video from camera
cap = cv2.VideoCapture(0)
marker_size = 0.15
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect ArUco markers
    corners, ids, _ = detector.detectMarkers(frame)

    if ids is not None:
        # Estimate pose
        rvecs, tvecs, _ = aruco.estimatePoseSingleMarkers(corners, marker_size, camera_matrix, dist_coeffs)

        for i in range(len(ids)):
            # Calculate distance
            distance = np.linalg.norm(tvecs[i])

            # Draw axis and distance on the image
            cv2.drawFrameAxes(frame, camera_matrix, dist_coeffs, rvecs[i], tvecs[i], marker_size * 0.5)
            cv2.putText(frame, f"Distance: {distance:.2f} meters", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
