import math

def QuaternionToEulerAngles(q):
    sinr_cosp = 2 * (q[0] * q[1] + q[2] * q[3])
    cosr_cosp = 1 - 2 * (q[1] ** 2 + q[2] ** 2)
    x = math.atan2(sinr_cosp, cosr_cosp)
    
    sinp = 2 * (q[0] * q[2] - q[3] * q[1])
    y = math.asin(sinp)
    
    siny_cosp = 2 * (q[0] * q[3] + q[1] * q[2])
    cosy_cosp = 1 - 2 * (q[2] ** 2 + q[3] ** 2)
    z = math.atan2(siny_cosp, cosy_cosp)

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


# print(QuaternionToEulerAngles([0.996325, -0.078153, 0.032918, 0.012072]))
# print(EulerAnglesToQuaternion([-3.53375340e+00, 7.67119047e-02, -1.78757976e+02]))