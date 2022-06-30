import math
import numpy as np

def rotationMatrixToEulerAngles(R):
    sy = math.sqrt(R[0,0] * R[0,0] +  R[1,0] * R[1,0])
    singular = sy < 1e-6
    if not singular:
        x = math.atan2(R[2,1] , R[2,2])
        y = math.atan2(-R[2,0], sy)
        z = math.atan2(R[1,0], R[0,0])
    else:
        x = math.atan2(-R[1,2], R[1,1])
        y = math.atan2(-R[2,0], sy)
        z = 0
    return [math.degrees(x), math.degrees(y), math.degrees(z)]

def EulerAnglesToQuaternion(e):
    e[0] = math.radians(e[0])
    e[1] = math.radians(e[1])
    e[2] = math.radians(e[2])
    cy = math.cos(e[2] * 0.5)
    sy = math.sin(e[2] * 0.5)
    cp = math.cos(e[1] * 0.5)
    sp = math.sin(e[1] * 0.5)
    cr = math.cos(e[0] * 0.5)
    sr = math.sin(e[0] * 0.5)

    w = cr * cp * cy + sr * sp * sy
    x = sr * cp * cy - cr * sp * sy
    y = cr * sp * cy + sr * cp * sy
    z = cr * cp * sy - sr * sp * cy

    return [w, x, y, z]


print(EulerAnglesToQuaternion(rotationMatrixToEulerAngles(np.array([
    [-0.7348139882087708, 0.0, 0.6782686710357666],
    [0.0, 0.9999999403953552, 0.0],
    [-0.6782686710357666, 0.0, -0.7348139882087708]]))))
    

print(rotationMatrixToEulerAngles(np.array([
    [-0.7348139882087708, 0.0, 0.6782686710357666],
    [0.0, 0.9999999403953552, 0.0],
    [-0.6782686710357666, 0.0, -0.7348139882087708]])))
