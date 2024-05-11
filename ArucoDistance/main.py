import CameraCalibrator as CC
import ArucoDistance as AD
import argparse
import json
import zmq

class RecognitionProcessor:
    def __init__(self, context: zmq.Context, servAddress):
        self.context = context
        self.socket = context.socket(zmq.PUSH)
        self.socket.connect(servAddress)

    def process(self, data):
        self.socket.send(json.dumps(data))

def main():
    DEFAULT_CALIBRATION_RESULT_PATH = "./CalibrationResult.json"
    DEFAULT_SERVER_DATA_PATH = "./Config.json"
    parser = argparse.ArgumentParser(description="Default argument parser for application control")
    parser.add_argument("--calibrate", type=bool, default=False, help="point if camera is need to calibrate(Default: False)")
    parser.add_argument("--camera_index", type=int, default=0, help="point camera index that will be calibrated(Default: 0)")

    namespace = parser.parse_args()

    if namespace.calibrate:
        calibrationFilePath = input(f"Input path calibration results will be stored({DEFAULT_CALIBRATION_RESULT_PATH} by default): ")
        if calibrationFilePath == "":
            calibrationFilePath = DEFAULT_CALIBRATION_RESULT_PATH

        camera_config = CC.calibrateUsingCamera()
        with open(calibrationFilePath, "w") as file:
            json.dump(camera_config, file)

        print(f"Calibration result: \n {camera_config}")
        print(f"It is stored at: {calibrationFilePath}")
        return

    calibrationFilePath = input(f"Input path to camera's calibration file({DEFAULT_CALIBRATION_RESULT_PATH} by default): ")
    if calibrationFilePath == "":
        calibrationFilePath = DEFAULT_CALIBRATION_RESULT_PATH
    
    with open(calibrationFilePath, "r") as file:
        camera_config = json.load(file)

    netConfigPath = input(f"Input path to net config where server's or broker's soket stored({DEFAULT_SERVER_DATA_PATH} by default)")
    if netConfigPath == "":
        netConfigPath = DEFAULT_SERVER_DATA_PATH

    with open(netConfigPath, "r") as file:
        config = json.load(file)

    context = zmq.Context(1)
    serverSocket = config["ServerSocket"]
    recognitionProcessor = RecognitionProcessor(context, serverSocket)

    AD.startRecognize(camera_config, namespace.camera_index, recognitionProcessor)
    




if __name__ == "__main__":
    main()
