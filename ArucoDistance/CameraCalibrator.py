import numpy as np
import cv2 as cv
import glob
 
# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
def calibrateUsingCamera(cameraIndex = 0, dirToStoreGoodCalibrationFrames = None, doLog = False):
    objp = np.zeros((7*7, 3), np.float32)
    objp[:, :2] = np.mgrid[0:7, 0:7].T.reshape(-1, 2)

    # Arrays to store object points and image points from all the images.
    objpoints = []  # 3d point in real world space
    imgpoints = []  # 2d points in image plane.

    gray = None
    cap = cv.VideoCapture(cameraIndex)
    goodFrames = 0
    while goodFrames < 15:
        ret, img = cap.read()
        if not ret:
            print("Warn: bad camera")
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        # Find the chess board corners
        ret, corners = cv.findChessboardCorners(gray, (7, 7), None)

        # If found, add object points, image points (after refining them)
        if ret == True:
            goodFrames += 1
            objpoints.append(objp)

            corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
            imgpoints.append(corners2)

            if(doLog):
                print("The image good for calibration")
            if(dirToStoreGoodCalibrationFrames is not None):
                cv.imwrite(f"{dirToStoreGoodCalibrationFrames}/{goodFrames}.jpg", img)

    if gray is None:
        print("Error in calibrateUsingCamera: Bad images, can't calibrate")
        return {}
    mtx_fake = np.zeros((3, 3))
    dist_fake = np.zeros((1, 5))
    ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(
        objpoints, imgpoints, gray.shape[::-1], mtx_fake, dist_fake, None, None, 0, criteria)
    return {
            "camera_matrix": mtx,
            "distortion" : dist,
            "rvecs" : rvecs,
            "tvecs" : tvecs,
            }

def calibrateUsingImages(dirWithImages):
    objp = np.zeros((7*7, 3), np.float32)
    objp[:, :2] = np.mgrid[0:7, 0:7].T.reshape(-1, 2)

    # Arrays to store object points and image points from all the images.
    objpoints = []  # 3d point in real world space
    imgpoints = []  # 2d points in image plane.

    images = glob.glob(f'{dirWithImages}/*.jpg')
    gray = None
    for fname in images:
        img = cv.imread(fname)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        # Find the chess board corners
        ret, corners = cv.findChessboardCorners(gray, (7, 7), None)

        # If found, add object points, image points (after refining them)
        if ret == True:
            objpoints.append(objp)

            corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
            imgpoints.append(corners2)

    if len(objpoints) == 0 or gray is None:
        print("Error in calibrateUsingImages: Bad images, can't calibrate")
        return {}
    mtx_fake = np.zeros((3, 3))
    dist_fake = np.zeros((1, 5))
    ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(
        objpoints, imgpoints, gray.shape[::-1], mtx_fake, dist_fake, None, None, 0, criteria)
    return {
            "camera_matrix": mtx,
            "distortion" : dist,
            "rvecs" : rvecs,
            "tvecs" : tvecs,
            }
