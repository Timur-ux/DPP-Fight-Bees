import zmq
import json

DEFAULT_CONFIG_PATH = "./Config.json"

def main():
    configPath = input(f"Input config path({DEFAULT_CONFIG_PATH} by default): ")
    if configPath == "":
        configPath = DEFAULT_CONFIG_PATH
    with open(configPath, "r") as file:
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
