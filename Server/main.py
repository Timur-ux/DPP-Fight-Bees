import zmq
import json

class Server:
    def __init__(self, context, serverSocket):
        self.context = context
        self.socket = context.socket(zmq.PULL)
        self.socket.connect(serverSocket)

    def process(self, message):
        print("Accepted message: ", message)
    
    def startProccessing(self):
        print("Message proccessing started")
        while True:
            message = self.socket.recv()
            self.process(message)

DEFAULT_SERVER_DATA_PATH = "./Config.json"

def main():
    configPath = input(f"Input path to config file({DEFAULT_SERVER_DATA_PATH} by default): ")
    if configPath == "":
        configPath = DEFAULT_SERVER_DATA_PATH

    with open(configPath, "r") as file:
        config = json.load(file)

    context = zmq.Context(1)
    serverSocket = config["ServerSocket"]
    server = Server(context, serverSocket)

    server.startProccessing()


if __name__ == "__main__":
    main()
