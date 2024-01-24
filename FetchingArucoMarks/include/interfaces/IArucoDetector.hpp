#ifndef I_ARUCO_DETECTOR_HPP_
#define I_ARUCO_DETECTOR_HPP_

#include <opencv2/core.hpp>
#include <list>

class IArucoDetector {
public:
	virtual std::list<ArucoData> fetchArucoData(cv::Mat image) = 0;
};

#endif // !I_ARUCO_DETECTOR_HPP_