#ifndef ARUCO_DATA_HPP_
#define ARUCO_DATA_HPP_

struct Vector3 {
	double x, y, z;

	Vector3() = default;
};

struct ArucoData {
	long long id;
	Vector3 position;
};

#endif // !ARUCO_DATA_HPP_