#ifndef SERVER_HPP_
#define SERVER_HPP_

#include "interfaces/IServer.hpp"
#include <zmq.hpp>

class Server : public IServer {
private:
	zmq::context_t* context;
	zmq::socket_t sendSocket;
public:
	Server(std::string configFileName);
	void send(std::string data) override;

	void sendArucoData(std::list<ArucoData> data);
};

#endif // !SERVER_HPP_