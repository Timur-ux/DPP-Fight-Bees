import numpy as np
import cv2
from pupil_apriltags import Detector
import time


def startRecognize(camera_config, cameraId, recognitionProcessor):
    camera_matrix = camera_config["camera_matrix"]
    dist_coeffs = camera_config["distortion"]

    at_detector = Detector(
        families="tag36h11",
        nthreads=1,
        quad_decimate=1.0,
        quad_sigma=0.0,
        refine_edges=1,
        decode_sharpening=0.25,
        debug=0
        )

    # Capture video from camera
    cap = cv2.VideoCapture(cameraId)
    marker_size = 0.05
    firstFrame = True
    while True:
        time.sleep(1/100)
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if not ret:
            break

        camera_fc_params = [camera_matrix[0][0], camera_matrix[1][1], camera_matrix[0][2], camera_matrix[1][2]]
        detectionResult = at_detector.detect(gray, estimate_tag_pose=True, camera_params = camera_fc_params, tag_size = marker_size)

        ids = []
        corners = []
        rvecs = []
        tvecs = []
        for result in detectionResult:
            ids.append(result.tag_id)
            corners.append(result.corners)
            rvecs.append(result.pose_R)
            tvecs.append(result.pose_t)

        if ids != []:
            for i in range(len(ids)):
                # Calculate distance
                distance = np.linalg.norm(tvecs[i])

                # recognitionProcessor.process({
                #     "distance": distance,
                #     "x": tvecs[i][0][0],
                #     "y": tvecs[i][0][1],
                #     "z": tvecs[i][0][2],
                #     "id" : ids[i]
                # })
                cv2.drawFrameAxes(frame, camera_matrix, dist_coeffs, rvecs[i], tvecs[i], marker_size * 0.5)
                cv2.putText(frame, f"Dist: {distance:.2f}m x: {tvecs[i][0][0]:.2f} y: {tvecs[i][1][0]:.2f} z: {tvecs[i][2][0]:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                cv2.putText(frame, f"Id: {ids[i]}", (100, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)


        cv2.imshow('Frame', frame)
        if(firstFrame):
            cv2.waitKey(0)
            firstFrame = False
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
