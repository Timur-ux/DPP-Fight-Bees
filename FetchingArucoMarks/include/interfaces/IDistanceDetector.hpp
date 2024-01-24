#ifndef I_DISTANCE_DETECTOR_HPP_
#define I_DISTANCE_DETECTOR_HPP_

#include <opencv2/core.hpp>
#include "../ArucoData.hpp"

class IDistanceDetector {
public:
	virtual Vector3 calcDistance(cv::Mat& image, ArucoData& arucoData) = 0;
};

#endif // !I_DISTANCE_DETECTOR_HPP_