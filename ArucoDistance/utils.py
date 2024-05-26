import json
from json import JSONEncoder
import numpy as np


class NumpyToJsonEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


def dumpConfig(path, config):
    with open(path, "w") as file:
        json.dump(config, file, cls=NumpyToJsonEncoder)


def loadCameraConfig(path):
    with open(path, "r") as file:
        camera_config = json.load(file)
    camera_config["camera_matrix"] = np.asarray(camera_config["camera_matrix"])
    camera_config["distortion"] = np.asarray(camera_config["distortion"])
    camera_config["rvecs"] = np.asarray(camera_config["rvecs"])
    camera_config["tvecs"] = np.asarray(camera_config["tvecs"])
    return camera_config
