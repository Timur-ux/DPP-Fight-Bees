#ifndef VIDEO_FRAME_FETCHER_HPP_
#define VIDEO_FRAME_FETCHER_HPP_

#include "interfaces/IFrameFetcher.hpp"

class VideoFrameFetcher : public IFrameFetcher {
private:
	cv::VideoCapture videoCapture_;
public:
	VideoFrameFetcher(int CameraIndex = 0);
	cv::Mat getFrame() override;
};

#endif // !VIDEO_FRAME_FETCHER_HPP_
