#ifndef I_FRAME_FETCHER_H_
#define I_FRAME_FETCHER_H_

#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>

class IFrameFetcher {
public:
	virtual cv::Mat getFrame() = 0;
};

#endif // !I_FRAME_FETCHER_H_
