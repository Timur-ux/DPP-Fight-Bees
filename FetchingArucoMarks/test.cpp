// read_webcam.cpp
#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>

using namespace cv;

int main() {
    VideoCapture v_cap(0);    // use 1 as id if using external webcam
    Mat img;
    while (true)  //generate exception once v_cap frame read is over
    {
        v_cap.read(img);                 // load each frame into img
        imshow("Display window", img);   // display img
        waitKey(10);                     // delay of 10 ms
    }
    return 0;
}