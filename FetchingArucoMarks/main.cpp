#include <iostream>
#include <memory>

#include "VideoFrameFetcher.hpp"
#include "ArucoDetector.hpp"
#include "Server.hpp"
#include "interfaces/IDistanceDetector.hpp"

int main(int argc, char* argw[]) {
    std::string configFileName = "config.json";
    if (argc > 1) {
        configFileName = argw[1];
    }

    VideoFrameFetcher frameFetcher{0};
    ArucoDetector arucoDetector;
    std::shared_ptr<IDistanceDetector> distanceDetector; // not implemented yet
    Server server(configFileName);

    while (true) {
        cv::Mat frame = frameFetcher.getFrame();
        std::list<ArucoData> arucoMarks = arucoDetector.fetchArucoData(frame);

        for (ArucoData& arucoMark : arucoMarks) {
            Vector3 arucoMarkPosition = distanceDetector->calcDistance(frame, arucoMark);
            arucoMark.position = arucoMarkPosition;
        }

        server.sendArucoData(arucoMarks);
    }

    return 0;
}