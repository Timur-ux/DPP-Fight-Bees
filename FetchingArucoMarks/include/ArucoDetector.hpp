#ifndef ARUCO_DETECTOR_HPP_
#define ARUCO_DETECTOR_HPP_

#include "interfaces/IArucoDetector.hpp"
#include "ArucoData.hpp"

class ArucoDetector : public IArucoDetector {
public:
	std::list<ArucoData> fetchArucoData(cv::Mat image) override;
};

#endif // !ARUCO_DETECTOR_HPP_
