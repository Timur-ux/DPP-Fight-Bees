#ifndef I_SERVER_HPP_
#define I_SERVER_HPP_

#include <string>

class IServer {
public:
	virtual void send(std::string) = 0;
};

#endif // !I_SERVER_HPP_