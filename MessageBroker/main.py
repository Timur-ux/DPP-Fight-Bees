import zmq
import json

CONFIG_NAME = "Config.json"

def main():
    with open(CONFIG_NAME, "r") as file:
        config = json.load(file)

    print(f"Starting broker with\n \
          CameraSocket: {config['CameraSocket']}\n \
          ServerSocket: {config['ServerSocket']}")

    context = zmq.Context(1)
    frontend = context.socket(zmq.PULL)
    backend = context.socket(zmq.PUSH)

    frontend.bind(config["CameraSocket"])
    backend.bind(config["ServerSocket"])
    
    while True:
        message = frontend.recv_multipart()
        backend.send_multipart(message)


if __name__ == "__main__":
    main()
