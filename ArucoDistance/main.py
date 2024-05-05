import CameraCalibrator as CC
import ArucoDistance as AD
import argparse


def main():
    parser = argparse.ArgumentParser(description="Default argument parser for application control")
    parser.add_argument("config_path", type=str, help="provide a path to config file(if calibrate select there config will be stored)")
    parser.add_argument("-c", "--camera", type=int, default=0, help="provide camera's id(default: 0)")
    parser.add_argument("--calibrate", type=bool, default=False, help="point if camera is need to calibrate")

if __name__ == "__main__":
    main()
