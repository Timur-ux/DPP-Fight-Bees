import numpy as np
import cv2
from cv2 import aruco

def startRecognize(camera_config, cameraId, recognitionProcessor):
    camera_matrix = camera_config["camera_matrix"]
    dist_coeffs = camera_config["distortion"]

    # Load ArUco dictionary
    aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
    detector_parameters = aruco.DetectorParameters()
    detector = aruco.ArucoDetector(aruco_dict, detector_parameters)

    # Capture video from camera
    cap = cv2.VideoCapture(cameraId)
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

                recognitionProcessor.process({
                    "distance": distance
                    })


    cap.release()
    cv2.destroyAllWindows()
