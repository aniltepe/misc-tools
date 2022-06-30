import numpy as np
import math
 
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
    return np.array([math.degrees(x), math.degrees(y), math.degrees(z)])


print(rotationMatrixToEulerAngles(np.array([
    [0.999366, -0.011501, 0.033694],
    [0.014167, 0.996697, -0.079968],
    [-0.032663, 0.080395, 0.996228]])))
