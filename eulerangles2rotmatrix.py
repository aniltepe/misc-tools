import math
import numpy as np

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



def quaternion_rotation_matrix(Q):
    q0 = Q[0]
    q1 = Q[1]
    q2 = Q[2]
    q3 = Q[3]
    r00 = 2 * (q0 * q0 + q1 * q1) - 1
    r01 = 2 * (q1 * q2 - q0 * q3)
    r02 = 2 * (q1 * q3 + q0 * q2)
    r10 = 2 * (q1 * q2 + q0 * q3)
    r11 = 2 * (q0 * q0 + q2 * q2) - 1
    r12 = 2 * (q2 * q3 - q0 * q1)
    r20 = 2 * (q1 * q3 - q0 * q2)
    r21 = 2 * (q2 * q3 + q0 * q1)
    r22 = 2 * (q0 * q0 + q3 * q3) - 1
    
    rot_matrix = np.array([[r00, r01, r02],
                           [r10, r11, r12],
                           [r20, r21, r22]])
                            
    return rot_matrix


# angles = [-15.374923, 0.456284, 13.602521]
angles = [0, 0, 90]
print(quaternion_rotation_matrix(EulerAnglesToQuaternion(angles)))

#vector:vec3(-0.372752, -0.927265, -0.035160) axises:mat3x3((-0.914354, 0.401586, -0.051827), (-0.062205, -0.012836, 0.997981), (0.400110, 0.915732, 0.036717)) degrees:vec3(-15.374923, 0.456284, 13.602521) output: vec3(-0.392694, -0.868473, -0.302565)-