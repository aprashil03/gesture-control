import numpy as np
import math

def calcAngles(fingers, res):
    fingers_angles = [] # 0 -> thumb... 4 -> pinky finger
    for finger in fingers:
        fp = [] # 3 points of one finger
        for finger_pts in finger:
            p1, p2, p3 = finger_pts[1]*res[0], finger_pts[2]*res[1], finger_pts[3]*1000
            fp.append((int(p1), int(p2), int(p3)))

        fingers_angles.append(angle_2p_3d(fp[0], fp[1], fp[2]))

    return fingers_angles

def angle_2p_3d(a, b, c):   

    vec1 = np.array([ a[0] - b[0], a[1] - b[1], a[2] - b[2] ])
    vec2 = np.array([ c[0] - b[0], c[1] - b[1], c[2] - b[2] ])

    vec1mag = np.sqrt([ vec1[0] * vec1[0] + vec1[1] * vec1[1] + vec1[2] * vec1[2] ])
    vec1norm = np.array([ vec1[0] / vec1mag, vec1[1] / vec1mag, vec1[2] / vec1mag ])

    vec2mag = np.sqrt(vec2[0] * vec2[0] + vec2[1] * vec2[1] + vec2[2] * vec2[2])
    vec2norm = np.array([ vec2[0] / vec2mag, vec2[1] / vec2mag, vec2[2] / vec2mag ])
    res = vec1norm[0] * vec2norm[0] + vec1norm[1] * vec2norm[1] + vec1norm[2] * vec2norm[2]
    angle_rad = np.arccos(res)

    return int(math.degrees(angle_rad))

        